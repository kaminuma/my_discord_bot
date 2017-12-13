import discord
import asyncio
import random
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
     if  message.content.startswith(""):
            random.randint(1,20)
            r = random.randint(1,20)
            if r == 10 :
                await client.send_message(message.channel, "")
            else :
                    await client.send_message(message.channel, '')

client.run('')
