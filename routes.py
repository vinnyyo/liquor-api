from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import services

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_status")
async def get_status():
    output = services.get_status()
    return output

@app.get("/take_shot")
async def take_shot():
    services.take_shot()
    return {"message": "Request received."}

@app.get("/take_shot/{ounces}")
async def take_shot_o(ounces: float):
    services.take_shot_o(ounces)
    return {"message": "Request received."}