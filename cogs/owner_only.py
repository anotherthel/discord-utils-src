from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='reload_cog',
        description='Reload cog (owner only)',
        aliases=['r_c', 'r-c']
    )
    async def reload_cog(self, ctx):
        if ctx.author.id == 640203987437748246:
            msg=ctx.message.content.split()
            msg.pop(0)
            msg=' '.join(msg)
            cogs = ['cogs.basic', 'cogs.help', 'cogs.b_info', 'cogs.invite', 'cogs.roles', 'cogs.misc', 'cogs.tags', 'cogs.mod', 'cogs.gb', 'cogs.eval', 'cogs.code', 'cogs.owner_only']
            if msg in cogs:
                c=await ctx.send('Loading cog...')
                try:
                    self.bot.unload_extension(msg)
                    self.bot.load_extension(msg)
                    await c.edit(content=':white_check_mark: Reloaded cog `{}`.'.format(msg))
                except Exception as e:
                    await c.edit(content=':regional_indicator_x: Something went wrong:\n```{}```'.format(e))
            else:
                await ctx.send(':regional_indicator_x: `{}` is not a cog.'.format(msg))
        else:
            return

def setup(bot):
    bot.add_cog(Owner(bot))
