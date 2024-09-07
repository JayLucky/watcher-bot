import discord
from discord.ext import commands
import json
import datetime

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_voice_state_update(member, before, after):
    notification_channel = bot.get_channel(config['notification_channel_id'])
    timestamp = discord.utils.format_dt(datetime.datetime.now(), style='f')
    
    if before.channel is None and after.channel is not None:
        # Member joined a voice channel
        await notification_channel.send(f'{timestamp} - {member.name} joined the voice channel {after.channel.name}!')
    elif before.channel is not None and after.channel is None:
        # Member left a voice channel
        await notification_channel.send(f'{timestamp} - {member.name} left the voice channel {before.channel.name}!')

bot.run(config['token'])