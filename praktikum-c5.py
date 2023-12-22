import os
os.system('clear')

a = True
Limit = 5
i = 0

while a:
    i += 1   
    print(f'Menjalankan Program {Limit + 1 - i}')
    if i == Limit:
        a = False
        print('Program berhenti di sini!')
    else:
        a = True     

