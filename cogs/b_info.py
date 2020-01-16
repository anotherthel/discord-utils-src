from discord.ext import commands
import discord, time, csv





class Stuff(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='info',
        description='Shows info on bot.',
        aliases=['ii']
    )
    async def testing(self, ctx):
        x=open('times.csv')
        xx=csv.reader(x)
        xxx=list(xx)
        time=xxx[0]
        time = ' '.join(time)
        embed=discord.Embed(title='thel vadam likes nothing jr.', description='(rewrite version w/ cogs)', color=0x000000)
        url=self.bot.user.avatar_url
        embed.set_thumbnail(url=url)
        embed.add_field(name='__Stats__', value='**discord.py version:** {}\n**Ping time (last):** {}ms\n**Shards:** {}\n**Num of guilds:** {}'.format(discord.__version__, time, self.bot.shard_count, len(self.bot.guilds)), inline=True)
        embed.add_field(name='__Created by:__', value='Thel Vadam likes nothing', inline=True)
        embed.add_field(name='Owner ID:', value='{}'.format(self.bot.owner_id))
        embed.add_field(name='Links:', value='[**invite**](https://discordapp.com/api/oauth2/authorize?client_id=665674407611727915&permissions=8&scope=bot)  | [**source**](https://github.com/insert-ctrl/discord-utils-src/tree/master)')
        embed.set_footer(text='ID: {} | Made by Thel Vadam likes nothing#1359 | Made using repl.it'.format(self.bot.user.id))
        sended=await ctx.send(embed=embed)
        await sended.add_reaction(emoji='👍')
        await sended.add_reaction(emoji='👎')
        await sended.add_reaction(emoji='⚙️')

    @commands.command(
        name='serverinfo',
        description='View server info.',
        aliases=['server', 'guild']
    )
    async def someother(self, ctx):
        humans=0
        bots=0
        for member in ctx.guild.members:
            if member.bot:
                bots+=1
            else:
                humans+=1
        embed=discord.Embed(title='__{}__'.format(ctx.guild), color=0x000000)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name='__Stats:__', value='**ID:** {}\n**Created:** {} (UTC)'.format(ctx.guild.id, ctx.guild.created_at), inline=False)
        embed.add_field(name='__Members__', value='**Members:** {}\n**Humans:** {}\n**Bots:** {}'.format(len(ctx.guild.members), humans, bots), inline=True)
        embed.add_field(name='Number of roles:', value='{}'.format(len(ctx.guild.roles)), inline=True)
        embed.add_field(name='__Channels__', value='**Text:** {}\n**Voice:** {}'.format(len(ctx.guild.text_channels), len(ctx.guild.voice_channels)), inline=False)
        embed.add_field(name='__Max members__:', value='{}'.format(ctx.guild.max_members), inline=False)
        embed.add_field(name='__Region:__', value='{}'.format(ctx.guild.region), inline=False)
        embed.add_field(name='__Description:__', value='{}'.format(ctx.guild.description), inline=False)
        await ctx.send(embed=embed)

    @commands.command(
        name='source',
        description='View bot src.',
        aliases=['src']
    )
    async def send_link(self, ctx):
        await ctx.send('https://github.com/insert-ctrl/discord-utils-src/tree/master')



    



def setup(bot):
    bot.add_cog(Stuff(bot))
