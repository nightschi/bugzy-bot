import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import time

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN') # Place DISCORD_BOT_TOKEN variable containing your discord bot token in .env file.
CHANNEL_ID = os.getenv('CHANNEL_ID') # Replace with the specific channel ID.
ROLE_NAME = os.getenv('ROLE_NAME') # Replace with the specific role name.

intents = discord.Intents.default()

intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=';', intents=intents)

# Log when the bot is ready.
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}.')

# Reply with explode gif.
@bot.command()
async def explode(ctx):
    await ctx.reply('https://tenor.com/view/wake-up-gif-12100055351253481367')

# Ping a role in a channel when a message is sent in that channel.
# The bot cannot trigger itself.
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.channel.id == int(CHANNEL_ID):
        role = discord.utils.get(message.guild.roles, name=ROLE_NAME)
        await message.channel.send(f'{role.mention}, {message.author.mention} has sent a message in this channel.')
    await bot.process_commands(message)

# Run the bot.
bot.run(DISCORD_BOT_TOKEN)
