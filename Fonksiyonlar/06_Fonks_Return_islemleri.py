def hesaplama(number1,number2,number3):
    print((number1+number2)*0.18 + 456)

hesaplama(12,22,3) +10 # bu işlem hatalı olacaktır bunun için return kullanılır

# Return kullanımı

def hesaplama(number1,number2,number3):
    return ((number1+number2)*0.18 + 456)

hesaplama(3,4,5)+1500  # oldu    BUNUN SEBEBİ İSE RETURN İŞLEMİ FONKSİYON DIŞINA ÇIKARIR VE TEKRAR KULLANILMASI İÇİN İŞLEM YAPAR.

sonuc=hesaplama(3,4,5)+1500

def hesaplama(number1,number2,number3):        # 3 tane parametre aldık
    number1 = number1*3
    number2 = number2*3         #  >> her bir parametreyi değerledik ve tekrar kendisine atadık
    number3=number3*3
    output=(number1+number2)/number3       # bir işlem sonucunu yeni bir değişkene aktardık
    return number1,number2,number3,output    # return ederek daha sonra kullanılabilmesini sağladık
hesaplama(100,200,62)
type(hesaplama(100,200,62))   #tuple tipinde
number1,number2,number3,output=hesaplama(1,2,6)  # her bir değeri kendi değerine sırası ile aktardık
hesaplama(100,200,62)
