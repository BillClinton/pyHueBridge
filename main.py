from fastapi import FastAPI
import uvicorn
import hue_client

app = FastAPI()


@app.get("/")
async def root():  
    return hue_client.groups()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)