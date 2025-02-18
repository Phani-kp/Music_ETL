from sqlalchemy import create_engine

class Loader:
    def __init__(self, config):
        self.config = config
        self.engine = create_engine(self.config['database_url'])

    def load(self, data):
        # Example: Load data into a SQL database
        data.to_sql(self.config['table_name'], self.engine, if_exists='replace', index=False)
