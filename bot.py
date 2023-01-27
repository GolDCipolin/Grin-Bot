import discord
import responses
from discord.ext import tasks, commands
import random

intents = discord.Intents.all()
grinlist = [] #fill the list with discord emotes


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = #discord bot token
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix='-', intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        send_messages.start()

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @tasks.loop(minutes=10)
    async def send_messages():
        await client.wait_until_ready()
        channel = client.get_channel() #fill in the channel ID
        index = random.randint(0, len(grinlist))
        await channel.send(grinlist[index])

    client.run(TOKEN)
