print("Nama : Nurul Salsabillah")
print("NIM : 231031087")
print("Prodi : Sistem Informasi")
print("Tanggal Lahir : 20-05-2005")

# Operasi aritmatika
a=87
print ("Nilai a =",a )
a=87
a+=1
print ("Nilai a+=1 akan menjadi", a)
a=87
a-=1
print ("Nilai a-=1 akan menjadi", a)
print ("Nilai a-=1 akan menjadi", a)
a=87
a*=2
print ("Nilai a*=2 akan menjadi", a)
a=87
a/=2
print ("Nilai a/=2 akan menjadi", a)
a=87
a%=2
print ("Nilai a%=2 akan menjadi", a)
a=87
a//=2
print ("Nilai a//=2 akan menjadi", a)
a=87
a**=2
print ("Nilai a**=2 akan menjadi", a)

#OR
b = True
print ("Nilai b=", b)
b|= False
print ("Nilai b|=False akan menjadi", b)
b= False
print ("Nilai b=", b)
b|= False
print ("nilai b|= False akan menjadi", b )

# AND
b= True
print ("Nilai b =", b )
b&= False
print ("Nilai b&= False akan menjadi", b )
b= False
print ("Nilai b =", b )
b&= False
print ("Nilai b&= False akan menjadi", b )

# XOR
b= True
print ("Nilai b =", b )
b^= False
print ("Nilai b^= False akan menjadi", b )
b= False
print ("Nilai b =", b )
b^= False
print ("Nilai b^= False akan menjadi", b )

#Shifting
c =0b0100
print ("Nilai c =",format (c , "04b") )
c >>=1
print ("Nilai c > >=1 akan menjadi ",format (c , "04b") )
c =0b0100
c <<=1
print ("Nilai c < <=1 akan menjadi ",format (c , "04b") )
print()
print()
a =7 # isi dengan ujung NIM
b =12 # Ubah dengan hasil jumlah ujung NIM dengan 5
print ("================== Besar dari 12")
hasil = a > 12
print (a ,"> 12 adalah ", hasil )
hasil = b >12
print (b ,"> 12 adalah ", hasil )

print ("================== Kecil dari 12")
hasil = a <12
print (a ,"< 12 adalah ", hasil )
hasil = b <12
print (b ,"< 12 adalah ", hasil )

print ("================== Besar atau sama dari 12")
hasil = a >=12
print (a ," >= 12 adalah ", hasil )
hasil = b >=12
print (b ," >= 12 adalah ", hasil )

print ("================== Besar atau sama dari 12")
hasil = a <=12
print (a ," <= 12 adalah ", hasil )
hasil = b <=12
print (b ," <= 12 adalah ", hasil )

print ("================== Sama dengan 12 ")
hasil = a ==12
print (a ,"== 12 adalah ", hasil )
hasil = b ==12
print (b ,"== 12 adalah ", hasil )

print ("================== Tidak sama dengan 12")
hasil = a !=12
print (a ,"!= 12 adalah ", hasil )
hasil = b !=12
print (b ,"!= 12 adalah ", hasil )
print()
print()
print ("============= NOT ============= ")
a = True
c = not a
print ("a adalah ",a )
print ("------c = not a- - - -- - - NOT ")
print ("c adalah ",c )

print ("============= OR =============")
a = True
b = True
c = a or b
print (a ,"OR",b ,"menjadi",c )

a = True
b = False
c = a or b
print (a ,"OR",b ,"menjadi",c )

a = False
b = True
c = a or b
print (a ,"OR",b ,"menjadi",c )

a = False
b = False
c = a or b
print (a ,"OR",b ,"menjadi",c )

print ("============= AND =============")
a = True
b = True
c = a and b
print (a ,"AND",b ,"menjadi",c )

a = True
b = False
c = a and b
print (a ,"AND",b ,"menjadi",c )

a = False
b = True
c = a and b
print (a ,"AND",b ,"menjadi",c )

a = False
b = False
c = a and b
print (a ,"AND",b ,"menjadi",c )

print ("============= XOR =============")
a = True
b = True
c = a ^ b
print (a ,"^",b ,"menjadi",c )

