from fastapi import FastAPI

import asyncio
import fastapi
import aiohttp
import uvicorn
import json
import requests

app = FastAPI()

url = 'https://w2.checkwa.com/check/'

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/whatsapp")
async def whatsapp_check(number: int, numbers: list=None) -> dict:
    results = []

    #connector = aiohttp.TCPConnector(limit=3) # асинхронные запросы, у сервиса лимит на 3 чека одновременно, можно поднять
    session = aiohttp.ClientSession()

    payload = json.dumps({
        "user": "theowll",
        "apikey": "43fd05-f190cc-0bfed7-26745e-b58da8",
        "number": number
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = await session.post(url, data=payload, headers=headers)
    responsejson = await response.json()
    await session.close()

    print(f"created task {number} // {responsejson}")

    return responsejson

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)