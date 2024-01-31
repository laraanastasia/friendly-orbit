from typing import Final
import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import random
import Karten

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

@bot.tree.command(name="hi")
async def hi(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! Nice to see you!")

@bot.tree.command(name="bye", description="bye")
async def bye(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention},es war katazisch mit dir zu reden ^^")
    
@bot.tree.command(name="ping",description="Sends the bot's latency.") 
async def ping(interaction:discord.Interaction): 
    await interaction.response.send_message(f"Pong,{interaction.user.mention}! Latency is {bot.latency}")

@bot.tree.command(name="anon_request", description="Do not worry about losing your face, nobody will know that it was you! ")
@app_commands.describe (suggestion = "What is your request?")
async def suggestion(interaction: discord.Interaction, suggestion: str):
    print(f'User: {interaction.user.name}, Suggestion: {suggestion}, Guild: {interaction.guild}, Channel: {interaction.channel}')
    await interaction.response.send_message (f'Add suggestion: {suggestion}', ephemeral=True)
    await interaction.channel.send (f"{suggestion}")

@bot.tree.command(name="tarot",description="Whats your destiny?") 
@app_commands.describe(amount="How many cards do you want to pull?")
async def tarot(interaction: discord.Interaction,amount:int):
    x= Karten.feature(amount)
    await interaction.response.send_message (f'You pulled {amount} cards ', ephemeral=True)
    await interaction.channel.send(embed=x)
    

#"your card : "+x+"\n"+"your card's reading : "+y




#Startup
    


@bot.event
async def on_ready():
    print(f'{bot.user} is now purring!')
    try:
        synced =await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

 

#main entry point
def main()-> None:
    bot.run(token=TOKEN)

if __name__ == '__main__':
    main()

