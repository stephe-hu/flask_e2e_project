import os
from dotenv import load_dotenv
from pandas import read_sql, DataFrame
from sqlalchemy import create_engine, inspect
from db.python_populate import insert_data

# Load environment variables from .env file
load_dotenv() 

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)


def get_tables(engine):
    """Get list of tables."""
    inspector = inspect(engine)
    return inspector.get_table_names()

def execute_query_to_dataframe(query: str, engine):
    """Execute SQL query and return result as a DataFrame."""
    return read_sql(query, engine)


# Example usage
tables = get_tables(db_engine)
print("Tables in the database:", tables)

# Retrieve data from the 'NYC' table
sql_query_nyc = "SELECT * FROM NYC"  # Modify as per your table
nyc_df = execute_query_to_dataframe(sql_query_nyc, db_engine)

# Print the DataFrame
print("Data from 'NYC' table:")
print(nyc_df)