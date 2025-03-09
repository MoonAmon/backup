class Config:
    def __init__(self, config_file):
        import json
        with open(config_file, 'r') as file:
            self.config = json.load(file)

    def get_source_directory(self):
        return self.config.get('source_directory')

    def get_backup_directory(self):
        return self.config.get('backup_directory')

    def get_file_types(self):
        return self.config.get('file_types', [])