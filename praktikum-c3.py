print("PRAKTIKUM 3")

nama  = "nurul salsabillah"
nim   = "231031087"
meet  = "Praktikum 3"
prodi = "Sistem Informasi C"
email = "nurulsalsabillah05@gmail.com"
ttl   = "Parepare,20 Mei 2005"
alamat= "Jl. Sumur Jodoh"
asal  = "Parepare"
hobi  = "Menyanyi"
tinggi= "152 cm"

print("-"*90)
str1 = "nurul salsabillah"
a = str1.center(90)
print(a)

str1 = "231031087"
a = str1.center(90)
print(a)
print()
print()
str1 = "praktikum 3(string)"
a = str1.rjust(90)
print(a)

str1 = "sistem informasi c"
a = str1.rjust(90)
print (a)

str1 = "nurulsalsabillah05@gmail.com"
a = str1.rjust(90)
print(a)
print("-"*90)

data_saya = "   Halo, nama saya {} dengan nim {} dari prodi {}, ini adalah file {}.Terima kasih"
nama = "nurul salsabillah"
nim  = 231031087
prodi= "Sistem Informasi C"
meet = "praktikum 3"
a = data_saya.format(nama,nim,prodi,meet)
print(a)

print()

print(f"""Biodata saya,
Nama\t: {nama.upper()}
NIM\t: {nim}
Prodi\t: {prodi}
TTL\t: {ttl}
Alamat\t: {alamat}
Asal\t: {asal}
Hobi\t: {hobi}
Tinggi\t: {tinggi}""")

print()
print()
#TUGAS
stat1 = 'duFort Frankel Sir Issac'
# Issac duFort Frankel Sir
print(stat1[19:],stat1[0:19])

stat2 = 'duFort Frankel Sir Issac'
# d F S Issac
print(stat2[0],stat2[7],stat2[15],stat2[19:])

stat3 = 'duFort Frankel Sir Issac'
# duFort F S I
print(stat3[0:7],stat3[7],stat3[15],stat3[19])

stat4 = 'duFort Frankel Sir Issac'
# I duFort Frankel Sir
print(stat4[19],stat4[0:18])

stat5 = 'duFort Frankel Sir Issac'
# Issac d F S
print(stat5[19:],stat5[0],stat5[7],stat5[15])

stat6 = 'duFort Frankel Sir Issac'.upper()
# ISSAC D F S
print(stat6[19:],stat6[0],stat6[7],stat6[15])

stat7 = '#duFort Frankel Sir Issac$'
# duFort Frankel Sir Issac
stat7 = stat7.strip("#$")
print(stat7)

stat8 = '#duFort-Frankel-Sir-Issac$'
# duFort Frankel Sir Issac
stat8 = stat8.strip("#$").replace("-"," ")
print(stat8)

stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
# duFort Frankel Sir Issac
import re
stat9 = re.findall(r'\w+', stat9)
hasil = ' '.join(stat9)
print(hasil)

stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
# DUFORT FRANKEL SIR ISSAC
import re
stat10 = re.findall(r'\w+', stat10)
hasil = ' '.join(stat10.upper() for stat10 in stat10)
print(hasil)
