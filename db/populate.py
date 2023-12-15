import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from faker import Faker
import random

# Load environment variables
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
fake = Faker()

year = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
        '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
        '2017', '2018', '2019', '2020']

leading_cause = ['Accidents Except Drug Posioning (V01-X39, X43, X45-X59, Y85-Y86)', 'Cerebrovascular Disease (Stroke: I60-I69)', 'Alzheimers Disease (G30)', 'Septicemia (A40-A41)', 'Diabetes Mellitus (E10-E14)', 'Essential Hypertension and Renal Diseases (I10, I12)']

sex = ['F', 'M']

race_ethnicity = ['Asian and Pacific Islander', 'Black Non-Hispanic', 'White Non-Hispanic', 'Hispanic']

def insert_fake_data(engine):
    with engine.connect() as connection:
        # Insert fake data into the 'NYC' table
        for _ in range(num_records):
            record = {
                "year": random.choice(year),
                "leading_cause": random.choice(leading_cause),
                "sex": random.choice(sex),
                "race_ethnicity": random.choice(race_ethnicity),
                "deaths": str(random.randint(1, 1000)),  
                "death_rate": str(random.uniform(1, 20)),  
                "age_adjusted_death_rate": str(random.uniform(1, 20))  
            }
            query = text(
                "INSERT INTO NYC (year, leading_cause, sex, race_ethnicity, deaths, death_rate, age_adjusted_death_rate) "
                "VALUES (:year, :leading_cause, :sex, :race_ethnicity, :deaths, :death_rate, :age_adjusted_death_rate)"
            )
            connection.execute(query, record)

        connection.commit()

if __name__ == "__main__":
    # Specify the number of records you want to insert
    num_records = 50
    insert_fake_data(db_engine)
    print("Fake data insertion complete!")