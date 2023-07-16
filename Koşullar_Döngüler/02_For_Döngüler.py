#################
# DÖNGÜLER- LOOP
#################
# for loop

öğrenciler=["ali","furkan","sezer","ayşe"]

for students in öğrenciler:   # öğrenciler listesindeki her bir elemanı gez ve students değişkenine aktar
    print(students)

for students in öğrenciler:
    print(students.upper())

salaries = [1000, 1100, 1200, 1400, 1700]


for maaslar in salaries:
    print("Maaş listesi : ", maaslar)

for maaslar in salaries:
    print(int(maaslar*20/100+maaslar))

def yeni_Maas(maas,zam_orani):            ## maaşına zam yaparak parametre girerek zamlı maaşı ekrana vermek
    return int(maas*zam_orani/100 + maas)



for maaslar in salaries:
    print("Yeni Maaş listesi %20 zamlı : ",yeni_Maas(maaslar,20))

salaries2 = [13200, 12100, 14200, 15400, 17600]

for maaslar in salaries2:
    print("Yeni Maaş listesi %20 zamlı : ",yeni_Maas(maaslar,20))

salaries = [1000, 1600, 3200, 4400, 6700]

for maaslar in salaries:       # MAAŞLAR VE HEPSİNE AYNI ANDA YAPILAN ZAM ORANI
    if 4500 > maaslar > 3000:
        print("maaşı 3000den büyük ve 4500 den küçük olanlar: ", maaslar)
    elif maaslar < 2000:
        print("Maaşı 2000 tl den düşük olanlar: ", maaslar)
    else:
        print("Maaşı 4500 tl den büyük olanlar ", maaslar)
    print("Yeni Maaş listesi %20 zamlı : ",yeni_Maas(maaslar,20))

salaries = [1000, 1600, 3200, 4400, 6700]

for maaslar in salaries:                     # MAAŞLARA GÖRE AYRI ZAM ORANLARI
    if 4500 > maaslar > 3000:
        print("maaşı 3000den büyük ve 4500 den küçük olanlar: ", maaslar ," 30 ZAMLI MAAŞ ORANI : " , yeni_Maas(maaslar,30))
    elif maaslar < 2000:
        print("Maaşı 2000 tl den düşük olanlar: ", maaslar," 35 ZAMLI MAAŞ ORANI : " , yeni_Maas(maaslar,35))
    else:
        print("Maaşı 4500 tl den büyük olanlar ", maaslar, " 45 ZAMLI MAAŞ ORANI : " , yeni_Maas(maaslar,45))
    print("ÖNCEKİ %20 MAAŞI ",yeni_Maas(maaslar,20))