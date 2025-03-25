import streamlit as st

st.title("🏦 My First Web App - Loan Eligibility Checker")

# Loan acceptance criteria
required_salary = 500000
required_years = 5

# Get user input
salary = int(st.number_input("💰 Input your annual salary:", value=0))
years_worked = int(st.number_input("⌛ Enter your years of work in the current job:", value=0))

# Check if the applicant meets the criteria
if st.button("Submit"):
    if salary >= required_salary and years_worked >= required_years:
        st.write("🎉 Congratulations! Your loan application is accepted.")
    else:
        st.write("❌ Sorry, your loan application is rejected.")
        if salary < required_salary:
            st.write(f"⚠️ Your salary (${salary}) is below the required ${required_salary}.")
        if years_worked < required_years:
            st.write(f"⚠️ Your work experience ({years_worked} years) is below the required {required_years} years.")
