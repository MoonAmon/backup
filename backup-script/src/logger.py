import logging
import os

class Logger:
    def __init__(self, log_file='backup.log'):
        self.logger = logging.getLogger('BackupLogger')
        self.logger.setLevel(logging.DEBUG)

        # Create a file handler
        fh = logging.FileHandler(os.path.join('logs', log_file))
        fh.setLevel(logging.DEBUG)

        # Create a console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # Create a formatter and set it for both handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)