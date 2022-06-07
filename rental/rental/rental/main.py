from mobil import Mobil
# from motor import Motor
from avanza import Avanza
from ayla import Ayla
from innova import Innova
from brio import Brio
from ayla import Ayla
from vario import Vario
from pcx import Pcx
from vega import Vega
from mxking import Mxking
from formavanza import Formavanza
from forminnova import Forminnova
from formayla import Formayla
from formbrio import Formbrio
from formvario import Formvario
from formpcx import Formpcx
from formmxking import Formmxking
from formvega import Formvega


def choiceavanza():
    choice = input(str("\nApakah ingin melanjutkan pemesanan? [Y/N]"))
    if choice == "Y":
        f = Formavanza()
        exit()
    elif choice == "N":
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        exit()


def choiceinnova():
    choice = input(str("\nApakah ingin melanjutkan pemesanan? [Y/N]"))
    if choice == "Y":
        f = Forminnova()
        exit()
    elif choice == "N":
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        exit()


def choiceayla():
    choice = input(str("\nApakah ingin melanjutkan pemesanan? [Y/N]"))
    if choice == "Y":
        f = Formayla()
        exit()
    elif choice == "N":
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        exit()


def choicebrio():
    choice = input(str("\nApakah ingin melanjutkan pemesanan? [Y/N]"))
    if choice == "Y":
        f = Formbrio()
        exit()
    elif choice == "N":
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        exit()


def choicevario():
    choice = input(str("\nApakah ingin melanjutkan pemesanan? [Y/N]"))
    if choice == "Y":
        f = Formvario()
        exit()
    elif choice == "N":
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        exit()


def choicepcx():
    choice = input(str("\nApakah ingin melanjutkan pemesanan? [Y/N]"))
    if choice == "Y":
        f = Formpcx()
        exit()
    elif choice == "N":
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        exit()


def choicemxking():
    choice = input(str("\nApakah ingin melanjutkan pemesanan? [Y/N]"))
    if choice == "Y":
        f = Formmxking()
        exit()
    elif choice == "N":
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        exit()


def choicevega():
    choice = input(str("\nApakah ingin melanjutkan pemesanan? [Y/N]"))
    if choice == "Y":
        f = Formvega()
        exit()
    elif choice == "N":
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        exit()


def mobilmanual():
    print("\nSilahkan pilih mobil manual yang tersedia \n 1.Avanza \n 2.Innova")


def mobilmatic():
    print("\nSilahkan pilih mobil matic yang tersedia \n 1.Ayla \n 2.Brio")


def motormanual():
    print("\nSilahkan pilih motor manual yang tersedia \n 1.MXKing \n 2.Vega")


def motormatic():
    print("\nSilahkan pilih motor matic yang tersedia \n 1.PCX \n 2.Vario")


def formpesan():
    print("Silahkan isi form pemesanan")


def show_menu():
    mobb = Mobil("", "")
    print("====================================")
    print("=======RENTAL MOBIL DAN MOTOR=======")
    print("============== Menu ================")
    mobb.pilihtipe()
    print("[1] Mobi Manual")
    print("[2] Mobil Matic")
    print("[3] Motor Matic")
    print("[4] Motor Manual")
    print("[0] Exit \n")
    print("====================================")
    pilih_menu = input("Pilih menu> ")
    if(pilih_menu == "1"):
        mobilmanual()
        mobil = input("Pilih menu> ")
        if(mobil == "1"):
            a = Avanza()
            a.info()
            a.tampilharga()
            choiceavanza()
        elif(mobil == "2"):
            i = Innova()
            i.info()
            i.tampilharga()
            choiceinnova()
        else:
            print("Error")
            exit()
    elif(pilih_menu == "2"):
        mobilmatic()
        motic = input("Pilih menu> ")
        if(motic == "1"):
            ay = Ayla()
            ay.info()
            ay.tampilharga()
            choiceayla()
        elif(pilih_menu == "2"):
            br = Brio()
            br.info()
            br.tampilharga()
            choicebrio()
        else:
            print("Error")
            exit()
    elif(pilih_menu == "3"):
        motormanual()
        motor = input("Pilih menu> ")
        if(motor == "1"):
            mx = Mxking()
            mx.info()
            mx.tampilharga()
            choicemxking()
        elif(motor == "2"):
            v = Vega()
            v.info()
            v.tampilharga()
            choicevega()
        else:
            print("Error")
            exit()
    elif(pilih_menu == "4"):
        motormatic()
        mototic = input("Pilih menu> ")
        if(mototic == "1"):
            p = Pcx()
            p.info()
            p.tampilharga()
            choicepcx()
        elif(mototic == "2"):
            var = Vario()
            var.info()
            var.tampilharga()
            choicevario()
        else:
            print("Error")
            exit()
    elif(pilih_menu == "0"):
        print("Terimakasih!")
        exit()
    else:
        print("error")


if __name__ == "__main__":
    while True:
        show_menu()
