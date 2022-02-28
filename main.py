import discord
from discord.ext import commands

import conf


bot = commands.Bot(command_prefix='>')
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Bot is running')
    
       
@bot.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == 'hello':
        await message.channel.send('Hey there')

    await bot.process_commands(message)

        
@bot.command()
async def help(ctx):
    """
    Display help
    """
    embed = discord.Embed(
        title='Bot Commands',
        description='Welcome to the help section. Here are all the commands for this game!',
        color=discord.Colour.green()
    )
    embed.set_thumbnail(url='')
    embed.add_field(
        name='>help',
        value='List all of the commands',
        inline=True
    )
    embed.add_field(
        name='>info',
        value='Display info',
        inline=True
    )

    await ctx.send(embed=embed)
        
        
@bot.command()
async def info(ctx):
    """
    ctx - context (information about how the command was executed)
    >info
    """

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)
    

    
bot.run(conf.KEY)
