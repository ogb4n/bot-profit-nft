import discord, os, json, sqlite3, time
from discord.ext.commands import MissingPermissions
from discord.ext import commands
from logger import *

db = sqlite3.connect("db.sqlite")
cur = db.cursor()

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="Enable debug mode", action="store_true")
    args = parser.parse_args()
    return args

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
load_dotenv()

bot = commands.Bot(command_prefix= '!', intents=intents)
@bot.remove_command('help')


@bot.event
async def on_ready():
    logger.addInfo("Le bot est prêt")
    logger.addInfo(f"le bot est connecté au serveur")

    await bot.change_presence(activity=discord.Streaming(name="Dhoney", url="https://twitch.tv/idhoney"))


if __name__ == '__main__':
    args = getArgs()
    logger = Logger("logs.log", args.debug)
    token = os.getenv("TOKEN")
    bot.run(token)
