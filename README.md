# Automating Data Migration to Azure Blob Storage

This project automates the process of migrating data to Azure Blob Storage. The Python script provided ensures that new data is updated in Azure on a regular schedule.

## Prerequisites

- Python 3.x
- Azure Storage Account
- Azure Storage Blob SDK for Python

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/automate-data-migration-azure.git
    cd automate-data-migration-azure
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Set up your Azure Storage Account and get the connection string.
2. Create a `.env` file in the project directory and add your Azure Storage connection string:
    ```env
    AZURE_STORAGE_CONNECTION_STRING=your_connection_string_here
    ```

## Usage

1. Run the Python script to migrate data to Azure Blob Storage:
    ```sh
    python migrate_data.py
    ```

2. To schedule the script to run regularly, you can use a task scheduler like `cron` (Linux/macOS) or Task Scheduler (Windows).

### Example `cron` job (Linux/macOS)

To run the script every day at midnight, add the following line to your `crontab`:
```sh
0 0 * * * /usr/bin/python3 /path/to/your/project/migrate_data.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact

For any questions or issues, please contact [contact@joshuaparep.com](mailto:contact@joshuaparep.com).
