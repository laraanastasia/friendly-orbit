from typing import Final
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random 

#load token
load_dotenv()
TOKEN: Final[str]= os.getenv('DISCORD_TOKEN')


#BOT SETUP
intents = discord.Intents.default()
intents.message_content = True #NOQA
bot= commands.Bot(command_prefix="cat!",intents=intents)
#client.remove_command("help")

#Message Functionality
@bot.command()
async def no(ctx):
    await ctx.send("https://tenor.com/view/no-nope-cat-cute-gif-4544032")
@bot.command()
async def yes(ctx):
    await ctx.send("https://tenor.com/view/yes-yescat-cat-nodding-nod-gif-21702876")

@bot.command()
async def scream(ctx):
    await ctx.send("https://tenor.com/view/cry-crying-cat-crying-cat-cry-why-gif-27571714")

@bot.command()
async def hello(ctx):
    await ctx.send("miau! =^-^= ")

@bot.command()
async def bye(ctx):
    await ctx.send("es war katazisch mit dir zu reden ^^")   

@bot.command()
async def rand(ctx):
    catgif_list= ["https://tenor.com/view/cat-gif-27443459","https://tenor.com/view/angry-cat-triggered-ahhh-meeeeoow-gif-16764869","https://tenor.com/view/goofy-cat-cat-cat-dance-cat-funny-funny-gif-13226486845730141702","https://tenor.com/view/crunch-cat-luna-eat-gif-3997701764820700221","https://tenor.com/view/chipi-chapa-dubi-dubidu-boom-gif-17214381249162738138","https://tenor.com/view/cat-gif-21186965","https://tenor.com/view/cat-huh-cat-huh-etr-gif-15332443943609734737","https://tenor.com/view/cat-apple-gif-21978863","https://tenor.com/view/no-nope-cat-cute-gif-4544032","https://tenor.com/view/yes-yescat-cat-nodding-nod-gif-21702876","https://tenor.com/view/cats-cat-bunny-shake-head-gif-24738682","https://tenor.com/view/cry-crying-cat-crying-cat-cry-why-gif-27571714",]
    i=random.choice(catgif_list)
    await ctx.send(i)
@bot.command()
async def love(ctx):
    await ctx.send("""
     ∧,,,∧
(  ̳• · • ̳)
/    づ♡ 
                   """)

@bot.command()
async def list(ctx):
    await ctx.send(""""
    cat!no
    cat!yes
    cat!love
    cat!scream
    cat!random
                   """)
    
@bot.command()
async def alex(ctx):
    await ctx.send("https://tenor.com/view/put-out-the-candle-put-it-out-birthday-cat-candles-out-neatdad-gif-2956237863302866726")  

#Startup

@bot.event
async def on_ready():
    print(f'{bot.user} is now purring!')

# Incoming Messages
#@bot.event
#async def on_message(message: Message)-> None:
 #   if message.author == bot.user:
 #       return
    
  #  username: str=str(message.author)
  #  user_message: str = message.content
  #  channel: str = str(message.channel)

  #  print(f'[{channel}] {username}: "{user_message}')
    

#main entry point
def main()-> None:
    bot.run(token=TOKEN)

if __name__ == '__main__':
    main()

