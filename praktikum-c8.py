import os
import random as rd
os.system('clear')

warna = ['merah','putih','hitam']
com = rd.choice(warna)
a = True

while a:
    pilih = input('Masukkan Pilihan [merah,putih,hitam]:\n')
    if pilih == com:
        print(f'Pilihan anda benar yaitu {pilih}')
        a = False
    else:
        print('Tebakan anda salah! coba lagi.')