# importing all the necessary packages and libraries
from django.shortcuts import render
import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow import keras
from keras.models import Model
from keras import backend as K
from keras.preprocessing import image
from keras.models import load_model
from django.db import connection
from django.core.files.base import ContentFile
from io import BytesIO
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.models import Sequential
#from tensorflow.keras.models import load_weights
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .forms import ReportForm
from .models import PatientReport
from .utils import generate_report_as_pdf
import logging
import base64
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

''' This snippet is for the view of the login page. Upon accessing the server, the user is asked to enter the
login credentials. This code checks if the credentials match with the superuser data. If not, the user
is redirected to the login page. '''
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_dashboard')
        else:
            messages.error(request, "Sorry! You do not have access to this site.")
            return redirect('login')
    else: 
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login.html')

''' The following code snippet is for using the trained DenseNet model to classify the condition of the lungs
in the uploaded xray. The labels are the possible predictions that the model can make.'''

labels = ['Cardiomegaly', 
          'Emphysema', 
          'Effusion', 
          'Hernia', 
          'Infiltration', 
          'Mass', 
          'Nodule', 
          'Atelectasis',
          'Pneumothorax',
          'Pleural_Thickening', 
          'Pneumonia', 
          'Fibrosis', 
          'Edema', 
          'Consolidation']

# to get weighted loss of the values to train the DenseNet model
# this step fixes the class imbalance problem
def get_weighted_loss(pos_weights, neg_weights, epsilon = 1e-7):
    
    def weighted_loss(y_true, y_pred):
        loss = 0.0
        for i in range(len(pos_weights)):
            y_true_i = y_true[:,i]
            y_pred_i = y_pred[:,i]

            positive_loss = -pos_weights[i] * y_true_i * tf.math.log(y_pred_i + epsilon)
            negative_loss = -neg_weights[i] * (1 - y_true_i) * tf.math.log(1 - y_pred_i + epsilon)

            loss += tf.reduce_mean(positive_loss + negative_loss)

        return loss

    return weighted_loss

pos_weights = np.array([0.02, 0.013, 0.128, 0.002, 0.175, 0.045, 0.054, 0.106, 0.038, 0.021, 0.01, 0.014, 0.016, 0.033])
neg_weights = 1 - pos_weights

# using a pretrained DenseNet model
base_model = DenseNet121(include_top=False)
x = base_model.output
# adding a global spatial average pooling layer
x = GlobalAveragePooling2D()(x)
# and a logistic layer
predictions = Dense(len(labels), activation="sigmoid")(x)
model = Model(inputs=base_model.input, outputs=predictions)
model.compile(optimizer='adam', loss=get_weighted_loss(pos_weights, neg_weights))
model.load_weights("pretrained_model.h5")
model.save("model_final.h5") # saving the model and its weights to use for predictions

labels = ['Cardiomegaly', 
          'Emphysema', 
          'Effusion', 
          'Hernia', 
          'Infiltration', 
          'Mass', 
          'Nodule', 
          'Atelectasis',
          'Pneumothorax',
          'Pleural_Thickening', 
          'Pneumonia', 
          'Fibrosis', 
          'Edema', 
          'Consolidation']

@login_required
def home_dashboard(request):
    return render(request, 'home_dashboard.html')

# the xray analyzer view to take in an uploaded image and make predictions using the saved model
def xray_analyzer(request):
   if request.method == 'POST' and request.FILES['xray_image']:
       # Get the uploaded X-ray image
       xray_image = request.FILES['xray_image']
       image_content = xray_image.read()
       img = image.load_img(BytesIO(image_content), target_size=(320,320)) # resizing to 320,320
       img_array = image.img_to_array(img) # converting to numpy array
       img_array = np.expand_dims(img_array, axis=0) # adding batch dimensions
       img_array = img_array / 255.0 # normalizing pixel values
       predictions = model.predict(img_array)
       prediction_df = pd.DataFrame(predictions, columns = labels)
       pred_result = prediction_df.idxmax(axis=1)
       return render(request, 'xray_analyzer.html', {'predictions': pred_result})
   else:
       return render(request, 'xray_analyzer.html')

logger = logging.getLogger(__name__)

''' This view generates reports of the model's predictions. Upon clicking Report Generator, the doctor is made
to enter the patient's details and the model's predictions. Once that's done, the doctor clicks the 
Generate Report button which automatically downloads the report as a pdf. This was done using the xhtml2pdf 
package of html. '''
def generate_report(request):
   if request.method == 'POST':
       form = ReportForm(request.POST, request.FILES)
       if form.is_valid():
           # following lines of code save the entries to a SQL db
           patient_name = form.cleaned_data['patient_name']
           age = form.cleaned_data['age']
           gender = form.cleaned_data['gender']
           image_modality = form.cleaned_data['image_modality']
           image = form.cleaned_data['image']
           prediction = form.cleaned_data['prediction']


           # saving report to the db
           report = PatientReport(
               patient_name = patient_name,
               age = age,
               gender = gender,
               image_modality = image_modality,
               image = image,
               prediction = prediction
           )
           report.image = image
           report.save()

           # Convert image to base64-encoded string
           image_base64 = base64.b64encode(image.read()).decode('utf-8')

           # Generate HTML report content
           report_html = f"""
               <h1>Patient Report</h1>
               <p>Patient Name: {report.patient_name}</p>
               <p>Age: {report.age}</p>
               <p>Gender: {report.gender}</p>
               <p>Image Modality: {report.image_modality}</p>
               <img src="data:image/png;base64,{image_base64}" alt="Image">
               <p>Prediction: {report.prediction}</p>
           """

           # offering the doctor the option to download the report as a pdf
           pdf_report = generate_report_as_pdf(report_html, report.patient_name)

           # serve PDF for download (https server)
           response = HttpResponse(pdf_report, content_type='application/pdf')
           response['Content-Disposition'] = f'attachment; filename="report.pdf"'
           return response
      
   else:
       form = ReportForm()


   return render(request, 'report_generator.html', {'form': form})
