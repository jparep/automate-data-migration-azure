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
