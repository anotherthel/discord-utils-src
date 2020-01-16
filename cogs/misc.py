from discord.ext import commands
import discord, csv, random, asyncio


colors = {
  'DEFAULT': 0x000000,
  'WHITE': 0xFFFFFF,
  'AQUA': 0x1ABC9C,
  'GREEN': 0x2ECC71,
  'BLUE': 0x3498DB,
  'PURPLE': 0x9B59B6,
  'LUMINOUS_VIVID_PINK': 0xE91E63,
  'GOLD': 0xF1C40F,
  'ORANGE': 0xE67E22,
  'RED': 0xE74C3C,
  'GREY': 0x95A5A6,
  'NAVY': 0x34495E,
  'DARK_AQUA': 0x11806A,
  'DARK_GREEN': 0x1F8B4C,
  'DARK_BLUE': 0x206694,
  'DARK_PURPLE': 0x71368A,
  'DARK_VIVID_PINK': 0xAD1457,
  'DARK_GOLD': 0xC27C0E,
  'DARK_ORANGE': 0xA84300,
  'DARK_RED': 0x992D22,
  'DARK_GREY': 0x979C9F,
  'DARKER_GREY': 0x7F8C8D,
  'LIGHT_GREY': 0xBCC0C0,
  'DARK_NAVY': 0x2C3E50,
  'BLURPLE': 0x7289DA,
  'GREYPLE': 0x99AAB5,
  'DARK_BUT_NOT_BLACK': 0x2C2F33,
  'NOT_QUITE_BLACK': 0x23272A
}

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
        await sent.add_reaction(emoji='👍')
        await sent.add_reaction(emoji='👎')


        


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
            embed.add_field(name='__Stats__', value='**ID:** {}\n**Discriminator:** #{}\n**Nick:** {}\n**Guild:** {}\n**Status:** {}\n**Platform:** {}\n**Permissions:** {}'.format(member.id, member.discriminator, member.nick, member.guild, member.status, on_mobile, member.guild_permissions))
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
            await msg.add_reaction(emoji='👍')
            await msg.add_reaction(emoji='👎')
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
        name='users',
        description='View users bot can see.',
        aliases=[]
    )
    async def get_users(self, ctx):
        await ctx.send('Users:')
        for user in self.bot.users:
            await ctx.send('{}'.format(user))

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
                    self.bot.load_extension(msg)
                    await c.edit(content='Reloaded cog `{}`.'.format(msg))
                except Exception as e:
                    await c.edit(content='```%s```'%(e))
            else:
                await ctx.send('`{}` is not a cog.'.format(msg))
        else:
            return

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









        
        


def setup(bot):
    bot.add_cog(Misc(bot))
        
