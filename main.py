from fastapi import FastAPI
from models import Light
import uvicorn
import hue_client

app = FastAPI()

@app.get("/lights")
async def root():  
    return hue_client.groups()

@app.post("/light")
def update(light: Light):
    return hue_client.set(light)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)