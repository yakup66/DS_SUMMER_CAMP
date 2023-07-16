def ornek1(number1,number2,number3):           # fonksiyon işlemlerini yeni fonksiyon olan ortak_fonksiyon için kullanıcaz >>
    return int((number1+number2)*number3)

def ornek2(number4,number5):                   # fonksiyon işlemlerini altta kullanıcaz >>
    return int(number4*10/100*number5*number5)

def ortak_fonksiyon(number1,number2,number3,k):  # number4 kullanmadığım için argüman olarak eklemedim
    a=ornek1(number1,number2,number3)            # a değerini içerden düzenledim ve yeni değer atadım
    b=ornek2(a,k)                                # a değerini burada kullandım ve bu fonksiyondaki k argümanımı kullanarak yeni değişken b ye atadım
    print(b*10)                                  # ardından b değişkenimi kullanarak işlem yaptım

""" Fonskiyonların içerisinde fonksiyon kullanacaksan eğer kullanacağın fonksiyonların argümanlarını
    yeni oluştucağın(ortak_fonksiyon) argüman kısmına eklemelisin
    - ortak_fonksiyon içinde kullanılan ornek1 ve ornek2 fonksiyonun argümanlarını ekledim
    - ornek1 ve ornek 2 argümanlarını işlemleri için yeni değişken a ve b oluşturuldu"""

ortak_fonksiyon(2,4,5,19)