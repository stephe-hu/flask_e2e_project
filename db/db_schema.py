"""

pip install sqlalchemy alembic mysql-connector-python
pip install pymysql
"""

## Part 1 - Define SQLAlchemy models 

from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

databaseURL = os.getenv("DB_URL")

Base = declarative_base()

class NYC(Base):
    __tablename__ = 'NYC'

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    leading_cause = Column(String(100), nullable=False)
    sex = Column(String(10), nullable=False)
    race_ethnicity = Column(String(50))
    deaths = Column(Integer, nullable=False)
    death_rate = Column(Integer, nullable=False)
    age_adjusted_death_rate = Column(Integer, nullable=False)


### Part 2 - initial sqlalchemy-engine to connect to db:
engine = create_engine(databaseURL)

## Test connection
inspector = inspect(engine)
inspector.get_table_names()


### Part 3 - create the tables using sqlalchemy models, with no raw SQL required:

Base.metadata.create_all(engine)

### Running migrations 
""" these steps are then performed in the termainl, outside of your python code

1. alembic init migrations
` alembic init migrations `

2. edit alembic.ini to point to your database
` sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name `

3. edit env.py to point to your models
`from db_schema import Base`
`target_metadata = Base.metadata `

4. create a migration
` alembic revision --autogenerate -m "create tables" `

5. run the migration
` alembic upgrade head `

in addition, you can run ` alembic history ` to see the history of migrations
or you can run with the --sql flag to see the raw SQL that will be executed

so it could be like:
` alembic upgrade head --sql `

or if you then want to save it:
` alembic upgrade head --sql > migration.sql `

6. check the database

7. roll back: To roll back a migration in Alembic, you can use the downgrade command. 
The downgrade command allows you to revert the database schema to a previous 
migration version. Here's how you can use it:

`alembic downgrade <target_revision>` 

or if you want to roll back to the previous version, you can use the -1 flag:
`alembic downgrade -1`
 

"""

