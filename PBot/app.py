# Discord Altyapı by Proxy Dev.
# Github: https://github.com/proxyhk
# Yayın Yılı: 2025 Ocak
# Discord: psxdev

import discord

TOKEN = "#TOKEN_CODE#" # Buraya bot tokeninizi yazınız.
OWNER_ID = 12345678912345678  # Buraya kendi Discord kullanıcı ID'ni yazabilirsin.

intents = discord.Intents.default()

bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} olarak giriş yaptı!")
    try:
        synced = await tree.sync()
        print(f"Slash komutları senkronize edildi: {len(synced)} komut")
    except Exception as e:
        print(f"Slash komutları senkronize edilirken hata oluştu: {e}")

@tree.command(name="ping", description="Botun gecikme süresini gösterir.")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)  # Milisaniye cinsinden gecikme
    await interaction.response.send_message(f"Pong! {latency}ms")

# /owner komutu (Bot sahibini gösterir)
@tree.command(name="owner", description="Botun sahibini gösterir.")
async def owner(interaction: discord.Interaction):
    owner_user = await bot.fetch_user(OWNER_ID)  # Discord'dan bot sahibinin bilgilerini al
    await interaction.response.send_message(f"Bu bot <@{OWNER_ID}> (`{owner_user.name}`) tarafından geliştirildi.")

bot.run(TOKEN)
