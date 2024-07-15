from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  

app = FastAPI()

allowed_hosts = ['https://maidy-hub--zm.web.app/']

@app.middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=['*'],
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
        
            'users': [{'name':"Mukuka Mulenga",'program':"Diploma in computerr studies"}]

            }