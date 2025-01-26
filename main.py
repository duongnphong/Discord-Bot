import discord
import os
import random
from discord.ext import commands
from discord.ui import View
from helpers import get_quote, get_time, is3, worldle_layout, update_em, check
from dotenv import load_dotenv

load_dotenv()
CHANNEL_ID = 1145648663163572224

# from alive import alive

# alive()

intents = discord.Intents.default()
intents.message_content = True
#Create an instant of Bot to connect to Discord
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

chat = [
  "đm tk Long", "Anh Nong!💜", "Nguyễn Hải Long nhà ở Cầu Giấy",
  "Nguyễn Hải Long crush DVA", "nó đang bận đi chơi tinder",
  "đang chill ở CircleK", "có 1 ước mơ là có ny vào mùa đông này",
  "'trong tình yêu ko có chỗ cho sự chờ đợi, chấm hết'", "1 là yêu, 2 là cút",
  "chú gà trống vô tình", "gà trống non tơ", "bố của tình yêu",
  "'tình yêu là gì?''", "tình yêu ko tồn tại nếu như có chỉ đến từ 1 nguồn",
  "rất hay thích phán xét người khác", "https://youtu.be/HUxDdmDd-u8",
  "Một cách đơn giản để hạnh phúc là tôn trọng những gì mình đang có",
  "Chờ đợi như là thử thách của tình yêu và tôi thì đéo đợi được",
  "Đôi khi giá trị của hạnh phúc được tính bằng thời gian người kia chờ đợi bạn.",
  "Sometimes waiting is the hardest thing of all", "sát thủ yêu em",
  "kẻ đánh cắp trái tim", "đô đốc tình yêu", "trưởng giáo phái yêu em",
  "tiến sĩ của cảm xúc", "cử nhân về cảm xúc lứa đôi",
  "chuyên viên nghiên cứu tình trường", "giám đốc tập đoàn chiyeuem",
  "tình yêu anh trao cho e chỉ 1, cả đời a chỉ yêu mình em",
  "nguyện làm con chó để yêu em",
  "Chờ đợi vốn dĩ đau khổ. Cố quên cũng đau khổ. Nhưng nỗi đau tệ nhất chính là không biết lựa chọn nên chờ đợi hay nên quên...",
  "nơi phù hợp nhất để chill có lẽ là CircleK"
]

# chat1 = [
#   "Quá nhi bất cải, thị vị quá hĩ!", "Dục tốc bất đạt", "Dĩ độc trị độc",
#   "Đa mưu, túc trí", "Hoa rơi hữu ý, nước chảy vô tình", "Hậu sinh, khả úy",
#   "Nhất nghệ tinh, Nhất thân vinh", "Nhất túy giải vạn sầu",
#   "Nhất ngôn, cửu đỉnh", "Nhất ngôn ký xuất, tứ mã nan truy",
#   "Nhứt công thành, nhì danh toại", "Song hổ phân tranh, nhứt hổ tử vong",
#   "Thế thiên hành đạo", "Thiên duyên tiền định", "Cẩn tắc vô ưu",
#   "Nhất kiến, chung tình", "Phục hổ, tàng long"
# ]


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user}')
#   await bot.get_channel(VOICE_CHAT_ID).connect()

#   def repeat(guild, voice, audio):
#     voice.play(audio, after=lambda e: repeat(guild, voice, audio))
#     voice.is_playing()

#   audio_source = discord.FFmpegOpusAudio('audio.mp3')

#   voice_client: discord.VoiceClient = discord.utils.get(
#     bot.voice_clients, guild=bot.get_channel(VOICE_CHAT_ID).guild)
#   if not voice_client.is_playing():
#     voice_client.play(
#       audio_source,
#       after=lambda e: repeat(bot.guilds, voice_client, audio_source))
#     voice_client.is_playing()
# Get the channel
  # channel = bot.get_channel(CHANNEL_ID)
  # if not channel:
  #     print("Channel not found!")
  #     return
  
  # # Fetch messages
  # print(f"Fetching messages from channel: {channel.name}")
  # messages = []
  # async for message in channel.history(limit=None):
  #     messages.append(f"[{message.created_at}] {message.author}: {message.content}")
  
  # # Save messages to a file
  # with open("chat_data.txt", "w", encoding="utf-8") as f:
  #     f.write("\n".join(messages))
  
  # print(f"Retrieved {len(messages)} messages. Data saved to chat_data.txt")
  # await bot.close()  # Stop the bot after fetching data


