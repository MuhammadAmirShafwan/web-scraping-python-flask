# 🕸️ Web Scraping Python Flask

Proyek ini adalah aplikasi sederhana berbasis Python dan Flask untuk melakukan **web scraping**. Aplikasi ini memungkinkan pengguna untuk mengambil data dari situs tertentu, memprosesnya, dan menampilkannya di antarmuka web secara real-time.

## 🧠 Tujuan Proyek

- Melatih kemampuan **web scraping** menggunakan Python.
- Menerapkan **Flask** sebagai web framework ringan.
- Menampilkan hasil scraping melalui antarmuka web.
- Cocok sebagai pembelajaran untuk pemula yang ingin memahami scraping dan backend sederhana dengan Python.

---

## 📦 Tech Stack

- **Python 3**
- **Flask** (Web framework)
- **Requests & BeautifulSoup** (Untuk scraping)
- **Bootstrap** (Untuk tampilan sederhana)

---

## 🚀 Cara Menjalankan Proyek

### 1. Clone Repository

```bash
git clone https://github.com/MuhammadAmirShafwan/web-scraping-python-flask.git
cd web-scraping-python-flask
```

### 2. Buat Virtual Environment (Opsional tapi direkomendasikan)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi

```bash
python app.py
```

### 5. Akses dari Browser

Buka browser dan akses:

```
http://localhost:5000
```

---

## 📝 Fitur Aplikasi

- Input URL yang ingin di-scrape.
- Mengambil konten tertentu dari halaman web (judul, harga, deskripsi, dll — tergantung implementasi).
- Menampilkan data hasil scraping di browser.

---

## 🧪 Contoh Penggunaan

Misalnya kamu ingin scraping data dari OLX atau situs jual beli lain, kamu bisa mengubah logika scraping di dalam file `scraper.py` atau bagian tertentu di `app.py`.

---

## 📂 Struktur Folder

```
web-scraping-python-flask/
│
├── app.py                # Entry point aplikasi Flask
├── scraper.py            # Fungsi utama untuk scraping
├── templates/
│   └── index.html        # Template HTML
├── static/               # Folder untuk file CSS/JS jika ada
└── requirements.txt      # Daftar dependencies Python
```

---
