#creating a tuple with different data types
tuplex = ("tuple",False,10.4,5)
print(tuplex)

tuplex = (1,2,3,4,5)
print(tuplex)
tuplex = tuplex + (6,)
print(tuplex)

tuplex = (50,100,70,60,50)
print(tuplex.count(50))

tuplex = (2,3,5,8,7,9,10,1,6)
_slice= tuplex[3:5]
print(_slice)
_slice = tuplex[:6]
print(_slice)