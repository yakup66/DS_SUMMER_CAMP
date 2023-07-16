
## if ile sorgulama yapma
number2=10
if number2 == 10:
     print("Number is 10")

number1=20
if number1==15:         # > burası true olunca koşul başlar ve print ifadesi çalışır
    print("Number1 is 15")

def numara_kontrol(number):
    if 36<number>10:               # işlem sağlanırsa bu sağlanmazsa else kullanılır
        print("Sayı 10'dan büyüktür")
    elif number<10:
        print("Sayı 10'dan küçüktür")
    elif number==36:
        print("Sayı 36'dır")
    else:
        print("Sayı 10'a eşittir")

numara_kontrol(7)
numara_kontrol(25)
numara_kontrol(10)
numara_kontrol(36)