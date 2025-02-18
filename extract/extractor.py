import pandas as pd

class Extractor:
    def __init__(self, config):
        self.config = config

    def extract(self):
        # Example: Extract data from a CSV file
        data = pd.read_csv(self.config['csv_path'])
        return data
