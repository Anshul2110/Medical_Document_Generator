from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_medical_report(data, patient_id: str):
    prompt = f"""
    You are a professional medical report generator.

    IMPORTANT:
    - Do NOT hallucinate data
    - Only use provided information
    - This is NOT a final clinical diagnosis
    - Maintain formal tone

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
    1. Patient Summary
    2. Clinical Findings
    3. Diagnosis Explanation
    4. Recommendations
    5. Disclaimer
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content