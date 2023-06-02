first_numbers = [9, 7, 10, 7, 10]
# dapatkan total nilai baris angka diatas
# dapatkan nilai yang paling maksimal dan minimal dari baris angka di atas
# berapa banyak angka yang bisa dibagi 2
# buat lah baris ganjil menjadi dikali 2 dan baris genap ditambah 4
# berapa banyak angka yang sama muncul di dalam baris angka tersebut
second_numbers = [2, 3]
# lakukan perkalian silang antara baris angka pertama dengan baris angka yang kedua
# sehingga menghasilkan
result = [
[18, 14, 20, 14, 20],
[27, 21, 30, 21, 30]
]
#kemudian dari hasil tersebut tambahkanlah masing - masing nilai berdasarkan posisi baris nya
result = [45, 35, 50, 35, 50]

#----------------------------------------------------------------
#Kode ADIWENO

print("---------------------------------")
print("# dapatkan total nilai baris angka diatas")
a = 0
for i in range(len(first_numbers)):
    a += first_numbers[i]
print(a)

print("\n# dapatkan nilai yang paling maksimal dan minimal dari baris angka di atas")
print("angka maks:", max(first_numbers))  
print("angka min:", min( first_numbers))

print("\n# berapa banyak angka yang bisa dibagi 2")
yangBisa = []
for i in first_numbers:
    if i % 2 == 0:
        yangBisa.append(i) 
banyak = len(yangBisa)
print("yang bisa dibagi 2:", yangBisa, "ada:", banyak)

print("\n# buat lah baris ganjil menjadi dikali 2 dan baris genap ditambah 4")
odd = []
even = []

for i in first_numbers:
    if i % 2 == 0:
        even.append(i+4) 
    else:
        odd.append(i*2) 
print("odd:", odd)
print("even:", even)

print("\n# berapa banyak angka yang sama muncul di dalam baris angka tersebut")
b = 0 
c = []
for i in first_numbers:
    if i in c:
        b += 1
    c.append(i)
print("jumlah angka yang terduplikat:", b)


print("\n---------------------------------")

print("# lakukan perkalian silang antara baris angka pertama dengan baris angka yang kedua\n# sehingga menghasilkan")
result = [[], []]

for firstTimes in first_numbers:
    firstTimes = firstTimes * second_numbers[0]
    result[0].append(firstTimes)
for secondTimes in first_numbers:
    secondTimes = secondTimes * second_numbers[1]
    result[1].append(secondTimes)

print(result)

print("\n#kemudian dari hasil tersebut tambahkanlah masing - masing nilai berdasarkan posisi baris nya")
add = 0
for thirdTimes in result[0]:
    result1 = result[0][add]
    result2 = result[1][add]
    allResult = result1 + result2
    result.append(allResult)
    add += 1
    
del result[0], result[0]

print(result)