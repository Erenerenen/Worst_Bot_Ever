from django.apps import apps
import discord
from discord.ext import commands
#from webserver import keep_alive


#bot = commands.Bot(command_prefix="")
client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}',format(client))

@client.event
async def on_message(message):
  
    if message.channel.name == 'porcaylamuhabbet':
      if message.author == client.user:
        return
      await message.channel.send('somethin')

#bot.command(pass_context=True)
#async def sex(ctx):
  #enbed = discord.Enbed(
    #title="Nesin lan sen",
    
  #)
 #await msg.add_reaction('Komur')
 # await msg.add_reaction('Sabun')
 # await ctx.message.add_reaction('Orospu cocugu')
    


#keep_alive()


client.run('OTgzNjYwMjA2NjI4MTcxNzk2.GR7Tg2.Bvf5Vp3lQHFdvBqPd1kGx8qltQprs4saOMeC6g')