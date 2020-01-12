from discord.ext import commands
import time, discord


pingtimes = []

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='ping_times',
        description='Get all ping times. (not now, while bot under construction.)',
        aliases=['p_t']
    )
    async def pings(self, ctx):
        embed=discord.Embed(title='All ping times', color=0x206694)
        embed.add_field(name='__Times__:', value='```{}```'.format(pingtimes), inline=False)
        await ctx.send(embed=embed)

    @commands.command(
        name='ping',
        description='Test your connection.',
        aliases=['p']
    )
    async def ping_cmd(self, ctx):
        msg = await ctx.send('```Pinging...```')
        time.sleep(0.5)
        timed=self.bot.latency*1000
        await msg.edit(content='```Pong. Time round-trip: {}ms.```'.format(timed))
        pingtimes.append(timed)

    @commands.command(
        name='announce',
        description='Announce.',
        aliases=['a_a'] #see? a_a
    )
    async def announce(self, ctx):
        def check(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author

        
        await ctx.send('Who will be recipient? (@ mention or @ everyone)')
        msg=await self.bot.wait_for('message', check=check)
        await ctx.send('Content:')
        content=await self.bot.wait_for('message', check=check)
        content=content.content
        msg=await ctx.send('Generating announcement...')
        message='> __Announcement__\n{}'.format(content)
        await msg.edit(content=message)




def setup(bot):
    bot.add_cog(Basic(bot))


