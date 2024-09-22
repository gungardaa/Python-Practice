import os
import datetime as dt

data = ["nama", "nim", "sks", "beasiswa", "tanggal lahir"]
mahasiswa = {}
i = 1

print(60*"=")
print(f"||{"DATABASE MAHASISWA":^56}||")
print(60*"=" + "\n")
while True:
    input_mahasiswa = {}
    key = f"MAH0{i}"

    print("\nSilakan masukkan data mahasiswa")
    while True:
        valid_value = True
        nama = input(f"{"Nama":<20}: ")
        if nama.strip() == "":
            os.system("cls")
            print("Nama tidak valid. Mohon masukkan kembali\n")
        else:
            for char in nama:
                if char.isalpha() or char in " .,":
                    continue
                else:
                    os.system("cls")
                    print("Nama tidak valid. Mohon masukkan kembali\n")
                    valid_value = False
            if valid_value:
                break
        
    while True:
        nim = input(f"{"NIM":<20}: ")
        if nim.isdecimal():
            break
        else:
            os.system("cls")
            print("NIM tidak valid. Mohon masukkan kembali\n")
        
    while True:
        sks = input(f"{"Jumlah SKS":<20}: ")
        if sks.isdecimal():
            if len(sks) > 3:
                os.system("cls")
                print("SKS tidak valid. Mohon masukkan kembali\n")
            else:
                break
        else:
            os.system("cls")
            print("SKS tidak valid. Mohon masukkan kembali\n")

    while True:
        beasiswa = input(f"{"Beasiswa (y/t)":<20}: ")
        if beasiswa == "y":
            beasiswa = "Ya"
            break
        elif beasiswa == "t":
            beasiswa = "Tidak"
            break
        else:
            os.system("cls")
            print("Beasiswa tidak valid. Mohon masukkan kembali\n")

    while True:
        tahun = input(f"{"Tahun lahir":<20}: ")
        if tahun.isdecimal():
            if int(tahun) > 2024:
                os.system("cls")
                print("Tahun lahir tidak valid. Mohon masukkan kembali\n")
            else:
                break
        else:
            os.system("cls")
            print("Tahun lahir tidak valid. Mohon masukkan kembali\n")

    while True:
        bulan = input(f"{"Bulan lahir (1-12)":<20}: ")
        if bulan.isdecimal():
            if int(bulan) > 12:
                os.system("cls")
                print("Bulan lahir tidak valid. Mohon masukkan kembali\n")
            else:
                bulan = f"{int(bulan):g}"
                break
        else:
            os.system("cls")
            print("Bulan lahir tidak valid. Mohon masukkan kembali\n")
    
    while True:
        tanggal = input(f"{"Tanggal lahir":<20}: ")
        if tanggal.isdecimal():
            if int(tanggal) > 31:
                os.system("cls")
                print("Tanggal lahir tidak valid. Mohon masukkan kembali\n")
            else:
                tanggal = f"{int(tanggal):g}"
                break
        else:
            os.system("cls")
            print("Tanggal lahir tidak valid. Mohon masukkan kembali\n")

    input_mahasiswa.update({"nama": nama, "nim": nim, "sks": sks, "beasiswa": beasiswa, "tanggal lahir": dt.date(int(tahun), int(bulan), int(tanggal)).strftime("%d/%m/%Y")})
    mahasiswa.update({key: input_mahasiswa})

    max_data = []
    for identitas in data:
        check = max(len(mahasiswa[f"MAH0{a}"][identitas]) for a in range(1, i+1))
        max_data.append(check)
    
    default = []
    for a in range(5):
        check = max(max_data[a], len(data[a]))
        default.append(check)

    print("-"*(31+(default[0] + default[1] + default[2] + default[3] + default[4])))
    print(f"|{"No.":^5}| {"Key":^6} | {"Nama":^{default[0]}} | {"NIM":^{default[1]}} | {"SKS":^{default[2]}} | {"Beasiswa":^{default[3]}} | {"Tanggal Lahir":^{default[4]}} |")
    print("-"*(31+(default[0] + default[1] + default[2] + default[3] + default[4])))

    for kunci, nilai in mahasiswa.items():
        if len(kunci) == 6:
            print(f"|{(kunci[-1]+kunci[-2]):^5}| {kunci:^6} | {nilai["nama"]:<{default[0]}} | {nilai["nim"]:^{default[1]}} | {nilai["sks"]:^{default[2]}} | {nilai["beasiswa"]:^{default[3]}} | {nilai["tanggal lahir"]:^{default[4]}} |")
        else:
            print(f"|{kunci[-1]:^5}| {kunci:^6} | {nilai["nama"]:<{default[0]}} | {nilai["nim"]:^{default[1]}} | {nilai["sks"]:^{default[2]}} | {nilai["beasiswa"]:^{default[3]}} | {nilai["tanggal lahir"]:^{default[4]}} |")

    print("-"*(31+(default[0] + default[1] + default[2] + default[3] + default[4])))
    
    while True:
        confirm = input(f"\nLanjutkan? (y/n) : ")
        if confirm == "y":
            i += 1
            break
        elif confirm == "n":
            print("\nProgram telah berakhir")
            exit()
        else:
            os.system("cls")
            print("Tidak valid. Mohon masukkan y/n\n")


