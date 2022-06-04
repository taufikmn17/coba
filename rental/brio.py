from mobil import Mobil

class Brio(Mobil):
    def __init__(self):
        super().__init__("Matic", "HONDA BRIO RS")
        
    def info(self):
        nopol = "B 4321 GG"
        print("Nomor Polisi: ", nopol)
        print("Tipe Mobil: %s \nMerek: %s" %(self.tipemobil, self.merek))

    def tampilharga(self):
        print("=================================")
        print("\tHARGA\n 1x24 jam: Rp.250.000")
