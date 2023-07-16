 # METOT : SINIFLAR İÇERİSİNDE TANIMLANAN FONKSİYONLARDIR.

  # KARAKTER DİZİSİ(STRİNG) METODLARI

dir(str)  # > tüm string metodlarını sana gösterir
########################
# METODLAR
########################

# LEN METODU
 # >> PYTHON İÇERİSİNDE GÖMÜLÜ METODDUR.
 # >> STRİNGLERDE BOYUT BİLGİSİNE ERİŞMEK İÇİN KULLANIRIZ.

name="yapay zeka"
type(name) # str
type(len)  # >> fonksiyon ya da metoddur

len(name) # string ifadesinin kaç elemandan oluştuğu bilgisini gösterir : 1o muş

# KULLANMIŞ OLDUĞUM BİR YAPININ METOD MU YOKSA FONKSİYON MU OLDUĞUNA NASIL KARAR VERİRİM.

# - bir fonksiyon class yapısı içerisinde tanımlandıysa buna >> metot denir
# - clas yapısı içinde değil ise > fonksiyondur
####   GÖREVLERİ AYNIDIR METOT CLAS İÇİNDE FONKSİYON İSE BAĞIMSIZDIR. ####



# upper() > BÜYÜTME                      KÜÇÜK VE BÜYÜK İÇİN KULLANILIRLAR
# lower() > KÜÇÜLTME
name.upper()
name.lower()


# replace()  >> KARAKTER DEĞİŞTİRME METODU
dogal=name.replace("yapay","doğal")        # replace("değiştilecek kısım"," yeni eklenecek kısım")
name
dogal

# split()  >> BÖLME İŞLEMİ AYIRMA İŞLEMİ YAPAR
name.split() # > > argüman girmeden yapılırsa boşluklara göre ayırır

# strip() >> boşlukları siler kırpar
name.strip()

# capitalize() >> ilk harfi büyütür
name.capitalize()
"yakup ertek".capitalize()

# DİR(DEĞİŞKEN ADI YA DA KARAKTER) >>>> UYGUN OLAN METOT İSİMLERİ GÖSTERİR

dir("merhaba")