import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("-----------------")
    await client.change_presence(game=discord.Game(name='zerobot 대화', type=1))


@client.event
async def on_message(message):
        if message.content.startswith("안녕 제로"):
            await client.send_message(message.channel, "안녕하세요!")

        if message.content.startswith('zero'):
            await client.send_message(message.channel, "저요?")

        if message.content.startswith('%도움말'):
            await client.send_message(message.channel, "안녕제로= 안녕하세요! zero= 저요? ")


client.run('NTQzMzI5MzAzOTQxODczNjY1.Dz6-Xw.4SvLRby1gI2d13-gTz7e-jHojK8')