from data import Buku

class PerpustakaanProcess:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self,kode,judul,pengarang,stok):
        for buku in self.daftar_buku:
            if buku.kode == kode:
                raise ValueError(f"kode buku'{kode}'sudah ada")

        buku_baru = Buku(kode,judul,pengarang,stok)
        self.daftar_buku.append(buku_baru)

    def lihat_buku(self):
        return self.daftar_buku

    def cari_buku(self,keyword):
        hasil_buku = []
        for buku in self.daftar_buku:
            if keyword.lower()in buku.judul.lower()or keyword.lower()in buku.kode.lower():
                hasil_buku.append(buku)
        return hasil_buku

    def update_buku(self,kode,judul=None,pengarang=None,stok=None):
        for buku in self.daftar_buku:
            if buku.kode == kode:
                if judul:
                    buku.judul = judul
                if pengarang:
                    buku.pengarang = pengarang
                if stok is not None:
                    buku.stok = stok
                return True
        return False

    def hapus_buku(self,kode):
        for i, buku in enumerate(self.daftar_buku):
            if buku.kode == kode:
                del self.daftar_buku[i]
                return True
        return False

