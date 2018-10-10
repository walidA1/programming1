leeftijd=eval(input('geef je leeftijd: '))
paspoort=(input('heb je nederlandse paspoort?'))
if leeftijd>=18 and paspoort=='ja' :
    print('je mag stemmen')
else:
    print('je mag niet stemmen')