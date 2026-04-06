from fastapi import FastAPI
from app.models import PatientInput
from app.services.anonymizer import anonymize_patient
from app.services.openai_service import generate_medical_report
from app.services.doc_generator import create_doc
from app.services.azure_blob import upload_to_blob

app = FastAPI(title="Medical Report AI")

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/generate-report")
def generate_report(patient: PatientInput):
    # Step 1: Anonymize
    patient_id = anonymize_patient(patient.name)

    # Step 2: Generate AI Report
    report_text = generate_medical_report(patient, patient_id)

    # Step 3: Create DOCX
    file_path = create_doc(report_text, patient_id)

    # Step 4: Upload to Azure
    blob_url = upload_to_blob(file_path)

    return {
        "patient_id": patient_id,
        "report_url": blob_url
    }