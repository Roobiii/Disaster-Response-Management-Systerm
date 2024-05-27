**Disaster Response Web Application**
**Overview**
The Disaster Response Web Application is designed to help emergency responders quickly classify and prioritize incoming disaster-related messages. This project uses machine learning to analyze and categorize text messages, enabling efficient resource allocation and response.

****Table of Contents**
Installation
Project Components
Usage
Data
Model
Web Application
Screenshots
Acknowledgments
License
Contact**

**Installation
Prerequisites**

Ensure you have the following installed:

Python 3.7+
pip (Python package installer)
NLTK data packages (punkt, wordnet)


**Dependencies
**
Install the necessary Python packages using pip:
pip install -r requirements.txt

**NLTK Data**
Download the required NLTK data packages:
import nltk
nltk.download(['punkt', 'wordnet'])

**Project Components**
The project is divided into three main parts:

ETL Pipeline: Extracts data from source files, transforms and cleans the data, and loads it into a SQLite database.
ML Pipeline: Trains a machine learning model to classify disaster messages.
Flask Web App: A web interface for users to input messages and get classification results.

**Usage**
**1. ETL Pipeline**
Run the ETL pipeline script to process the data:
python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db

**2. ML Pipeline**
Run the ML pipeline script to train the model:
python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl

**3. Flask Web App**
Run the Flask web application:
python app/run.py
Open your web browser and go to http://localhost:3001 to use the web app.

**Data**
**Source**
The dataset used in this project consists of real messages sent during disaster events. It includes:

**disaster_messages.csv**: Contains the messages.
**disaster_categories.csv**: Contains the categories for each message.
**Database**
The processed data is stored in a SQLite database (DisasterResponse.db).

**Model
Training**
The model is a multi-output classifier based on RandomForestClassifier. It is trained to categorize messages into multiple categories such as 'medical help', 'search and rescue', 'water', 'food', etc.

**Evaluation**
The model's performance is evaluated using classification metrics, and a detailed classification report is generated for each category.

**Web Application**
The Flask web application provides a user-friendly interface to classify disaster messages.

**Features**
**Message Input:** Users can input a message into a text box.
**Message Classification:** The app returns the categories that the message belongs to.
**Visualizations: **Displays various visualizations about the dataset.

**
Routes**
/: Main page with the message input form and visualizations.
/go: Page to display the classification results for a user's input message.


**Screenshots**

![image](https://github.com/Roobiii/Disaster-Response-Management-Systerm/assets/135594548/862ff67a-c85d-45be-bfe6-f7e6b4a24aee)

![image](https://github.com/Roobiii/Disaster-Response-Management-Systerm/assets/135594548/eb66a53f-b058-41c8-88bf-af338e29d170)
**Home page with input form and visualizations**


![image](https://github.com/Roobiii/Disaster-Response-Management-Systerm/assets/135594548/9cfa7285-db05-45fb-9095-ce77329a7b75)
**Results page showing the classification of the input message**


![image](https://github.com/Roobiii/Disaster-Response-Management-Systerm/assets/135594548/bdbcba11-1149-424d-85ca-068e87622b6b)
**Contact us page**

**Acknowledgments**
This project is part of the Data Science Nanodegree program by Udacity.
The dataset is provided by Figure Eight.

**requirements.txt**
To ensure that all dependencies are installed correctly, include a requirements.txt file with the following content:

Flask==2.0.1
nltk==3.6.2
numpy==1.19.5
pandas==1.2.4
scikit-learn==0.24.2
SQLAlchemy==1.4.15
joblib==1.0.1
tqdm==4.61.1

License
©Roobika

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

**Contact**
For any queries, please contact Roobika at roobikaviswanathan@gmail.com.


