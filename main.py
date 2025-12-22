import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN') # Place ISCORD_BOT_TOKEN variable containing your discord bot token in .env file.
USER_ID = os.getenv('USER_ID') # Replace with the specific user ID.

intents = discord.Intents.default()

intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=';', intents=intents)

# Log when the bot is ready.
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}.\n')

# Log messages sent to bot.
@bot.event
async def on_message(message):
    print(f'{message.author.name} said: {message.content}')
    await bot.process_commands(message)

# Assign a specific role to a user when they use the 'assign' command.
@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name='streamer-ping')
    await ctx.author.add_roles(role)
    await ctx.send(f'{ctx.author.mention}, you have been assigned the streamer ping role.')

# Remove a specific role from a user when they use the 'remove' command.
@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name='streamer-ping')
    await ctx.author.remove_roles(role)
    await ctx.send(f'{ctx.author.mention}, the streamer ping role has been removed from you.')

# Reply with explode gif.
@bot.command()
async def explode(ctx):
    await ctx.reply('https://tenor.com/view/wake-up-gif-12100055351253481367')

# Ping a certain role when a new message from a specific user is received.
@bot.event
async def on_message(message):
    if message.author.id == int(USER_ID):  # Replace with the specific user ID
        role = discord.utils.get(message.guild.roles, name='streamer-ping')  # Replace with the specific role name
        if role:
            await message.channel.send(f'{role.mention}, a new message from {message.author.mention} has been received.')
    await bot.process_commands(message)

# Run the bot.
bot.run(DISCORD_BOT_TOKEN)