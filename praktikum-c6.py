import os
os.system('clear')

a = True

while a:
    pilih = input('Apakah ingin melanjutkan? [y/n]')
    if pilih == 'y':
        print('Terima Kasih!')
    elif pilih == 'n' :
        print('Sampai jumpa Lagi :)') 
    else:
        print('jangan aneh deh! :(')    
    