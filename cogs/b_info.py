from discord.ext import commands
import discord, time


class Stuff(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='info',
        description='Shows info on bot.',
        aliases=['i']
    )
    async def testing(self, ctx):
        embed=discord.Embed(title=':gear: discord utils', description='(rewrite version w/ cogs)', color=0x000000)
        url=self.bot.user.avatar_url
        embed.set_thumbnail(url=url)
        embed.add_field(name='__Stats__', value='discord.py version: {}\nPing time: {}ms\nShards: {}\nNum of guilds: {}'.format(discord.__version__, None, self.bot.shard_count, len(self.bot.guilds)), inline=True)
        embed.add_field(name='__Created by:__', value='Thel Vadam likes nothing', inline=True)
        embed.add_field(name='__Code__', value='Lang: Python 3.7\nLibrary: discord.py, discord.ext\nCogs: 7\nLines: 605\nFiles: 10 :sunglasses:\nMethod: rewrite', inline=False)
        embed.add_field(name='Invite link:', value='https://discordapp.com/api/oauth2/authorize?client_id=665674407611727915&permissions=8&scope=bot', inline=False)
        embed.add_field(name='Source:', value='https://github.com/insert-ctrl/discord-utils-src/tree/master', inline=False)
        embed.set_footer(text='ID: {}'.format(self.bot.user.id))
        sended=await ctx.send(embed=embed)
        await sended.add_reaction(emoji='👍')
        await sended.add_reaction(emoji='👎')
        await sended.add_reaction(emoji='⚙️')

    @commands.command(
        name='serverinfo',
        description='View server info.',
        aliases=[]
    )
    async def someother(self, ctx):
        embed=discord.Embed(title='__{}__'.format(ctx.guild), color=0x000000)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name='Server ID:', value='{}'.format(ctx.guild.id), inline=False)
        embed.add_field(name='Number of members:', value='{}'.format(len(ctx.guild.members)), inline=True)
        embed.add_field(name='Number of roles:', value='{}'.format(len(ctx.guild.roles)), inline=True)
        embed.add_field(name='__Channels__', value='Text: {}\nVoice: {}'.format(len(ctx.guild.text_channels), len(ctx.guild.voice_channels)), inline=False)
        embed.add_field(name='__Max members__:', value='{}'.format(ctx.guild.max_members), inline=False)
        await ctx.send(embed=embed)

    @commands.command(
        name='source',
        description='View bot src.',
        aliases=['src']
    )
    async def send_link(self, ctx):
        await ctx.send('https://github.com/insert-ctrl/discord-utils-src/tree/master')

    @commands.command(
        name='cogs',
        description='Nonems',
        aliases=[]
    )
    async def view_cogs(self, ctx):
        cogs = ['cogs.basic', 'cogs.help', 'cogs.b_info', 'cogs.invite', 'cogs.roles', 'cogs.misc', 'cogs.tags', 'cogs.mod']
        msg=await ctx.send('Getting cogs...')
        string=''
        for cog in cogs:
            string += cog
            string += '\n'
        time.sleep(0.75)
        await msg.edit(content='{}'.format(string))

def setup(bot):
    bot.add_cog(Stuff(bot))
