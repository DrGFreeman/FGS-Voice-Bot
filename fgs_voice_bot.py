import os

import discord
from dotenv import load_dotenv

load_dotenv()

ROLE_ID = int(os.getenv("ROLE_ID"))

client = discord.Client()


@client.event
async def on_voice_state_update(member, before, after):

    if after.channel is None and before.channel is not None:
        role = member.guild.get_role(ROLE_ID)
        if role is not None:
            await member.remove_roles(role, reason="Left voice chat")

    if after.channel is not None and before.channel is None:
        role = member.guild.get_role(ROLE_ID)
        if role is not None:
            await member.add_roles(role, reason="Joined voice chat")


client.run(os.getenv("TOKEN"))
