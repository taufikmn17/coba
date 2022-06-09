from motor import Motor

class Vario(Motor):
    def __init__(self):
        super().__init__("Matic", "HONDA Vario 160cc")
        
    def info(self):
        nopol = "K 1111 RC"
        print("Nomor Polisi: ", nopol)
        print("Tipe motor: %s \nMerek: %s" %(self.tipemotor, self.merek))

    def tampilharga(self):
        print("=================================")
        print("\tHARGA\n 1x24 jam: Rp.60.000")
        
