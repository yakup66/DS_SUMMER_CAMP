  # KARAKTER DİZİLERİ- STRİNGLER

# TEK TIRNAK -ÇİFT TIRNAK FARKI YOK
"TIKLA"
'TIKLA'

#  ÖNEMLİ  > BİR PRİNT KULLANIMI PROGRAM YA DA FONSKİYON YAZARKEN EKRANA BİLGİ PAYLAŞMAK İÇİN PRİNT İÇİNDE KULLANIRSIN.

print("tıkla")

# ÇOK SATIRLI KARAKTER DİZİSİ KULLANIMI  """  ARASINA YAZILABİLİR ALT SATIRA EKLENEBİLİR """

 # ÖRNEK
long_string=""" MERHABA BURAYA ÇOK SATIR EKLEME
   İŞLEMİ YAPABİLİRSİN AYNI ZAMANDA ALT
   SATIRA GEÇEBİLİRSİN """

# KARAKTER DİZİLERİNDEKİ ELEMANLARA ULAŞMAK -İNDEX OLARAK ERİŞİM

a="tıkla"
a[0]
a[3]
  # harflerin bir kısmı için slice işlemi
a[0:2] # 2 dahil olmadan 2 ye kadar git demek > tı

 # DAHA UZUN İFADELER İÇİN

b="merhaba ben yapay zeka size nasıl yardımcı olabilirim"
 # uzun ifadelerde kullanım
b[0:23]

# KARAKTER SORGULAMA
"yapay zeka" in b # > burasını b değişkeninde bulacak ve true olacaktır

"Yapay zeka" in b # > burasını harf büyük o yüzden false olacaktır.
