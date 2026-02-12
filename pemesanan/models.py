from django.db import models

class KelasTravel(models.Model):
    nama_kelas = models.CharField(max_length=100)
    def __str__(self): return self.nama_kelas

class Jadwal(models.Model):
    kelas = models.ForeignKey(KelasTravel, on_delete=models.CASCADE)
    rute = models.CharField(max_length=200) 
    jam_berangkat = models.TimeField()
    # TAMBAHKAN BARIS DI BAWAH INI
    sopir = models.CharField(max_length=100, default="Bpk. Supardi")
    mobil = models.CharField(max_length=100, default="Toyota Hiace")
    
    def __str__(self): 
        return f"{self.rute} ({self.jam_berangkat}) - {self.sopir}"

class Tiket(models.Model):
    jadwal = models.ForeignKey(Jadwal, on_delete=models.CASCADE)
    nama_penumpang = models.CharField(max_length=200)
    nomor_kursi = models.CharField(max_length=10)
    harga_tiket = models.IntegerField()
    tanggal_pesan = models.DateTimeField(auto_now_add=True)
    
    # Tabel Tambahan untuk Pengeluaran & Perbaikan
class BiayaOperasional(models.Model):
    KATEGORI_PILIHAN = [
        ('BBM', 'Bahan Bakar'),
        ('SERVIS', 'Perbaikan/Servis'),
        ('GAJI', 'Gaji Sopir'),
        ('LAIN', 'Lain-lain'),
    ]
    kategori = models.CharField(max_length=20, choices=KATEGORI_PILIHAN)
    deskripsi = models.TextField()
    nominal = models.IntegerField()
    tanggal = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.kategori} - {self.nominal}"