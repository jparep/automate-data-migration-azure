from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the connection string from .env
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# Debug: Print the connection string to verify it's loaded correctly (optional)
# print(f"Connection string: {connection_string}")

# Validate the connection string
if not connection_string or "AccountName" not in connection_string:
    raise ValueError("AZURE_STORAGE_CONNECTION_STRING is missing required details or not loaded properly. Check your .env file.")

# Define container and blob details
container_name = "health-data-container"
blob_name = "employee.csv"
local_file_path = "./data/employee.csv"
downloaded_file_path = "./data/downloaded_employee.csv"  # Path for downloaded file

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Access the container
container_client = blob_service_client.get_container_client(container_name)
if not container_client.exists():
    raise ValueError(f"Container '{container_name}' does not exist in the storage account.")

# Upload the file
blob_client = container_client.get_blob_client(blob_name)
with open(local_file_path, "rb") as file:
    blob_client.upload_blob(file, overwrite=True)
    print(f"File '{blob_name}' uploaded successfully to container '{container_name}'.")

# Download the file
with open(downloaded_file_path, "wb") as downloaded_file:
    download_stream = blob_client.download_blob()
    downloaded_file.write(download_stream.readall())
    print(f"File '{blob_name}' downloaded successfully to '{downloaded_file_path}'.")
