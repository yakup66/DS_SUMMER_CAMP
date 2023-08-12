######### COMPREHENSIONS ###########

#######
 # LIST COMPREHENSIONS
###########

# BİR LİSTE ÜZERİNDE GEZMEK VE BİRDEN FAZLA İŞLEM UYGULAMAK BELİRLİ LİSTE İÇERİSİNE TEKRAR EKLEME GİBİ İŞLEMLERİ TEK SATIRDA YAPA R.

maaslar=[2000,3000,4300,5400,6900,7200]

 # tanımlanan bir fonksiyon oluşturduk ve daha sonra for içinde kullan
def yeni_maaslar(x):
    return x * 20 / 100 + x    #  >> burada fonksiyonu tanımladık

yeni_liste=[]              # maasları yeni_maas fonksiyonundan geçirerek yeni_liste içine apend yani ekledik
for maas in maaslar:
    if maas > 2000:
        yeni_liste.append(yeni_maaslar(maas*2))
    else:
        yeni_liste.append(yeni_maaslar(maas*2))
yeni_liste

[yeni_maaslar(maas*2) if maas > 2000 else yeni_maaslar(maas) for maas in maaslar]

#maaş listesinde elemanları 3 ile çarp
[maas * 3 for maas in maaslar]

#maaşı 3000 den az olanları ya da x sayısından az olanları 2 ile çarp (sadece if kullanılacak ise if sonda kullanılır)

[maas * 2 for maas in maaslar if maas < 6000 ]

# maaşı 3000 den büyük olanlar ve KÜÇÜK OLANLARA
#
# ( DİPNOT > ) İF TEK KULLANILACAK İSE EN SONDA ELSE İLE BİRLİKTE İSE FOR EN SONDA OLUR

[yeni_maaslar(maas * 2 ) if maas < 5000 else yeni_maaslar(maas * 0.3) for maas in maaslar]

# ELİMİZDE 2 ADET LİSTE VAR
box_yes=["index","python","enumerate"]   # İSTEDİKLERİM > büyük harfli olsun
box_no=["alternating","enumerate","zip","python","lambda"] # İSTEMİYORUM  > küçük harfli olsun

# iki listedeki elemanlar içerisinde istediklerim büyük diğerleri küçük olsun bunu coprehensions yapısı ile yap

result = [box_list.upper() if box_list in box_yes else box_list.lower() for box_list in box_no]
print(result)

## TAM TERSİ İŞLEM İÇİN NOT İN  KULLANILIR
[box_list.upper() if box_list not in box_yes else box_list.lower() for box_list in box_no]


 # elemanları tek tek yalayıp yazdıralım  #   > burada maaslar listesindeki elemanları ekrana verdik ve yeni_maaslar fonksiyonunu kulllandık

for tum_maaslar in maaslar:
    print("Zamlı maaşlar",yeni_maaslar(tum_maaslar))   # for döngüsü içerisinde kullandık (yeni_maaslar)
                                                    # her bir elemanda gez ve yeni_maaslar kullanarak her bir elemana %20 zam yaptık ardından ekrana zamlı verdik

 # zam yapılan yukarıdaki verileri yeni bir listede sakla.

bos_liste=[]  #   > bu boş listeye zam yapılan ve işlem yapılan yeni maaşları ekleyeceğiz.

for maas in maaslar:
    bos_liste.append(yeni_maaslar(maaslar))
for tum_maaslar in maaslar:
    bos_liste.append(yeni_maaslar(tum_maaslar))


