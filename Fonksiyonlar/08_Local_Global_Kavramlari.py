############
#####
##############>>>>> Local ve Global kavram

list_top=[2,3,4]           # >>>>> Global etki alanındadır her yerden erişilebilir.
type(list_top)
def ekleme(a,b):
    c=a*b                 # c ifadesi local olduğu için kullanamazsın
    list_top.append(c) # Local etki alanında olan c'yi global etki alanına gönderilmesi ve etkilemesini sağladık.
    print(list_top)

ekleme(2,3)
ekleme(99,10)
list_top
ekleme(11,1)