import yaml
from extract.extractor import Extractor
from transform.transformer import Transformer
from load.loader import Loader

def main():
    try:
        # Load configuration
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        
        # Extract data
        extractor = Extractor(config['extract'])
        data = extractor.extract()
        
        # Transform data
        transformer = Transformer(config['transform'])
        transformed_data = transformer.transform(data)
        
        # Load data
        loader = Loader(config['load'])
        loader.load(transformed_data)
    
    except FileNotFoundError:
        print("Configuration file not found.")
    except KeyError as e:
        print(f"Missing configuration for: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
