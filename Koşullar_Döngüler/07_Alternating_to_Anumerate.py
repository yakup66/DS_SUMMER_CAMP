###############################
# alternating fonksiyonunu enumerate ile nasıl yazarız ve ne işe yarar?
##############################################################################

# çift index büyültme, tek indextekilerini küçültme işlemi

def altnating_withEnumerate(string):     # string ifadenin hem index, hem de kendisinde de gezmeliyim
    new_text=""                          # nedeni ise tek mi çift mi olarak sorgulamak ve değiştirmek.

    for t,letter in enumerate(string):   # burada enumerate() ifadesi yerine range(len(string)) ifadesini kullanabiliriz.
        if t % 2 ==0:                     # enumerate ile daha kolay kullanım ve kod okunabilirliği için çok iyi
            new_text += letter.upper()
        else:
            new_text += letter.lower()
    print(new_text)

altnating_withEnumerate("hi my name is jakop and i am hard time for learning python ")