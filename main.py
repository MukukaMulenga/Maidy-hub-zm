from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  

app = FastAPI()

origins = ['https://maidy-hub--zm.web.app','http://localhost:5173']

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],       
)

@app.get('/',tags=['root'])
async def getDefault():
    return {
        'message':"Welcome to maidy hub zm backend!"
    }


@app.get('/api/users',tags=['users'])
async def getUsers():
    return {
        
            'users': {'name':"Mukuka Mulenga",'program':"Diploma in computerr studies"}

            }