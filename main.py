import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

TOKEN = 'здесь токен'

# команды
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./{attachment.filename}')
            await ctx.send(get_class(image=f'./{attachment.filename}', model='keras_model.h5' , labels='labels.txt'))
    else:
        await ctx.send('вы забыли прикрепить картинку')

bot.run(TOKEN)
