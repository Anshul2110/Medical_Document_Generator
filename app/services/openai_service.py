from openai import AzureOpenAI
from app.config import AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT

client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version="2024-12-01-preview"
)

def generate_medical_report(data, patient_id: str):
    prompt = f"""
    You are a professional medical report generator and an expert in radiology. Based on the provided patient information, symptoms, x-ray observations, and diagnosis, generate a comprehensive advanced medical report.

    IMPORTANT:
    - Do NOT hallucinate 
    - Only use provided information
    - Maintain formal tone used in medical reports
    - Provide accurate and higly advanced medical insights based on the data

    Patient ID: {patient_id}
    Age: {data.age}
    Gender: {data.gender}

    Symptoms:
    {data.symptoms}

    X-ray Observations:
    {data.xray_observations}

    Diagnosis:
    {data.diagnosis}

    Generate structured report with:
    1. Patient Summary (do not include patient ID here)
    2. Clinical Findings
    3. Diagnosis Explanation (in case diagnosis is empty, explain based on symptoms and x-ray))
    4. Recommendations
    5. Disclaimer
    """

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content