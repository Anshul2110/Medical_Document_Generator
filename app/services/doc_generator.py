import os
from docx import Document

def create_doc(report_text: str, patient_id: str):
    doc = Document()

    doc.add_heading("Medical Report", 0)
    doc.add_paragraph(f"Patient ID: {patient_id}")

    for line in report_text.split("\n"):
        doc.add_paragraph(line)

    file_path = f"{patient_id}.docx"
    doc.save(file_path)

    return file_path