def kataUnik(file):
    listKata = []
    with open(file, 'r') as f:
        teksBerita = f.readlines()
    for line in teksBerita:
        kata = line.strip().split(" ")
        listKata.extend(kata)
    isiBerita = " ".join(listKata)
    print("========Isi Berita========")
    print(isiBerita)
    print()
    print("========Kata Unik Pada Berita========")
    print(listKata)
    f.close()
        

namaFile = "berita.txt"
kataUnik(namaFile)

