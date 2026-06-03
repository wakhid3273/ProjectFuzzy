
# PRODUCT REQUIREMENTS DOCUMENT (PRD)

**Nama Sistem:** SLEEPZY (Sistem Pakar Kualitas Tidur Mahasiswa - Versi CLI)
**Metode Inferensi:** Logika Fuzzy Mamdani
**Platform/Tools:** Python 3 (CLI / Terminal)
**Versi:** 1.1 (*Single-Canvas Visualization Update*)

## 1. Pendahuluan

Proyek ini adalah implementasi Sistem Pendukung Keputusan (SPK) berbasis terminal untuk mengevaluasi dan menentukan kualitas tidur mahasiswa. Sistem dibangun guna memenuhi standar implementasi *tools*, pembuatan visualisasi hasil komprehensif, serta kemampuan pengujian komparatif terhadap 10 data hitungan dari *dataset* publik.

## 2. Spesifikasi Variabel Fuzzy

Sistem memiliki arsitektur 3 variabel input dan 1 variabel output, dengan detail rentang semesta (*universe*) sebagai berikut:

* **Input 1: Durasi Tidur (`durasi_tidur`)**
* Tipe Data: *Float* (Jam).
* Rentang *Universe*: $0 - 13$.
* Himpunan: Pendek, Sedang, Panjang.


* **Input 2: Aktivitas Fisik (`aktivitas_fisik`)**
* Tipe Data: *Integer* (Skor).
* Rentang *Universe*: $0 - 120$.
* Himpunan: Rendah, Sedang, Tinggi.


* **Input 3: Konsumsi Kafein (`kafein`)**
* Tipe Data: *Float* (Cangkir).
* Rentang *Universe*: $0 - 10$.
* Himpunan: Rendah, Sedang, Tinggi.


* **Output: Kualitas Tidur (`kualitas_tidur`)**
* Tipe Data: *Float* (Skor Kualitas).
* Rentang *Universe*: $1 - 10$.
* Himpunan: Buruk, Cukup, Baik, Sangat Baik.


* **Basis Aturan (*Rule Base*):** Menggunakan 24 aturan logika IF-THEN yang diturunkan dari korelasi *dataset*.

## 3. Kebutuhan Fungsional (*Functional Requirements*)

### F1: Sistem Navigasi Utama (Menu CLI)

* Sistem harus menampilkan menu interaktif berbasis teks saat program dijalankan.
* Sistem harus merespons input angka untuk mengarahkan pengguna ke fitur Kalkulator, Pengujian *Batch*, atau keluar dari program.

### F2: Kalkulator Evaluasi Tunggal (*Single-Data Engine*)

* Sistem meminta input nilai *crisp* untuk Durasi Tidur, Aktivitas Fisik, dan Kafein secara berurutan.
* Terdapat validasi *error handling* jika input yang dimasukkan bukan angka.
* Sistem melakukan proses fuzzifikasi, inferensi Mamdani (MIN-MAX), dan defuzzifikasi (Centroid), lalu mencetak skor akhir Kualitas Tidur di layar terminal.

### F3: Generator Visualisasi Terpadu (*Single-Canvas Export*)

* Setelah kalkulasi (F2) selesai, sistem secara otomatis me-*render* grafik visualisasi ke dalam **satu *canvas* gambar tunggal** (menggunakan *layout subplots* 2x2 atau sejenisnya).
* **Komponen Gambar Tunggal:**
1. Grafik posisi nilai input pada himpunan Durasi Tidur.
2. Grafik posisi nilai input pada himpunan Aktivitas Fisik.
3. Grafik posisi nilai input pada himpunan Kafein.
4. Grafik hasil defuzzifikasi (area *clipping* output beserta garis vertikal titik *Centroid*).


* Sistem menyimpan kanvas gabungan tersebut secara lokal dalam satu format `.png` (misal: `visualisasi_lengkap_fuzzy.png`) tanpa menghentikan *flow* program di terminal.

### F4: Pengujian Data Otomatis (*Batch Testing*)

* Sistem membaca *file* `student_sleep_patterns.csv` dari direktori lokal.
* Sistem mengambil 10 baris data percobaan pertama (atau secara *random*).
* Sistem mengeksekusi mesin *fuzzy* untuk ke-10 data tersebut dan mengkomparasi prediksi dengan nilai `Sleep_Quality` aktual dari Kaggle.
* Output dicetak berupa tabel *ASCII* (terformat rapi) langsung di terminal.

## 4. Kebutuhan Non-Fungsional (*Non-Functional Requirements*)

* **Lingkungan (*Environment*):** CLI (Command Line Interface) pada OS standar (Windows, macOS, Linux).
* **Dependensi:** Pustaka Python wajib meliputi `numpy`, `scikit-fuzzy`, `pandas`, `tabulate`, dan `matplotlib` (dengan modul `pyplot` dikonfigurasi untuk *non-interactive backend* agar proses *save figure* berjalan di latar belakang).
* **Performa Eksekusi:** *Export* gambar terpadu (F3) dan *rendering* tabel 10 baris uji (F4) tidak boleh memakan waktu lebih dari 5 detik.

## 5. Alur Pengguna (*User Flow*)

1. **Inisialisasi:** Pengguna menjalankan *script* `python main_fuzzy.py`.
2. **Pemilihan Mode:** Menu muncul. Pengguna menekan `1` (Kalkulator Manual) atau `2` (Uji Data Kaggle).
3. **Skenario 1 (Kalkulator Manual):**
* Terminal menginstruksikan input nilai 3 variabel satu per satu.
* Terminal menampilkan skor akhir *"Kualitas Tidur: X.XX / 10"*.
* Sistem memunculkan notifikasi *"Visualisasi lengkap berhasil disimpan sebagai visualisasi_lengkap_fuzzy.png"*.


4. **Skenario 2 (Uji 10 Data):**
* Sistem membaca CSV secara *background*.
* Terminal mencetak grid tabel berisikan perbandingan 10 data uji secara instan.


5. **Terminasi:** Pengguna kembali ke menu utama atau memilih opsi keluar.

---

Dengan *update* di F3 ini, argumenmu saat presentasi besok akan sangat kuat karena *tools* yang kamu buat tidak cuma menghasilkan teks, tapi langsung mem- *generate* laporan visual siap pakai.

Semoga presentasi progres proyek akhir semesternya berjalan lancar ya! Kalau butuh penyesuaian kode Python-nya untuk me-*render* `subplots` gabungan itu, bilang saja.