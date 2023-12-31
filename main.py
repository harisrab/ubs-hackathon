import json
from typing import Optional

from challanges.airport import run_airport
from challanges.generations import run_generations
from challanges.minesweeper import run_minesweeper
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/airport')
async def airport(request: Request):
    payload = await request.json()

    print(f"[+] Payload Received {payload}")
    print("\n\n")

    results = run_airport(payload)

    print("\n\n")
    print(f"[+] Result Returned {results}")

    return results


@app.post('/digital-colony')
async def digital_colony(request: Request):
    payload = await request.json()

    print(f"[+] Payload Received {payload}")
    print("\n\n")

    results = run_generations(payload)

    print("\n\n")
    print(f"[+] Result Returned {results}")

    return results


@app.post('/minesweeper')
async def minesweeper(request: Request):
    payload = await request.json()

    print(f"[+] Payload Received {payload}")
    print("\n\n")

    results = run_minesweeper(payload)

    print("\n\n")
    print(f"[+] Result Returned {results}")

    return results
