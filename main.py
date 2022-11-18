import json
from fastapi import FastAPI
app = FastAPI()

@app.get("/GET")
async def root():
    num = int(input("Enter an integer number: "))
    return get(num)

def get(x):
    result = ''
    if x % 3==0: result +='G' 
    if x % 5==0: result +='N'
    output = {"result": result}
    return output if output else x


