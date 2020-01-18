from discord.ext import commands
import discord, csv, random, asyncio




colors=[0x000000,0xFFFFFF,0x1ABC9C,0x2ECC71,0x3498DB,0x9B59B6,0xE91E63,0xF1C40F,0xE67E22,0xE74C3C,0x95A5A6,0x34495E,0x34495E,0x11806A,0x11806A,0x1F8B4C,0x206694,0x71368A,0xAD1457,0xC27C0E,0xA84300,0x7289DA0,0x99AAB5]




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
        sent = await ctx.send('```{}```'.format(quoted[r]))
        await sent.add_reaction(emoji='\U0001f44d')
        await sent.add_reaction(emoji='\U0001f44e')


        
    @commands.command(
        name='xkcd',
        description='Show an xkcd comic.',
        aliases=['xxxx']
    )
    async def xkcd(self, ctx):
        msg = ctx.message.content.split()
        if len(msg) == 1:
            r=random.randint(1, 2250)
            await ctx.send('https://xkcd.com/{}/'.format(r))
        else:
            num = int(msg[1])
            if num <= 2250 and num >= 1:
                await ctx.send('https://xkcd.com/{}/'.format(str(num)))

    @commands.command(
        name='color',
        description='Show a random color.',
        aliases=[]
    )
    async def rand_color(self, ctx):
        c=random.choice(colors)
        try:
            embed=discord.Embed(title='Random color:', description=c, color=c)
            embed.add_field(name='<--', value='*Look to the left to see color, not here!*', inline=False)
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send('```{}```'.format(e))

    @commands.command(
        name='profile',
        description='View stats of user.',
        aliases=['prof']
    )
    async def profile_user(self, ctx, member:discord.Member):
        try:
            await self.bot.fetch_user(ctx.author.id)
            embed=discord.Embed(title='{}'.format(member.name), color=0x000000)
            url=member.avatar_url
            embed.set_thumbnail(url=url)
            on_mobile=''
            if member.is_on_mobile():
                on_mobile = 'Mobile :iphone:'
            else:
                on_mobile = 'PC :desktop:'
            embed.add_field(name='__Stats__', value='**ID:** {}\n**Discriminator:** #{}\n**Nick:** {}\n**Guild:** {}\n**Status:** {}\n**Platform:** {}\n**Bot:** {}\n**Permissions:** {}'.format(member.id, member.discriminator, member.nick, member.guild, member.status, on_mobile, member.bot, member.guild_permissions))
            roles=[]
            for role in member.roles:
                roles.append(role.name)
            roles = ', '.join(roles)
            embed.add_field(name='__Roles:__', value=roles, inline=False)
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f'```{e}```')

    @commands.command(
        name='set_status',
        description='set bot status (owner only)',
        aliases=['s_s', '$_$']
    )
    async def set_status(self, ctx):
        if ctx.author.id == 640203987437748246:
            ctx.message.content = ctx.message.content.split()
            ctx.message.content.pop(0)
            msg=' '.join(ctx.message.content)
            game=discord.Game(msg)
            await self.bot.change_presence(status=discord.Status.online, activity=game)
            msg=await ctx.send('Setting status...')
            await asyncio.sleep(0.75)
            await msg.edit(content='Status changed to:\nStatus: `discord.Status.online`\nActivity: `{}`'.format(game))
            await msg.add_reaction(emoji='\U0001f44d')
            await msg.add_reaction(emoji='\U0001f44e')
        else:
            await ctx.send('`set_status` is an owner only command.')
            return

    @commands.command(
        name='create_channel',
        description='Create a new channel (owner only)',
        aliases=[]
    )
    async def create_channel(self, ctx):
        if ctx.author.id == 640203987437748246:
            guild=ctx.message.guild
            mm=ctx.message.content.split()
            mm.pop(0)
            mm=' '.join(mm)
            await guild.create_text_channel(mm)
            msg=await ctx.send('Creating channel...')
            await asyncio.sleep(0.75)
            await msg.edit(content='Channel created.')
        else:
            await ctx.send('`create_channel` is an owner only command.')
            return



    @commands.command(
        name='reload_cog',
        description='Reload cog (owner only)',
        aliases=['r_c']
    )
    async def reload_cog(self, ctx):
        if ctx.author.id == 640203987437748246:
            msg=ctx.message.content.split()
            msg.pop(0)
            msg=' '.join(msg)
            cogs = ['cogs.basic', 'cogs.help', 'cogs.b_info', 'cogs.invite', 'cogs.roles', 'cogs.misc', 'cogs.tags', 'cogs.mod']
            if msg in cogs:
                c=await ctx.send('Loading cog...')
                try:
                    self.bot.unload_extension(msg)
                    self.bot.load_extension(msg)
                    await c.edit(content=':white_check_mark: Reloaded cog `{}`.'.format(msg))
                except Exception as e:
                    await c.edit(':x: Something went wrong:\n```{}```'.format(e))
            else:
                await ctx.send(':x: `{}` is not a cog.'.format(msg))
        else:
            return

    @commands.command(
        name='cogs',
        description='View all bots cogs.',
        aliases=[]
    )
    async def view_cogs(self, ctx):
        try:
            await ctx.send('{}'.format(self.bot.cogs))
        except Exception as e:
            await ctx.send('```{}```'.format(e))

    @commands.command(
        name='u_a',
        description='See avatar of user.',
        aliases=['user_av']
    )
    async def show_av(self, ctx, member: discord.Member):
        embed=discord.Embed(title="{}'s avatar".format(member), color=0x000000)
        url=member.avatar_url
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(
        name='urban',
        description='View urban dictionary definition of word.',
        aliases=[]
    )
    async def urban_def(self, ctx):
        msg = ctx.message.content.split()
        if len(msg) == 2:
            await ctx.send('https://www.urbandictionary.com/define.php?term={}'.format(msg[1]))
        elif len(msg) > 2:
            await ctx.send(':x: Something went wrong. Try this:\n`ut.urban [insert __one__ word]`')
        else:
            await ctx.send('```list index out of range.```')











        
        


def setup(bot):
    bot.add_cog(Misc(bot))
        
