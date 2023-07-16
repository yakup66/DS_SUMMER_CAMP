################
#Set-küme
################

# -Değiştirilebilir
# -Sırasız ve Eşsizdir    ******* Önemli <<<<<< kesişimi,bileşimi nedir soruların cevabını ararken kullanılır
# - Kapsayıcıdır
# set() ya da set{} olarak oluşturulabilir

set0=set([2,3,4])
set1=set([2,5,3])

########
 # differece() > İki kümenin Birleşimi
########

# SORU 1- SET0 DA OLUP SET1 DE OLMAYANLARI BULMA
set0.difference(set1)  # yani 4

# Soru 2 - Set1 de olup set0 da olmayanlar
set1.difference(set0)  # yani 5

# Soru 3 - her iki setin birleşimi nedir yani her iki sette ortak olanlar?
set1.symmetric_difference(set0)
set0.symmetric_difference(set1)

########
 # İntersection() > İki kümenin Kesişimi
########
set0=set([2,3,4])
set1=set([2,5,3])

set0.intersection(set1) # 2 3 oldu
set1.intersection(set0) # 2 3 oldu
###########
# KESİŞİM İFADE ETMENİN DİĞER YOLU
###########
set0 & set1
# FARKI
set0-set1


###############
# union() > Kümenin birleşimi
###############

set0.union(set1)  # 2 3 4 5
set1.union(set0)

## kümenin kesişimi boş mu dolu mu öğrenmek için >>> isdisjoint()

# > isdisjoint()
set0=set([2,3,4])
set1=set([2,5,3])
set0.isdisjoint(set1)  # false boş değil

set1.isdisjoint(set0)

####################
# BİR KÜME DİĞER KÜMENİN ALT KÜMESİM Mİ SORUSU > TRUE OR FALSE
####################
# > issubset()
set0=set([2,3,4])
set1=set([2,5,3,4,7,8,9])
set0.issubset(set1) # true > sert0 set1'in alt kümesi
set1.issubset(set0)  # false

#####################
# issuperset() > bir küme diğer kümeyi kapsıyor mu ?
#####################
set0.issuperset(set1) # false
set1.issuperset(set0) # true
