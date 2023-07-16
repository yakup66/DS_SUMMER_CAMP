
###################
# -Uygulama - Mulakat sorusu

#########################

# öğrenci_bol fonksiyonunu yazın
# çift ve tek indexe sahip olan öğrencileri farklı farklı listelere alın
# oluşturulan bu liste tek bir liste olarak return olsun yani tek seferde geri döndürsün değerleri

ogrenciler=["Mehmet","Ali","Leyla","Büşra", "Kamil", "Tekin","Selim" ]

def ogrenci_bol (ogrenciler):
    grup = [[], []]     # grup içerisinde yer alan indexlere göre ayrı ayrı eleman gönderimi sağlayacağım.
    for index,ogrenci in enumerate(ogrenciler):
        if index % 2 == 0:
            grup[0].append(ogrenci)
        else:
            grup[1].append(ogrenci)
    print("ÖĞRENCİLERİN TEK VE ÇİFT İNDEXİNE GÖRE AYRI LİSTEYE EKLENMESİ : ",grup)
    return grup
ogrenci_bol(ogrenciler)
st = ogrenci_bol(ogrenciler)

st[0]
st[1]
