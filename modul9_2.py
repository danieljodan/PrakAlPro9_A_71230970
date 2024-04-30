def masukanUser():
    listSementara = []
    inputan = 0
    while inputan != "done":
        inputan = input("Masukkan Angka yang ingin dijumlahkan: ")
        if inputan != "done":
            angkaInputan = int(inputan)
            listSementara.append(angkaInputan)
            print("Ketik \"done\" bila ingin menyelesaikan perhitungan")
        
    print("List yang sudah Anda masukkan", listSementara)
    print("Nilai maksimum:", max(listSementara))
    print("Nilai minimum:", min(listSementara))

masukanUser()

