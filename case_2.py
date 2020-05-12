# Soal kasus 2 
N = [19,22,3,28,26,17,18,4,28,0]

# Rencana fungsi
def fungsi_balik(array):
    jarak = len(array) - 1
    hasil = [] 
    for i in range(jarak,-1,-1):
        hasil.append(array[i])

    print(hasil)

# Memanggil fungsi
fungsi_balik(N)
