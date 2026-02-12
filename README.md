# 🚌 Permata Jingga Travel - Sistem Reservasi Tiket

Sistem Informasi Manajemen Reservasi Tiket Travel berbasis Django & REST API

## 🌟 Fitur Utama

- 📊 Dashboard statistik real-time
- 🚗 Manajemen armada (mobil & sopir)
- 🎫 Cetak tiket otomatis
- 📅 Jadwal keberangkatan
- 💰 Laporan keuangan & biaya operasional
- 🔐 Autentikasi JWT

## 🛠️ Tech Stack

- **Backend:** Django 5.x + Django REST Framework
- **Frontend:** HTML5, Bootstrap 5, JavaScript (Fetch API)
- **Database:** SQLite (dev) / PostgreSQL (production)
- **Auth:** JWT (SimpleJWT)
- **API Docs:** Swagger UI

## 📦 Instalasi

1. Clone repository
```bash
git clone https://github.com/fazyraww/permata-jingga.git
cd permata-jingga
```

2. Buat virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Migrasi database
```bash
python manage.py migrate
```

5. Buat superuser
```bash
python manage.py createsuperuser
```

6. Jalankan server
```bash
python manage.py runserver
```

7. Akses aplikasi
- Frontend: http://localhost:8000
- Admin: http://localhost:8000/admin
- API Docs: http://localhost:8000/api/docs

## 📸 Screenshots

<img width="1900" height="912" alt="image" src="https://github.com/user-attachments/assets/89950050-b440-4090-84cc-7e463fcda6e4" />


## 👤 Author

Fahmi Fahrezy - UAS Framework Programming
