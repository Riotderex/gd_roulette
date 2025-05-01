import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

def load_demons_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            demons = [line.strip() for line in f if line.strip()]
            return demons
    except Exception as e:
        print(f"Ошибка при чтении {filename}: {e}")
        return []

@bot.command()
async def easy_demon_roulette(ctx):
    demons = load_demons_from_file("easy_demons.txt")
    if not demons:
        await ctx.send("Список Easy Demons пуст или не найден.")
        return

    random_demon = random.choice(demons)
    await ctx.send(f"🎲 Случайный Easy Demon: **{random_demon}**")

@bot.command()
async def medium_demon_roulette(ctx):
    demons = load_demons_from_file("medium_demons.txt")
    if not demons:
        await ctx.send("Список Medium Demons пуст или не найден.")
        return

    random_demon = random.choice(demons)
    await ctx.send(f"🎲 Случайный Medium Demon: **{random_demon}**")

@bot.command()
async def hard_demon_roulette(ctx):
    demons = load_demons_from_file("hard_demons.txt")
    if not demons:
        await ctx.send("Список Hard Demons пуст или не найден.")
        return

    random_demon = random.choice(demons)
    await ctx.send(f"🎲 Случайный Hard Demon: **{random_demon}**")

@bot.command()
async def insane_demon_roulette(ctx):
    demons = load_demons_from_file("insane_demons.txt")
    if not demons:
        await ctx.send("Список Insane Demons пуст или не найден.")
        return

    random_demon = random.choice(demons)
    await ctx.send(f"🎲 Случайный Insane Demon: **{random_demon}**")

@bot.command()
async def extreme_demon_roulette(ctx):
    demons = load_demons_from_file("extreme_demons.txt")
    if not demons:
        await ctx.send("Список Extreme Demons пуст или не найден.")
        return

    random_demon = random.choice(demons)
    await ctx.send(f"🎲 Случайный Extreme Demon: **{random_demon}**")

bot.run("")  # Используй .env в реальном кодеm