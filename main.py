from fastapi import FastAPI 

app = FastAPI()

@app.get('/',tags=['root'])
async def getDefault():
    return {
        'message':"Welcome to maidy hub zm backend!"
    }