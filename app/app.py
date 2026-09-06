import streamlit as st
import requests
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: #FAFAFA;
}
h1 {
    color: #4DA8FF;
}
p, label, .stMarkdown {
    color: #E0E0E0 !important;
}
div.stButton > button {
    background-color: #4DA8FF;
    color: #0E1117;
    border-radius: 8px;
    padding: 0.5em 2em;
    font-weight: 600;
    border: none;
}
div.stButton > button:hover {
    background-color: #3A8FDF;
    color: white;
}
[data-testid="stNumberInput"] input, [data-testid="stSelectbox"] > div {
    background-color: #1C1F26;
    color: #FAFAFA;
}
[data-testid="stMetricValue"] {
    color: #4DA8FF;
}
</style>
""", unsafe_allow_html=True)

st.title("Loan Risk Assessment")
st.write("Enter applicant details to assess credit risk")

loan_amnt = st.number_input("Loan Amount", min_value=500, value=15000)
term = st.selectbox("Term (months)", [36, 60])
int_rate = st.number_input("Interest Rate (%)", min_value=0.0, value=12.5)
installment = st.number_input("Monthly Installment", min_value=0.0, value=450.0)
grade = st.selectbox("Credit Grade (1=A best, 7=G worst)", [1,2,3,4,5,6,7], index=2)
emp_length = st.slider("Employment Length (years)", 0, 10, 5)
annual_inc = st.number_input("Annual Income", min_value=0, value=60000)
dti = st.number_input("Debt-to-Income Ratio", min_value=0.0, value=18.5)
open_acc = st.number_input("Open Credit Accounts", min_value=0, value=8)
revol_bal = st.number_input("Revolving Balance", min_value=0, value=12000)
revol_util = st.number_input("Revolving Utilization (%)", min_value=0.0, value=45.0)
total_acc = st.number_input("Total Accounts", min_value=0, value=20)

if st.button("Assess Risk"):
    payload = {
        "loan_amnt": loan_amnt, "term": term, "int_rate": int_rate,
        "installment": installment, "grade": grade, "emp_length": emp_length,
        "annual_inc": annual_inc, "dti": dti, "open_acc": open_acc,
        "revol_bal": revol_bal, "revol_util": revol_util, "total_acc": total_acc
    }
    response = requests.post("https://credit-risk-api-x3z5.onrender.com/predict", json=payload)
    result = response.json()
    
    st.metric("Default Probability", f"{result['default_probability']*100:.1f}%")
    st.write("Risk Category:", result['risk_category'])