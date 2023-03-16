import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


#messages as an aswer
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('1'):
        await message.channel.send('1')

    if message.content.startswith('2'):
        await message.channel.send('2')

    if message.content.startswith('tosti'):
        await message.channel.send('')

#reply messages
@client.event
async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('hello'):
            await message.reply('hi')
            
        if message.content.startswith('hi'):
            await message.reply('sup')

        if message.content.startswith('hi!'):
            await message.reply('Hi how are you?')
        
#        if message.content.startswith('insert more commans here'):
#            await message.  reply('insert your replys here')

client.run('insert your token here')
