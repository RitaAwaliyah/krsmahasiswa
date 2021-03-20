#input nim
teks = input("Masukkan NIM : ")
nim = teks[5:7] 
    
if (nim == '20'):
    sks = 20
    print("Anda mahasiswa tahun pertama. Anda bisa mengambil paling banyak", 20 ,"SKS.\n") 
elif (nim == '19'):
    sks = 22 
    print("Anda mahasiswa tahun kedua. Anda bisa mengambil paling banyak", 22 ,"SKS.\n")
elif (nim == '18'):
    sks = 24 
    print("Anda mahasiswa tahun ketiga. Anda bisa mengambil paling banyak", 24 ,"SKS.\n")
elif (nim == '17'):
    sks = 26 
    print("Anda mahasiswa tahun keempat. Anda bisa mengambil paling banyak", 26 ,"SKS.\n")
else:
    print("NIM tidak ada") 


jm_sks = 0 
while True:  
    print("Jumlah SKS yang diambil: ", jm_sks)
    matkul = input("Masukkan nama mata kuliah yang diambil atau x untuk selesai : ") 
    if (matkul == "x" ): 
        print("Pengisian Rencana Studi selesai.\n") 
        break 
    max_sks = int(input("Masukkan beban SKS mata kuliah tersebut: ")) 
    jm_sks = jm_sks + max_sks 
    if (jm_sks == sks):  
        print("Pengisian Rencana Studi selesai.\n")
        break 
    elif (jm_sks > sks): 
        print("Jumlah SKS melebihi SKS maksimal.")
        print("Pengisian Rencana Studi selesai.\n")
        break 
    print("Berhasil mengambil mata kuliah", matkul, "dengan bobot", max_sks, "SKS")