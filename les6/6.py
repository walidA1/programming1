def wijzig(lijst):
    if lijst==['a','b','c']:
        lijst.clear()
        lijst.append('d')
        lijst.append('e')
        lijst.append('f')

lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)
