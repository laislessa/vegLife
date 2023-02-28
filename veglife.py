from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def inicio():
    return {"texto":"Living a green life!"} 

@app.get('/home')
async def home():
    return {"vegLife"} 