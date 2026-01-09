from data import Buku
from process import PerpustakaanProcess
from view import PerpustakaanView

perpus= PerpustakaanProcess()
tampilan= PerpustakaanView()

try:
    perpus.tambah_buku("B1","Permata","Bhayangkara",5)
    perpus.tambah_buku("B2","Lalalaland","James",4)
except:
    pass

print("\n"+"="*50)
print("SELAMAT DATANG DI PERPUSTAKAAN")
print("="*50)

while True:
    tampilan.tampilan_menu()
    try:
        pilihan=input("\n Pilihan Menu(0-5):")

        #Menambahkan
        if pilihan == "1":
            print("\n TAMBAH BUKU BARU")
            kode= input("\n Pilihan Kode : ").strip()
            judul= input("\n Judul Buku : ").strip()
            pengarang= input("\n Pengarang Buku : ").strip()
            stok= input("\n Stok Buku : ").strip()

            if not kode or not judul or not pengarang or not stok:
                tampilan.pesan_error("Wajib terisi")
                continue

            try:
                stok_int=int(stok)
                if stok_int<0:
                    tampilan.pesan_error("Stok tidak boleh negatif")
            except ValueError:
                tampilan.pesan_error("Stok wajib angka")
                continue

            if len(kode)>10:
                tampilan.pesan_error("Kode buku maksimal 10 karakter")
                continue

            try:
                perpus.tambah_buku(kode,judul,pengarang,stok)
                tampilan.pesan_sukses("Buku berhasil ditambahkan")
            except ValueError as e:
                tampilan.pesan_error(str(e))

        #melihat
        elif pilihan == "2":
            daftar= perpus.lihat_buku()
            tampilan.tampilan_tabel(daftar)

        #mencari
        elif pilihan == "3":
            keyword = input("\n Pilihan Keyword: ").strip()
            if not keyword:
                tampilan.pesan_error("Keyword tidak boleh kosong")
                continue
            hasil = perpus.cari_buku(keyword)

            if hasil:
                tampilan.pesan_info(f"Ditemukan {len(hasil)} buku")
                tampilan.tampilan_tabel(hasil)
            else:
                tampilan.pesan_info("Buku tidak ada")

        #mengupdate
        elif pilihan == "4":
            kode=input("\nMasukkan kode buku yang akan diupdate:").strip()
            if not kode:
                tampilan.pesan_error("kode tidak boleh kosong")
                continue
            print("\n(Tekan Enter jika tidak ingin merubah)")
            judul=input("judul baru : ").strip()
            pengarang=input("Pengarang baru : ").strip()
            stok=input("Stok baru : ").strip()
            stok_int= None
            if stok:
                try:
                    stok_int=int(stok)
                    if stok_int<0:
                        tampilan.pesan_error("Stok tidak boleh negatif")
                        continue
                except ValueError:
                    tampilan.pesan_error("Stok harus berupa angka")
                    continue
            if perpus.update_buku(kode,judul or None,pengarang or None, stok_int):
                tampilan.pesan_sukses("Buku berhasil diupdate")
            else:
                tampilan.pesan_error(f"Buku tidak ada")

        #Menghapus
        elif pilihan == "5":
            kode=input("\nMasukkan kode buku yang akan dihapus:").strip()
            if not kode:
                tampilan.pesan_error("kode tidak boleh kosong")
                continue
            konfirmasi= input(f"Yakin ingin hapus buku'{kode}'? (y/n): ").lower()
            if konfirmasi == "y":
                if perpus.hapus_buku(kode):
                    tampilan.pesan_sukses("Buku berhasil dihapus")
                else:
                    tampilan.pesan_error(f"Buku dengan kode '{kode}' tidak ditemukan")
            else:
                tampilan.pesan_info("Penghapusan dibatalkan.")

        #Keluar
        elif pilihan == "0":
            print("\n"+"="*50)
            print("Terima kasih sudah menggunakan program ini")
            print("="*50+"\n")
            break
        else:
            tampilan.pesan_error("Pilihan tidak valid, pilih 0-5")

    except KeyboardInterrupt:
        print("Program dihentikan")
        break
    except Exception as e:
       tampilan.pesan_error(f"\n ERROR: {e}")