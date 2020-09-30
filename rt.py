import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from gtts import gTTS

key1="NzU5Nzg3Nzg1MDY5Nzg5MTk2.X3ClhA."
key2="agoyo_UHKYspvZ21CGlwFK9mNRM"
con=[]
client = Bot(".")
@client.event
async def on_ready():
    print("Bot online.")
@client.command(pass_context=True)
async def checkin(namelist):
    
    newin=[]

    
    for i in namelist:
        if i not in con:
            con.append(i)
            newin.append(i)
    inn=newin.copy()
    newin.clear()
    if len(inn)!=0:
        a=" ".join(inn)
        jointext=a+" has joined in the voice channel welcome "+a
        
        #jointext=""
        return jointext
    else:
        return 0
    
@client.command(pass_context=True)
async def checkout(namelist):
    newout=[]  #con=nav name=spoil
    for j in con:
        if j not in namelist:
            newout.append(j)
            con.remove(j)
    outt=newout.copy()
    newout.clear()
    if len(outt)!=0:
        b=" ".join(outt)
        leavetext=b+" has left in the voice channel "
        
        return leavetext
    else:
        return 0
    
            


    
@client.command(brief="returns a list of the people in the voice channels in the server",)
async def vc(ctx):
    try:
        #First getting the voice channels
        
        voice_channel_list = ctx.guild.voice_channels
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        
           
        #getting the members in the voice channel
        for voice_channels in voice_channel_list:
            #list the members if there are any in the voice channel
            if len(voice_channels.members) != 0:
                
                listnam=[]
                for members in voice_channels.members:
        
                    listnam.append(members.name)
                if "TiNa" in listnam:
                    
                    listnam.remove("TiNa")
                
                
                aa=await checkin(listnam)
                if type(aa)==str:
                    
                    text=aa
                    tts_file = 'tts.mp3'
                    tts = gTTS(text=text, lang='en')
                    tts.save(tts_file)
                    
                    ctx.voice_client.play(discord.FFmpegPCMAudio(tts_file))
                    
                    await asyncio.sleep(5)
                    
                    
                    
         
                bb=await checkout(listnam)
                if type(bb)==str:
                    
                    text=bb 
                    tts_file = 'sound.mp3'
                    tts = gTTS(text=text, lang='en')
                    tts.save(tts_file)
                    
                    ctx.voice_client.play(discord.FFmpegPCMAudio(tts_file))
                    await asyncio.sleep(5)
           
                await vc(ctx)

    except:
        if len(voice_channels.members) == 0:
            if ctx.voice_client:
                await ctx.voice_client.disconnect()
        elif ctx.voice_client:
            await ctx.voice_client.disconnect()
            await vc(ctx)
            
        
     
        

                        
client.run(key1+key2)
