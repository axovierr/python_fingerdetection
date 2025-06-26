# 🖐️ Finger Detection with Webcam Real-time

Proyek gabut ini hanya bisa mendeteksi jumlah jari tangan yang terbuka secara **real-time** pake webcam, dengan bantuan dari **MediaPipe** dan **OpenCV**.
Program mendeteksi dua tangan (kiri dan kanan), menampilkan jumlah jari masing-masing, dan menghitung total jari secara keseluruhan dengan warna yang berbeda.

---

## 🎥 Fitur yang ada di dalam proyek ini :
- 🟥 Tangan kanan → teks merah
- 🟨 Tangan kiri → teks kuning
- 🟩 Total jari terbuka → teks hijau

---

## ✅ Fitur Utama
- Deteksi kedua tangan secara simultan
- Hitung jumlah jari tangan kiri dan kanan secara akurat
- Tampilkan total jumlah jari
- Bekerja secara real-time melalui webcam

---

## 🚀 Cara Running Program

### 1. Clone Repository dulu bos

```bash
git clone https://github.com/axovierr/python_fingerdetection.git
cd python_fingerdetection
```

### 2. Buat dan Aktifin .environment

**Untuk Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Untuk macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependecies nya yang ada di Requirement
```bash
pip install -r requirements.txt
```

### 4. Tinggal jalankan program aja pake prompt di bawah (Masuk ke venv terlebih dahulu)
```bash
venv\Scripts\activate.bat
python main.py
```

