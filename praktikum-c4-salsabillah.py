nim = ['2','3','1','0','3','1','0','8','7']

print(nim)

print('item indeks 0 (pertama)',nim[0])
print('item indeks 1 (kedua)',nim[1])
print(f'item indeks 0 (pertama) {nim[0]}')
print(f'item indeks 1 (kedua)   {nim[1]}')
print(f'item indeks terakhir {nim[len(nim)-1]}')
print(f'item indeks terakhir {nim[-1]}')
print(f'item indeks (pertama) {nim[-len(nim)]}')
print()

#LATIHAN LIST
data = ['Nurul Salsabillah',2023,'Aktif']
nilai= [90,89,93,97]

print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])
print()
print(f'{data[0]} status kuliah: {data[2]}')
print(f'Data terbesar nilai adalah: {max(nilai)}')
print(f'Data terkecil nilai adalah: {min(nilai)}')
print(f'Rata-rata nilai adalah: {sum(nilai)/len(nilai)}')
print()

#LATIHAN TUPLE
data = ['Mahasiswa',2023,'Aktif']
nilai= [90,89,93,97]

print(data[1])
print(data[-1])
print(nilai[1:-1])
print()
print(f'Jumlah mahasiswa adalah: {len(nilai)}')
print(f'Data terbesar nilai adalah: {max(nilai)}')
print(f'Data terkecil nilai adalah: {min(nilai)}')
print(f'Rata-rata nilai adalah: {sum(nilai)/len(nilai)}')
print()

#LATIHAN NESTED LIST
data = [['Nurul Salsabillah','N S',2023,'Aktif'],
        [90,89,93,97],
        [20,22],
        ['S1-Reguler','Ganjil','Sistem Informasi C']]

print(data[0][0])
print(data[-1][0])
print(data[2][0:])
print()
print(f'Program pendidikan: {data[0][0]} {data[-1][0]}')
print(f'Angkatan: {data[0][1]} {data[-1][1]}')
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}')
print(f'Data terbesar {data[0][0]} adalah: {max(data[1])}')
print(f'Data terkecil {data[0][0]} adalah: {min(data[1])}')
print(f'Rata-rata nilai {data[0][0]} adalah: {sum(nilai)/len(nilai)}')
print()

#TUGAS
matkul = ['Matkul1',
          'matkul2',
          'matkul3',
          'matkul4',
          'matkul5']
sks = [2,3,2,3,3]
data.append(matkul)
data.append(sks)
print(data)
print()

# Tambahkan matkul dan sks ke dalam data (pakai append)
# DAFTAR MATA KULIAH
#Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f'Mata kuliah 1: {data[4][0]} dengan jumlah {data[5][0]} sks')

#Mata kuliah 2: Matkul2 dengan jumlah 3 sks
print(f'Mata kuliah 2: {data[4][1]} dengan jumlah {data[5][1]} sks')

#Mata kuliah 3: Matkul3 dengan jumlah 2 sks
print(f'Mata kuliah 3: {data[4][2]} dengan jumlah {data[5][0]} sks')

#Mata kuliah 4: Matkul4 dengan jumlah 3 sks
print(f'Mata kuliah 4: {data[4][3]} dengan jumlah {data[5][1]} sks')

#Mata kuliah 5: Matkul5 dengan jumlah 3 sks
print(f'Mata kuliah 5: {data[4][4]} dengan jumlah {data[5][1]} sks')
print()

data[4].append('matkul6')
data[5].append(2)
print(data)
print()
data[4].append('matkul7')
data[5].append(2)
print(data)
print()
data[4].append('matkul8')
data[5].append(3)
print(data)
print()

#Mata kuliah 6: Matkul6 dengan jumlah .. sks
print(f'Mata kuliah 6: {data[4][5]} dengan jumlah {data[5][5]} sks ')

#Mata kuliah 7: Matkul7 dengan jumlah .. sks
print(f'Mata kuliah 7: {data[4][6]} dengan jumlah {data[5][6]} sks ')

#Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f'Mata kuliah 8: {data[4][7]} dengan jumlah {data[5][7]} sks ')
print()

# Tambah Nilai jadi 8 (pakai append)
# Nama mahasiswa: Nurul Salsabillah
print(f'Nama Mahasiswa: {data[0][0]}')
# Inisial Nurul Salsabillah: N S
print(f'Inisial {data[0][0]}: {data[0][1]}')
# NIM Nurul Salsabiilah: 231031087
print(f'NIM {data[0][0]}: {"".join(nim)}')
# Program Nurul Salsabillah: S1-Reguler Sistem Informasi C
print(f'Program pendidikan {data[0][0]}: {data[3][0]} {data[3][2]}')
# Angkatan Nurul Salsabillah: Ganjil-2023
print(f'Angkatan {data[0][0]}: {data[3][1]}-{data[0][2]}')
# Total sks Nurul Salsabillah adalah: 20
print(f'Total sks {data[0][0]}: {data[2][0]}')
# Jumlah Nilai Nurul Salsabillah: 4
print(f'Jumlah nilai {data[0][0]}: {len(data[1])}')
# Nilai tertinggi Nurul Salsabillah: 97
print(f'Nilai tertinggi {data[0][0]}: {max(data[1])}')
# Nilai terendah Nurul Salsabillah: 89
print(f'Nilai terendah {data[0][0]}: {min(data[1])}')
# Rata-rata nilai Nurul Salsabillah: 92.25
print(f'Rata-rata nilai {data[0][0]}: {sum(nilai)/len(nilai)}')
