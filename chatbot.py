import busArrivalInfo
import discord
from discord import app_commands

token = "MTA0NzM2ODQzMzEyNzQwMzU5MA.Ge2rFE.65ELobzpR3UP_3NMLugRyhq8XAigk5DuSohlLg"

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
    await interaction.response.send_message(f"pong @{round(bot.latency*1000)}ms")

@tree.command(name="언제와", description='버스번호, 방향("한강타운" 또는 "한보구암")', guild=discord.Object(id=1047369928874934323))
async def self(interaction: discord.Interaction, 버스번호: int, 방향: str):
    arrival = busArrivalInfo.getArrivalInfo(버스번호, "가양2단지성지아파트.동양고등학교", 방향)
    await interaction.response.send_message(f"{버스번호} {방향}방면\n가장 가까운 버스: {arrival[0]}\n그 다음으로 가까운 버스: {arrival[1]}")
bot.run(token)