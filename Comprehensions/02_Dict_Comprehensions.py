##################
# DİCT COMPREHENSIONS

dictionary={"a":1,
            "b":2,
            "c":3,
            "d":4}
dictionary.keys()
dictionary.values()
dictionary.items()  # tupple olarak key ve value olarak ulaşırız

#HER BİR VALUE'NİN KARESİNİ ALALIM

{k: v ** 2 for (k,v) in dictionary.items()}  # burada k,v değerleri için dictionary içerisinde gezerek (k,v) atamasını ve k sabit v ise 2 ile çarpma işlemi yaptık.

# HER BİR KEY DEĞERİNİ BÜYÜK HARF YAP VE VALUE DEĞERİNİ İSE 0.9 İLE ÇARP ÜSTÜNE 2 EKLE
{k.upper(): v ** 0.9 + 2 for (k,v) in dictionary.items()}

# 0.9 A BÖL VE YENİ BİR DEĞİŞKENE AKTAR VE EKRANA VER

new_dictionary={k.lower(): v/0.9 -2 for (k,v) in dictionary.items()}
new_dictionary
dictionary.items()