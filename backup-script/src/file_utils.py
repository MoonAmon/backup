import shutil

def copy_file(source, destination):
    shutil.copy2(source, destination)

def get_files_by_type(source_dir, file_types):
    import os
    files_to_backup = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if any(file.endswith(file_type) for file_type in file_types):
                files_to_backup.append(os.path.join(root, file))
    return files_to_backup

def create_backup_directory(backup_dir):
    import os
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)