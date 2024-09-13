import discord
from discord.ext import commands

# Define bot intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

# Create bot instance with prefix '!'
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # Optionally send a message to a specific channel (commented out for now)
    channel = bot.get_channel(1284066726874583133)
    if channel:
        await channel.send('Hello! I am online.')
        # this is a test embed text thingy
        embed = discord.Embed(title="Character Name: Volta", description="Harnesses the power of lightning to disrupt her opponents.", color=0x00ff00)
        embed.add_field(name="Faction", value="Shine", inline=False)
        embed.add_field(name="Special Skill", value="Lightning Rod", inline=False)
        embed.add_field(name="Effect", value="Stuns the enemy for the first turn.", inline=False)
        embed.add_field(name="Chance", value="100%", inline=False)
        await channel.send(embed=embed)

# Command: Respond to '!ping'
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Event: Handle command errors
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'An error occurred: {error}')

# Run the bot with the token
TOKEN = 'MY_TOKEN'
bot.run(TOKEN)