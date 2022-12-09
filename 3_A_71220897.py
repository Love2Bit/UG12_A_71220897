batas = int(input('Masukkan Pembatas : '))
ban = int(input('Masukan Angka yang dilarang : '))

for i in range(batas):
    if i == ban:
        continue
    print(i, " ", end='')