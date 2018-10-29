

import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''


bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

def main():
    getUser('186439054139588608')

def getUser(id):
    flaz = server.get_member('self',id)
    print(flaz)

if __name__ == '__main__':
    bot.run('email','pass')
    main()
