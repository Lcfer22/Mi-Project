from random import randint

def Random(angkaMin, angkaMax):
    return randint(angkaMin, angkaMax)

g_angkaMin = 1
g_angkaMax = 10
g_batasInputMax = 3

angkaSaatIni = 0
angkaRandom = Random(g_angkaMin, g_angkaMax)
while (angkaSaatIni < g_batasInputMax):
    angkaInput = int(input("Masukkan Angka : "))
    if (angkaInput > g_angkaMax):
        print("Angka terlalu besar!")
    elif (angkaInput < g_angkaMin):
        print("Angka terlalu kecil!")
    else:
        angkaSaatIni += 1
        if (angkaInput == angkaRandom):
            print("Selamat anda berhasil menebak")
            break
        else:
            print("Coba lagi")

if (angkaSaatIni >= g_batasInputMax and angkaInput != angkaRandom):
    print("Game Over")
    print("Tebakan yang benar : ", angkaRandom)
