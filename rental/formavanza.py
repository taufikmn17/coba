class Formavanza:
    def __init__(self):
        print("Silahkan pilih lama sewa: \n 1. 1 hari \n 2. 2 hari \n 3. 3 hari \n 4. 4 hari \n 5. 5 hari")
        lamasewa = input("Masukkan pilihan: ")
        if(lamasewa == "1"):
            print("\n\tDETAIL DATA PEMESANAN")
            print("\t*Sewa paling lama: 5 hari\n")
            print("Total: Rp.300.000")
        elif(lamasewa == "2"):
            print("\n\tDETAIL DATA PEMESANAN")
            print("\t*Sewa paling lama: 5 hari\n")
            print("Total: Rp.600.000")
        elif(lamasewa == "3"):
            print("\n\tDETAIL DATA PEMESANAN")
            print("\t*Sewa paling lama: 5 hari\n")
            print("Total: Rp.900.000")
        elif(lamasewa == "4"):
            print("\n\tDETAIL DATA PEMESANAN")
            print("\t*Sewa paling lama: 5 hari\n")
            print("Total: Rp.1.200.000")
        elif(lamasewa == "5"):
            print("\n\tDETAIL DATA PEMESANAN")
            print("\t*Sewa paling lama: 5 hari\n")
            print("Total: Rp.1.500.000")
        else:
            print("Tidak ada pilihan hari!")
        self.nama = input("Masukkan nama: ")
        self.noktp = input("Masukkan No.KTP: ")
        self.alamat = input("Masukkan Alamat: ")
        print("==================================")
        print("Alamat anda: ", self.alamat)
        a = input("Ingin melanjutkan ke pembayaran? [Y/N]")
        if(a == "Y"):
            print("\nSilahkan pilih metode pembayaran: \n 1. Transfer \n 2. Cash")
            cot = input("Silahkan pilih menu> ")
            if(cot == "1"):
                print("Silahkan melakukan pembayaran ke rekening ini: 123")
            elif(cot == "2"):
                print("Silahkan datang langsung ke kasir!")
            else:
                print("Anda memasukkan pilihan yang salah")
        else:
            print("Anda membatalkan pesanan!")

