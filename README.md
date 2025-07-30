# Sentiment Analysis App

This is a simple web-based Sentiment Analysis Application that analyzes the sentiment of user input text as Positive, Negative, or Neutral using Natural Language Processing techniques.

## Features

- Real-time sentiment prediction from user input
- Clean and responsive UI
- Displays result with sentiment category
- Easy to run locally

## Tech Stack

- Frontend:HTML, CSS
- Backend:Python, Flask
- NLP Library:TextBlob
- Other Tools:Git, GitHub

## Folder Structure
sentimentAnalysisApp/
├── static/
│ └── style.css
├── templates/
│ └── index.html
├── app.py
├── requirements.txt
└── README.md


##  How to Run the Project

### 1. Clone the Repository

bash
git clone https://github.com/Navyashreee2002/sentimentAnalysisApp.git
cd sentimentAnalysisApp


##2. create virtual environment
python -m venv venv
# Activate it:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

3.Install Dependencies
pip install -r requirements.txt

#If no requirements.txt, run:
pip install flask textblob
python -m textblob.download_corpora


4. Run the App
python app.py


