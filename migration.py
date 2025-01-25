from dotenv import load_dotenv
import os
from azure.storage.blob import BlobServiceClient

# Load environment variables from .env file
load_dotenv()

# Retrieve the connection string
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

if not connection_string:
    raise ValueError("AZURE_STORAGE_CONNECTION_STRING is missing or not loaded properly.")

print(f"Connection string: {connection_string}")  # Debugging output

# Use the connection string to create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Example container and blob
container_name = "state-health-data"
blob_name = "state_health_data.csv"
local_file_path = "/path/to/your/state_health_data.csv"

# Ensure the container exists
container_client = blob_service_client.get_container_client(container_name)
try:
    container_client.create_container()
    print(f"Container '{container_name}' created.")
except Exception as e:
    print(f"Container already exists: {e}")

# Upload a file
blob_client = container_client.get_blob_client(blob_name)
with open(local_file_path, "rb") as file:
    blob_client.upload_blob(file, overwrite=True)
    print(f"File '{blob_name}' uploaded successfully.")
