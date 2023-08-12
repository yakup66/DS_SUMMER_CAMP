###################
# İSMİNDE "INS" OLANLAIRN BAŞINA FLAG DİĞERLERİNE NO_FLAG EKLE
######################

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

["FLAG_" + col for col in df.columns if "ins" in col]

# COMPREHENSIONS İLE FLAG VE NO_FLAG EKLEME İŞLEMİNİ TEK SATIRDA TAMAMLADIK.
["FLAG_" + col if "ins" in col else "NO_FLAG_" + col for col in df.columns ]

# KALICI HALE GETİRELİM  BUNUN İÇİN DF.COLUMNS DEĞİŞKENİNE GÖNDERMEK KALIYOR
df.columns = ["FLAG_" + col if "ins" in col else "NO_FLAG_" + col for col in df.columns ]