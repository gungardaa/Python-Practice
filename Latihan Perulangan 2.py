# Versi Sempurna (alas tidak harus ganjil, bisa nentuin karakter bebas)

while True:
    char = str(input("Masukkan character: "))
    alas = input("Masukkan alas segitiga: ")
    try:
        alas = int(alas)
        break
    except ValueError:
        print("Mohon masukkan angka")

print("")
print("Segitiga rata kiri")
for i in range(1, alas+1):
    print(i*char)
    
print("\nSegitiga rata kiri terbalik")
for i in range(alas, 0, -1):
    print(i*char)

print("\nSegitiga rata kanan")
for i in range(1, alas+1):
    print(" "*((alas-i)*len(char)) + i*char)
    
print("\nSegitiga rata kanan terbalik")
for i in range(alas, 0, -1):
    print(" "*((alas-i)*len(char)) + i*char)

# di bawah ini untuk len(char) ganjil dan alas ganjil
# len(char) ganjil dengan alas genap tidak bisa dibuat
if len(char) % 2 == 1:
    if alas % 2 == 0:
        print("\nSegitiga rata tengah tidak dapat dikonstruksi\n")
    else:
        print("\nSegitiga rata tengah")
        for i in range(1, alas+1, 2):
            spasi = (int(((alas-i)*len(char))/2))
            print(" "*spasi + i*char)
        
        print("\nSegitiga rata tengah terbalik")
        for i in range(alas, 0, -2):
            spasi = (int(((alas-i)*len(char))/2))
            print(" "*spasi + i*char)

# di bawah ini jika len(char) genap
# baik alas ganjil maupun genap bisa dibuat
else:
    print("\nSegitiga rata tengah")
    for i in range(1, alas+1):
        spasi = (int(((alas-i)*len(char))/2))
        print(" "*spasi + i*char)

    print("\nSegitiga tengah terbalik")
    for i in range(alas, 0, -1):
        spasi = (int(((alas-i)*len(char))/2))
        print(" "*spasi + i*char)   