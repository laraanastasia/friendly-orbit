from typing import Final
import os
from discord.ext import commands
from discord import Intents, Client,Message
from dotenv import load_dotenv
from response import get_response

#load token
load_dotenv()
TOKEN: Final[str]= os.getenv('DISCORD_TOKEN')


#BOT SETUP
intents:Intents = Intents.default()
intents.message_content = True #NOQA
bot= commands.Bot(command_prefix="cat!",intents=intents)
#client.remove_command("help")

#Message Functionality

async def send_message(message:Message, user_message: str)-> None:
    if not user_message:
        print("Message was empty becouse intents were not enabled ")
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

#Startup

@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now purring!')

# Incoming Messages
@bot.event
async def on_message(message: Message)-> None:
    if message.author == bot.user:
        return
    
    username: str=str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}')
    await send_message(message, user_message)

#main entry point
def main()-> None:
    bot.run(token=TOKEN)

if __name__ == '__main__':
    main()