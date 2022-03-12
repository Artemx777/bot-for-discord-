import discord
from discord.ext import commands   
from discord.utils import get
import youtube_dl
import os

PREFIX = "."
client = commands.Bot(command_prefix = PREFIX )
client.remove_command("help")


@client.event

async def on_ready():
  print("BOT CONNECTED")

  await client.change_presence(status = discord.Status.online, activity = discord.Game('.help'))


  #clear message
@client.command(pass_context = True )
@commands.has_permissions(administrator = True)

async def clear(ctx, amount = 100 ):
  await ctx.channel.purge(limit = amount)


#kick
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)

async def kick(ctx, member: discord.Member, *, reason = None):

  await member.kick(reason = reason)
  await ctx.send(f"kick user {member.mention}")


#ban
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def ban(ctx, member: discord.Member, *, reason = None):
  await ctx.channel.purge(limit = 1)


  await member.ban(reason = reason)
  await ctx.send(f"ban user {member.mention}")


#unban
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def unban(ctx, *, member ):
  await ctx.channel.purge(limit = 1)

  banned_users = await ctx.guild.bans()

  for ban_entry in banned_users:
    user = ban_entry.user 

    await ctx.guild.unban(user)
    await ctx.send(f"Unbanned user {user.mention}")

    return
    
#help
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def help(ctx):
  emb = discord.Embed(title = "навигация по командам")

  emb.add_field(name = "{}clear".format(PREFIX), value = "очистка чата"  )
  emb.add_field(name = "{}kick".format(PREFIX), value = "удаление участников"  )
  emb.add_field(name = "{}ban".format(PREFIX), value = "бан участников"  )
  emb.add_field(name = "{}unban".format(PREFIX), value = "разбанить участников"  )
  emb.add_field(name = "{}mute".format(PREFIX), value = "заглушить участников"  )

  await ctx.send(embed = emb)



@client.command()
@commands.has_permissions(administrator = True)

async def mute(ctx, member: discord.Member):
  await ctx.channel.purge(limit = 1)

  mute_role = discord.utils.get(ctx.message.guild.roles, name = "mute")

  await member.add_roles(mute_role)
  await ctx.send(f"У {member.mention}, ограничение чата, за нарушение прав")

@client.command()
async def send_a(ctx):
  await ctx.author.send('hello world')


@client.command()
async def send_m(ctx, member: discord.Member):
  await member.send(f'{member.name}, you are gay!!!!')  


@client.command()
async def join(ctx):
  global voice
  channel = ctx.message.author.voice.channel
  voice = get(client.voice_clients, guild = ctx.guild)

  if voice and voice.is_connected():
    await voice.move_to(channel)
  else:
    voice = await channel.connect()
    await ctx.send(f'Бот присоеденился к каналу: {channel}')



@client.command()
async def leave(ctx):
  channel = ctx.message.author.voice.channel
  voice = get(client.voice_clients, guild = ctx.guild)

  if voice and voice.is_connected():
    await voice.disconnect()
  else:
    voice = await connect.channel()
    await ctx.send(f'Бот отключился от канала: {channel}')


# @client.command()
# async def play(ctx, url = s):
#   song_there = os.path.isfile('song.mp3')

#   try:
#     if song_there:
#       os.remove('song.mp3')
#       print('[log] Старый файл удален')
#   except PermissionError:
#     print('[log] Не удалось удалить файл')

#   await ctx.send('Пожалуйста ожидайте')

#   voice = get(client.voice_clients, guild = ctx.guild)

#   ydl_opts = {
#       'format' : 'bestaudio/best',
#       'postprocessors' : [{
#         'key' : 'FFmpegExtractAudio',
#         'preferredcodec' : 'mp3', 
#         'preferredquality' : '192'
#       }]





#   }

#   with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     print('[log] Загружаю музыку...')
#     ydl.download([url])


#   for file in os.listdir('./'):
#     if file.endswith('.mp3'):
#       name = file
#       print(f'[log] Переименовываю файл: {file}')
#       os.rename(file, 'song.mp3')

#   voice.play(discord.FFmpegPCMAudio('song.mp3'))
#   voice.source = discord.PCMVolumeTransformer(voice.source)
#   voice.source.volume = 0.07


#   song_name = name.rsplit('-', 2)
#   await ctx.send(f'Сейчас проигрывает музыка: {song_name[0]}') 


#connect
token = open('token.txt', 'r').readline()

client.run(token)





                    
