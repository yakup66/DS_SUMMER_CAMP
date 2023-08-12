###########
# BİR VERİ DEĞİŞKENİNDEKİ İSİMLERİ DEĞİŞTİRMEK
##############

# KÜTÜPHANE İMPORT ETME ŞEKLİ

import seaborn as sns    # > seaborn import ettik ve sns ile
df = sns.load_dataset("car_crashes")   # seaborn kütüphanesinden "car_crashes" veri setini çektik ve df şeklinde kaydettik
df.columns

# df.columns denildiğinde data frame içerisindeki değişken isimleri gelir yani kolon isim başlıkları diyebiliriz.
"""
   total  speeding  alcohol  ...  ins_premium  ins_losses  abbrev
0    18.8     7.332    5.640  ...       784.55      145.08      AL
1    18.1     7.421    4.525  ...      1053.48      133.93      AK
2    18.6     6.510    5.208  ...       899.47      110.35      AZ """ # > şeklinde total,speeding, alcohol gibi

# DATA FRAME ÇEKTİĞİMİZ YUKARIDAKİ DEĞİŞKEN İSİMLERİNİ BÜYÜLT?

for col in df.columns:
    print(col.upper())  # hepsi büyük oldu ama birlikte ekrana versin yani değişken sonuçlarını da versin
                        # YANİ KALICI BİR ŞEKİLDE DF' E YANSITMAK İSTİYORUM

df_list=[]
for col in df.columns:
    df_list.append(col.upper())  # df.columns içerisinde geziyorum her bir elemanı upper ile büyük harf yapıp
                                 # df_list ekliyorum

df.columns = df_list  #değişken isimlerini aktardık
# TAMAMLANDI

# LIST COMPREHENSIONS İLE YAPILIŞI

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]
df.columns