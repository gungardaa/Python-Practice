# Versi lebih sempurna

import os

list_buku = []

while True:
    print("\nMasukkan data buku")
    while True:
        judul = input("Judul buku\t:  ")
        if judul.strip() == "":
            os.system("cls")
            print("Judul buku harus diisi")
        else:
            break
    
    while True:
        penulis = input("Penulis\t\t:  ")
        if penulis.strip() == "":
            os.system("cls")
            print("Penulis buku harus diisi")
        else:
            break
    
    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    max_judul = max(len(buku[0]) for buku in list_buku)
    max_penulis = max(len(buku[1]) for buku in list_buku)

    default_judul = max(max_judul, len("Judul Buku"))
    default_penulis = max(max_penulis, len("Penulis"))
    
    print(f"\n{"No".center(4)} | {"Judul Buku".center(default_judul)} | {"Penulis".center(default_penulis)}")
    print("-"*(default_judul + default_penulis + 11))

    for buku in list_buku:
        print(f"{str(list_buku.index(buku)+1).center(4)} | {buku[0]:<{default_judul}} | {buku[1]:<{default_penulis}}")
    print("-"*(default_judul + default_penulis + 11))

    while True:
        confirm = input("Lanjutkan? (y/n) ")
        if confirm == "y":
            break
        elif confirm == "n":
            print("\nProgram telah berakhir\n")
            exit()
        else:
            os.system("cls")
            print("Mohon masukkan y/n\n")