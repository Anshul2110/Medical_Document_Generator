import streamlit as st
import requests

st.title("🩺 Medical Report Generator")

name = st.text_input("Patient Name")
age = st.number_input("Age", min_value=0)
gender = st.text_input("Gender")

symptoms = st.text_area("Symptoms")
xray = st.text_area("X-ray Observations")
diagnosis = st.text_area("Diagnosis")

if st.button("Generate Report"):
    data = {
        "name": name,
        "age": age,
        "gender": gender,
        "symptoms": symptoms,
        "xray_observations": xray,
        "diagnosis": diagnosis,
    }

    with st.spinner("Generating report..."):
        res = requests.post(
            "http://127.0.0.1:8000/generate-report",
            json=data
        )

    if res.status_code == 200:
        result = res.json()
        st.success("Report Generated!")

        st.write("Patient ID:", result["patient_id"])
        st.link_button("Download Report", result["report_url"])
    else:
        st.error("Error generating report")