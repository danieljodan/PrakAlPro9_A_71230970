# Program Menampilkan 3 Nilai Terbaik
def tigaNilaiTerbaik (listNilai):
    if len(listNilai) < 3:
        print("Masukkan list dengan minimal 3 nilai")
    else:
        listNilai.sort()
        for i in range(-1,-4,-1):
            print(listNilai[i])

tigaNilaiTerbaik([13,4,5,2,1,8,9])

