# Soal case 3
soal = 5

# Rencana fungsi
def cetak_gambar(angka):
    for i in range(angka,0,-1):
        print(' '*(i-1) + ' *'*(angka))


# Membuat fungsi
cetak_gambar(soal)