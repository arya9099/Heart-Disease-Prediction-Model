❤️ Heart Disease Prediction

This project predicts the risk of heart disease using Logistic Regression trained on a heart disease dataset.
It includes:

Data preprocessing & model training (src/train_model.py)

Model evaluation (src/evaluate_model.py)

An interactive Streamlit web app (app/streamlit_app.py) for predictions

📂 Project Structure

Heart_Disease_prediction/
├── data/
│   └── heart_dataset.csv          # Dataset (CSV format)
│
├── models/
│   ├── model.pkl                  # Trained model (Logistic Regression)
│   └── scaler.pkl                 # StandardScaler for preprocessing
│
├── src/
│   ├── train_model.py             # Data preprocessing & model training
│   └── evaluate_model.py          # Model evaluation
│
├── app/
│   └── streamlit_app.py           # Streamlit UI for predictions
│
├── requirements.txt               # Project dependencies
└── README.md                      # Documentation

📊 Dataset

The dataset contains 13 features + 1 target column:

Feature	Description
age	Age of patient (years)
sex	Sex (1 = male, 0 = female)
cp	Chest pain type (0–3)
trestbps	Resting blood pressure (mm Hg)
chol	Serum cholesterol (mg/dL)
fbs	Fasting blood sugar > 120 mg/dL (1 = true, 0 = false)
restecg	Resting electrocardiographic results (0–2)
thalach	Maximum heart rate achieved
exang	Exercise-induced angina (1 = yes, 0 = no)
oldpeak	ST depression induced by exercise
slope	Slope of peak exercise ST segment (0–2)
ca	Number of major vessels colored by fluoroscopy (0–4)
thal	Thalassemia (0–3)
target	1 = heart disease, 0 = no disease
⚙️ Installation (Mac/Linux)

Clone repo / navigate to project:

cd ~/Desktop/Heart_Disease_prediction


Create virtual environment:

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


(Optional) Upgrade pip:

python3 -m pip install --upgrade pip

🧑‍💻 Training the Model

Run:

cd src
python3 train_model.py


This will:

Clean the dataset (remove duplicates, handle missing values)

Train a Logistic Regression model

Save:

models/model.pkl (trained model)

models/scaler.pkl (feature scaler)

📈 Evaluating the Model

Run:

cd src
python3 evaluate_model.py


This prints:

Accuracy

Precision, Recall, F1-score

🌐 Running the Web App

Start the app:

cd app
streamlit run streamlit_app.py


Open your browser → http://localhost:8501

Enter patient details (13 features) → Get prediction result:

✅ Low Risk

⚠️ High Risk

📦 Requirements

Main dependencies:

pandas

numpy

scikit-learn

matplotlib

seaborn

streamlit

Install via:

pip install -r requirements.txt

🚀 Future Improvements

Add support for multiple ML models (RandomForest, XGBoost)

Visualize feature importance in the app

Deploy app with Docker or Streamlit Cloud

✍️ Author: Arya Sujit Borawake❤️ Heart Disease Prediction

This project predicts the risk of heart disease using Logistic Regression trained on a heart disease dataset.
It includes:

Data preprocessing & model training (src/train_model.py)

Model evaluation (src/evaluate_model.py)

An interactive Streamlit web app (app/streamlit_app.py) for predictions

📂 Project Structure

Heart_Disease_prediction/
├── data/
│   └── heart_dataset.csv          # Dataset (CSV format)
│
├── models/
│   ├── model.pkl                  # Trained model (Logistic Regression)
│   └── scaler.pkl                 # StandardScaler for preprocessing
│
├── src/
│   ├── train_model.py             # Data preprocessing & model training
│   └── evaluate_model.py          # Model evaluation
│
├── app/
│   └── streamlit_app.py           # Streamlit UI for predictions
│
├── requirements.txt               # Project dependencies
└── README.md                      # Documentation

📊 Dataset

The dataset contains 13 features + 1 target column:

Feature	Description
age	Age of patient (years)
sex	Sex (1 = male, 0 = female)
cp	Chest pain type (0–3)
trestbps	Resting blood pressure (mm Hg)
chol	Serum cholesterol (mg/dL)
fbs	Fasting blood sugar > 120 mg/dL (1 = true, 0 = false)
restecg	Resting electrocardiographic results (0–2)
thalach	Maximum heart rate achieved
exang	Exercise-induced angina (1 = yes, 0 = no)
oldpeak	ST depression induced by exercise
slope	Slope of peak exercise ST segment (0–2)
ca	Number of major vessels colored by fluoroscopy (0–4)
thal	Thalassemia (0–3)
target	1 = heart disease, 0 = no disease
⚙️ Installation (Mac/Linux)

Clone repo / navigate to project:

cd ~/Desktop/Heart_Disease_prediction


Create virtual environment:

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


(Optional) Upgrade pip:

python3 -m pip install --upgrade pip

🧑‍💻 Training the Model

Run:

cd src
python3 train_model.py


This will:

Clean the dataset (remove duplicates, handle missing values)

Train a Logistic Regression model

Save:

models/model.pkl (trained model)

models/scaler.pkl (feature scaler)

📈 Evaluating the Model

Run:

cd src
python3 evaluate_model.py


This prints:

Accuracy

Precision, Recall, F1-score

🌐 Running the Web App

Start the app:

cd app
streamlit run streamlit_app.py


Open your browser → http://localhost:8501

Enter patient details (13 features) → Get prediction result:

✅ Low Risk

⚠️ High Risk

📦 Requirements

Main dependencies:

pandas

numpy

scikit-learn

matplotlib

seaborn

streamlit

Install via:

pip install -r requirements.txt

🚀 Future Improvements

Add support for multiple ML models (RandomForest, XGBoost)

Visualize feature importance in the app

Deploy app with Docker or Streamlit Cloud

✍️ Author: Arya Sujit Borawake
