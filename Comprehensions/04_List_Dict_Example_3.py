###############
# SÖZLÜK İLE KEY'İ STRİNG, VE VALUESİ AŞAĞIDAKİ GİBİ LİSTE OLAN SÖZCÜK OLUŞTURMAK
# SADECE SAYISAL DEĞİŞKENLER İÇİN YAPILACAKTIR.
####################

import  seaborn as sns


df = sns.load_dataset("car_crashes")
df.columns

# SADECE SAYISAL,NUMERİK DEĞİŞKENLERE UYGULAYALIM
num_cols = [col for col in df.columns if df[col].dtype != "0"]
                                         # df[col].tipi =eşit değil ise "0" yani objectolmayanları yani string olmayanları getirir tam olarak sayısalları istedik.
                                         # df[col].dtype !="0" numerik,sayısal tipteki değişkenleri getirir
dict = {}
agg_list = ["mean","min", "max", "sum"]
# key değerlerine değişken isimlerini, value değerlerine ise agg_list değerlerini vermek istiyorum

for col in num_cols:
    dict[col] = agg_list
dict

# COMPREHENSIONS İLE TEK SATIRDA YAPILIŞI

{col: agg_list for col in num_cols}