'''buatlah fungsi yang bisa melakukan check terhadap kata yang memiliki sifat
palindrome, yaitu kata yang apabila dibalik maka tetap menghasilkan kata yang sama
contoh: kodok -> kodok (true), katak -> katak (true), ab -> ba (false)'''


pal = input('Input a Palindrome word: ')
pal = pal.replace(' ','').lower()   #to remove space and change to lower case
if pal == pal[::-1]:
    print("reversed:", pal[::-1])
    print(True)
else:
    print("reversed:", pal[::-1])
    print(False)

