import pandas as pd
from pathlib import Path
from fastapi import FastAPI 

p = Path(__file__).parent/"refer.xlsx"



app = FastAPI()

@app.get('/name')
def get_name():
    df = pd.read_excel(p,header = None)
    value = df.iloc[0,0]
    return {'name': str(value)}
