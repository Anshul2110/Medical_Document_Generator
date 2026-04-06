import hashlib

def anonymize_patient(name: str) -> str:
    return hashlib.sha256(name.encode()).hexdigest()[:12]