from googletrans import Translator
translator = Translator()
#translator.translate('안녕하세요.')
#<Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
while(True):
    srcText = input("Văn bản cần dịch: ")
    if srcText == 'x':
        break
    result = translator.translate(srcText, dest='vi').text
    print("Kết quả : "+result)