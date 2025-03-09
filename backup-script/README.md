# Backup Script

This project provides a Python-based backup script that allows users to back up specific types of files from a source directory to a designated backup directory. The script is configurable, enabling users to specify which file types to include in the backup process.

## Project Structure

```
backup-script
├── src
│   ├── backup.py          # Main script to initiate the backup process
│   ├── config.py          # Configuration handling
│   ├── file_utils.py      # Utility functions for file operations
│   └── logger.py          # Logging setup
├── logs                   # Directory for log files
│   └── .gitkeep           # Keeps the logs directory in version control
├── config
│   └── backup_config.json  # Configuration settings in JSON format
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore             # Files and directories to ignore by Git
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/backup-script.git
   cd backup-script
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Before running the backup script, you need to configure the `backup_config.json` file located in the `config` directory. This file allows you to specify:

- `source_directory`: The directory from which files will be backed up.
- `backup_directory`: The directory where the backup will be stored.
- `file_types`: An array of file extensions to include in the backup (e.g., `[".txt", ".jpg"]`).

## Usage

To run the backup script, execute the following command in your terminal:

```
python src/backup.py
```

Follow the prompts to select the types of files you wish to back up.

## Logging

The application logs its operations in the `logs` directory. You can check the log files for detailed information about the backup process, including any errors that may occur.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.