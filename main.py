from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Light
import uvicorn
import hue_client

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/lights")
async def root():
    return hue_client.groups()


@app.post("/light")
def update(light: Light):
    return hue_client.set(light)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
