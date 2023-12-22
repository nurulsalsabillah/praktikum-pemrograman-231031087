import os
os.system('clear')

pwd_benar = 'si23c'
a = True 
limit = 3
i = 0
while a:
    i <= 1
    pwd = input('Masukkan password:')
    if pwd == pwd_benar:
        print('Selamat anda berhasil login')
        a = False
    else:
        if i < limit:
            print('Password salah! coba lagi.')
            print(f'Kesempatan Anda tersisa {limit-1} kali')
            a = True
        else: 
            print('Kesempatan anda habis!')
            a = False
        
            