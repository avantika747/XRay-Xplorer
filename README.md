# XRAY-XPLORER

# Welcome to the XRay-Xplorer project!

This piece of software is designed to help doctors upload images of Chest XRays to a portal, which then processes the image and returns a result about the whether the image has any of the 14 different pathologies that the model has been trained to identify. It includes features such as user authentication, uploading and storing X-ray images, analyzing images using machine learning models, and generating medical reports based on the analysis.

**Please watch the videos in the demo_videos folder to get a sense of the working. GitHub will not allow you to view the videos on the platform itself. Please click "View raw" to download the .mp4 files and watch the videos on your system.**

# Features:
1. This is a web application developed using Python's Django development framework.
2. Flow of action: Run Server --> Login --> XRay-Xplorer Dashboard --> Analyze XRay/Generate Report.
3. The entire development process was done using VS Code on macOS.
4. HTML templates were created for each page of the web app, CSS was used for basic styling.
5. In parallel, a pretrained DenseNet121 model was used to train a set of chest xrays. The weights were then saved for use in this project.
6. A set of permitted doctors are allowed access to login after being made 'superusers'.
7. The details of these permitted doctors, i.e., the superusers who are allowed access to the system, are stored in SQL databases. Similarly, the report information for each patient is also stored in a SQL database. 
8. This project makes use of all main functionalities of a application made using Django - views, forms, sqlite database, urls, migrations. 


# Installation and Instructions for Developers: 
1. To install, please clone the entire repository to your Desktop to run locally.
   ```bash
   git clone https://github.com/avantika747/EC530-Final-Project
   ```
2. It is recommended to use VS Code.
3. Navigate to the directory 
   ```bash
   cd name_of_directory
   ```
4. Install all necessary dependencies.
5. Set up the SQL database
   ```bash
   python manage.py migrate
   ```
7. If you wish to add more superusers with access to the XRay-Xplorer portal, you can do so by:
   ```bash
   python manage.py createsuperuser
   ```
   You will be prompted to enter a username and a password (password twice for confirmation).
9. Run the server
   ```bash
   python manage.py runserver
   ```

# Other Important Points:
1. If you run into problems while running the server, please make sure to install all dependencies using pip install.
2. You can use the images in the test_images folder for testing.
3. Please ensure that the images used for testing are of type .png
4. The Backend user authentication of Django was overridden in this project. A custom user backend authentication logic was developed instead. So unless you create superusers, you would not be able to access the portal.
5. Unit Tests have been included in tests.py - GitHub Actions was also invoked to automate this.
6. Elaborate comments have been included throughout in all parts of the project for better understanding.
7. If cloning the repository does not produce the desired results, please download the files individually and store them in a file directory that follows the same schematic.
8. The weights used to train the DenseNet model have not been included in this repository owing to memory constraints, since it is a large .h5 file over 25MB. If the weights are required for personal use or experimentation, please raise a GitHub Issue and allow time for a response from me.
9. This project will continue to be updated in the future for more bug fixes, feature updates, functionality improvements and so on. 


# EC530-Software Engineering concepts applied in this project:
1. Software Development - Continuous Integration, Continuous Development
2. Modularity - Web Services, HTTP Requests, HTML-CSS Templates, Forms, User Authentication, Generating Report PDFs
3. Data Management - SQL Databases to store information of permitted superusers and patient's report information
4. Application Frameworks - Web Framework using Python's Django
5. AI/ML - Image Classification using DenseNet121 model


# Screenshots of important results:
Some important screenshots here, but for a better understanding, please do watch the videos!
<br>
![image](https://github.com/avantika747/EC530-Final-Project/assets/66120758/b0706287-ab0d-444a-947f-d163fb04a5ab)
![image](https://github.com/avantika747/EC530-Final-Project/assets/66120758/fde6d8a3-4316-4571-a233-a2464b668aba)
![image](https://github.com/avantika747/EC530-Final-Project/assets/66120758/4e3e4136-022f-487d-a581-2a9a50746918)
![image](https://github.com/avantika747/EC530-Final-Project/assets/66120758/30c8e2f8-eb7f-483c-9632-119d95a81281)
![image](https://github.com/avantika747/EC530-Final-Project/assets/66120758/2cd3509e-9bf3-48b6-bdf3-51ececaf9e94)
![image](https://github.com/avantika747/EC530-Final-Project/assets/66120758/0dd3ab83-a04a-444b-87aa-0150f0dc974d)



























