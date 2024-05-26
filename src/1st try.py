'''
import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function

connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
print('Iniciando conexion...')
engine = create_engine(connection_string).execution_options(autocommit=True)
engine.connect()


# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
result_dataFrame = pd.read_sql("Select * from books;", engine)
print(result_dataFrame)
result_dataFrame = pd.read_sql("SELECT sampledb FROM information_schema.tables WHERE table_schema = 'public';", engine)
print(result_dataFrame)
# 4) Use pandas to print one of the tables as dataframes using read_sql function
'''