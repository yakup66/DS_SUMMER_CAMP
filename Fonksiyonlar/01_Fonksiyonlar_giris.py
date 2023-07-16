####################################################################
# FONKSİYONLAR-KOŞULLAR-DÖNGÜLER-COMPREHENSIONS
####################################################################
# - FONKSİYONLAR (Function)
# - KOŞULLAR     (CONDITIONS)
# - DÖNGÜLER     (LOOPS)
# - COMPREHESIONS

# DEVAMI DİĞER EĞİTİM İÇERİKLERİNDE NOTLARI BULUNMAKTADIR.

# FONKSİYON NEDİR?
 # Belirli görevleri yerine getirmek için yazdığımız kod parçalarıdır.

print("b")
# fonksiyon okuryazarlığı ve bilgi alma, edinme süreci önemlidir
# ?print # > bu kodu python console kısmına yazdığında fonksiyon ile ilgili ve alabileceği,uygun olan tüm parametreleri gösterir.
# ya da
help(print) # python console yazdığında bilgi verilir
# çıktısı >>>> Signature: print(*args, sep=' ', end='\n', file=None, flush=False)

# # # ÖNEMLİ # # # FONKSİYON OKURYAZARLIĞI HAKKINDA BİLGİ
# ?print çıktısını ele alalım, python console ?print yazdığımızda şu çıktıyı alırız.
"""Signature: print(*args, sep=' ', end='\n', file=None, flush=False)  # print içine girilebilecek argümanlar
Docstring:                                                          # argümanların tanımları
Prints the values to a stream, or to sys.stdout by default.         # ++ tüm argümanlar varsayılan olarak print() için tanımldır.
sep
  string inserted between values, default a space.                  # ++  > sep=' '
end
  string appended after the last value, default a newline.          # ++  > end='\n'
file
  a file-like object (stream); defaults to the current sys.stdout.  # ++  > file=None
flush
  whether to forcibly flush the stream.                             # ++  > flush=False
Type:      builtin_function_or_method"""


# peki parametre ve argüman arasındaki farkı nedir
# Parametre > Fonksiyon tanımlanması zamanında ifade edilen değişkenlerdir
# Argüman   > Fonksiyonlar çağrıldığında parametre ifadelerine karşılık olarak girilen değerlerdir.
# DİPNOT > GENEL OLARAK ARGÜMAN İFADESİ KULLANILMAKTADIR.

####################################################################
 ############## FONKSİYON NASIL TANIMLANIR #################
####################################################################
# def ile tanımlanır


### GİRİLEN SAYILARI 2 İLE ÇARPAN FONKSİYON TANIMLASIN

def hesaplama(x): # fonksiyona isim ver> hesaplama # ve argüman ekle (x)
    print(x*2)  #yapacağı iş

hesaplama(5)

def toplama(sayi1,sayi2):
    print(sayi1+sayi2)

toplama(12,23)

toplama(sayi2=34,sayi1=33)  # bu şekilde de kullanarak işlem yapabilirsin. Burada argüman sırası olduğu için işlem sağlayabilirsin.

