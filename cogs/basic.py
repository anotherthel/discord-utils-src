from discord.ext import commands
import time, discord, datetime


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
        time_1 = time.perf_counter()
        await ctx.trigger_typing()
        time_2 = time.perf_counter()
        ping = round((time_2-time_1)*1000)
        await msg.edit(content='```Pong. Time round-trip: {}ms.```'.format(ping))
        pingtimes.append(ping)

    @commands.command(
        name='announce',
        description='Announce.',
        aliases=['a_a'] #see? a_a
    )
    async def announce(self, ctx):
        def check(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author

        if len(ctx.message.content.split()) <= 1:
            await ctx.send('Missing: `recipient`.\nExample: `@everyone`')
            return
        message=ctx.message.content.split()
        message.pop(0)
        message=' '.join(message)
        await ctx.send('Content:')
        content=await self.bot.wait_for('message', check=check)
        content=content.content
        msg=await ctx.send('Generating announcement...')
        response='> __Announcement__ @{}\n{}'.format(message,content)
        await msg.edit(content=response)

    @commands.command(
        name='pin',
        description='Pin a message.',
        aliases=[]
    )
    async def pin_message(self, ctx):
        def check(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author
        c=await ctx.send('Awaiting message:')
        messages=await self.bot.wait_for('message', check=check)
        await messages.pin()
        await c.edit(content="Message pinned:\n`{}`".format(messages.content))

def setup(bot):
    bot.add_cog(Basic(bot))


