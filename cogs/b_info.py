from discord.ext import commands
import discord


class Stuff(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='info',
        description='Shows info on bot.',
        aliases=['i']
    )
    async def testing(self, ctx):
        embed=discord.Embed(title='discord utils', description='(rewrite version w/ cogs)', color=0x000000)
        url=self.bot.user.avatar_url
        embed.set_thumbnail(url=url)
        embed.add_field(name='__Stats__', value='discord.py version: {}\nPing time: {}ms'.format(discord.__version__, None), inline=True)
        embed.add_field(name='__Created by:__', value='Thel Vadam likes nothing', inline=True)
        embed.add_field(name='__Code__', value='Lang: Python 3.7\nLibrary: discord.py, discord.ext\nCogs: 7\nLines: 605\nFiles: 10 :sunglasses:\nMethod: rewrite', inline=False)
        embed.add_field(name='Invite link:', value='https://discordapp.com/api/oauth2/authorize?client_id=665674407611727915&permissions=8&scope=bot')
        embed.add_field(name='Source:', value='', inline=False)
        embed.set_footer(text='ID: {}'.format(self.bot.user.id))
        await ctx.send(embed=embed)

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
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Stuff(bot))
