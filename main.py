import discord, os, json, sqlite3, time
from discord.ext.commands import MissingPermissions
from discord.ext import commands, tasks
from discord import app_commands, ui
from discord.utils import get
from logger import *

db = sqlite3.connect("avant-garde.sqlite")
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

	
@bot.command(aliases=['AddWallet', 'Addwallet', 'addWallet', 'Walletadd', 'walletadd', 'WalletAdd', 'walletAdd'])
async def addwallet(ctx, wallet_id=None, wallet_address=None):
    """Permet d'ajouter un wallet"""
    try:
        cur.execute(f"SELECT * FROM users WHERE discord_id = {ctx.author.id}")
        result = cur.fetchone()
        if not result:
            await ctx.send(f"oui ça marche {ctx.author.name}, tu possèdes l'id {ctx.author.id}, tu essaies d'ajouter le wallet {wallet_address} a ton wallet n°{wallet_id}")
            cur.execute(f"INSERT INTO users(discord_id, wallet_{wallet_id}) VALUES ({ctx.author.id}, '{wallet_address}');")
            db.commit()
        else:
            cur.execute(f"UPDATE users SET wallet_{wallet_id} = '{wallet_address}' WHERE discord_id = {ctx.author.id}")
            db.commit()
            logger.addInfo(f"Le wallet a bien été ajouté a la liste de {ctx.author.name}")
            await ctx.send(f"tu as bien ajouté le wallet a ta liste")
    except Exception as e:
        print(e)

@bot.command(aliases=['DelWallet', 'Delwallet', 'delWallet'])
async def delwallet(ctx, wallet_id=None):
    """Permet d'ajouter un wallet"""
    try:
        cur.execute(f"SELECT * FROM users WHERE discord_id = {ctx.author.id}")
        result = cur.fetchone()
        if not result:
            await ctx.send(f"oui ça marche {ctx.author.name}, tu possèdes l'id {ctx.author.id}, tu essaies d'ajouter le wallet {wallet_address} a ton wallet n°{wallet_id}")
            cur.execute(f"INSERT INTO users(discord_id, wallet_{wallet_id}) VALUES ({ctx.author.id}, 'none');")
            db.commit()
        else:
            cur.execute(f"UPDATE users SET wallet_{wallet_id} = 'none' WHERE discord_id = {ctx.author.id}")
            db.commit()
            logger.addInfo(f"Le wallet a bien été supprimé de la liste de {ctx.author.name}")
            await ctx.send(f"tu as bien supprimé le wallet a ta liste")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    args = getArgs()
    logger = Logger("logs.log", args.debug)
    token = os.getenv("TOKEN")
    bot.run(token)
