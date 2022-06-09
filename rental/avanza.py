from mobil import Mobil

class Avanza(Mobil):
    def __init__(self):
        super().__init__("Manual", "TOYOTA Avanza")
        
    def info(self):
        nopol = "B 1111 SS"
        print("Nomor Polisi: ", nopol)
        print("Tipe Mobil: %s \nMerek: %s" %(self.tipemobil, self.merek))

    def tampilharga(self):
        print("=================================")
        print("\tHARGA\n 1x24 jam: Rp.300.000")