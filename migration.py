from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the connection string from the .env file
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# Validate the connection string
if not connection_string:
    raise ValueError("AZURE_STORAGE_CONNECTION_STRING is not set or not loaded properly. Check your .env file.")

# Define container and blob details
container_name = "health-data-container"  # Container name
blob_name = "employee.csv"  # Name of the file in ABS
local_file_path = "./data/employee.csv"  # Path to local file

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Ensure the container exists (create it if necessary)
try:
    container_client = blob_service_client.get_container_client(container_name)
    container_client.create_container()
    print(f"Container '{container_name}' created.")
except Exception as e:
    print(f"Container already exists or cannot be created: {e}")

# Upload the file
try:
    blob_client = container_client.get_blob_client(blob_name)
    with open(local_file_path, "rb") as file:
        blob_client.upload_blob(file, overwrite=True)
        print(f"File '{blob_name}' uploaded successfully to container '{container_name}'.")
except FileNotFoundError:
    print(f"Error: Local file '{local_file_path}' not found.")
except Exception as e:
    print(f"An error occurred during file upload: {e}")
