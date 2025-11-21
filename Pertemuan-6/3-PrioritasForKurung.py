"""
SOAL DARI DOSEN!!
Penjelasan kamu sudah tepat dan rapi, terutama dengan menekankan bahwa tanda kurung memiliki prioritas tertinggi sebelum operator lain. Langkah perhitungan juga benar, hanya perlu diperhatikan bahwa pada Python, hasil pembagian dengan / adalah 2.0 (float), bukan 2 seperti pada matematika biasa. Sehingga output akhir sebenarnya adalah 28.0.

Pertanyaan Lanjutan:
Bagaimana jika ekspresi yang sama ditulis menggunakan tanda kurung seperti ini:

hasil = (10 + 5) * (2 ** 2) - (8 / 4)

"""


real_operation = (10 + 5) * (2 ** 2) - (8 / 4)

# Hasil menggunakan pembagian biasa
print("===Hasil sebelumnya===\n")
print(f"Hasil dari (10 + 5) * (2 ** 2) - (8 / 4) =  {real_operation}") 
print(f"Tipe data = {type(real_operation)}\n") # pengecekan tipe data

# Gunakan pembagian (//) untuk convert + membulatkan data type menjadi int 
operasi_revisi = (10 + 5) * (2 ** 2) - (8 // 4)

print("===Hasil setelahnya===\n")
print(f"tipe data = {type(operasi_revisi)}") 
print(f"Hasil = {operasi_revisi}")
