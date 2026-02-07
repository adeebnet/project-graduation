import discord

class MenuTombol(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Bagaimana cara saya melakukan pembelian?", style=discord.ButtonStyle.success)
    async def tombol1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Untuk melakukan pembelian, silakan pilih barang yang Anda minati dan klik "Tambahkan ke Kartu Belanja". Kemudian, lanjutkan ke Keranjang Belanja dan ikuti petunjuk untuk menyelesaikan pembelian Anda.', ephemeral=True)

    @discord.ui.button(label="Bagaimana saya dapat mengetahui status pesanan saya?", style=discord.ButtonStyle.success)
    async def tombol2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Anda dapat mengetahui status pesanan Anda dengan masuk ke akun Anda di situs web kami dan membuka bagian "Pesanan Saya". Di sana, Anda akan melihat status pesanan Anda saat ini.', ephemeral=True)

    @discord.ui.button(label="Bagaimana saya bisa membatalkan pesanan?", style=discord.ButtonStyle.success)
    async def tombol3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Jika Anda ingin membatalkan pesanan, silakan hubungi tim layanan pelanggan kami sesegera mungkin. Kami akan berusaha sebaik mungkin untuk membantu Anda membatalkan pesanan sebelum pesanan dikirim.', ephemeral=True)

    @discord.ui.button(label="Apa yang harus saya lakukan jika pesanan tiba dalam keadaan rusak?", style=discord.ButtonStyle.success)
    async def tombol4(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Jika Anda menerima barang yang rusak, segera hubungi layanan pelanggan kami dan berikan foto kerusakannya. Kami akan membantu Anda menukar atau mengembalikan barang tersebut.', ephemeral=True)

    @discord.ui.button(label="Bagaimana cara menghubungi dukungan teknis?", style=discord.ButtonStyle.success)
    async def tombol5(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Anda dapat menghubungi dukungan teknis kami dengan menghubungi nomor telepon yang tersedia di situs web kami. Atau, Anda dapat menghubungi kami melalui chatbot kami.', ephemeral=True)

    @discord.ui.button(label="Bisakah saya mengubah metode pengiriman selama pembayaran?", style=discord.ButtonStyle.success)
    async def tombol6(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Ya, Anda dapat mengubah informasi pengiriman di halaman pembayaran. Metode pengiriman dan ketentuan yang tersedia akan dicantumkan di sana.', ephemeral=True)