############# FONKSİYONLARIN STATEMENT /BODY BÖLÜMLERİ ############
            ############################################
# fonksiyon 3 tane string değeri yazdırması
def ornek():
    print("merhaba")
    print("selam")
    print("nasılsın?")

ornek()

def carpma(number1,number2):
    sonuc=number1*number2
    print(sonuc)

carpma(12,3)


#Girilen değerleri liste içerisinde saklayacak fonksiyon yaz

list_store=[]
def add_arguman(a,b):                 # 2tane argüman aldık ve işlem yaptırıyoruz
    sonuc=a*b
    list_store.append(sonuc)          # >>> oluşturduğumuz boş listenin içine her defasında çağırılan ve girilen işlem yapılan argümanları ekler
    print("Listedeki elamanlar :", list_store) # > ardından ise ekrana bu şekilde metod çağırma sonrası çıktısını verir
# not > listeler değiştirilebilir olduğu için metod içine eleman ekleme yapabildik.

# APPEND METODU İlgili VERİ YAPISINDA KALICI DEĞİŞİKLİKLER OLDUĞU İÇİN YENİDEN ATAMA İHTİYACINA GEREK KALMAZ.
# UYGULANAN LİSTE'DE KALICI OLACAKTIR. > LOCAL ETKİ ALANIDIR. FONKSİYONUN ETKİ ALANINDADIR. GLOBALDE DEĞİLDİR.
# list_store > global
# list_store.append() > local alandadır.
add_arguman(23,12)
add_arguman(3,5)
add_arguman(1,2)
add_arguman(99,2)
list_store