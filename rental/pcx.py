from motor import Motor

class Pcx(Motor):
    def __init__(self):
        super().__init__("Matic", "HONDA PCX 150cc")
        
    def info(self):
        nopol = "K 6666 ST"
        print("Nomor Polisi: ", nopol)
        print("Tipe motor: %s \nMerek: %s" %(self.tipemotor, self.merek))
    def tampilharga(self):
        print("=================================")
        print("\tHARGA\n 1x24 jam: Rp.75.000")
