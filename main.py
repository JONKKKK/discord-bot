from datetime import datetime as dt
import discord
client = discord.Client()
helpMessage = """
**you cant be helped**
"""

@client.event
async def on_ready():
    activeServers = client.servers
    sum = 0
    for s in activeServers:
        sum += len(s.members)
    print("hey nerds im in %s server(s) with %s users xd" % (len(client.servers), sum))
    await client.change_presence(game=discord.Game(name = "ur mom xd | smol.help"))


@client.event
async def on_message(message):
    msg = message.content

    if msg == "smol.help":
        await client.send_message(message.channel, content = helpMessage)
        print("%s is a big nerd and thinks they can get help." % message.author)
    
    if msg == "smol.ping":
        startTime = dt.now()
        await client.send_message(message.channel, content = "Pong!")
        endTime = dt.now()
        await client.send_message(message.channel, content = "(took %s seconds)" % endTime - startTime)
    