# Reply when the bot is mentioned
@bot.event
async def on_message(message):
  if message.author == bot.user or message.author.bot:
    return

  if bot.user.mentioned_in(message):
    mention = message.author.mention
    await message.channel.send(f"Hey {mention} No tag allowed!")

  if ("CS50") in message.content.upper():
    emoji = "💜"
    await message.add_reaction(emoji)

  if ("PHONG") in message.content.upper():
    emoji = "💜"
    await message.add_reaction(emoji)

  if ("<@645597915359739904>") in message.content:
    mess = random.choice(chat)
    await message.channel.send(mess)

  # if ("<@400288870677348375>") in message.content:
  #   mess = random.choice(chat1)
  #   await message.channel.send(mess)

  await bot.process_commands(message)


# Daily quote with cooldown
@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def quote(ctx):
  td = get_time()
  quote = (f'Your quote for {td} is:\n```yaml\n{get_quote()}\n```')
  await ctx.send(quote)


# Notice users when cooldown is still active
@quote.error
async def quote_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    time = float(error.retry_after) / 3600.00
    await ctx.send("Come back tomorrow, after {:.0f} hour(s)".format(time))


point = {"yr": 0, "pc": 0}


# class of rps games
class MyView(View):

  @discord.ui.button(emoji="✊", custom_id="rock")
  async def button0_callback(self, interaction, button):
    choices = [1, 2, 3]
    pc = random.choice(choices)
    con = "You chosed ✊"
    if pc == 1:
      await interaction.response.edit_message(
        content=
        f"{con} - Cheems chosed ✊ -> Tie\nYou: {point['yr']} - {point['pc']} :Cheems"
      )
    elif pc == 2:
      point["pc"] += 1
      if is3(point["yr"], point["pc"]) == True:
        await interaction.response.edit_message(
          content=
          f"{con} - Cheems chosed 🤚\n**You lost the game!**\nYou: {point['yr']} - {point['pc']} :Cheems",
          view=None)
        point["pc"] = point["yr"] = 0
      else:
        await interaction.response.edit_message(
          content=
          f"{con} - Cheems chosed 🤚 -> You lost\nYou: {point['yr']} - {point['pc']} :Cheems"
        )
    else:
      point["yr"] += 1
      if is3(point["yr"], point["pc"]) == True:
        await interaction.response.edit_message(
          content=
          f"{con} - Cheems chosed ✌\n**You won the game!**\nYou: {point['yr']} - {point['pc']} :Cheems",
          view=None)
        point["pc"] = point["yr"] = 0
      else:
        await interaction.response.edit_message(
          content=
          f"{con} - Cheems chosed ✌ -> You won\nYou: {point['yr']} - {point['pc']} :Cheems"
        )

  @discord.ui.button(emoji="🤚", custom_id="paper")
  async def button1_callback(self, interaction, button):
    con = "You chosed 🤚"
    choices = [1, 2, 3]
    pc = random.choice(choices)
    if pc == 2:
      await interaction.response.edit_message(
        content=
        f"{con} - Cheems chosed 🤚 -> Tie\nYou: {point['yr']} - {point['pc']} :Cheems"
      )
    elif pc == 3:
      point["pc"] += 1
      if is3(point["yr"], point["pc"]) == True:
        await interaction.response.edit_message(
          content=
          f"{con} - Cheems chosed ✌\n**You lost the game!**\nYou: {point['yr']} - {point['pc']} :Cheems",
          view=None)
        point["pc"] = point["yr"] = 0
      else:
        await interaction.response.edit_message(
          content=
          f"{con} - Cheems chosed ✌ -> You lost\nYou: {point['yr']} - {point['pc']} :Cheems"
        )
    else:
      point["yr"] += 1
      if is3(point["yr"], point["pc"]) == True:
        await interaction.response.edit_message(
          content=
          f"{con} - Cheems chosed ✊\n**You won the game!**\nYou: {point['yr']} - {point['pc']} :Cheems",
          view=None)
        point["pc"] = point["yr"] = 0
      else:
        await interaction.response.edit_message(
          content=
          f"{con} - Cheems chosed ✊ -> You won\nYou: {point['yr']} - {point['pc']} :Cheems"
        )

  @discord.ui.button(emoji="✌", custom_id="scissors")
  async def button2_callback(self, interaction, button):
    con = "You chosed ✌"
    choices = [1, 2, 3]
    pc = random.choice(choices)
    if pc == 3:
      await interaction.response.edit_message(
        content=
        f"{con} - Cheems chosed ✌ -> Tie\nYou: {point['yr']} - {point['pc']} :Cheems"
      )
    elif pc == 1:
      point["pc"] += 1
      if is3(point["yr"], point["pc"]) == True:
        await interaction.response.edit_message(
          content=
          f"{con} - Cheems chosed ✊\n**You lost the game!**\nYou: {point['yr']} - {point['pc']} :Cheems",
          view=None)
        point["pc"] = point["yr"] = 0
      else:
        await interaction.response.edit_message(
          content=
          f"{con} - Cheems chosed ✊ -> You lost\nYou: {point['yr']} - {point['pc']} :Cheems"
        )
    else:
      point["yr"] += 1
      if is3(point["yr"], point["pc"]) == True:
        await interaction.response.edit_message(
          content=
          f"{con} - Cheems chosed 🤚\n**You won the game!**\nYou: {point['yr']} - {point['pc']} :Cheems",
          view=None)
        point["pc"] = point["yr"] = 0
      else:
        await interaction.response.edit_message(
          content=
          f"{con} - Cheems chosed 🤚 -> You won\nYou: {point['yr']} - {point['pc']} :Cheems"
        )


