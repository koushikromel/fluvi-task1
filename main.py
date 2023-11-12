from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import random
import string


app = FastAPI(title="Random Password Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate_password", tags=["Password Generator"])
async def generate_password(max_length: int = Query(default=20, description="Maximum length of the password to be generated")):
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=max_length))
    
    return {"password": password}