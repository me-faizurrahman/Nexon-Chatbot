import discord
from neuralintents import GenericAssistant


chatbot=GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

client = discord.Client()

print("Bot Running...")


@client.event
async def on_message(message):
     if message.author == client.user:
         return
     if message.content.startswith("$aibot"):
         response = chatbot.request(message.content[7:])
         await message.channel.send(response)



client.run("OTg4Nzk0MDQ4MzY0MDUyNTEx.GIOLah.sbs_pdRt1qrJUeGrAuBusimwTuzNoVbv9dSVq0")