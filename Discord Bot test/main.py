from discord import *
from discord.ext import commands
intents = Intents.default()
intents.message_content=True


Token = ''
client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print("Bot is Online!")
    print('--------------')

client.run(Token)
