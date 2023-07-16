# Dictionary( SÖZLÜKLER )
############################
# Değiştirilebilir
# Sırasızdır (3.7 sürümünden sonrası sıralıdır)
# Kapsyıcıdır

# key - value değerleri ile tanımlarsın.
# süslü parantez ile oluşturulur

dictionary={"Reg": "Regression",
            "log": "Logistic Regression",        # okunabilirlik için virgül sonrsaı alt satıra geç
            "Cart": "Classification and Reg"}

dictionary["Reg"]  # çağırdığında değeri gelir

dictionary={"Reg":["RMSE",10],
      "Log":["MSE",20],
      "Cart":["SSE",30]}    # value tarafına liste girilebilir ve

dictionary["Log"]

dictionary={"Reg":10,    # int olarakta değerleri yapabilirim
      "Log":20,
      "Cart":30}

####################################
# KAPSAYICILIK ÖZELLİĞİ
####################################

dictionary={"Reg":["RMSE",10],           ## ÖNEMLİ > KAPSAYICILIK ÖZELLİĞİ -> FAZLA VERİ YAPISINI TUTTU
            "Log":["MSE",20],
            "Cart":["SSE",30]}           # peki ben "Cart" anahtarındaki 30 değerine erişmek istiyorsam


####################################
# SIRALI OLMASI VE ERİŞİLEBİLİR OLMASI
####################################
# şu şekilde içerdeki değere erişebilirsin
dictionary["Cart"]
dictionary["Cart"][1]                    # ÖNEMLİ > SIRALI OLMASI VE ERİŞİLEBİLİR OLMASI -> SIRALAMA VER ERİŞME İŞLEMİ
########################
# KEY SORGULAMA
########################
"Log" in dictionary
## yukarıdaki dictionary içinde "Log" var mı diye sorguladık

#######################
# KEY'E GÖRE DEĞERLERE ERİŞME İŞLEMİ
   # 2 FARKLI ŞEKİL VAR
#######################
# 1
dictionary["Reg"]
# 2
dictionary.get("Reg")   # bu şekilde de elemanlara-değerlere erişebiliriz.

####################################
# DEĞİŞTİRİLEBİLİRLİK ÖZELLİĞİ
####################################

dictionary["Reg"]=["Ckv",39]  # şeklinde değeri ve içindekilere erişerek değiştirebiliriz.

# METODLAR İLE ERİŞİM>>>
#########################
# TÜM KEY'LERE ERİŞMEK
#########################
dictionary.keys()         # tüm keylere erişilebilen metod bulunmaktadır

#########################
# TÜM VALUE'LERE ERİŞMEK
#########################
dictionary.values()

################################
# TÜM ÇİFTLERİ TUPLE FORMATINDA ERİŞMEK VE LİSTEYE ÇEVİRMEK
################################
dictionary.items()  # tuple cinsinden liste içindeki herşeyi bize verdi

######
# yeni bir değer atamak-oluşturmak -> update()
######
dictionary.update({"Yeni":77})
dictionary