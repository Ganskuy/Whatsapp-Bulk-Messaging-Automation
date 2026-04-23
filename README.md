Siap — ini versi **final README.md full, clean, dan siap langsung copy-paste ke GitHub tanpa perlu edit lagi**:

```markdown
# WhatsApp Bulk Messaging Automation

Script Python untuk mengirim pesan WhatsApp ke banyak nomor secara otomatis menggunakan WhatsApp Web dan Selenium.

---

## 📌 Overview

Project ini memungkinkan pengiriman pesan massal dengan membaca daftar nomor dari file CSV, kemudian mengirim pesan satu per satu melalui WhatsApp Web secara otomatis.

Fitur tambahan seperti validasi nomor, rekap pengiriman, dan delay acak membantu mengurangi risiko kegagalan dan deteksi spam.

---

## ✨ Features

- Mengirim pesan ke banyak nomor dari file CSV  
- Otomatis menambahkan kode negara Indonesia (`+62`)  
- Deteksi nomor tidak valid  
- Progress bar selama proses pengiriman  
- Rekap hasil pengiriman (berhasil & gagal)  
- Pengiriman laporan otomatis ke nomor pertama  
- Penanganan popup WhatsApp Web  

---

## 🛠️ Tech Stack

- Python  
- Selenium  
- Pandas  
- WebDriver Manager  
- TQDM  

---

## 📂 Project Structure

```

.
├── auto_messaging_v2_2.py
├── nomor.csv
└── README.md

````

---

## 📄 CSV Format

File `nomor.csv` harus memiliki format berikut:

```csv
nomor
08123456789
08234567890
````

**Catatan:**

* Nomor tidak perlu menggunakan kode negara (`62`)
* Pastikan format bersih tanpa spasi atau karakter tambahan

---

## ⚙️ Installation

1. Clone repository:

```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

2. Install dependencies:

```bash
pip install selenium pandas webdriver-manager tqdm
```

---

## ▶️ Usage

Jalankan script dengan perintah:

```bash
python auto_messaging_v2_2.py
```

Langkah selanjutnya:

1. Browser akan membuka WhatsApp Web
2. Scan QR code untuk login
3. Tekan `ENTER` di terminal
4. Proses pengiriman akan dimulai

---

## ✉️ Customize Message

Edit bagian berikut di dalam script:

```python
pesan = """
Isi pesan kamu di sini
"""
```

---

## 📊 Output

Script akan menghasilkan:

### Success

Daftar nomor yang berhasil menerima pesan

### Failed

Daftar nomor yang gagal (invalid atau error)

### Recap

Ringkasan hasil pengiriman akan:

* Ditampilkan di terminal
* Dikirim ke nomor pertama

Contoh:

```
REKAP PENGIRIMAN

Berhasil: 10 nomor
 - 628123456789

Gagal: 2 nomor
 - 628111111111
```

---

## 🐞 Debugging

Jika terjadi error, file debug akan otomatis dibuat:

```
debug_<nomor>.html
```

File ini dapat digunakan untuk menganalisis kondisi halaman WhatsApp Web saat terjadi error.

---

## ⚠️ Important Notes

* Gunakan delay untuk menghindari pemblokiran akun
* Hindari penggunaan untuk spam
* Pastikan mematuhi kebijakan WhatsApp

---

## 🔐 Disclaimer

Project ini dibuat untuk tujuan pembelajaran dan otomatisasi.
Segala bentuk penyalahgunaan merupakan tanggung jawab pengguna.

---

## 🤝 Contributing

Kontribusi sangat terbuka. Silakan buat pull request untuk perbaikan atau pengembangan fitur.

---

## 📄 License

Project ini bebas digunakan untuk keperluan pembelajaran dan pengembangan.

```
