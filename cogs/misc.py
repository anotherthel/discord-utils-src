from discord.ext import commands
import discord, csv, random

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='nick_set',
        description='Change bot nick.',
        aliases=['n_s', 'ns']
    )
    async def change_nick(self, ctx):
        ctx.message.content=ctx.message.content.split()
        if len(ctx.message.content) > 1:
            ctx.message.content.pop(0)
            nick=' '.join(ctx.message.content)
            if len(nick)<=32:
                await ctx.guild.get_member(self.bot.user.id).edit(nick=nick)
                await ctx.send('Nick changed to `{}`.'.format(nick))
            else:
                await ctx.send('Name too long. Max len: 32')
        else:
            await ctx.send('Missing: `name`')

    @commands.command(
        name='annoy someone',
        description='Nonems',
        aliases=['iass']
    )
    async def annoy_someone(self, ctx):
        ff=open('blank.csv')
        readed=csv.reader(ff)
        quoted=list(readed)
        r=random.randint(0, 178)
        embed=discord.Embed(
            title='[          ]', 
            description='[          ]', 
            color=0x000000)
        embed.add_field(name='Full site here:\nhttp://patorjk.com/misc/chainletters/179waystoannoypeople.htm', value='```{}```'.format(quoted[r]))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))
        
