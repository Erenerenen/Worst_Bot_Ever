import discord
from discord.ext import commands
from django.apps import AppConfig
class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return

        print('yolo')
        if message.channel.name == 'porcaylamuhabbet':
           if message.author == self.user:
            return
        await message.channel.send('somethin')

   

class BotappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'botapp'
    def ready(self):
        print('yo')
        client = MyClient()  
        
        #client.run('OTgzNjYwMjA2NjI4MTcxNzk2.GR7Tg2.Bvf5Vp3lQHFdvBqPd1kGx8qltQprs4saOMeC6g')

















































#@client.event
#async def on_ready():
    #print('We have logged in as {0.user}',format(client))

#@client.event
#async def on_message(message):
  #print('yolo')
  #if message.channel.name == 'porcaylamuhabbet':
      # if message.author == client.user:
      #   return
      # await message.channel.send('somethin')
