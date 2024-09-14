import discord
from discord.ext import commands
import random
import json

# Define bot intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

# Create bot instance with prefix '!'
bot = commands.Bot(command_prefix='!', intents=intents)

# Load character data from a file
with open('characters.json', 'r') as f:
    characters_data = json.load(f)

# Load rarity colors from JSON file
with open('rarity_colors.json', 'r') as file:
    rarity_colors = json.load(file)

def roll_character():
    # Define rarity probabilities
    rarities = {'S': 0.015, 'A': 0.085, 'B': 0.20, 'C': 0.70}
    
    # Choose a rarity based on weighted probabilities
    chosen_rarity = random.choices(list(rarities.keys()), weights=rarities.values())[0]
    
    # Filter characters by chosen rarity
    available_characters = [char for char in characters_data['characters'] if char['rarity'] == chosen_rarity]
    
    # Pick a random character from the filtered list
    return random.choice(available_characters)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # Optionally send a message to a specific channel (commented out for now)
    channel = bot.get_channel(1284066726874583133)
    if channel:
        await channel.send('Hello! I am online.')
        # Updated embed message for testing
        embed = discord.Embed(
            title="Buwen's Testing",
            description="Version: 0.1.1\nCurrent features being attempted: Responsiveness and rolling commands\nIncorporating characters list thus far",
            color=0x00ff00
        )
        await channel.send(embed=embed)

# Command: Respond to '!ping'
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Roll a character
@bot.command(name='roll')
async def roll(ctx):
    character = roll_character()

     # Convert rarity to color
    rarity_color = int(rarity_colors.get(character['rarity'], "#FFFFFF").replace("#", "0x"), 16)
    
    # Create an embed with the character details
    embed = discord.Embed(
        title=f"{character['rarity']} - {character['name']}",
        description=(
            f"Source: {character['source']} by {character['first_author']}\n"
            f"Description: {character['description']}"
        ),
        color=rarity_color
    )
    embed.add_field(name="Element", value=character['element'], inline=False)
    embed.add_field(name="Type", value=character['type'], inline=False)
    
    # Send the embed to the channel
    await ctx.send(embed=embed)

# Event: Handle command errors
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'An error occurred: {error}')

# Run the bot with the token
TOKEN = 'MY_TOKEN'
bot.run(TOKEN)