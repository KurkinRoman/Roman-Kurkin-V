x = int(input())    #Задача №1
y = 1
while y ** 2 <= x:
    print(y ** 2)
    y += 1


x = int(input()) #Задача №6
i = 0 
s = -1 
while x!=0:
    s+=x
    i+=1
    x=int(input())
print(s/i)
