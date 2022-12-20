import busArrivalInfo
import map
import discord
from discord import app_commands

token = "TOKEN"

class myBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=1047369928874934323))
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Available"))
        print("Bot is ready")


bot = myBot(intents=discord.Intents.default())
tree = app_commands.CommandTree(bot)


@tree.command(name="ping", description="ping the user", guild=discord.Object(id=1047369928874934323))
async def self(interaction: discord.Interaction):
    channel = await interaction.user.create_dm()
    await interaction.response.send_message(f"pong @{round(bot.latency*1000)}ms")
    await channel.send(file=discord.File('./foliumMap.png'))


@tree.command(name="도움말", description="동양 버스 봇 사용 방법을 알려드립니다.", guild=discord.Object(id=1047369928874934323))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"/언제와 [ 버스번호 ] [ 방향 ]\n------------------------------\n버스번호 예시: 6631\n방향 예시: 한강타운\n\n*방향\n가양한강타운아파트 방향: 한강타운\n한보구암마을아파트 방향: 한보구암")


@tree.command(name="언제와", description="/언제와 [ 버스번호 ] [ 방향 ]", guild=discord.Object(id=1047369928874934323))
async def self(interaction: discord.Interaction, 버스번호: int, 방향: str):
    channel = await interaction.user.create_dm()
    arrival = busArrivalInfo.getArrivalInfo(버스번호, "가양2단지성지아파트.동양고등학교", 방향)
    gpsXYList = busArrivalInfo.getBusPos(버스번호)
    map.getMap(gpsXYList)
    await interaction.response.send_message(f"{버스번호} | {방향}방면\n\n가장 가까운 버스: {arrival[0]}\n그 다음으로 가까운 버스: {arrival[1]}")
    await channel.send(file=discord.File('./foliumMap.png'))


bot.run(token)