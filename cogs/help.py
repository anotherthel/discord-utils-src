'''
FYI

This file is effectivly useless, as it is not updated, so it doesn't really help.
'''


from discord.ext import commands 
import discord


default=0x000000

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(name='help_all', description='Show all commands.', aliases=['h_a'])
    async def helpa(self, ctx):
        embed=discord.Embed(title='All commands', color=0x000000)
        embed.add_field(name='*Look below, not here!*', value='```announce, pin, ping, ping_times, invite, iass, nick_set, add_role, create_role, roles, info, serverinfo, create_tag, tags, del_tag, clear_tags, profile```')
        await ctx.send(embed=embed)

    @commands.command(
        name='help_page 1',
        description='Show help page 1',
        aliases=['hp 1']
    )
    async def help1(self, ctx):
        url=self.bot.user.avatar_url
        embed=discord.Embed(title='__Help__ (page 1)', description='Basic commands', color=0)
        embed.set_thumbnail(url=url)
        embed.add_field(name='`ping_times`', value='Get all ping times.', inline=False)
        embed.add_field(name='`ping`', value='Test your connection. Returns time in ms.', inline=False)
        embed.add_field(name='`announce`', value='Send an announcement.', inline=False)
        embed.add_field(name='`pin`', value='Awaits message which is then pinned.', inline=False)
        embed.set_footer(text='By Thel \'Vadam likes nothing')
        await ctx.send(embed=embed)

    @commands.command(
        name='help_page 2',
        description='Shows help page 2',
        aliases=['hp 2']
    )
    async def help2(self, ctx):
        url=self.bot.user.avatar_url
        embed=discord.Embed(title='__Help__ (page 2)', description='Info commands.', color=0x000000)
        embed.set_thumbnail(url=url)
        embed.add_field(name='`info`', value='Get info on bot.', inline=False)
        embed.add_field(name='`serverinfo`', value='Get info on current server.', inline=False)
        embed.add_field(name='`cogs`', value='View all bots cogs.', inline=False)
        await ctx.send(embed=embed)


    @commands.command(name='help_page 3', description='Shows help page 3', aliases=['hp 3'])
    async def help4(self, ctx):
        url=self.bot.user.avatar_url
        embed=discord.Embed(title='__Help__ (page 3)', description='Roles', color=0x000000)
        embed.set_thumbnail(url=url)
        embed.add_field(name='`add_role`', value='Add a role to yourself.', inline=False)
        embed.add_field(name='`roles`', value='View all roles.', inline=False)
        embed.add_field(name='`create_role`', value='Create a new role.', inline=False)
        await ctx.send(embed=embed)

    @commands.command(
        name='help_page 4',
        description='Shows help page 4.',
        aliases=['hp 4']
    )
    async def help3(self, ctx):
        url=self.bot.user.avatar_url
        embed=discord.Embed(title='__Help__ (page 4)', description='Tags', color=0x000000)
        embed.set_thumbnail(url=url)
        embed.add_field(name='`tags`', value='View all tags.', inline=False)
        embed.add_field(name='`create_tag`', value='Creates a tag.', inline=False)
        embed.add_field(name='`clear_tags`', value='Clears all tags.', inline=False)
        embed.add_field(name='`del_tag`', value='Deletes specified tag.', inline=False)
        await ctx.send(embed=embed)
    
    @commands.command(name='help_page 5', description='Shows help page 5.', aliases=['hp 5', 'hp -1'])
    async def help6(self, ctx):
        url=self.bot.user.avatar_url
        embed=discord.Embed(title='__Help__ (page 5)', description='Misc', color=0x000000)
        embed.set_thumbnail(url=url)
        embed.add_field(name='`nick_set`', value='Change the bots nick.', inline=False)
        embed.add_field(name='`annoy someone`', value='Gives you a quote from 179 ways to annoy someone.', inline=False)
        embed.add_field(name='`profile @[insert name]`', value='Get profile of `name`.', inline=False)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Help(bot))
