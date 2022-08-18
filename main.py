from ektraksi_fitur import color_moment
from svm import training, prediksi,evaluasi
from clear_scr import clear_screen

def menu():
    print("===================================")
    print("[1] Ektraksi Fitur")
    print("[2] Training dan Testing")
    print("[3] Prediksi")
    print("[4] Evaluasi")
    print("[0] Keluar")

menu()
option = int(input("Enter your option:"))

while option != 0:
    if option ==1:
        color_moment()
        print("ektraksi fitur selesai")
    elif option ==2:
        training()
        print("Training Selesai")
    elif option ==3:
        prediksi()
        print("Prediksi Selesai")
    elif option ==4:
        evaluasi()
        print("Evaluasi Selesai klasifikasi")
    else:
        print("invalid option")

    print("\n")
    input ("tekan enter")
    clear_screen()
    menu()
    option = int(input("enter your option:"))

    

    