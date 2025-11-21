"""
Studi Kasus 1: Penilaian Kelulusan

    Input: Nilai ujian (0–100)
    Syarat:
        Lulus jika nilai ≥ 70
        Tidak lulus jika nilai < 70
    Output
"""

print(f"{5*"="}Studi Case 1{5*"="}") # border (optional)

theGrade = int(input("Nilai Ujianmu = ")) 

if theGrade >= 70: # lebih dari sama dengan 70, kalo kena angka 70 masih dianggap lulus
    print("Selamat kamu lulus, Tidak perlu remedial")
else:
    print("Tidak Lulus, hubungi dosen untuk pengulangan ujian!!")


