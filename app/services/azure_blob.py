from azure.storage.blob import BlobServiceClient
from app.config import AZURE_CONN_STR, AZURE_CONTAINER

def upload_to_blob(file_path: str):
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONN_STR)

    blob_client = blob_service_client.get_blob_client(
        container=AZURE_CONTAINER,
        blob=file_path
    )

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    return blob_client.url  