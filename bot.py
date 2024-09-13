import discord
from discord.ext import commands

# Define intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Create bot instance with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: On Ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    channel = bot.get_channel(1284066726874583133)  # Replace with your text channel ID
    if channel:
        await channel.send('Hello! I am online.')

# Command: Ping
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot
TOKEN = 'MTI4NDA0ODYwMTkwNzA3MzA5OQ.G2z8v-.KKaerAOkEuazl122NjPDqUGKc1qm0o5IfyoL2A'
bot.run(TOKEN)