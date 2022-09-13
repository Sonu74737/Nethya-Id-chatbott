from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re
from magic_filter import F
import asyncio


API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
STRING = os.environ.get("STRING", None) 
MONGO_URL = os.environ.get("MONGO_URL", None)


bot = Client(STRING, API_ID, API_HASH)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]


@bot.on_message(
    filters.command("/chatboton", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def addchat(_, message): 
    LogicDB = MongoClient(MONGO_URL)
    
    Logic = LogicDB["LogicDB"]["Logic"] 
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_Logic = Logic.find_one({"chat_id": message.chat.id})
    if not is_Logic:
        Logic.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"Logic-AI Is Enabled")
    else:
        await message.reply_text(f"Logic-AI Is Enabled!")


@bot.on_message(
    filters.command("/chatbotoff", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def rmchat(_, message): 
    LogicDB = MongoClient(MONGO_URL)
    
    Logic = LogicDB["LogicDB"]["Logic"] 
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_Logic = Logic.find_one({"chat_id": message.chat.id})
    if not is_Logic:
        await message.reply_text("Logic-AI is Disabled! ")
    else:
        Logic.delete_one({"chat_id": message.chat.id})
        await message.reply_text("Logic-AI is disable!")





@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def LogicAI(client: Client, message: Message):

   LogicDB = MongoClient(MONGO_URL)
    
   Logic = LogicDB["LogicDB"]["Logic"] 

   is_Logic = Logic.find_one({"chat_id": message.chat.id})
   if is_Logic:
       if message.reply_to_message:      
           botget = await bot.get_me()
           botid = botget.id
           if not message.reply_to_message.from_user.id == botid:
               return
           await bot.send_chat_action(message.chat.id, "typing")
           if not message.text:
               msg = "/"
           else:
               msg = message.text
           try: 
               x = requests.get(f"https://kukiapi.xyz/api/apikey=5470479796-KUKIHS0Joi0bl5/message={msg}").json()
               x = x['reply']
               await asyncio.sleep(1)
           except Exception as e:
               error = str(e)
           await message.reply_text(x)
           
   


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def LogicAI(client: Client, message: Message):
    await bot.send_chat_action(message.chat.id, "typing")
    if not message.text:
        msg = "/"
    else:
        msg = message.text
    try:
        x = requests.get(f"https://kukiapi.xyz/api/apikey=5470479796-KUKIHS0Joi0bl5/message={msg}").json()
        x = x['reply']
        await asyncio.sleep(1)
    except Exception as e:
        ERROR = str(e)
   
    



@bot.on_message(
    filters.command("chat", prefixes=["/", ".", "?", "-"]))
async def LogicAI(client: Client, message: Message):
    await bot.send_chat_action(message.chat.id, "typing")
    if not message.text:
        msg = "/"
    else:
        msg = message.text.replace(message.text.split(" ")[0], "")
    try:
        x = requests.get(f"https://Kukiapi.xyz/api/apikey=5470479796-KUKIHS0Joi0bl5/message={msg}").json()
        x = x['reply']
        await asyncio.sleep(1)
    except Exception as e:
        ERROR = str(e)
    
    





@bot.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start(client, message):
    self = await bot.get_me()
    busername = self.username
    if message.chat.type != "private":
        
        await message.reply("Hello")
                            
        
    else:
       
        
        Pass



@bot.on_message(filters.command(["allo"], prefixes=["h"]))
async def help(client, message):
    self = await bot.get_me()
    busername = self.username
    if message.chat.type != "private":
        
        await message.reply("Hey!")
      

@bot.on_message(filters.command(["ii"], prefixes=["h"]))
async def help(client, message):
    self = await bot.get_me()
    busername = self.username
    if message.chat.type != "private":
        
        await message.reply("Hey!!")
        

  



bot.run()

