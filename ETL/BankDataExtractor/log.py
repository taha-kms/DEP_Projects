import os
import datetime

class Log:
    def __init__(self, log_file='files/log.txt'):
        self.log_file = log_file
        # Ensure the log file exists
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        open(self.log_file, 'a').close()  # Create file if it doesn't exist

    def _log(self, level, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, 'a') as f:
            f.write(f"{level} | {timestamp} | {message}\n")

    def info(self, message):
        self._log('INFO', message)

    def error(self, message):
        self._log('ERROR', message)
