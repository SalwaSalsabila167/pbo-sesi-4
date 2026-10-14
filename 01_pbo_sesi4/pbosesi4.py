class Karyawan:
    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.nama = nama                    # Atribut public
        self.id_karyawan = id_karyawan        # Atribut public
        self.__gaji_pokok = gaji_pokok        # Atribut private (encapsulation)

    # Getter untuk mengambil nilai gaji pokok
    def get_gaji_pokok(self):
        return self.__gaji_pokok

    # Setter untuk mengubah nilai gaji pokok dengan validasi
    def set_gaji_pokok(self, gaji_baru):
        if gaji_baru > 0:
            self.__gaji_pokok = gaji_baru
        else:
            print("Peringatan: Gaji pokok tidak boleh kurang dari atau sama dengan 0!")

    # Method dasar untuk menghitung gaji total
    def hitung_gaji_total(self):
        return self.__gaji_pokok

    # Method untuk menampilkan informasi dasar karyawan
    def tampilkan_info(self):
        print(f"\n--- INFORMASI GAJI KARYAWAN ---")
        print(f"ID Karyawan  : {self.id_karyawan}")
        print(f"Nama         : {self.nama}")
        print(f"Gaji Pokok   : Rp {self.get_gaji_pokok():,.0f}")


# Inheritance dari Karyawan
class KaryawanTetap(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):      
        # Memanggil constructor dari class induk (super)
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan            # Atribut tambahan public

    # Method Overriding (Polymorphism): Mengubah rumus hitung gaji total
    def hitung_gaji_total(self):
        return self.get_gaji_pokok() + self.tunjangan

    # Override / Tambahan info khusus Karyawan Tetap
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Tunjangan    : Rp {self.tunjangan:,.0f}")
        print(f"Total Gaji   : Rp {self.hitung_gaji_total():,.0f}")
        print("-" * 35)


# ==========================================
# PROGRAM UTAMA DENGAN INPUT INTERAKTIF
# ==========================================
if __name__ == "__main__":
    print("=== MASUKKAN DATA KARYAWAN TETAP ===")
    
    # Mengambil input dari pengguna di terminal
    nama_input = input("Masukkan Nama Karyawan        : ")
    id_input = input("Masukkan ID Karyawan          : ")
    
    # Gaji dan tunjangan dikonversi ke tipe data float/int
    gaji_input = float(input("Masukkan Gaji Pokok (Rp)      : "))
    tunjangan_input = float(input("Masukkan Tunjangan (Rp)       : "))
    
    # Membuat objek KaryawanTetap dari data yang diinput
    karyawan_user = KaryawanTetap(nama_input, id_input, gaji_input, tunjangan_input)
    
    # Menampilkan hasil output
    karyawan_user.tampilkan_info()

    # Contoh uji coba setter dengan nilai salah
    pilihan_uji = input("\nApakah ingin menguji validasi gaji negatif? (y/t): ")
    if pilihan_uji.lower() == 'y':
        gaji_salah = float(input("Masukkan angka gaji baru yang <= 0 (contoh: -1000): "))
        karyawan_user.set_gaji_pokok(gaji_salah)