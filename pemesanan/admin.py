from django.contrib import admin
from .models import KelasTravel, Jadwal, Tiket

@admin.register(KelasTravel)
class KelasTravelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_kelas')

@admin.register(Jadwal)
class JadwalAdmin(admin.ModelAdmin):
    # Menampilkan rute, jam, dan kelas di daftar jadwal
    list_display = ('id', 'rute', 'jam_berangkat', 'kelas')
    list_filter = ('kelas',)

@admin.register(Tiket)
class TiketAdmin(admin.ModelAdmin):
    # Hapus 'rute_perjalanan' dan 'tanggal_berangkat' karena sudah pindah ke model Jadwal
    list_display = ('id', 'nama_penumpang', 'nomor_kursi', 'harga_tiket', 'get_rute', 'get_kelas')
    
    # Fungsi pembantu untuk menampilkan data dari tabel Jadwal (Relasi)
    def get_rute(self, obj):
        return obj.jadwal.rute
    get_rute.short_description = 'Rute'

    def get_kelas(self, obj):
        return obj.jadwal.kelas.nama_kelas
    get_kelas.short_description = 'Kelas'