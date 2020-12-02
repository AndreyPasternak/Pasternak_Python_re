user = input('введите последоваетльность')
var1 = user[1::2]
print(var1)
var2 = user[::2]
print(var2)
for x in user:
    user[x], user[x+1] = user[x+1], user[x]
    print(x)








