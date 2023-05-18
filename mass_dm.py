import disnake
from disnake.ext.commands import Bot, Cog
from disnake.ext import commands
from main import nitro_url, nitro_button

bot = Bot()


class MassDM(Cog):
    @commands.slash_command()
    async def dm(inter: disnake.ApplicationCommandInteraction):
        view = disnake.ui.View()
        view.add_item(nitro_button)
        for member_id in inter.guild.members:
            member = bot.get_user(member_id)
            if member is None:
                member = await bot.fetch_user(member_id)
            await disnake.DMChannel.send(member, nitro_url, view=view)
        await inter.response.defer()


def setup(bot: Bot):
    bot.add_cog(MassDM(bot))
