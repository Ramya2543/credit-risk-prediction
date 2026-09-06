# Credit Risk & Loan Default Prediction

An end-to-end machine learning system that predicts the probability a loan applicant will default, with full explainability and a live interactive risk assessment tool.

🔗 **Live App:** https://credit-risk-ramya.streamlit.app
🔗 **Live API Docs:** https://credit-risk-api-x3z5.onrender.com/docs

## Problem Statement

Lenders need to assess credit risk before approving loans. This project builds a machine learning model that predicts the probability of default based on applicant and loan characteristics, and explains *why* each prediction was made — critical for responsible, auditable lending decisions.

## Dataset

- **Source:** [Lending Club Loan Data](https://www.kaggle.com/datasets/adarshsng/lending-club-loan-data-csv) (Kaggle)
- **Size:** 2.26 million loan records (2007–2020)
- **Target definition:** Only loans with a finished outcome were used — "Fully Paid" (0) vs "Charged Off" (1). Loans still "Current," "Late," or "In Grace Period" were excluded since their final outcome isn't known yet.
- **Final modeling dataset:** 1.3M+ rows, ~20% default rate (imbalanced)

## Approach

1. **Data Cleaning:** Handled missing values (median imputation for numeric, "Unknown" category for missing employment length)
2. **Feature Engineering:** Selected 15 features known at application time (no data leakage), encoded categorical variables
3. **Modeling:** Compared Logistic Regression (baseline), Random Forest, and XGBoost
4. **Tuning:** Hyperparameter search via RandomizedSearchCV
5. **Explainability:** SHAP values for global feature importance and individual prediction explanations
6. **Deployment:** FastAPI backend + Streamlit frontend, both deployed live

## Results

| Model | ROC-AUC |
|---|---|
| Logistic Regression (baseline) | 0.702 |
| Random Forest | 0.699 |
| **XGBoost (tuned)** | **0.716** |

## Tech Stack

Python, Pandas, NumPy, scikit-learn, XGBoost, SHAP, FastAPI, Streamlit, Render, Streamlit Community Cloud

## Project Structure

\`\`\`
credit-risk-prediction/
├── api/                # FastAPI backend
│   ├── main.py
│   └── requirements.txt
├── app/                 # Streamlit frontend
│   ├── app.py
│   └── requirements.txt
├── models/               # Trained model artifacts
├── notebooks/            # EDA, modeling, explainability
├── data/                 # Raw and processed data (gitignored)
└── requirements.txt       # Full dev environment
\`\`\`

## How to Run Locally

\`\`\`bash
git clone https://github.com/Ramya2543/credit-risk-prediction.git
cd credit-risk-prediction
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt

# Run API
cd api
uvicorn main:app --reload

# In a new terminal, run app
cd app
streamlit run app.py
\`\`\`

## Author

Ramya — [GitHub](https://github.com/Ramya2543)