# EC530-Final-Project
EC530: XRAY-XPLORER FINAL PROJECT

** Welcome to the XRay Xplorer project! **

This piece of software is designed to help doctors upload images of Chest XRays to a portal, which then processes the image and returns a result about the whether the image has any of the 14 different pathologies that the model has been trained to identify. It includes features such as user authentication, uploading and storing X-ray images, analyzing images using machine learning models, and generating medical reports based on the analysis.

Features: <br>
1. This is a web application developed using Python's Django development framework.
2. Flow of action: Run Server --> Login --> XRay-Xplorer Dashboard --> Analyze XRay/Generate Report
3. The entire development process was done using VS Code.
4. HTML templates were created for each page of the web app, CSS was used for basic styling.
5. In parallel, a pretrained DenseNet121 model was used to train a set of chest xrays. The weights were then saved for use in this project.
6. A set of permitted doctors are allowed access to login after being made 'superusers'. 
7. This project makes use of all main functionalities of a application made using Django - views, forms, sqlite database, urls, migrations.
