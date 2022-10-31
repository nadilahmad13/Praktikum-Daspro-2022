# Program HitungVokal
# Membaca masukan sejumlah karakter dan menyimpannya ke file data.txt
# Membaca isi file data.txt, menghitung dan menampilkan ada berapa
# banyak karakter huruf hidup dalam file
# KAMUS
mark = '.' # constant mark : character = '.'

def TulisTeks():
    # Membaca kalimat (kumpulan karakter) diakhiri mark dari keyboard
    # dan menyimpannya ke file data.txt
    # KAMUS LOKAL
    # f : SEQFILE of char
    # kalimat
    # ALGORITMA
    f = open("dataku.txt",'w')
    kalimat = input() # Baca sebuah kalimat dari keyboard

    # diakhiri mark '.'
    # Kalimat kosong hanya ada mark
    f.write(kalimat) # Menuliskan kalimat ke file
    f.close()

TulisTeks()
count = 0
f = open("dataku.txt", "r")
s = f.readline().lower()
for char in s:
    if char in ["a","i","u","e","o"]:
        count += 1
print(count)