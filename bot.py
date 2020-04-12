import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='&')

suck_enabled = False
suck_id = 0

@bot.event
async def on_message(message):
    if(message.author.bot == False):       
        if(suck_enabled == True and str(suck_id) == str(message.author.id)):
            await message.channel.send('suck my dick')       
    await bot.process_commands(message)

@bot.command()
async def suck(ctx, message):

    global suck_id
    global suck_enabled

    suck_enabled = not suck_enabled
    suck_id = message[3:21]
    


bot.run('Njk4NzE0NDkyODQ2MjExMTMy.XpJ2ww.drFonnMice4xO8vShhiNXdZ4mVU')