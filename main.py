from pymongo import MongoClient
from uuid import uuid4
import os
from dotenv import load_dotenv
import datetime
import asyncio

load_dotenv()

mongoDB = os.getenv('MONGO_DB_KEY')
client = MongoClient(mongoDB)

db = client["jetickets"]

custumer = db["database_tickets"]


def registerTicket(title, category, description, amount, date, time):
    id = int(uuid4()) >> 100
    ticket = {
                'title': title,
                'category' :category,
                'description': description,
                'amount': amount,
                'date': date,
                'time': time   
            }
    ticket['_id'] = id
    custumer.insert_one(ticket).inserted_id
    return ticket

def deleteTicket(id):
    ticket = {"_id": id}
    custumer.delete_one(ticket)

