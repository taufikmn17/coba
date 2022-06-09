from motor import Motor

class Vega(Motor):
    def __init__(self):
        super().__init__("Manual", "YAMAHA Vega ZR 115cc")
        
    def info(self):
        nopol = "K 7676 KK"
        print("Nomor Polisi: ", nopol)
        print("Tipe motor: %s \nMerek: %s" %(self.tipemotor, self.merek))
        
    def tampilharga(self):
        print("=================================")
        print("\tHARGA\n 1x24 jam: Rp.50.000")
        
