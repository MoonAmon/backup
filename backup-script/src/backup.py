import os
import shutil
import json
from file_utils import create_backup_directory, get_files_by_type
from logger import Logger
from config import Config

def main():
    # Initialize logger
    logger = Logger()
    
    # Load configuration
    config = Config()
    source_dir = config.get_source_directory()
    backup_dir = config.get_backup_directory()
    file_types = config.get_file_types()

    # Create backup directory if it doesn't exist
    create_backup_directory(backup_dir)

    # Get files to backup
    files_to_backup = get_files_by_type(source_dir, file_types)

    # Backup files
    for file in files_to_backup:
        try:
            shutil.copy(file, backup_dir)
            logger.log_info(f"Backed up: {file} to {backup_dir}")
        except Exception as e:
            logger.log_error(f"Error backing up {file}: {e}")

if __name__ == "__main__":
    main()