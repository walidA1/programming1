def standaardprijs(afstandKM):
    if afstandKM > 50:
        bedrag=15+afstandKM*0.60
    else:
        if afstandKM<0:
            afstandKM==0
        bedrag = afstandKM*0.80
    return bedrag

def ritprijs(leeftijd,weekendrit,afstandKM):
    weekendrit==("ja")
    if weekendrit==True:
        if leeftijd<12 or leeftijd>64:
            print(standaardprijs(afstandKM)*0.70)
        else:
            print(standaardprijs(afstandKM))
    else:
        if leeftijd < 12 or leeftijd > 64:
            print(standaardprijs(afstandKM)*0.65)
        else:
            print(standaardprijs(afstandKM)*0,60)
    return


leeftijd=eval(input("leeftijd: "))
weekendrit=input("weekendrit?: ")

print(standaardprijs(10))

print(ritprijs(leeftijd, weekendrit,10))

