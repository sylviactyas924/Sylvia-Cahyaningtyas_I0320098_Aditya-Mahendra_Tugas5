# Input nama dan nilai pengguna
nama = input('Masukkan nama Anda:')
nilai = float(input('Masukkan nilai Anda:'))

# Output
if nilai >= 85:
    print('Hallo,', nama, '! Nilai Anda setelah dikonversi adalah A')
elif nilai >= 80:
    print('Hallo,', nama, '! Nilai Anda setelah dikonversi adalah A-')
elif nilai >= 75:
    print('Hallo,', nama, '! Nilai Anda setelah dikonversi adalah B+')
elif nilai >= 70:
    print('Hallo,', nama, '! Nilai Anda setelah dikonversi adalah B')
elif nilai >= 65:
    print('Hallo,', nama, '! Nilai Anda setelah dikonversi adalah C+')
elif nilai >= 60:
    print('Hallo,', nama, '! Nilai Anda setelah dikonversi adalah C')
else:
    pass
print()