## konversi satuan jarak 
## input dasar (km) kilometer

try: # code
    jarak_km = float(input("Jarak (km)\t= "))
    print("\n")
    convert_option = int(input("Konversi ke dalam:\n1.m (Meter)\n2.cm (centimeter) \n3.inch \nPilih Angka : "))

    print("\n")
    if convert_option == 1: # Km To Meter
        convert = jarak_km * 1000
        print(f"\n{jarak_km} km setara dengan = {float(convert):,} M")
    elif convert_option == 2:
        convert = jarak_km * 100000
        print(f"\n{jarak_km} km setara dengan = {float(convert):,} cm")
    elif convert_option == 3:
        default_inch_km = 39370.1
        convert = jarak_km * default_inch_km
        print(f"\n{jarak_km} km setara dengan = {float(convert):,} inch")
    else:
        print("\nTidak ada pilihan yang Tersedia!!")
        
    print("\nSelesai!!\n")

except KeyboardInterrupt: # ketika keluar dari console via CTRL + Z
    print("\nForce End")
except ValueError: # Menghindari orang salah ketik data input
    print("\nJangan salah masukin/melewati input ya!!")




