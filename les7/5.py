def gemiddelde():
    zin = input('typ een willekeurige zin:')
    lst = zin.split(" ")
    aantal_woorden = 0
    lengte_woorden = 0
    for word in lst:
        aantal_woorden +=1
        lengte = len(word)
        lengte_woorden += lengte
    print (lengte_woorden/aantal_woorden)
gemiddelde()