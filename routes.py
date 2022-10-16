from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import services
from fastapi.responses import HTMLResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", response_class=HTMLResponse)
async def root():
    with open('shot.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/take_shot")
async def take_shot():
    services.take_shot()
    return {"message": "Request received."}

@app.get("/take_shot/{ounces}")
async def take_shot_o(ounces: float):
    services.take_shot_o(ounces)
    return {"message": "Request received."}