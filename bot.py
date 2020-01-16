from discord.ext import commands
from keep_alive import keep_alive
from discord.utils import get
import discord

start=0

def get_prefix(client, message):

    prefixes = ['ut.', 'Util.', 'Utils.', 'u.', '[[']   

    if not message.guild:
        prefixes = ['ut.']   
    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(                         
    command_prefix=get_prefix,              
    description='A sorta useless Util bot.',  
    owner_id=640203987437748246,            
    case_insensitive=True             
)

cogs = ['cogs.basic', 'cogs.b_info', 'cogs.invite', 'cogs.roles', 'cogs.misc', 'cogs.tags', 'cogs.mod']


@bot.event
async def on_ready():                                       
    print(f'Logged in as {bot.user.name} id:{bot.user.id}')
    for cog in cogs:
        bot.load_extension(cog)
        print(cog)
    game=discord.Game('ut.help for help (duh)')
    await bot.change_presence(status=discord.Status.online, activity=game)
    return

@bot.event
async def on_member_join(member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = '```{0.mention}, welcome to {1.name}!```'.format(member, guild)
            await guild.system_channel.send(to_send)



keep_alive()
bot.run('NjY1Njc0NDA3NjExNzI3OTE1.XhpDnw.0Wy-z58Gz_HEgrWHQK3SgQkreGU', bot=True, reconnect=True)
