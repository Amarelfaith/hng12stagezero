from fastapi import FastAPI
from datetime import datetime 
from pydantic import BaseModel


app = FastAPI()

class ProfileResponse(BaseModel):
    email: str
    current_datetime: str
    github_url: str
    
    

@app.get("/profile", response_model=ProfileResponse)
def get_profile():
    return {

        "email": "abubakarelfaith@gmail.com",
        "current_datetime": datetime.utcnow().isoformat(),
        "github_url": "https://github.com/Amarelfaith/hng12stagezero"
    }