a = True
b = False
c = a ^ b
print (a ,"^",b ,"menjadi",c )

a = False
b = True
c = a ^ b
print (a ,"^",b ,"menjadi",c )

a = False
b = False
c = a ^ b
print (a ,"^",b ,"menjadi",c )
# TUGAS
# Buat kode untuk masing masing operator berikut
print (' ============= NAND ============= ')
print (' ============= NOR ============== ')
print (' ============= NXOR ============= ')
print()
print()
print ("============== IS")
a =5
b =5
print("Nilai a =",a ,"Identitas =",hex (id( a ) ) )
print("Nilai b =",b ,"Identitas =",hex (id( b ) ) )
hasil = a is b
print("a is b = ", hasil )

a =5
b =6

print("Nilai a =",a ,"Identitas =",hex (id( a ) ) )
print("Nilai b ",b ,"Identitas =",hex (id( b ) ) )
hasil = a is b
print("a is b =", hasil)

print("============== IS NOT")
a =5
b =5
print("Nilai a =",a ,"Identitas =",hex (id( a ) ) )
print("Nilai b =",b ,"Identitas =",hex (id( b ) ) )
hasil = a is not b
print("a is not b = ", hasil )

a =5
b =6
print("Nilai a =",a ,"Identitas =",hex (id( a ) ) )
print("Nilai b =",b ,"Identitas =",hex (id( b ) ) )
hasil = a is not b
print("a is not b =", hasil )
print()
print()
print ("======================= IN")
nama_lengkap = "Bacharuddin Jusuf Habibie"
test = "a"
cek = test in nama_lengkap
print ( test +" terdapat di "+ nama_lengkap +" adalah "+ str( cek ) )

test = "rud"
cek = test in nama_lengkap
print ( test +" terdapat di "+ nama_lengkap +" adalah "+ str( cek ) )

test = "bac"
cek = test in nama_lengkap
print ( test +" terdapat di "+ nama_lengkap +" adalah "+ str( cek ) )

print ("======================= NOT IN")
nama_lengkap = "Bacharuddin Jusuf Habibie"
test = "a"
cek = test not in nama_lengkap
print ( test +" tidak terdapat di "+ nama_lengkap +" adalah "+str ( cek ) )

test = "rud"
cek = test not in nama_lengkap
print ( test +" tidak terdapat di "+ nama_lengkap +" adalah "+str ( cek ) )

test = "bac"
cek = test not in nama_lengkap
print ( test +" tidak terdapat di "+ nama_lengkap +" adalah "+str ( cek ) )

print()
print()
# Penggunaan pengecekan pada suatu data
data = ["Institut ",
        "Teknologi ",
        "Bacharuddin ",
        "Jusuf ",
        "Habibie "]
print ("data = ", data )
print ("======================= IN")
test1 = "Habibie "
test2 = "Parepare "
cek = test1 in data
print ("Apakah "+ test1 +" Terdapat di dalam data ? "+str ( cek ) )
cek = test2 in data
print ("Apakah "+ test2 +" Terdapat di dalam data ? "+str ( cek ) )


print ("======================= NOT IN ")
test1 = "institut "
test2 = "Institut "
cek = test1 not in data
print ("Apakah "+ test1 +" Tidak terdapat di dalam data ? "+ str( cek ) )
cek = test2 not in data
print ("Apakah "+ test2 +" Tidak terdapat di dalam data ? "+ str ( cek ) )
print()
print()
a =20 # ubah menjadi tanggal lahir anda
a +=60
b =5 # ubah menjadi bulan lahir anda
b += 90
print (" ============================= OR ")
print ("Nilai ",a ,"dalam biner = ", format (a ,"08b") )
print ("Nilai ",b ,"dalam biner = ", format (b ,"08b") )
print (" - - - - - - - - - - - - - - - - - - - - - - - - - - - -(|)")
hasil = a | b
print ("Nilai ",a ,"|",b ,"dalam biner = ", format ( hasil ,"08b") )

