 #####################################
 #  > ENUMERATES / COUNTER > OTOMATİK İNDEX ÜRETİCİ   -- > FOR LOOP İLE KULLANILABİLİR.

 # bir nesne içinde gezerken, elemanlara işlem yaparken index bilgisini takip etmek için kullanılabilen
  # ve bu indexe göre işlem yapmak için kullanılır

# SORU - İNDEXİ ÇİFT OLANLARA VE TEK OLANLARA FARKLI İŞLEM YAPMAK?

ogrenciler=["Mehmet","Ali","Leyla","Büşra"]

for yeni_bilgi in ogrenciler:
    print(yeni_bilgi)

#index bilgisini nasıl elde ederim ?

for index,student in enumerate(ogrenciler):
    print(index,student)

# Öğrencilerin çift index ve tek index ayrımı yaparak listelere ayrı ayrı almak?

A=[]
B=[]

ogrenciler=["Mehmet","Ali","Leyla","Büşra"]
                                            # enumerate(ogenciler) listesindeki enumerate fonks bize index ve isimleri
                                            # sırası ile aktarır
for index,student in enumerate(ogrenciler):      # index alanı : index    for index,student in < kısmı için
    if index % 2 == 0:                           # student'e : ogrenciler listesindeki elemanları aktarır.
        A.append(student)                   # enumerate sayesinde indexe göre atama ve listelere tek,çift olarak gönderme
    else:                                   #  - işlemi yaptık.
        B.append(student)
print(ogrenciler)


A
B