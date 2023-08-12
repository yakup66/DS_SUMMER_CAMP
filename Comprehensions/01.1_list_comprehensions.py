salaries=[2000,3000,4000,5000,6000]  # liste tanımladık

def new_salary(x):          # >>> burada x parametresinin yerine girilecek değere göre bir fonksiyon oluşturduk
    return print(x * 20 / 100 + x)

null_list=[]  # > burada boş bir liste tanımladık. AMACIMIZ BU LİSTEYE YENİ ZAMLI MAAŞLARI AKTARMAK.

for salary in salaries:        #  >>>> maaş listesindeki elemanları tümünü gezer ve new_salary ile listedeki elemanları
    print(new_salary(salary))  #       fonksiyon içi hesaplamaya göre teker teker alır hesaplar ve ekrana verir.

# yukarıdaki tüm listeye new_salary fonks ile %20 zam hesaplaması yaparak yeni bir değişkene yani salary'e aktardık.

# YENİ LİSTEYE ŞU ŞEKİLDE EKLEYEBİLİRSİN

for salary in salaries:
    null_list.append(new_salary(salary))
    # eklenen her bir değer her bir satırda gözükecektir.

[new_salary(salary * 2) if salary < 4000 else new_salary(salary) for salary in salaries]

# maaşlar listesindeki her bir elemanı 2 ile çarp

[salary * 2 for salary in  salaries]

[salary * 3 for salary in salaries if salary < 3000 ]     # TEK BİR İF YAPISI VAR İSE İF SAĞ TARAFTA YER ALIR

[salary * 3 if salary < 3000 else salary * 0 for salary in salaries]  # burada if ve else beraber kullanıldığı için sol tarafta yer aldı

[new_salary(salary * 3) if salary < 3000 else salary * 0.3 for salary in salaries]

# İF VE ELSE KULLANILDIĞI İÇİN FOR EN SAĞ TARAFTA
# YAKALANAN HER BİR ÖĞRENCİ VAR İSE BÜYÜT VE KÜÇÜLTME
students = {"john", "mark", "Venessa", "Mariam"}  # tüm öğrenciler OLANLARI KÜÇÜK HARF YAP
student_no = {"john", "Venessa"}       # istemediğim öğrenciler BURADA OLMAYANLARI BÜYÜK

[student.lower() if student in student_no else student.upper() for student in students]

 # YUKARIDAKİ İFADEYİ NOT İN İLE KULLANMAK

[student.upper() if student not in student_no else student.lower() for student in students]
                          # not in kullanarak tam tersi yapabilirsin
                          # student içinde değil ise büyüt yapabilirsin