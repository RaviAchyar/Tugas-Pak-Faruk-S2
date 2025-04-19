def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = (tugas * 0.2) + (uts * 0.4) + (uas * 0.6)
    return nilai_akhir

nilai = hitung_nilai_akhir(26, 42, 87)
print(f"Nilai akhir mahasiswa: {nilai}")
