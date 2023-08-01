#############
###  lambda, map, filter, reduce fonksiyonları
# vektör seviyesinde işlem yapmasında kullanılan bazı araçlardır.
# lambda ve map önemlidir
# lambda applay fonksiyonu ile kullanılmakta ve önemlidir

# lambda : fonksiyondan farkı ise kullan at fonksiyonudur. fonksiyon tanımlama şeklidir.
""" Lambda’nın gücü, başka bir fonksiyonun içinde anonim bir fonksiyon olarak kullanıldığında daha iyi gösterilir.

Bir argüman alan bir fonksiyon tanımınız olduğunu ve bu argümanın bilinmeyen bir sayı ile çarpılacağını söyleyin. """

def fonks_exam(a,b):   # normalde bu şekilde fonk kullanarak işlem yapıyorduk
    return a+b
# Lambda ise kullan at fonksiyonudur
# -atama işlemi yapılmadan kullanılabilirdir
# lambda örnek:
new_fonk=lambda a,b:a+b    # lambda ile fonks tanımladık a,b argümanlarından oluşan : işlem
#fonk ismi=lambda a, b argümanlarından oluşan  : yapacağı işi yazınız
new_fonk(11,4)
fonks_exam(12,6)

##### map
# map ve applay fonkisyonu
 # seni döngü yazmaktan kurtaran bir fonksiyondur
#içinde gezilecek nesne ver ve işlemini verdikten sonra otomatik yapar

maaslar=[2400,3500,5500,6600,7500]

def yeni_maas(x):              # zam oluşturulabilen fonksiyon örneği
    return  x * 25 / 100 + x  # kendisine girilen değere %25 zam uygulayan fonksiyon

yeni_maas(8300)

for zamli_maas in maaslar:
   print(yeni_maas(zamli_maas))

