import discord
from discord.ext import commands

Dey = commands.Bot(command_prefix = '/')

@Dey.event
async def on_ready():
    print("-----BOT_Dey is online-----\n")

@Dey.event
async def on_member_join(member):
    print(f'[member] has came.\n')
        '''
    channel = Dey.get_channel(366077676097634304)
    await channel.send(f'[member] has came.\n'
        '''
Dey.run("NjAxNjI2NTk0Nzc1NDAwNDc4.XTFLsQ.hqHxQuPo5vbDhiykBxvgQiqYJVM")