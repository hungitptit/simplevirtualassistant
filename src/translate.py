from googletrans import Translator
translator = Translator()
#translator.translate('안녕하세요.')
#<Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
while(True):
    srcText = input("Src: ")
    if srcText == 'x':
        break
    result = translator.translate(srcText, dest='en').text
    print("Dest : "+result)