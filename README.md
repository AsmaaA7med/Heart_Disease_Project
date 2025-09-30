# Heart Disease Project

## 📌 Overview
This project predicts the presence of heart disease using the **UCI Heart Disease dataset**.  
It includes preprocessing, exploratory data analysis (EDA), feature selection, supervised and unsupervised models, and a Streamlit app for prediction.

## 📂 Project Structure
Heart_Disease_Project/

├── data/ # dataset files (not included in repo)
├── notebooks/ # Jupyter notebooks (EDA, models, etc.)
├── models/ # saved models (joblib/pkl)
├── results/ # plots, evaluation metrics
├── ui/ # Streamlit app
├── deployment/ # ngrok setup, deployment notes
├── requirements.txt # dependencies
└── README.md # project description


## ⚙️ Installation
```bash
# clone the repo
git clone <your-repo-url>
cd Heart_Disease_Project

# create & activate virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows

# install dependencies
pip install -r requirements.txt

📊 Running Notebooks

Open Jupyter or VS Code and run the notebooks inside notebooks/ step by step:

01_data_preprocessing.ipynb

02_EDA.ipynb

03_feature_selection.ipynb

04_supervised_models.ipynb

05_unsupervised_models.ipynb

06_model_tuning.ipynb

🚀 Run the Streamlit App
streamlit run ui/app.py

🌍 Deploy with ngrok (optional)

Follow the instructions in deployment/ngrok_setup.txt.
Example:

ngrok http 8501

📑 Deliverables

models/final_model.pkl → trained pipeline (preprocessing + model)

results/plots/ → correlation heatmap, ROC curves, etc.

results/evaluation_metrics.txt → precision, recall, f1, ROC-AUC

📚 Dataset

Source: UCI Heart Disease Dataset
