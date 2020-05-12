# List huruf kapital
kapital = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
    "S","T","U","V","W","X","Y","Z"
]

# Soal case 1
soal = "mamaMakanPepayaWaktuBuka"

# Membuat fungsi
def hitung_kata(string):
    # Dimulai dari angka 1 karena kata "mama" diawali huruf kecil
    hasil = 1
    for huruf in string:
        if huruf in kapital:
            hasil += 1
        else:
            hasil += 0
    print(hasil)

# Memanggil fungsi
hitung_kata(soal)