jawaban = 3
tebakan = 0

while tebakan != jawaban:
    tebakan = int(input("Tebak angka (1-10): "))
    if tebakan < jawaban:
        print("Terlalu kecil!")
    elif tebakan > jawaban:
        print("Terlalu besar!")
    else:
        print("Tebakan benar!")