print (" ============================= AND ")
print ("Nilai ",a ,"dalam biner = ", format (a ,"08b") )
print ("Nilai ",b ,"dalam biner = ", format (b ,"08b") )
print (" - - - - - - - - - - - - - - - - - - - - - - - - - - - -(&)")
hasil = a & b
print ("Nilai ",a ,"&",b ,"dalam biner = ", format ( hasil ,"08b") )

print (" ============================= XOR ")
print ("Nilai ",a ,"dalam biner = ", format (a ,"08b") )
print ("Nilai ",b ,"dalam biner = ", format (b ,"08b") )
print (" - - - - - - - - - - - - - - - - - - - - - - - - - - - -(^)")
hasil = a ^ b
print ("Nilai ",a ,"^",b ,"dalam biner = ", format ( hasil ,"08b") )

print (" ============================= NOT ")
print ("Nilai ",a ,"dalam biner = ", format (a ,"08b") )
print (" - - - - - - - - - - - - - - - - - - - - - - - -(~a)")
hasil = ~a
print ("Nilai ~",a ,"dalam biner = ", format ( hasil ,"08b") )
       
print ("Nilai ",b ,"dalam biner = ", format (b ,"08b") )
print (" - - - - - - - - - - - - - - - - - - - - - - - -(~b)")
hasil = ~b
print ("Nilai ~",b ,"dalam biner = ", format ( hasil ,"08b") )

print ("============================= > > ")
print ("Nilai ",a ,"dalam biner = ", format (a ,"08b") )
print (" - - - - - - - - - - - - - - - - - - - - - - - - - -( > >2)")
hasil = a >> 2
print ("Nilai ",a ," > >2 dalam biner = ", format ( hasil ,"08b") )

print ("Nilai ",b ,"dalam biner = ", format (b ,"08b") )
print (" - - - - - - - - - - - - - - - - - - - - - - - - - -( > >2)")
hasil = b >> 2
print ("Nilai ",b ," > >2 dalam biner = ", format ( hasil ,"08b") )
       
print ("============================= < < ")
print ("Nilai ",a ,"dalam biner = ", format (a ,"08b") )
print (" - - - - - - - - - - - - - - - - - - - - - - - - - -( < <2)")
hasil = a << 2
print ("Nilai ",a ," < <2 dalam biner = ", format ( hasil ,"08b") )
       
print ("Nilai ",b ,"dalam biner = ", format (b ,"08b") )
print (" - - - - - - - - - - - - - - - - - - - - - - - - - -( < <2)")
hasil = b << 2
print ("Nilai ",b ," < <2 dalam biner = ", format ( hasil ,"08b") )
print()
# TUGAS
print("=============================NOT AND")
print("=============================NOT OR")
print("=============================NOT XOR")
print("=============================NOT (>>2)")
print("=============================NOT (<<2)")

#jawaban
print()
a=20  
a +=60
b=5 
b+= 90

print("=============================NOT AND")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~&)")
hasil=~(a&b)
print("Nilai",a,"~&",b,"dalam biner =", format(hasil,"08b"))

print()
print("=============================NOT OR")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~|)")
hasil=~(a|b)
print("Nilai",a,"~|",b,"dalam biner =", format(hasil,"08b"))

print()
print("=============================NOT XOR")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~^)")
hasil=~(a^b)
print("Nilai",a,"~^",b,"dalam biner =", format(hasil,"08b"))

print()
print( "----------------------------NOT (>>2)")
hasil= ~(a >> 2)
print("Nilai",a,"~>>2 dalam biner =", format(hasil,"08b"))

print("Nilai",b,"dalam biner     =", format(b,"08b"))
print( "----------------------------NOT (>>2)")
hasil= ~(b >> 2)
print("Nilai",b,"~>>2 dalam biner =", format(hasil,"08b"))

print()
print( "----------------------------NOT (<<2)")
hasil= ~(a << 2)
print("Nilai",a,"~<<2 dalam biner =", format(hasil,"08b"))

print("Nilai",b,"dalam biner     =", format(b,"08b"))
print( "----------------------------NOT (<<2)")
hasil= ~(b << 2)
print("Nilai",b,"~<<2 dalam biner =", format(hasil,"08b"))



    
