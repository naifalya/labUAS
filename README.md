#  Sistem Manajemen Perpustakaan Sederhana

**Project UAS Bahasa Pemrograman**


##  Tentang Project

Program ini adalah sistem manajemen perpustakaan sederhana yang dibuat menggunakan Python. Program ini menerapkan konsep **Object-Oriented Programming (OOP)** dan **Modular Programming** untuk mengelola data buku perpustakaan dengan fitur lengkap seperti menambah, melihat, mencari, mengupdate, dan menghapus data buku.

Project ini dibuat untuk memenuhi tugas UAS Bahasa Pemrograman dengan fokus pada penerapan konsep OOP, pemisahan modul (class data, process, dan view), serta implementasi validasi input yang baik.


## Struktur Program

Program ini menggunakan struktur **modular** dengan pemisahan file berdasarkan fungsinya:

```
perpustakaan/
│
├── data.py       # Class Buku (struktur data)
├── process.py    # Class PerpustakaanProcess (logika program)
├── view.py       # Class PerpustakaanView (tampilan)
└── main.py       # Program utama
```

### Penjelasan Setiap File

#### 1. `data.py` - Class Data
Berisi class `Buku` yang mendefinisikan struktur data buku dengan atribut:
- `kode` - Kode unik buku (maksimal 10 karakter)
- `judul` - Judul buku
- `pengarang` - Nama pengarang
- `stok` - Jumlah stok buku (harus angka positif)

#### 2. `process.py` - Class Process (Business Logic)
Berisi class `PerpustakaanProcess` yang menangani semua operasi data:
- `tambah_buku()` - Menambah buku baru, akan raise error jika kode sudah ada
- `lihat_buku()` - Mengembalikan list semua buku
- `cari_buku()` - Mencari buku berdasarkan keyword (tidak case sensitive)
- `update_buku()` - Mengupdate data buku tertentu
- `hapus_buku()` - Menghapus buku dari daftar

File ini menggunakan **list** (`self.daftar_buku = []`) sebagai tempat penyimpanan data sementara.

#### 3. `view.py` - Class View (Tampilan)
Berisi class `PerpustakaanView` yang menangani semua tampilan ke user:
- `tampilan_menu()` - Menampilkan menu pilihan
- `tampilan_tabel()` - Menampilkan data buku dalam format tabel yang rapi
- `pesan_sukses()` - Menampilkan pesan ketika operasi berhasil
- `pesan_error()` - Menampilkan pesan error
- `pesan_info()` - Menampilkan informasi umum

Tabel otomatis memotong teks yang terlalu panjang agar tetap rapi.

#### 4. `main.py` - Program Utama
File ini menghubungkan semua komponen dan menjalankan program. Di sini terdapat:
- Loop menu utama
- Handling input dari user
- Validasi input sebelum diproses
- Exception handling untuk menangani error



## Penerapan Konsep OOP & Modular

### Object-Oriented Programming (OOP)

**1. Encapsulation (Pembungkusan)**
- Data dan method dibungkus dalam class
- Contoh: Class `Buku` membungkus data kode, judul, pengarang, dan stok
- Contoh: Class `PerpustakaanProcess` menyimpan list buku dalam `self.daftar_buku`

**2. Separation of Concerns**
- Setiap class punya tugas yang jelas dan terpisah
- Class `Buku` hanya untuk struktur data
- Class `PerpustakaanProcess` hanya untuk logika operasi data
- Class `PerpustakaanView` hanya untuk tampilan

**3. Abstraction**
- User tidak perlu tahu implementasi internal
- User hanya perlu tahu cara pakai method seperti `tambah_buku()` atau `hapus_buku()`

### Modular Programming

**1. Pemisahan File**
Program dipecah menjadi 4 file berbeda berdasarkan fungsinya. Ini membuat program:
- Lebih mudah dibaca dan dipahami
- Lebih mudah di-debug kalau ada error
- Lebih mudah dikembangkan (misal mau ganti tampilan, tinggal edit `view.py`)

**2. Reusable Code**
Method-method dalam class bisa dipanggil berkali-kali tanpa perlu menulis ulang kode yang sama.



##  Validasi Input

Program memiliki beberapa layer validasi untuk memastikan data yang diinput valid:

### 1. Validasi Field Kosong
Semua field wajib diisi (kode, judul, pengarang, stok). Program menggunakan `.strip()` untuk menghilangkan spasi di awal/akhir input.

### 2. Validasi Tipe Data
Stok harus berupa angka (integer). Jika user input huruf, program akan menampilkan error "Stok wajib angka".

### 3. Validasi Range
Stok tidak boleh negatif. Angka minus tidak masuk akal untuk stok buku.

### 4. Validasi Panjang Karakter
Kode buku maksimal 10 karakter agar tidak merusak tampilan tabel.

### 5. Validasi Duplikasi
Kode buku harus unik. Jika kode sudah ada, program akan menampilkan error menggunakan `raise ValueError`.

### 6. Exception Handling
Program menggunakan `try-except` untuk menangkap error:
- `ValueError` untuk validasi tipe data dan duplikasi
- `KeyboardInterrupt` untuk handle Ctrl+C dengan baik
- Generic exception untuk error yang tidak terduga

**Contoh implementasi:**
```python
try:
    stok_int = int(stok)
    if stok_int < 0:
        tampilan.pesan_error("Stok tidak boleh negatif")
except ValueError:
    tampilan.pesan_error("Stok wajib angka")
```


##  Tampilan Table View

Data buku ditampilkan dalam bentuk tabel dengan format yang rapi:

```
===========================================================================
kode      judul                         pengarang                stok 
===========================================================================
B1        Permata                       Bhayangkara              5    
B2        Lalalaland                    James                    4    
===========================================================================
Total: 2 buku
```


##  Screenshot

### 1. Menu Utama
![Menu Utama](screenshots/menu.png)

### 2. Daftar Buku (Table View)
![Daftar Buku](screenshots/daftar_buku.png)

### 3. Tambah Buku
![Tambah Buku](screenshots/tambah_buku.png)

### 4. Validasi Error
![Validasi](screenshots/validasi.png)



## 🎥 Video Dokumentasi

**Link YouTube:** (https://youtu.be/g2Zq3zGdMFM)

Video berisi penjelasan tentang:
- Struktur program dan penerapan konsep OOP & modular
- Demo semua fitur (tambah, lihat, cari, update, hapus)
- Penjelasan sistem validasi input
- Tampilan table view

**Durasi:** Maksimal 10 menit

