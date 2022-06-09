from mobil import Mobil

class Innova(Mobil):
    def __init__(self):
        super().__init__("Manual", "TOYOTA Innova Venturer")
        
    def info(self):
        nopol = "B 1234 AA"
        print("Nomor Polisi: ", nopol)
        print("Tipe Mobil: %s \nMerek: %s" %(self.tipemobil, self.merek))

    def tampilharga(self):
        print("=================================")
        print("\tHARGA\n 1x24 jam: Rp.350.000")