import os
from dotenv import load_dotenv

class ConfigLoader:
    def __init__(self, env_path='.env'):
        self.env_path = env_path
        self.load_env_config()

    def load_env_config(self):
        load_dotenv(self.env_path)
        self.base_path = os.getenv('BASE_PATH')
        self.api_key = os.getenv('API_KEY')
        self.log_dir = os.getenv('LOG_DIR')
        self.log_file = os.getenv('LOG_FILE')

    def get_env_variables(self):
        return {
            'BASE_PATH': self.base_path,
            'API_KEY': self.api_key,
            'LOG_DIR': self.log_dir,
            'LOG_FILE': self.log_file
        }