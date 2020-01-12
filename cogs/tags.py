from discord.ext import commands
import discord

tags = []

class Tags(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='tags',
        description='View all tags.',
        aliases=['ts']
    )
    async def all_tags(self, ctx):
        embed=discord.Embed(title='__Tags__', color=0x000000)
        if len(tags) > 0:
            embed.add_field(name='All:', value='```{}```'.format(tags), inline=False)
        else:
            embed.add_field(name='No tags', value='*Use ut.create_tag [link] to create one.*', inline=False)
        await ctx.send(embed=embed)
    
    @commands.command(
        name='create_tag',
        description='Create a new tag.',
        aliases=['c_t', 'ct']
    )
    async def create_tag(self, ctx):
        msg=ctx.message.content.split()
        try:
            msg.pop(0)
            msg=' '.join(msg)
            to_be_edited=await ctx.send('Creating tag...')
            tags.append(msg)
            await to_be_edited.edit(content='Tag created: `{}`'.format(msg))
        except Exception as e:
            await ctx.send('```{}```'.format(e))

    @commands.command(
        name='clear_tags',
        description='Clears all tags.',
        aliases=[]
    )
    async def clear_tags(self, ctx):
        msg = await ctx.send('Clearing tags...')
        tags=[]
        await msg.edit(content='Tags deleted. Tags: `{}`'.format(tags))

    @commands.command(
        name='del_tag',
        description='Deletes specific tag.',
        aliases=[]
    )
    async def del_tag(self, ctx):
        loaded=ctx.message.content.split()
        try:
            loaded.pop(0)
            loaded=' '.join(loaded)
            if loaded in tags:
                msg=await ctx.send('Deleting tag...')
                tags.remove(loaded)
                await msg.edit(content='Tag deleted.')
            else:
                await ctx.send('Tag not found.')
        except Exception as e:
            await ctx.send('```{}```'.format(e))


def setup(bot):
    bot.add_cog(Tags(bot))
