##########################
# BREAK - WHİLE - CONTİNUE

#BREAK : ARANAN VE YAKALAN KOŞUL SAĞLANDIĞINDA KOŞULUN DURMASINI SAĞLAR.

maaslar=[1000,2200,3000,4600,5400,8000]

for yeni_veri in maaslar:                            # BREAK KOMUT KULLANIMI
    if yeni_veri == 3000:
        break
    print("Rapor oluşturuldu / maaş bilgisi 3000 oldu ve durdu.", yeni_veri)

for yeni_veri in maaslar:                             # CONTİNUE KOMUT KULLANILDI
    if yeni_veri > 4700:
        continue
    print(yeni_veri)


 ##   WHİLE DÖNGÜSÜ ?
number = 1
while number < 10:            # WHİLE DÖNGÜSÜ BİR KOŞULUN TAMAMLANMASI SÜRESİNCE DEVAM EDER. KOŞUL DOĞRU OLDUĞU SÜRECE İŞLEM YAPAR.
    print(number)             # BU İŞLEMDE NUMBER < 10 OLANA KADAR ALTTAKİ İŞLEMLERİ YAPAR.
    number +=1