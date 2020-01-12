from discord.ext import commands
from keep_alive import keep_alive
from discord.utils import get


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

cogs = ['cogs.basic', 'cogs.help', 'cogs.b_info', 'cogs.invite', 'cogs.roles', 'cogs.misc', 'cogs.tags']


@bot.event
async def on_ready():                                       
    print(f'Logged in as {bot.user.name} id:{bot.user.id}')
    for cog in cogs:
        bot.load_extension(cog)
        print(cog)
    return

@bot.event
async def on_member_join(member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = '```{0.mention}, welcome to {1.name}!```'.format(member, guild)
            await guild.system_channel.send(to_send)



keep_alive()
bot.run('token here', bot=True, reconnect=True)
