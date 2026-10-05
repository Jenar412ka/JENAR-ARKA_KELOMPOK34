class MahasiswaTekkom:
    tes = 0
    def __init__(self, nama, konsentrasi):
        self.nama = nama
        self.konsentrasi = konsentrasi
        MahasiswaTekkom.tes =+ 1

    def profil(self):
        print(f"Halo! Saya {self.nama}, mahasiswa Teknik Komputer dengan fokus di {self.konsentrasi}.")

    def deadline_tugas(self, hari):
        print("Waktu tersisa untuk pengumpulan project:")
        while hari > 0:
            print(f"{hari} hari lagi...")
            hari -= 1
        print("Waktu habis! Sistem ditutup.")
    
    @classmethod
    def coba (cls):
      return f"Total Hari: {cls.tes}"
      

obj = MahasiswaTekkom("Dafa Briangga", "Industrial Automation")

obj.profil()
print("-" * 30)
obj.deadline_tugas(3)
print("-" * 30)
print(obj.coba() )