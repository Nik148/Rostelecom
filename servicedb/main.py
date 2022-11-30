from fastapi import FastAPI
from aio_pika import connect_robust
import json
import asyncio
from schema import UserSchema
from db import database
from pika_service import consume


app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    loop = asyncio.get_running_loop()
    task = loop.create_task(consume(loop))
    await task


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



