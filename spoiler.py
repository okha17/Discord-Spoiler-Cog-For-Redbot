import discord
import logging
import asyncio
from redbot.core import commands


class Spoilercog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content
        if msg != "!spoiler":
            return
        # If the command !spoiler was typed correctly
        if msg == "!spoiler":
            # If there is no image attachment exit
            if not message.attachments:
                error = "Upload an image for me to use!"
                await message.channel.send(error)
                return
            # There is an attachment
            else:
                # get the first attachment which is an image
                file = message.attachments[0]
                file.filename = f"SPOILER_{file.filename}"
                spoiler = await file.to_file(spoiler=True)
				await message.channel.send("Sent by ", message.author)
                await message.channel.send(file=spoiler)
                await message.delete()
        # For any other catches exit
        else:
            return
