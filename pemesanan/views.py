from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import KelasTravel, Jadwal, Tiket
from .serializers import KelasTravelSerializer, JadwalSerializer, TiketSerializer
from .models import BiayaOperasional
from .serializers import BiayaOperasionalSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class BiayaOperasionalViewSet(viewsets.ModelViewSet):
    queryset = BiayaOperasional.objects.all()
    serializer_class = BiayaOperasionalSerializer

# --- API VIEWS (Tetap Sama) ---
class KelasTravelViewSet(viewsets.ModelViewSet):
    queryset = KelasTravel.objects.all()
    serializer_class = KelasTravelSerializer
    permission_classes = [AllowAny]

class JadwalViewSet(viewsets.ModelViewSet):
    queryset = Jadwal.objects.all()
    serializer_class = JadwalSerializer
    permission_classes = [AllowAny]

class TiketViewSet(viewsets.ModelViewSet):
    queryset = Tiket.objects.all()
    serializer_class = TiketSerializer
    permission_classes = [AllowAny]

# --- WEB VIEWS ---
def web_tiket_list(request):
    """Halaman Dashboard Utama / Tabel Tiket"""
    return render(request, 'tiket_list.html')

def web_login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login_frontend.html', {'error': 'Username atau Password salah!'})
    return render(request, 'login_frontend.html')

def web_jadwal_armada(request):
    konteks = {
        'daftar_jadwal': Jadwal.objects.all()
    }
    return render(request, 'jadwal_armada.html', konteks)

def web_sopir_list(request):
    """View untuk daftar sopir"""
    return render(request, 'sopir_list.html')

# --- CRUD VIEWS DENGAN LOGIKA TAMBAHAN ---

class TiketCreateView(CreateView):
    model = Tiket
    fields = ['nama_penumpang', 'jadwal', 'nomor_kursi', 'harga_tiket']
    template_name = 'tiket_form.html'
    success_url = reverse_lazy('dashboard')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Tambahkan class form-control agar bagus tampilannya
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            
        form.fields['nama_penumpang'].widget.attrs.update({'placeholder': 'Masukkan Nama Lengkap'})
        form.fields['nomor_kursi'].widget.attrs.update({'placeholder': 'Contoh: A1 atau 05'})
        form.fields['harga_tiket'].widget.attrs.update({'id': 'id_harga_tiket', 'readonly': 'readonly'})
        form.fields['jadwal'].empty_label = "-- Pilih Jadwal & Rute --"
        return form

class TiketUpdateView(UpdateView):
    model = Tiket
    fields = ['nama_penumpang', 'jadwal', 'nomor_kursi', 'harga_tiket']
    template_name = 'tiket_form.html'
    success_url = reverse_lazy('dashboard')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Penting: Django otomatis mengisi 'instance' ke dalam form di UpdateView
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        
        # Samakan ID dan atribut agar script JS harga tetap jalan
        form.fields['harga_tiket'].widget.attrs.update({'id': 'id_harga_tiket'})

class TiketDeleteView(DeleteView):
    model = Tiket
    template_name = 'tiket_confirm_delete.html'
    success_url = reverse_lazy('dashboard')
    
class BiayaOperasionalViewSet(viewsets.ModelViewSet):
    queryset = BiayaOperasional.objects.all()
    serializer_class = BiayaOperasionalSerializer
    permission_classes = [IsAuthenticated]