# rock, paper, scissors games
@bot.command()
async def rps(ctx):
  view = MyView()
  await ctx.send("Try to reach 3 points to win!", view=view)


# show an embed of all the bot commands
@bot.command()
async def helper(ctx):
  e = discord.Embed(title="Cheems the Doggo", description="*prefix = !*")
  e.set_image(
    url="https://mcdn.coolmate.me/image/October2021/meme-cheems-1.png")
  # e.set_thumbnail(
  #   url="https://mcdn.coolmate.me/image/October2021/meme-cheems-1.png")
  e.add_field(name="`helper`",
              value="Introduce bot general usage",
              inline=False)
  e.add_field(name="`quote`", value="Get a daily quote", inline=False)
  e.add_field(name="`rps`",
              value="Play a game of rock ✊, paper 🤚, scissors ✌",
              inline=False)
  e.add_field(
    name="`word`",
    value=
    "Play a game of :regional_indicator_w::regional_indicator_o::regional_indicator_r::regional_indicator_d::regional_indicator_l::regional_indicator_e:",
    inline=False)
  e.add_field(name="`daily`",
              value="Take an user input of a Japanese sentence",
              inline=False)
  e.add_field(name="`leaderboard`",
              value="Show all users streaks of !daily",
              inline=False)

  await ctx.send(embed=e)


# play a game of wordle
@bot.command()
async def word(ctx):
  word = []
  f = open("words.txt")
  for row in f:
    word.append(row.strip())
  ans = random.choice(word)
  # await ctx.send(ans)

  trial = 0
  guess_correct = False
  clue = ""
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  await ctx.send("Start guessing the word!")
  em = worldle_layout()
  emdisplay = await ctx.send(embed=em)

  while trial < 6 and not guess_correct:
    while True:
      try:
        message = await bot.wait_for(
          "message", check=lambda message: message.author == ctx.author)
        if len(message.content) == 5:
          break
        else:
          raise ValueError
      except ValueError:
        await ctx.send("Invalid guess", delete_after=3)
        await message.delete(delay=3)

    trial += 1
    alphabet, clue, guess_correct = check(ans, message.content, alphabet)
    em = update_em(em, clue, alphabet)
    await emdisplay.edit(embed=em)
    # await ctx.send(clue)

  if guess_correct:
    await ctx.send("Welldone!")
    return
  else:
    await ctx.send(f"Nice try, the word is {ans}")
    return

  @bot.command()
  async def ml(ctx, *what):
    await ctx.send(what)


bot.run(os.environ['TOKEN'])
