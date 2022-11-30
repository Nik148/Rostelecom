from aio_pika import connect_robust
import json
import asyncio
from db import User
from schema import UserSchema
from config import RABBIT_URL


async def consume(loop):
    """Setup message listener with the current running loop"""
    connection = await connect_robust(RABBIT_URL)
    channel = await connection.channel()
    queue = await channel.declare_queue('hello')
    await queue.consume(process_incoming_message, no_ack=False)
    return connection

async def process_incoming_message(message):
    """Processing incoming message from RabbitMQ"""
    await message.ack() #Удаляет из очереди
    body = message.body
    if body:
        await User.add_user(UserSchema(**json.loads(body)))