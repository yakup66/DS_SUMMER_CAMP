#########################
# ÖN TANIMLI ARGÜMANLAR/PARAMETRELER ( DEFAULT PARAMETERS/ARGUMENTS )
########################

# KULLANICI DAHA KOLAY KULLANSIN DİYE FONKSİYONUN ÇALIŞMASINI SÜRDÜRMESİNİ SAĞLAR.

def ornek_arguman(a,b):
    c=a/b
    print(c)

ornek_arguman(12,5) # burada istenilen bir arguman kullanıcı tarafından girilmez ise hata verir
                    # hatayı almamak ve ek bir yardım için

# Kullanıcı hata almadan işlem yapması ve varsayılan argüman olması için şu şekilde;
def ornek_arguman(a=12,b=12):
    c=a/b
    print(c)            # VARSAYILAN ARGÜMAN SONUCU 1 VE EKRANA ÇIKTI 1 VERİLECEKTİR

ornek_arguman()   # sonuç 1
ornek_arguman(22,3)  # sonuç 7.33 oldu
