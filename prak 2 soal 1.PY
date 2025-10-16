#input
try :
    suhu = float(input("inputkan besaran suhu :"))
except ValueError as e :
    print("error : ". e)
    exit ()
format_suhu = input("format suhu (c/f/k) :")
z = input("konversi suhu (c/f/k) :")
hasil = "" 

#proses#if(format_suhu == konversi_suhu) :
 #   hasil = f'{suhu} {format_suhu.upper()}'
# x adalah suhu
# y adalah format suhu
def konversisuhu(x, y, z) :
    global hasil
    #cek kondisi untuk celsius ke forenheat
    if y == 'c'and z == 'f' :
        f = (9,5) * x + 32
        hasil = f'{f}{z.upper()}'
    # cek kondisi suhu untuk celsius ke kelvin
    if y == 'c' and z == 'k' :
        k = x + 273.15
        hasil = f'{k}{z.upper()}'
    # cek kondisi forenheat ke celcius
    elif y == 'f' and z == 'c' :
        c = (x - 32) * (5/9)
        hasil = '{c} {z.upper()}'
    # cek kondisi forenheat ke kelvin
    elif y == 'f' and z == 'k' :
        k == (5/9) * x + 459.67
        hasil = f'{k} {z.upper()}'
    #cek kondisi untuk kelvin ke celcius
    elif y == 'k' and z == 'f' :
        f = (x - 273,15) * (9/5) + 72
        hasil = f'{f} {z.upper()}'
    else :
        hasil = "konversi nilai tidak valid"

if(format_suhu == z):
    hasil = f'{suhu} {format_suhu.upper()}'
else :
    konversisuhu(suhu, format_suhu, konversisuhu)
#output
print(hasil)