ulangi = True

while ulangi:
    bulan = int(input("Masukkan bulan (1-12): "))
    tahun = int(input("Masukkan tahun: "))

    if 1 <= bulan <= 12 and tahun > 0:
        if bulan == 2:
            if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
                jumlah_hari = 29
            else:
                jumlah_hari = 28
        elif bulan in [4, 6, 9, 11]:
            jumlah_hari = 30
        else:
            jumlah_hari = 31

        print(f"Jumlah hari pada bulan {bulan} tahun {tahun} adalah {jumlah_hari} hari.")
        ulangi = False  # Keluar dari perulangan
    else:
        print("Input tidak valid! Silakan coba lagi.\n")
