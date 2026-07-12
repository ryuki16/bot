import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Hore! Bot {bot.user.name} sudah aktif dan siap bantu remaja!")

# Perintah untuk tanya cara pilah sampah (!pilah [nama_benda])
@bot.command(aliases=['sort'])
async def pilah(ctx, *, benda: str):
    
    if "plastik" in benda or "botol" in benda:
        respons = f"🥤 **{benda.capitalize()}** masuk ke sampah **Anorganik (Bisa Didaur Ulang)**. Kumpulin dulu, nanti bisa dibawa ke Bank Sampah terdekat ya!"
    elif "makanan" in benda or "daun" in benda or "sayur" in benda:
        respons = f"🍎 **{benda.capitalize()}** masuk ke sampah **Organik**. Cocok banget dijadiin pupuk kompos di halaman rumah!"
    elif "kardus" in benda or "kertas" in benda:
        respons = f"📦 **{benda.capitalize()}** bisa didaur ulang! Tapi pastikan kondisinya kering dan gak kena minyak ya."
    else:
        respons = f"🔍 Waduh, bot belum tahu pasti tentang **{benda}**. Coba pilah berdasarkan bahannya: plastik/kertas (anorganik) atau sisa makanan (organik)!"
        
    await ctx.send(respons)

# Perintah untuk minta ide kerajinan dari sampah
@bot.command(aliases=['craft', 'upcycle'])
async def ide(ctx, *, bahan: str):
    bahan = bahan.lower()
    
    if "kardus" in bahan:
        respons = "✨ **Ide Upcycle Kardus:** Jangan dibuang! Kamu bisa potong dan rakit jadi **tempat skincare aesthetic** atau kotak pembatas laci kamarmu."
    elif "botol" in bahan:
        respons = "✨ **Ide Upcycle Botol Plastik:** Potong bagian tengahnya, hias pakai cat akrilik, dan sulap jadi **pot tanaman hidroponik** kamar yang keren!"
    elif "baju" in bahan or "kaos" in bahan:
        respons = "✨ **Ide Upcycle Baju Bekas:** Gunting bagian lengan dan jahit bawahnya untuk diubah jadi **tote bag belanja** tanpa perlu keahlian menjahit rumit!"
    else:
        respons = f"💡 Belum ada ide spesifik untuk **{bahan}**. Tapi coba cek Pinterest untuk cari keyword: *'DIY upcycle {bahan}'*!"

    await ctx.send(respons)

# help command
@bot.command(aliases=['commands'])
async def daftar_perintah(ctx):
    help_message = [
        "📚 **Daftar Perintah Bot Lingkungan:**",
        "1. `!pilah [nama_benda]` - Tanyakan cara memilah sampah dari benda tertentu.",
        "2. `!ide [bahan]` - Dapatkan ide kerajinan dari bahan bekas.",
        "3. `!daftar_perintah` - Menampilkan daftar perintah ini.",
    ]
    help_message = "\n".join(help_message)
    await ctx.send(f"Available commands:\n{help_message}")

bot.run('token')
