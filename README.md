# Music ETL

Music ETL (Extract, Transform, Load) project is designed to extract music data from various sources, transform the data into a usable format, and load it into a database for analysis.

## Features

- Extract music data from different sources (e.g., APIs, CSV files)
- Transform data into a consistent format
- Load data into a database
- Simple and extensible architecture

## Requirements

- Python 3.8+
- pandas
- SQLAlchemy

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Music_ETL.git
cd Music_ETL
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Configure your data sources and database connection in `config.yaml`.
2. Run the ETL pipeline:

```bash
python etl.py
```

## Project Structure

- `extract/`: Contains modules for extracting data from different sources.
- `transform/`: Contains modules for transforming the extracted data.
- `load/`: Contains modules for loading the transformed data into a database.
- `config.yaml`: Configuration file for data sources and database connection.
- `etl.py`: Main script to run the ETL pipeline.

## License

This project is licensed under the MIT License.
