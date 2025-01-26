from azure.storage.blob import BlobServiceClient

# Replace with your connection string
connection_string = "<your_connection_string>"

# Define container and blob details
container_name = "state-health-data"  # Container name
blob_name = "employee.csv"   # Name of the file in ABS
local_file_path = "./data/employee.csv"  # Path to local file

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Ensure the container exists (create it if necessary)
container_client = blob_service_client.get_container_client(container_name)
try:
    container_client.create_container()
    print(f"Container '{container_name}' created.")
except Exception as e:
    print(f"Container already exists: {e}")

# Upload the file
blob_client = container_client.get_blob_client(blob_name)
with open(local_file_path, "rb") as file:
    blob_client.upload_blob(file, overwrite=True)
    print(f"File '{blob_name}' uploaded successfully to container '{container_name}'.")
