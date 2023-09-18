sayi1 = int(input('1. Sayıyı Giriniz: '))
sayi2 = int(input('2. Sayıyı Giriniz: '))
islem = input('Toplama için (+) Çıkarma için (-) Çarpım (*) Bölme(/) girin: ')

if islem == '+':
    sonuç = sayi1 + sayi2
    print('Toplam:', sonuç)
elif islem == '-':
    sonuç = sayi1 - sayi2
    print('Fark:'- sonuç)
elif islem == '*':
    sonuç = sayi1 * sayi2
    print('Çarpımı:',sonuç)
elif islem == '/':
    sonuç = sayi1 / sayi2
    print('Bölümü:', sonuç)
else:
    print('HATALI GİRİŞ! TEKRAR DENE.')