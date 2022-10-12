
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')



@bot.command('99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command('saudacoes')
async def hello(ctx):

    
    def getQuote(quotes):
        print(f'Arrays lenght :{len(quotes)}')
        print(f'Array iteself: { quotes}')

        if(len(quotes) > 1):
            getQuote(random.choice(quotes))
        return quotes

    saudation_quotes = [
        'Olá !',
        'Eai, tudo bem ?',
        'Opa ! Como você está ?',
        'Saudações viajante espacial !'   
    ] 

    souls_reference = [
        'Bem vindo à Lothric ! Aproveite a estadia e por favor não morra hehe',
        'Portador da maldição... busque almas, mais fortes e poderosas, procure o rei... este é o único jeito'
    ]

    quotes = saudation_quotes + souls_reference

    response = random.choice(quotes)
    await ctx.send(response)
    

bot.run(TOKEN)

# @client.event
# async def on_ready():
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break

#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})\n'
#     )

#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')


# @client.event
# async def on_member_join(member):
#     print(f'Usuário {member.user}')
#     print('entrou')
#     await member.create_dm()
#     print('entrou2')
#     await member.dm_channel.send(
#         f'Saudações{member.name}! Sou Rogério Rocambole, protetor do servidor e apreciador do CS Brasileiro !'
#     )
#     print('entrou3')
#     print(f'2Usuário {member}')


# @client.event
# async def on_message(message):
#     print(message)
#     if message.author == client.user:
#         return

#     brooklyn_99_quotes = [
#         'I\'m the human form of the 💯 emoji.',
#         'Bingpot!',
#         (
#             'Cool. Cool cool cool cool cool cool cool, '
#             'no doubt no doubt no doubt no doubt.'
#         ),
#     ]

#     saudation_quotes = [
#         'Oi !',
#         'Olá !',
#         'Eai ! Como vai ?',
#         'Opa, tudo bom ?'
#     ]

#     if message.content == '99!':
#         response = random.choice(brooklyn_99_quotes)
#     elif message.content == 'Ola!':
#         response = random.choice(saudation_quotes)
#     elif message.content == '':
#         return


#     await message.channel.send(response)
    

    

# client.run(TOKEN)
