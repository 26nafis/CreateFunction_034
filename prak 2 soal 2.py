lambda jarijari : 3.14159 * jarijari

try :
    jari =float(input("isikan nilai jari - jari : "))
    result = luas (jari)
    print(f"luas dari lingkaran dengan jari-jari {jari} adalah {result}")
except ValueError :
    print ("nilai jari-jari harus angka")