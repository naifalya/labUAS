class PerpustakaanView:
    def tampilan_menu(self):
        print("\n"+"="*50)
        print("    SISTEM PERPUSTAKAAN")
        print("="*50)
        print("1. tambah buku")
        print("2. tampilan buku")
        print("3. cari buku")
        print("4. update buku")
        print("5. hapus buku")
        print("0. Keluar")
        print("="*50)

    def tampilan_tabel(self, daftar_buku):
        if len(daftar_buku) == 0:
            print("\n[!] belum ada buku dalam perpustakaan")
            return
        print("\n"+"="*75)
        print(f"{'kode':<10}{'judul':<30}{'pengarang':<25}{'stok':<5}")
        print("="*75)
        for buku in daftar_buku:
            judul_pendek = buku.judul[:28]+"..."if len(buku.judul) > 30 else buku.judul
            pengarang_pendek = buku.pengarang[:23] +"..."if len(buku.pengarang)>25 else buku.pengarang
            print(f"{buku.kode:<10}{judul_pendek:<30}{pengarang_pendek:<25}{buku.stok:<5}")
        print("="*75)
        print(f"Total: {len(daftar_buku)}buku")

    def pesan_sukses(self,pesan):
        print(f"\n[Berhasil]{pesan}")

    def pesan_error(self,pesan):
        print(f"\n [x]ERROR {pesan}")

    def pesan_info(self,pesan):
        print(f"\n [i] {pesan}")