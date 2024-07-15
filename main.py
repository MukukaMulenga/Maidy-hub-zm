from fastapi import FastAPI 

app = FastAPI()

@app.get('/',tags=['root'])
async def getDefault():
    return {
        'message':"Welcome to maidy hub zm backend!"
    }


@app.get('/api/users',tags=['users'])
async def getUsers():
    return {
        [
            {'name':"Mukuka Mulenga",'program':"Diploma in computerr studies"}
        ]
    }