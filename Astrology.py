import discord
Signs=["Aries ♈️","Taurus ♉️:","Gemini ♊️","Cancer ♋️","Leo ♌️","Virgo ♍️","Libra ♎️","Scorpio ♏️","Sagittarius ♐️","Capricorn ♑️","Aquarius ♒️","Pisces ♓️"]
Dates=["March 21 - April 19","April 20 - May 20"," May 21 - June 20","June 21 - July 22","July 23 - August 22","August 23 - September 22","September 23 - October 22","October 23 - November 21","November 22 - December 21","December 22 - January 19","January 20 - February 18","February 19 - March 20"]

def make_embed():
    embed = discord.Embed(title="Astrology Signs") 
    embed.set_footer(text="‎",icon_url="https://cdn.discordapp.com/attachments/1179867724592193637/1202193113389473832/image.png?ex=65cc9095&is=65ba1b95&hm=dddcb13b59f2772b6b4b352884d8c9424eea27a426e6ac544f854addb88a2ff1&" ) 
    for i in  range(11):
        embed.add_field(name=Signs[i], value=f"{'-'*10}\n {Dates[i]} \n{'-'*10} ", inline=False)

    return embed



