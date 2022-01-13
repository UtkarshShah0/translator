import googletrans
from googletrans import Translator
translator=Translator()
a=input("Enter The Message You Want To Translate: ")
print("Enter In Small Letters")
b=input("Enter The Language In Which Message Is Written: ")
c=input("Enter The Language In Which Message Is To Be Translated: ")
d=googletrans.LANGUAGES
def get_key_from_value(d, val):
    keys=[k for k, v in d.items() if v== val]
    if keys:
        return keys[0]
    return None
k1= get_key_from_value(d, b)
k2= get_key_from_value(d, c)
result=translator.translate(a, src=k1, dest=k2)
print("The Message You Entered ",a)
print("Translated",b,"-->",c)
print("The Translated Message Is: ",result.text)
