# PRODUCT REQUIREMENTS DOCUMENT (PRD)

**Nama Sistem:** SLEEPZY (Sistem Pakar Kualitas Tidur Mahasiswa - Versi CLI)
**Metode Inferensi:** Logika Fuzzy Mamdani
**Platform/Tools:** Python 3 (CLI / Terminal)
**Versi:** 1.1 (_Single-Canvas Visualization Update_)

## 1. Pendahuluan

Proyek ini adalah implementasi Sistem Pendukung Keputusan (SPK) berbasis terminal untuk mengevaluasi dan menentukan kualitas tidur mahasiswa. Sistem dibangun guna memenuhi standar implementasi _tools_, pembuatan visualisasi hasil komprehensif, serta kemampuan pengujian komparatif terhadap 10 data hitungan dari _dataset_ publik.

## 2. Spesifikasi Variabel Fuzzy

Sistem memiliki arsitektur 3 variabel input dan 1 variabel output, dengan detail rentang semesta (_universe_) sebagai berikut:

- **Input 1: Durasi Tidur (`durasi_tidur`)**
- Tipe Data: _Float_ (Jam).
- Rentang _Universe_: $0 - 13$.
- Himpunan: Pendek, Sedang, Panjang.

- **Input 2: Aktivitas Fisik (`aktivitas_fisik`)**
- Tipe Data: _Integer_ (Skor).
- Rentang _Universe_: $0 - 120$.
- Himpunan: Rendah, Sedang, Tinggi.

- **Input 3: Konsumsi Kafein (`kafein`)**
- Tipe Data: _Float_ (Cangkir).
- Rentang _Universe_: $0 - 10$.
- Himpunan: Rendah, Sedang, Tinggi.

- **Output: Kualitas Tidur (`kualitas_tidur`)**
- Tipe Data: _Float_ (Skor Kualitas).
- Rentang _Universe_: $1 - 10$.
- Himpunan: Buruk, Cukup, Baik.

- **Basis Aturan (_Rule Base_):** Menggunakan 27 aturan logika IF-THEN yang diturunkan dari korelasi _dataset_.

## 3. Kebutuhan Fungsional (_Functional Requirements_)

### F1: Sistem Navigasi Utama (Menu CLI)

- Sistem harus menampilkan menu interaktif berbasis teks saat program dijalankan.
- Sistem harus merespons input angka untuk mengarahkan pengguna ke fitur Kalkulator, Pengujian _Batch_, atau keluar dari program.

### F2: Kalkulator Evaluasi Tunggal (_Single-Data Engine_)

- Sistem meminta input nilai _crisp_ untuk Durasi Tidur, Aktivitas Fisik, dan Kafein secara berurutan.
- Terdapat validasi _error handling_ jika input yang dimasukkan bukan angka.
- Sistem melakukan proses fuzzifikasi, inferensi Mamdani (MIN-MAX), dan defuzzifikasi (Centroid), lalu mencetak skor akhir Kualitas Tidur di layar terminal.

### F3: Generator Visualisasi Terpadu (_Single-Canvas Export_)

- Setelah kalkulasi (F2) selesai, sistem secara otomatis me-_render_ grafik visualisasi ke dalam **satu _canvas_ gambar tunggal** (menggunakan _layout subplots_ 2x2 atau sejenisnya).
- **Komponen Gambar Tunggal:**

1. Grafik posisi nilai input pada himpunan Durasi Tidur.
2. Grafik posisi nilai input pada himpunan Aktivitas Fisik.
3. Grafik posisi nilai input pada himpunan Kafein.
4. Grafik hasil defuzzifikasi (area _clipping_ output beserta garis vertikal titik _Centroid_).

- Sistem menyimpan kanvas gabungan tersebut secara lokal dalam satu format `.png` (misal: `visualisasi_lengkap_fuzzy.png`) tanpa menghentikan _flow_ program di terminal.

### F4: Pengujian Data Otomatis (_Batch Testing_)

- Sistem membaca _file_ `student_sleep_patterns.csv` dari direktori lokal.
- Sistem mengambil 10 baris data percobaan pertama (atau secara _random_).
- Sistem mengeksekusi mesin _fuzzy_ untuk ke-10 data tersebut dan mengkomparasi prediksi dengan nilai `Sleep_Quality` aktual dari Kaggle.
- Output dicetak berupa tabel _ASCII_ (terformat rapi) langsung di terminal.

## 4. Kebutuhan Non-Fungsional (_Non-Functional Requirements_)

- **Lingkungan (_Environment_):** CLI (Command Line Interface) pada OS standar (Windows, macOS, Linux).
- **Dependensi:** Pustaka Python wajib meliputi `numpy`, `scikit-fuzzy`, `pandas`, `tabulate`, dan `matplotlib` (dengan modul `pyplot` dikonfigurasi untuk _non-interactive backend_ agar proses _save figure_ berjalan di latar belakang).
- **Performa Eksekusi:** _Export_ gambar terpadu (F3) dan _rendering_ tabel 10 baris uji (F4) tidak boleh memakan waktu lebih dari 5 detik.

## 5. Alur Pengguna (_User Flow_)

1. **Inisialisasi:** Pengguna menjalankan _script_ `python main_fuzzy.py`.
2. **Pemilihan Mode:** Menu muncul. Pengguna menekan `1` (Kalkulator Manual) atau `2` (Uji Data Kaggle).
3. **Skenario 1 (Kalkulator Manual):**

- Terminal menginstruksikan input nilai 3 variabel satu per satu.
- Terminal menampilkan skor akhir _"Kualitas Tidur: X.XX / 10"_.
- Sistem memunculkan notifikasi _"Visualisasi lengkap berhasil disimpan sebagai visualisasi_lengkap_fuzzy.png"_.

4. **Skenario 2 (Uji 10 Data):**

- Sistem membaca CSV secara _background_.
- Terminal mencetak grid tabel berisikan perbandingan 10 data uji secara instan.

5. **Terminasi:** Pengguna kembali ke menu utama atau memilih opsi keluar.

---

Dengan _update_ di F3 ini, argumenmu saat presentasi besok akan sangat kuat karena _tools_ yang kamu buat tidak cuma menghasilkan teks, tapi langsung mem- _generate_ laporan visual siap pakai.

Semoga presentasi progres proyek akhir semesternya berjalan lancar ya! Kalau butuh penyesuaian kode Python-nya untuk me-_render_ `subplots` gabungan itu, bilang saja.
