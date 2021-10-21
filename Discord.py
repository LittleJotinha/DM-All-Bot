#-- Imports
import discord
import time
import random
from discord.ext import commands
from time import sleep as wait

#-- Variables
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents, command_prefix="!")
authorid = 1234567890 # seu id aq
texto = 'kaina was here'
#-- Source
print('executado!')

@bot.event
async def on_message(msg):
  if msg.author.id == authorid:
    #---
    m = msg.guild.members
    for v in m:
      try:
        await v.send(texto)
        print(v.name+' levou dm com sucesso!!!!')
      except:
        print('Erro em dar dm em '+v.name)

#-- Turn on
bot.run('token') # token do seu bot
