# Import libraries
from dotenv import load_dotenv
import os
from azure.storage.blob import BlobServiceClient

# Load environment variables from .env file
load_dotenv()

# Retrive connection string from environment variable
connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

# Use the connection string to create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)


# Container and Blob names
container_name = "health-data-container"
blob_name = "health-data.csv"
local_file_path = "./data/health-data.csv"

# Ensure the container exists
try:
    container_client = blob_service_client.create_container(container_name)
    print(f"Container '{container_name}' created.")
except Exception as e:
    print(f"Container '{container_name}' already exists or could not be created. Error: {e}")
    
# Upload the file to the container
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
    print(f"File '{local_file_path}' uploaded to container '{container_name}' as blob '{blob_name}'.")