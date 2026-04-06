from pydantic import BaseModel

class PatientInput(BaseModel):
    name: str
    age: int
    gender: str
    symptoms: str
    xray_observations: str
    diagnosis: str