import discord
import asyncio
import random
import datetime
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient
import platform
#bot_prefix= "."
#description = ("```Xorian Bot Made By Diaxminator```")
#client = client = Bot(description="Psssst, Ok Green is talking!", command_prefix=".", pm_help = True)
client = discord.Client()
owid = ('297800633224921099')
altid = ('362677230855389184')
zookid = ('342333167514025986')
client.login('email', 'password')
#kickto = (ctx, userName, discord.User)


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=".info | Как дела?" ))
    print('Bot Fired Up!!')
    print(client.user.name)
    print(client.user.id)
    print('We have logged in as {0.user}'.format(client))
    print('Invite: https://discordapp.com/oauth2/authorize?client_id={}&scope=bot'.format(client.user.id))
    print('------')

#@client.command(pass_context = True)
#async def kick(ctx, userName: discord.User):
 #   await client.kick(userName)

#@client.command(pass_context = True)
#async def ban(ctx, userName: discord.User):
 #   await client.ban(userName)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.upper().startswith(".PING"):
        userID = message.author.id
        await client.send_message(message.channel, "Pong! <@%s>" % (userID))
        
    elif message.content.startswith(".8ball"):
        userID = message.author.id
        await client.send_message(message.channel, random.choice(["It is certain :8ball:",
                                                                  "When and why? :8ball:",
                                                                  "I am aware of your presence :8ball:",
                                                                  "It is decidedly so :8ball:",
                                                                  "Without a doubt :8ball:",
                                                                  "Yes, definitely :8ball:",
                                                                  "You may rely on it :8ball:",
                                                                  "As I see it, yes :8ball:",
                                                                  "Most likely :8ball:",
                                                                  "Outlook good :8ball:",
                                                                  "I am a bot, I have no age :8ball:",
                                                                  "Yes :8ball:",
                                                                  "No :8ball:",
                                                                  "Signs point to yes :8ball:",
                                                                  "Reply hazy try again :8ball:",
                                                                  "Ask again later :8ball:",
                                                                  "Better not tell you now :8ball:",
                                                                  "Cannot predict now :8ball:",
                                                                  "Concentrate and ask again :8ball:",
                                                                  "Don't count on it :8ball:",
                                                                  "My reply is no :8ball:",
                                                                  "My sources say no :8ball:",
                                                                  "Outlook not so good :8ball:",
                                                                  "I am not 21 :8ball:",
                                                                  "I come from Pluto :8ball:",
                                                                  "I would not say so :8ball:",
                                                                  "I would say so :8ball:",
                                                                  "What the hell? :8ball:",
                                                                  "Are you Jewish? :8ball:",
                                                                  "I am :8ball:",
                                                                  "Meat beat rhymes :8ball:",
                                                                  "What is your honest opinion about that? :8ball:",
                                                                  "Noob :8ball:",
                                                                  "Be honest, you've killed someone before :8ball:",
                                                                  "The ting goes skrrrrra! :8ball:",
                                                                  "Fire in da boof! :fire: :8ball:",
                                                                  "I am not :8ball:",
                                                                  "If you liked meat :8ball:",
                                                                  "Aselith loves me :8ball:",
                                                                  "Very doubtful :8ball:"]))


    
    if message.content.startswith('.countmsg'): 
         counter = 0
         tmp = await client.send_message(message.channel, 'Calculating messages...')
         async for log in client.logs_from(message.channel, limit=10000):
            if log.author == message.author:
                counter += 1

         await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('.sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping') #Your message counter

    if message.content.upper().startswith(".PENG"):
        userID = message.author.id
        await client.send_message(message.channel, "Ting <@%s> :heart: " % (userID))

    if message.content.upper().startswith(".ID"):
        userID = message.author.id
        await client.send_message(message.channel, "Your ID is ***%s***" % (userID))

    if message.content.upper().startswith(".CLIENTID"):
        cID = client.user.id
        await client.send_message(message.channel, "Client ID is ***%s***" % (cID))

    if message.content.upper().startswith(".DICE"):
        await client.send_message(message.channel, random.choice(["**`1`**",
                                                                  "**`2`**",
                                                                  "**`3`**",
                                                                  "**`4`**",
                                                                  "**`5`**",
                                                                  "**`6`**"]))

    if message.content.upper().startswith(".FLIP"):
        await client.send_message(message.channel, random.choice(["**Heads!!**",
                                                          "**Tails!!**"]))

    if message.content.startswith('.guess'):
        await client.send_message(message.channel, 'Guess a number between 1 to 10')

        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'Sorry, you took too long. It was {}.'
            await client.send_message(message.channel, fmt.format(answer))
            return
        if int(guess.content) == answer:
            await client.send_message(message.channel, 'You are right!')
        else:
            await client.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))

    

    
    


        

    elif message.content.startswith(".say"):
        variable = message.content[len('.say'):].strip()
        if variable == "@everyone":
            await client.send_message(message.channel, "Don't you think that will be a good idea")
        elif variable == "@here":
            await client.send_message(message.channel, "You really think that's a good idea?")
        else:
            await client.send_message(message.channel, variable) #Random SAY command

            

    elif message.content.startswith(".embed"):
        emb = (discord.Embed(description="This is an embed! :fire:", colour=0x3DF270))
        emb.set_author(name="Hello Guys!", icon_url='https://cdn.discordapp.com/attachments/394129809283874816/394132241233739776/wow-2370205_960_720.png?size=812')
        await client.send_message(message.channel, embed=emb) #Random embed command

    if message.content.startswith(".info"):
        embed = discord.Embed(title="***Bot info***", colour=discord.Colour(0x007c0c), description="This is a simple bot coded by a user called: <@297800633224921099>. It doesn't do many things however I will be adding useful stuff in the future. Any ideas? DM me!", timestamp=datetime.datetime.utcfromtimestamp(1515529800))
        embed.set_image(url="https://cdn.discordapp.com/attachments/396714817810857984/404006428643164160/Message.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/394129809283874816/400343955952107522/info-1345871_960_720.png")
        embed.set_author(name="Diaxminator", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/attachments/394129809283874816/400343220585758730/badge.png")
        embed.set_footer(text="Last Updated", icon_url="https://cdn.discordapp.com/attachments/394129809283874816/400343955952107522/info-1345871_960_720.png")
        embed.add_field(name="Help commands", value="Use .h1 & .h2 for help commands.")
        embed.add_field(name="Invite", value="The invite link is https://discordapp.com/oauth2/authorize?client_id=394100392071266305&scope=bot")
        embed.add_field(name="Owner", value="<@297800633224921099>", inline=True)
        embed.add_field(name="Dev", value="<@336138482021957642>", inline=True)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith(".h1"):
        embed = discord.Embed(title="**COMMANDS LIST**", colour=discord.Colour(0x0cadc3), description="This is the list of commands available", timestamp=datetime.datetime.utcfromtimestamp(1514337763))
        embed.set_author(name="Page 1/2", icon_url="https://cdn.discordapp.com/attachments/394129809283874816/394129817836060673/help-md.png?size=512")
        embed.set_footer(text="By Diaxminator#3407", icon_url="https://cdn.discordapp.com/attachments/373102431128518657/395397108993359872/DiscordLogoNew.png")
        embed.add_field(name="Public", value=""".ping = Pong!!
.8ball = The 8 ball that you can talk to!
.say = Make the bot say something!
.fruit = Replies with a random fruit!
.giph = A random giph! (a bit broken)
.cookie = Replies with a cookie!
.darren = Darren style! """)
        await client.send_message(message.channel, embed=embed)#Help 1

    elif message.content.startswith(".h2"):
        embed = discord.Embed(title="**COMMANDS LIST**", colour=discord.Colour(0x0cadc3), description="This is the list of commands available", timestamp=datetime.datetime.utcfromtimestamp(1514337763))
        embed.set_author(name="Page 2/2", icon_url="https://cdn.discordapp.com/attachments/394129809283874816/394129817836060673/help-md.png?size=512")
        embed.set_footer(text="By Diaxminator#3407", icon_url="https://cdn.discordapp.com/attachments/373102431128518657/395397108993359872/DiscordLogoNew.png")
        embed.add_field(name="Public", value="""
.animal = Replies with an animal!
.countmsg = Counts your total messages on the server!
.id = Shows your ID!
.clientid = Shows the bots ID!
.sleep = Sends the bot to sleep (but wakes him up after 5s)
.rr = Russian Roulette """)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('.help'):
        await client.send_message(message.channel, 'Pick the page you want to be directed to (2 pages)')

        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=10.0, author=message.author, check=guess_check)
        if (guess.content) == ("1"):
            embed = discord.Embed(title="**COMMANDS LIST**", colour=discord.Colour(0x0cadc3), description="This is the list of commands available", timestamp=datetime.datetime.utcfromtimestamp(1514337763))
            embed.set_author(name="Page 1/2", icon_url="https://cdn.discordapp.com/attachments/394129809283874816/394129817836060673/help-md.png?size=512")
            embed.set_footer(text="By Diaxminator#3407", icon_url="https://cdn.discordapp.com/attachments/373102431128518657/395397108993359872/DiscordLogoNew.png")
            embed.add_field(name="Public", value="""
.ping = Pong!!
.8ball = The 8 ball that you can talk to!
.say = Make the bot say something!
.fruit = Replies with a random fruit!
.giph = A random giph! (a bit broken)
.cookie = Replies with a cookie!
.darren = Darren style! """)
            await client.send_message(message.channel, embed=embed)
        if (guess.content) == ("2"):
            embed = discord.Embed(title="**COMMANDS LIST**", colour=discord.Colour(0x0cadc3), description="This is the list of commands available", timestamp=datetime.datetime.utcfromtimestamp(1514337763))
            embed.set_author(name="Page 2/2", icon_url="https://cdn.discordapp.com/attachments/394129809283874816/394129817836060673/help-md.png?size=512")
            embed.set_footer(text="By Diaxminator#3407", icon_url="https://cdn.discordapp.com/attachments/373102431128518657/395397108993359872/DiscordLogoNew.png")
            embed.add_field(name="Public", value="""
.animal = Replies with an animal!
.countmsg = Counts your total messages on the server!
.id = Shows your ID!
.clientid = Shows the bots ID!
.sleep = Sends the bot to sleep (but wakes him up after 5s)
.rr = Russian Roulette
.guess = Play a game with the bot! Guess between 10 numbers!""")
            await client.send_message(message.channel, embed=embed)

        else:
            emb = (discord.Embed(description="That page doesn't exist!!", colour=0xe80a0a))
            emb.set_author(name="ERROR!", icon_url='https://cdn.discordapp.com/attachments/403414327677419564/407582374277414912/contacts.png')
            await client.send_message(message.channel, embed=emb) #NEW HELP COMMAND
        

    elif message.content.upper().startswith(".FRUIT"):
        await client.send_message(message.channel, random.choice([":apple:",
                                                                  ":pineapple:",
                                                                  ":banana:",
                                                                  ":green_apple:",
                                                                  ":watermelon:",
                                                                  ":tomato:",
                                                                  ":strawberry:",
                                                                  ":lemon:",
                                                                  ":pear:",
                                                                  ":melon:",
                                                                  ":hot_pepper:",
                                                                  ":peach:",
                                                                  ":cherries:",
                                                                  ":tangerine:",
                                                                  ":grapes:"])) #Fruits
    

    elif message.content.upper().startswith(".GIPH"):
        await client.send_message(message.channel, random.choice(["https://gph.is/2mL4InV",
                                                                  "https://gph.is/2DASzrX",
                                                                  "https://gph.is/1oSIjPm",
                                                                  "https://gph.is/2qo6ieW",
                                                                  "https://gph.is/29acIGx",
                                                                  "https://gph.is/1BwA6n7",
                                                                  "https://gph.is/1PGe5P9",
                                                                  "https://gph.is/1beYJsd",
                                                                  "https://gph.is/14nYhDL",
                                                                  "https://gph.is/11RYBzC",
                                                                  "https://gph.is/1JnJv8g",
                                                                  "https://gph.is/181yJz6",
                                                                  "https://gph.is/2gH1ITz",
                                                                  "https://gph.is/1nW19c0",
                                                                  "https://gph.is/2fGZZP1",
                                                                  "https://gph.is/2nErVch",
                                                                  "https://gph.is/1ZIqp2w",
                                                                  "https://gph.is/2jklRUC",
                                                                  "https://gph.is/2oYGgkJ",
                                                                  "https://gph.is/1LPXEIu",
                                                                  "https://gph.is/2eauqNP",
                                                                  "https://gph.is/296hG6z",
                                                                  "https://gph.is/298U2I6",
                                                                  "https://gph.is/2j94mZk",
                                                                  "https://gph.is/2xsBYGE",
                                                                  "https://gph.is/GCkCZr",
                                                                  "https://gph.is/2honSg3",
                                                                  "https://gph.is/2npfYVD",
                                                                  "https://gph.is/2DgTKNe",
                                                                  "https://gph.is/2zcD3PM",
                                                                  "https://gph.is/2cBIXzi",
                                                                  "https://gph.is/2DGYgVv",
                                                                  "https://gph.is/2n1VsfF"])) #Giph Command

    elif message.content.upper().startswith(".ANIMAL"):
        await client.send_message(message.channel, random.choice([":dog:",
                                                                  ":cat:",
                                                                  ":mouse:",
                                                                  ":hamster:",
                                                                  ":rabbit:",
                                                                  ":bear:",
                                                                  ":panda_face:",
                                                                  ":koala:",
                                                                  ":tiger:",
                                                                  ":lion:",
                                                                  ":cow:",
                                                                  ":pig:",
                                                                  ":frog:",
                                                                  ":octopus:",
                                                                  ":monkey_face:",
                                                                  ":chicken:",
                                                                  ":penguin:",
                                                                  ":bird:",
                                                                  ":baby_chick:",
                                                                  ":wolf:",
                                                                  ":boar:",
                                                                  ":horse:",
                                                                  ":unicorn:",
                                                                  ":bee:",
                                                                  ":bug:",
                                                                  ":snail:",
                                                                  ":spider:",
                                                                  ":scorpion:",
                                                                  ":crab:",
                                                                  ":snake:",
                                                                  ":turtle:",
                                                                  ":fish:",
                                                                  ":dolphin:",
                                                                  ":whale:",
                                                                  ":crocodile:",
                                                                  ":leopard:",
                                                                  ":tiger2:",
                                                                  ":water_buffalo:",
                                                                  ":ox:",
                                                                  ":cow2:",
                                                                  ":camel:",
                                                                  ":elephant:",
                                                                  ":goat:",
                                                                  ":sheep:",
                                                                  ":pig2:",
                                                                  ":mouse2:",
                                                                  ":rat:",
                                                                  ":rooster:",
                                                                  ":turkey:",
                                                                  ":dove:",
                                                                  ":chipmunk:",
                                                                  ":dragon:"])) #Animal Command

                                                                

    if message.content == ".cookie":
        await client.send_message(message.channel, ":cookie:") #Just a cookie

    if message.content == ".darren":
        await client.send_message(message.channel, random.choice(["https://cdn.discordapp.com/attachments/394129809283874816/394133638507134976/cauliflower-raw.png",
                                                                  "https://cdn.discordapp.com/attachments/394129809283874816/394134979619061760/sprouts-xlarge_trans_NvBQzQNjv4BqZgEkZX3M936N5BQK4Va8RWtT0gK_6EfZT336f62EI5U.png"])) #Darren command

    if message.content.startswith(".react"):
        msg = await client.send_message(message.channel, "React with thumbs up or thumbs down")
        res = await client.wait_for_reaction([':thumbsup:',':thumbsdown:'], message=msg)
        await client.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))
    
        

    



