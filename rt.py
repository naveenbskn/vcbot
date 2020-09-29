import discord
from discord.ext import commands
from gtts import gTTS


key1="NzYwMzgwNjMyMDUxNjEzNzM2.X3LNpQ"
key2=".L3ObKvI4xRiNoNk9uk7JXV3V52o"
client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print("Bot online.")
    



@client.command(pass_context=True)
async def join(ctx):
    """음성 채널에 입장."""
    if ctx.voice_client:
        await ctx.send("already on vc.")
        return

    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("enter into vc")

@client.command(pass_context=True)
async def leave(ctx):
    
    if ctx.voice_client:
        await ctx.voice_client.disconnect()

@client.command(pass_context=True)
async def voice(ctx):
    
    if not ctx.voice_client or ctx.voice_client.is_playing():
        return
    text="hi welcome naveen"
    tts_file = 'tts.mp3'
    tts = gTTS(text=text, lang='en')
    tts.save(tts_file)
    #voicechannel = discord.utils.get(ctx.guild.channels, name='queue')
    #vc = await voicechannel.connect()
    #vc.play(discord.FFmpegPCMAudio("tts.mp3"), after=lambda e: print('done', e))
    ctx.voice_client.play(discord.FFmpegPCMAudio(tts_file))



client.run(key1+key2)
