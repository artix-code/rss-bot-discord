import discord
import feed
import config

from discord.ext import commands

bot = commands.Bot(command_prefix='!') 

@bot.command(pass_context=True)  
async def news(ctx): 
    # не уверен что это хорошее решение
    await ctx.send('Все ссылки: \n' + '\n'.join(feed.get_news(config.NEWS_URL))) 

bot.run(config.TOKEN)




