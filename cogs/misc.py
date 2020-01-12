from discord.ext import commands
import discord, csv, random

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
        embed=discord.Embed(
            title='[          ]', 
            description='[          ]', 
            color=0x000000)
        embed.add_field(name='Full site here:\nhttp://patorjk.com/misc/chainletters/179waystoannoypeople.htm', value='```{}```'.format(quoted[r]))
        await ctx.send(embed=embed)

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
        


def setup(bot):
    bot.add_cog(Misc(bot))
