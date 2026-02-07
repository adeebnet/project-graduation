import discord
import sqlite3
from tombol import MenuTombol
from discord.ext import commands
from config import TOKEN_DISCORD
from discord import app_commands
import os

from database import setup_db, save_question

# Inisiasi Bot Discord
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None  # MATIKAN help bawaan
)


@bot.event
async def on_ready():
    await bot.tree.sync()
    setup_db()
    print(f"Login sebagai {bot.user}")


@bot.tree.command(name="help", description="Kirim pertanyaan ke admin")
@app_commands.describe(pertanyaan="Isi pertanyaan kamu")
async def help_command(interaction: discord.Interaction, pertanyaan: str):
    save_question(
        interaction.user.id,
        interaction.user.name,
        pertanyaan
    )

    await interaction.response.send_message(
        "Pertanyaan kamu sudah disimpan. Tunggu admin jawab.",
        ephemeral=True  # cuma dia yang lihat
    )

@bot.command() # !start
async def start(ctx):
    await ctx.send(
        "Halo! Saya adalah bot yang menghasilkan gambar berdasarkan deskripsi teks.\n"
        "Cukup kirimkan deskripsi teks."
    )

@bot.command()
async def help(ctx):
    await ctx.send("**# HELP MENU **", view=MenuTombol())

@bot.event
async def on_message(message):
    user_id = message.author.id
    content = message.content.strip()

    if content == "1":
        await message.channel.send(
            'Untuk melakukan pembelian, silakan pilih barang yang Anda minati dan klik '
            '"Tambahkan ke Kartu Belanja". Kemudian, lanjutkan ke Keranjang Belanja dan ' \
            'ikuti petunjuk untuk menyelesaikan pembelian Anda.'
        )

    if content == "2":
        await message.channel.send(
            'Anda dapat mengetahui status pesanan Anda dengan masuk ke akun Anda di ' \
            'situs web kami dan membuka bagian "Pesanan Saya". Di sana, Anda akan melihat ' \
            'status pesanan Anda saat ini.'
        )

    if content == "3":
        await message.channel.send(
            'Jika Anda ingin membatalkan pesanan, silakan hubungi tim layanan pelanggan ' \
            'kami sesegera mungkin. Kami akan berusaha sebaik mungkin untuk membantu Anda ' \
            'membatalkan pesanan sebelum pesanan dikirim.'
        )

    if content == "4":
        await message.channel.send(
            'Jika Anda menerima barang yang rusak, segera hubungi layanan pelanggan ' \
            'kami dan berikan foto kerusakannya. Kami akan membantu Anda menukar atau ' \
            'mengembalikan barang tersebut.'
        )

    if content == "5":
        await message.channel.send(
            'Anda dapat menghubungi dukungan teknis kami dengan menghubungi nomor telepon ' \
            'yang tersedia di situs web kami. Atau, Anda dapat menghubungi kami melalui chatbot kami.'
        )

    if content == "6":
        await message.channel.send(
            'Ya, Anda dapat mengubah informasi pengiriman di halaman pembayaran. Metode pengiriman ' \
            'dan ketentuan yang tersedia akan dicantumkan di sana.'
        )
        
    await bot.process_commands(message)

bot.run(TOKEN_DISCORD)