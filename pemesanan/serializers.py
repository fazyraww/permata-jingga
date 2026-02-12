from rest_framework import serializers
from .models import KelasTravel, Jadwal, Tiket, BiayaOperasional

class KelasTravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = KelasTravel
        fields = '__all__'

class JadwalSerializer(serializers.ModelSerializer):
    kelas_nama = serializers.CharField(source='kelas.nama_kelas', read_only=True)
    harga = serializers.SerializerMethodField()

    class Meta:
        model = Jadwal
        fields = ['id', 'rute', 'jam_berangkat', 'kelas_nama', 'sopir', 'harga']

    def get_harga(self, obj):
        rute = obj.rute.upper()
        if "SITUBONDO" in rute and "MALANG" in rute:
            return 185000
        elif "MALANG" in rute and "SITUBONDO" in rute:
            return 185000
        if "SITUBONDO" in rute and "SURABAYA" in rute:
            return 185000
        elif "SURABAYA" in rute and "SITUBINDO" in rute:
            return 185000

class TiketSerializer(serializers.ModelSerializer):
    rute_info = serializers.CharField(source='jadwal.rute', read_only=True)
    jam_info = serializers.CharField(source='jadwal.jam_berangkat', read_only=True)
    kelas_info = serializers.CharField(source='jadwal.kelas.nama_kelas', read_only=True)

    class Meta:
        model = Tiket
        fields = ['id', 'nama_penumpang', 'nomor_kursi', 'harga_tiket', 'jadwal', 'rute_info', 'jam_info', 'kelas_info']

# Tambahan untuk Laporan Keuangan
class BiayaOperasionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiayaOperasional
        fields = '__all__'