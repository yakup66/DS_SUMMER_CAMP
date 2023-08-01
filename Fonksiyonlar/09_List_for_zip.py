########
# zip ile tüm listelerinizi ayrı ayrı listeleri tek listede toplamasına olanak sağlar

ogrenciler=["Mehmet","Ali","Leyla","Büşra", "Kamil", "Tekin","Selim" ]
maaslar=[1000,2200,3000,4600,5400,8000]
ages=[17,18,22,25,33]

list(zip(ogrenciler,maaslar,ages))         # her birisinde bulunan elemanları aynı sırada zipleyerek bir araya getirir.
                                            # her birini tek bir eleman şeklinde görebilirsiniz.