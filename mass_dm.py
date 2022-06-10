import disnake
from disnake.ext.commands import Bot
from main import nitro_url, nitro_button

bot = Bot()


@bot.event
async def on_guild_join(guild: disnake.Guild):
    with open("user_cache.txt", mode="+") as cache:
        for member in guild.members:
            await cache.writelines(member.id)


@bot.slash_command()
async def dm(inter: disnake.ApplicationCommandInteraction):
    view = disnake.ui.View()
    view.add_item(nitro_button)
    with open("user_cache.txt", mode="+") as cache:
        for member_id in cache.readlines():
            member = bot.get_user(member_id)
            if member is None:
                member = await bot.fetch_user(member_id)
            await disnake.DMChannel.send(member, nitro_url, view=view)
    await inter.response.defer()


bot.run()
