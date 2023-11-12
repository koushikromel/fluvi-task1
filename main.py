from fastapi import FastAPI, Query
import random
import string


app = FastAPI()

@app.get("/generate_password")
async def generate_password(max_length: int = Query(default=20, description="Maximum length of the password to be generated")):
    """
    Generate Random password
    
    Parameters:
        max_length(int): Maximun Length of the password to be generated
    
    Returns:
        password(str): Randomly generated password
    """
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=max_length))
    
    return {"password": password}