class Transformer:
    def __init__(self, config):
        self.config = config

    def transform(self, data):
        # Example: Transform data (e.g., rename columns)
        data = data.rename(columns=self.config['rename_columns'])
        return data
