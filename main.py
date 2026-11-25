import pandas as pd
from fastapi import FastAPI

app = FastAPI()

SHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1xeDb643KkXquTrzkn5m1vnB0E-RETqJSX2DjLyx3v5U"
    "/export?format=csv&gid=1488283114"
)


@app.get("/name")
def get_name():
    df = pd.read_csv(SHEET_URL, header=None)
    row = df.to_string(index = False, header = False
    return {"name": row}
