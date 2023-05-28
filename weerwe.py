import discord
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    elif message.content.startswith('$hello'):
        await message.channel.send("Hi!")

    elif message.content.startswith('$sovet'):
        await message.channel.send("Сортировать мусор для специальных баков с мусором, Не портить растения, Не шуметь не включать громкую музыку, Не использоватьна природе бытовую химию")

    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith("$password"):
        def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


client.run("MTEwNTkwNzcyOTcwMjMyMjIxNg.G-9OCa.jmTxsEf8m4vl7tNRW8eNzp8XWFWicXHeOdwjZk")
