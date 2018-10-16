file=open('Kaartnummers.txt','r')
regels=file.readlines()
file.close()
for regel in regels:
    kaartinfo=regel.split(', ')
    print('{}heeft kaartnummer: {}'.format(kaartinfo[1].strip(),kaartinfo[0]))



