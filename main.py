import pandas as pd
from pathlib import Path
from fastapi import FastAPI 

sheet = "https://docs.google.com/spreadsheets/d/1xeDb643KkXquTrzkn5m1vnB0E-RETqJSX2DjLyx3v5U/edit?gid=1488283114#gid=1488283114"



app = FastAPI()

@app.get('/name')
def get_name():
    df = pd.read_excel(sheet,header = None)
    value = df.iloc[0,0]
    return {'name': str(value)}
