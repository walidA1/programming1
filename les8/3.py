invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
g=invoer.split("-")
volgorde=g.sort()
n = [int(i) for i in g]
som= sum(n)

print('Gesorteerde list van ints: '+str(n)+'\nGrootste getal: '+str(max(n))+' en Kleinste getal: '+str(min(n)))
print('aantal getallen: '+str(len(n))+' en Som van de getallen: '+str(som))
print('Gemiddelde: '+str(som / len(n)))