########################################################################################################################


    if message.content.upper().startswith("?BAM"):
        userID = message.author.id
        await client.send_message(message.channel, random.choice(["Yeah go on! Lets bam the whole server!!",
                                                                  "You have successfully bammed that user!!",
                                                                  "Bam I see :thinking:",
                                                                  "Try to bam me boi",
                                                                  "You get bammed for breaking rule 23, didn't you know?"]))

    if message.content.upper().startswith('.RR'):        
        await client.send_message(message.channel, '*You spin the cylinder of the revolver with 1 bullet in it...*')
        await asyncio.sleep(2)
        await client.send_message(message.channel, '*...you place the muzzle against your head  :gun:  and pull the trigger...*')
        await asyncio.sleep(3)
        await client.send_message(message.channel, random.choice(["***` X ...your brain gets splattered all over the wall. X `***",
                                                                  "**`...you live to see another day.`**",
                                                                  "**`...you live to see another day.`**",
                                                                  "**`...you live to see another day.`**",
                                                                  "**`...you live to see another day.`**",
                                                                  "**`...you live to see another day.`**"]))

########################################################################################################################
        #DEV COMMANDS

    if message.content.startswith(".admin_panel_status"):
        if message.author.id == owid:
            emb = (discord.Embed(description="You do have permission access admin commands!", colour=0x28d329))
            await client.send_message(message.channel, embed=emb)
        else:
            emb = (discord.Embed(description="Unfortunately you do not have access to dev commands :(", colour=0xfe0000))
            await client.send_message(message.channel, embed=emb)


    if message.content.startswith(".dev_8ball"):
            variable = message.channel, random.choice(["Hi",
                                                       "Hello",
                                                       "Bye"])
            if variable == "What":
                await client.send_message(message.channel, "Grammer nazi")
            elif variable == "You":
                await client.send_message(message.channel, "Stop grammar noob")
                                      

    #Embed
    if message.content.startswith(".admin_emb1"):
        if message.author.id == owid:
            embed = discord.Embed(title="title ~~(did you know you can have markdown here too?)~~", colour=discord.Colour(0x74bb17), url="https://discordapp.com", description="this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown. ```\nyes, even code blocks```", timestamp=datetime.datetime.utcfromtimestamp(1514337763))
            embed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
            embed.set_author(name="author name", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
            embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
            embed.add_field(name=":think:", value="some of these properties have certain limits...")
            embed.add_field(name=":think:", value="try exceeding some of them!")
            embed.add_field(name=":think:", value="an informative error should show up, and this view will remain as-is until all issues are fixed")
            embed.add_field(name=":think:", value="these last two", inline=True)
            embed.add_field(name=":think:", value="are inline fields", inline=True)
            await client.send_message(message.channel, embed=embed)
        else:
            emb = (discord.Embed(description="Insufficient Permission!", colour=0xfe0000))
            await client.send_message(message.channel, embed=emb)
            
        
    if message.content.startswith(".admin_info1"):
        if message.author.id == owid:
            embed = discord.Embed(title="***Bot info***", colour=discord.Colour(0x007c0c), description="This is a simple bot coded by a user called: <@297800633224921099>. It doesn't do many things however I will be adding useful stuff in the future. Any ideas? DM me!", timestamp=datetime.datetime.utcfromtimestamp(1515529800))
            embed.set_image(url="https://cdn.discordapp.com/attachments/396714817810857984/404006428643164160/Message.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/394129809283874816/400343955952107522/info-1345871_960_720.png")
            embed.set_author(name="Diaxminator", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/attachments/394129809283874816/400343220585758730/badge.png")
            embed.set_footer(text="Last Updated", icon_url="https://cdn.discordapp.com/attachments/394129809283874816/400343955952107522/info-1345871_960_720.png")
            embed.add_field(name="Help commands", value="Use .h1 & .h2 for help commands.")
            embed.add_field(name="Invite", value="The invite link is https://discordapp.com/oauth2/authorize?client_id=394100392071266305&scope=bot")
            embed.add_field(name="Owner", value="<@297800633224921099>", inline=True)
            embed.add_field(name="Dev", value="<@336138482021957642>", inline=True)
            await client.send_message(message.channel, embed=embed)
        else:
            emb = (discord.Embed(description="Insufficient Permission!", colour=0xfe0000))
            await client.send_message(message.channel, embed=emb)

    if message.content.startswith(".admin_commands"):
        if message.author.id == owid:
            embed = discord.Embed(title="**ADMIN COMMANDS LIST**", colour=discord.Colour(0x0cadc3), description="This is the list of commands available", timestamp=datetime.datetime.utcfromtimestamp(1514337763))
            embed.set_footer(text="By Diaxminator#3407", icon_url="https://cdn.discordapp.com/attachments/373102431128518657/395397108993359872/DiscordLogoNew.png")
            embed.add_field(name="Admin Commands List", value="""info1
commands
panel_status
emb1""")
            await client.send_message(message.channel, embed=embed)
        else:
            emb = (discord.Embed(description="Insufficient Permission!", colour=0xfe0000))
            await client.send_message(message.channel, embed=emb)

    if message.content.startswith('.admin_halp'):
        await client.send_message(message.channel, 'Pick the page you want to be directed to (2 pages)')

        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=10.0, author=message.author, check=guess_check)
        if (guess.content) == ("1"):
            await client.send_message(message.channel, '.ping = pong | .peng = ting')
        if (guess.content) == ("2"):
            await client.send_message(message.channel, '.tang = tong | .poo = shit')
        else:
            await client.send_message(message.channel, """That page doesn't exist!""")



####################################################################################################################
        #Welcome messages for Quality Drops 

@client.event
async def on_member_join(Member : discord.User):
    await client.send_message(client.get_channel("403407018012049420")," Please warmly welcome our newest member **<@%s>**! Please read the <#404159815208927234> and <#403434303826034698>. If you need help, feel free to DM one of our Moderators! Enjoy!" % Member.id)
@client.event
async def on_member_remove(member : discord.User):
    await client.send_message(client.get_channel("403407018012049420"),":rose::rose: In the memories of **%s** :rose::rose: " % member.name)

client.run("Mzk0MTAwMzkyMDcxMjY2MzA1.DUJoSw.ewxgvZjxbtbwDPk8jETQxHAJC00")
