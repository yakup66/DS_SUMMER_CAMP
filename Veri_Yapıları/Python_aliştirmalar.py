#######      LİSTE(LİST)  ##############
# - DEĞİŞTİRİLEBİLİR
# - SIRALIDIR. İNDEX İŞLEMLERİ YAPILABİLİR
# - KAPSAYICIDIR.

notes=[1,2,3,4]
type(notes)

names=["a","b","c","d"]
hepsi_olabilir=[1,2,3,"a","b",True,[1,2,3]]  # listeler farklı tipleri barındırabilir. *** ÖNEMLİ - KAPSAYICILIK ÖZELLİĞİ

hepsi_olabilir[0]
hepsi_olabilir[5]

hepsi_olabilir[6]  # önce listeye eriştim daha sonra
hepsi_olabilir[6][2]   # liste içinde listenin elemanına eriştim

type(hepsi_olabilir[6])  # list tipinde
type(hepsi_olabilir[6][2]) # int tipinde                     *****LİSTELER SIRALIDIR VE ERİŞİLEBİLİR.

hepsi_olabilir[6][1] = [99]
hepsi_olabilir # liste içindeki listedeki elemanına eriştik ve değiştirdik

notes # 1,2,3,4,5
notes[2]=656           # köşeli parantez koyarak içinde yeni bir liste oluşturabilir ya da notes içine direkt eleman değiştirebilirsin.
notes # 1,2,656,4,5,
                                   #  ****** LİSTELER DEĞİŞTİRİLEBİLİR **********

# ************ LİSTELER İÇİN METOT KULLANIMLARI**************

# append() >>> Ekleme metodu
notes.append(33)
notes
# len()    >>> Uzunluk verir
len(notes) # 6
len(hepsi_olabilir) # 7

# pop()  >>> İndexe göre eleman silme işlemi
notes.pop(3)
notes

# insert()  >>> indexe ekler
notes
notes.insert(0,150)     # sıfırıncı indexe 150 ekledi
notes
