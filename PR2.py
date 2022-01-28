def func():             # Задание №5
    a = int(input())
    b = int(input())
    c = int(input())
    print(min(a,b,c))
func()

х1 = int(input())          # Задание №6
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (х1 + y1 + x2 + y2) % 2 == 0:
    print('ДА')
else:
    print('НЕТ')