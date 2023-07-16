
####### UYGULAMA SORUSU- ÖRNEK SORU

# NE YAPMALISIN? > AŞAĞIDA VERİLEN STRİNG İFADE ŞEKLİNDEKİ BİLGİYİ ŞARTLARA GÖRE DÜZENLEMELİSİN?

# ÖNCESİ >  hi my name is jakop and i am learning python
# SONRASI > Hi My NaMe İs JaKoP aNd İ aM lEaRnİnG pYtHoN

#çift indekstekileri küçült , tek indekstekileri küçült
# fonksiyon, döngü, if else yapılmalıdır.

range(len("hi my name is jakop and i am learning python"))  # 0-44 e kadar dedi
                      # range() metodu> iki değer arasında sayı üretmemizi sağlar.
                      # içine argüman girmeden range(0,12) olursa 0,12 arası alır

for i in range(len("hi my name is jakop and i am learning python")):
    print(i)                                  # > burada range metodu içindeki string ifadenin uzunluğu kadar 0,44 arası
                                              # - gez dedik ve sonucu her bir i değişkenine aktararak adım sayısını verdi.

def metin(string):      # ÇOK ÖNEMLİ İNCELE BUNU    #girilen stringin indexlerinde gezerek işlem yapar.
    new_string = ""                                 # range> burada range içine stringin boyutunu verdik,sayı vermedik
    for string_index in range(len(string)):         # >> buraya kadar fonksiyonda girilen bir ifadenin
        if string_index % 2 == 0:                   #  tüm indexlerini gezebiliyoruz.
            new_string += string[string_index].upper() # index çift ise büyük harfe
        else:
            new_string += string[string_index].lower() # index küçük ise küçük harfe çevir.
    print(new_string)                               # > dikkat > döngü dışına almalısın> en sonki çıktıyı print(new_string)

# DİPNOT :
   # YUKARIDA VERİLEN += İFADESİ NE DEMEKTİR.
   # BURAYA İLGİLİ İFADEYİ EKLE VE BU İFADENİN YENİ DEĞERİ OLARAK MEVCUT HALİNİ KORU.
   # YANİ YENİ EKLENECEK VERİ İLE HER SEFERİNDE GÜNCELLE VE ESKİSİNİ DE KORU DEMEKTİR.
   # ÖRNEKKK>>>>>> MERHABA> M EKLENDİ, E EKLENDİ > ME OLDU / R EKLENDİ > MER OLDU GİBİ.
metin("hi my name is jakop and i am learning python")