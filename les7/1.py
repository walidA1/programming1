def conver(Celsius):
    Fahrenheit=Celsius*1.8+32
    return Fahrenheit

def table(temp):
    print('  F     C')
    for n in temp:
        conver(n)
        print('{:5} {:5}'.format(conver(n),n))





temp=range(-30,41,10)
table(temp)