import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('clean_ecom.csv')

engine = create_engine(
    "mysql+pymysql://root:0902@localhost/ecom_analysis"
)

df.to_sql('ecom_analysis',
    con=engine,
    index=False,
    if_exists='replace'
    )

print('Data succesfully imported.....')