#############
# UYGULAMA- MÜLAKAT SORU ÖRNEĞİ DICT COMPREHENSIONS
#############

# ÇİFT SAYILARIN KARESİNİ ALARAK BİR SÖZLÜĞE EKLENMESİNİ SAĞLA
#teklere atama yapma
#çiftlere atama yap
#karesi aldıktan sonra yap
#key'ler orjinal aynı kalacak
# valueler ise değişecektir

numbers=range(10)
new_dict={}

# Comprehensions ile çözüm

{n: n ** 2 for n in numbers if n % 2 == 0}
# key sabit tuttuk yani>  n:
# value değerinin karesini aldık yani> n**2

# Klasik tarz çözüm şekli

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2 ## DİPNOT
    #  new_dict[key]=key**2 burası ise value olur > yani key=n n**2 yeri ise key değeri kullanarak value değeri oluşur


new_dict