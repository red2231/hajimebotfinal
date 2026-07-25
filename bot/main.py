from dotenv import load_dotenv
load_dotenv()

from os import getenv
token = getenv('TOKEN')

from discord.ext import commands


but = commands.Bot(command_prefix="?")
@but.event
async def on_ready():
    print("bot pronto")

but.run(token)

