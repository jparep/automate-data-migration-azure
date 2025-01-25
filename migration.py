from dotenv import load_dotenv
import os
from azure.storage.blob import BlobServiceClient

# Load environment variables from .env file
load_dotenv()

# Retrieve the connection string
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

if not connection_string:
    raise ValueError("AZURE_STORAGE_CONNECTION_STRING is missing or not loaded properly.")

# Use the connection string to create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Container and blob details
container_name = "state-health-data"  # Container name
blob_name = "employee.csv"  # Name of the file in Azure Blob Storage
local_file_path = "./data/employee.csv"  # Local path to the file

# Ensure the container exists
container_client = blob_service_client.get_container_client(container_name)
try:
    container_client.create_container()
    print(f"Container '{container_name}' created.")
except Exception as e:
    print(f"Container already exists: {e}")

# Upload the file
try:
    blob_client = container_client.get_blob_client(blob_name)
    with open(local_file_path, "rb") as file:
        blob_client.upload_blob(file, overwrite=True)
        print(f"File '{blob_name}' uploaded successfully to container '{container_name}'.")
except FileNotFoundError:
    print(f"Error: File '{local_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
