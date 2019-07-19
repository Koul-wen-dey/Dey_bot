import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding = 'utf8') as jset:
    jdata = json.load(jset)
Dey = commands.Bot(command_prefix = '/')

@Dey.event
async def on_ready():
    print("-----BOT_Dey is online-----\n")

@Dey.event
async def on_member_join(member):
    print(f'{member} has came.\n')   
    #channel = Dey.get_channel(366077676097634304)
    #await channel.send(member + 'has came.')
@Dey.event
async def on_member_remove(member):
    print(f'{member} has gone.\n')   
    #channel = Dey.get_channel(366077676097634304)
    #await channel.send(member + 'has gone.')

@Dey.command()
async def ping(ctx):
    await ctx.send(Dey.latency*1000)
Dey.run(jdata['TOKEN'])