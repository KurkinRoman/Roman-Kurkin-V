
from this import s
from tkinter import*
from tkinter import font
win = Tk()
win.title('GUI')
win.geometry('1000x800')

def func_1():
    x = txt1.get()
    N = int(x)
    s = 1
    res = ''
    while s ** 2 <= N:
        res += str(s ** 2)
        s += 1
        res = res + ' '
    ans1.configure(text = res)

tsk1 = Label(win, text='№1 По данному целому числу N распечатайте все квадраты\n натуральных чисел, не превосходящие N, в порядке возрастания.', font=("Times New Roman", 12, 'bold'))
tsk1.place(x=10, y=20)
t1 = Label(win, text='Введите N:')
t1.place(x=500, y=20)
txt1 = Entry(win, width=10)
txt1.place(x=600, y=20)
btn1 = Button(win, text='Выполнить', command=func_1, bg='grey', fg='white')
btn1.place(x=680, y=17)
ot1 = Label(win, text='Ответ: ')
ot1.place(x=760, y=20)
ans1 = Label(win, text='', font=('Times New Roman', 10, 'bold'), width=13, bg='grey')
ans1.place(x=800, y=20)

def func_1():
    a = txt2.get()
    N = int(a)
    x = 2
    while (N % x) > 0:
        x += 1
    ans2.configure(text = x)

tsk2 = Label(win, text='№2 Дано целое число, не меньшее 2. Выведите\n его наименьший натуральный делитель, отличный от 1.', font=("Times New Roman", 12, 'bold'))
tsk2.place(x=10, y=75)
t2 = Label(win, text='Введите число:')
t2.place(x=500, y=74)
txt2 = Entry(win, width=10)
txt2.place(x=600, y=74)
btn2 = Button(win, text='Выполнить', command=func_1, bg='grey', fg='white')
btn2.place(x=680, y=70)
ot2 = Label(win, text='Ответ: ')
ot2.place(x=760, y=74)
ans2 = Label(win, text='', font=('Times New Roman', 10, 'bold'), width=13, bg='grey')
ans2.place(x=800, y=74)

def func_2():
    a = txt3.get()
    x = int(a)
    y = 1
    while (2 ** (y + 1)) <= x:
        y += 1
    ans3.configure(text = y)

tsk3 = Label(win, text='№3 По данному натуральному числу N найдите \nнаибольшую целую степень двойки, не превосходящую N.\nВыведите показатель степени и саму степень. \nОперацией возведения в степень пользоваться нельзя!', font=("Times New Roman", 12, 'bold'))
tsk3.place(x=10, y=130)
t3 = Label(win, text='Введите N:')
t3.place(x=500, y=140)
txt3 = Entry(win, width=10)
txt3.place(x=600, y=140)
btn3 = Button(win, text='Выполнить', command=func_2, bg='grey', fg='white')
btn3.place(x=680, y=135)
ot3 = Label(win, text='Ответ: ')
ot3.place(x=760, y=137)
ans3 = Label(win, text='', font=('Times New Roman', 10, 'bold'),bg='grey', width=13)
ans3.place(x=800, y=138)

def func_3():
    a = txt4_1.get()
    x = int(a)
    b = txt4_2.get()
    y= int(b)
    day = 1
    while y > (x * 1.1):
        day += 1
        x *= 1.1
    ans4.configure(text = day)

tsk4 = Label(win, text='№4 В первый день спортсмен пробежал x километров, \nа затем он каждый день увеличивал пробег\n на 10% от предыдущего значения. По данному \nчислу y определите номер дня, на который\n пробег спортсмена составит не менее y\nкилометров. Программа получает на вход\n действительные числа x и y и должна\n вывести одно натуральное число.', font=("Times New Roman", 12, 'bold'))
tsk4.place(x=10, y=220)
t4 = Label(win, text='Введите X, Y:')
t4.place(x=500, y=255)
txt4_1 = Entry(win, width=10)
txt4_1.place(x=600, y=255)
txt4_2 = Entry(win, width=10)
txt4_2.place(x=680, y=255)
btn4 = Button(win, text='Выполнить', command=func_3, bg='grey', fg='white')
btn4.place(x=760, y=251)
ot4 = Label(win, text='Ответ: ')
ot4.place(x=840, y=255)
ans4 = Label(win, text='', font=('Times New Roman', 10, 'bold'), bg='grey', width=13)
ans4.place(x=880, y=255)

count = 0
def func_4():
    global count
    a = txt5.get()
    if (a != 0):
        count += 1
    else:
        ans5.configure(text = count)
        txt5.delete(0, 'end')

tsk5 = Label(win, text='№5 Программа получает на вход последовательность\n целых неотрицательных чисел, каждое число записано\n в отдельной строке. Последовательность завершается числом 0,\n при считывании которого программа должна\n закончить свою работу и вывести количество\n членов последовательности (не считая завершающего \nчисла 0). Числа, следующие за числом 0, считывать не нужно.', font=("Times New Roman", 12, 'bold'))
tsk5.place(x=10, y=300)
t5 = Label(win, text='Введите числа:')
t5.place(x=500, y=330)
txt5 = Entry(win, width=10)
txt5.place(x=600, y=330)
btn5 = Button(win, text='Выполнить', command=func_4,bg='grey', fg='white')
btn5.place(x=680, y=326)
ot5 = Label(win, text='Ответ: ')
ot5.place(x=760, y=330)
ans5 = Label(win, text='', font=('Times New Roman', 10, 'bold'),width=13, bg='grey')
ans5.place(x=800, y=330)

l = 0
sum = 0
def func_5():
    global l
    S = txt6.get()
    print(S)
    global sum
    if s != "0":
        l += 1
        sum += int(S)
    else:   
        ans6.configure(text = sum / (l + 1))        
    txt6.delete(0,END)

tsk6 = Label(win, text='№6 Определите среднее значение всех элементов \nпоследовательности, завершающейся числом 0.', font=("Times New Roman", 12, 'bold'))
tsk6.place(x=10, y=450)
t6 = Label(win, text='Введите цисла:')
t6.place(x=500, y=450)
txt6 = Entry(win, width=10)
txt6.place(x=600, y=450)
btn6 = Button(win, text='Выполнить', command=func_5, bg='grey', fg='white')
btn6.place(x=680, y=450)
ot6 = Label(win, text='Ответ: ')
ot6.place(x=760, y=450)
ans6 = Label(win, text='', font=('Times New Roman', 10, 'bold'), width='13', bg='grey')
ans6.place(x=800, y=450)

b = 0
a = 10000000
def func_6():
    n=txt7.get()
    global b
    global a
    if(int(n) > a):
        b += 1
    a = int(n)
    if(int(n) == 0):
        ans7.configure(text=b)
    txt7.delete(0, END)
tsk7 = Label(win, text="№7 Последовательность состоит из натуральных \nчисел и завершается числом 0. Определите, сколько\n элементов этой последовательности больше\n предыдущего элемента.", font=('Times New Roman', 12, 'bold'))
tsk7.place(x=10, y=500)
t7 = Label(win, text='Введите цисла:')
t7.place(x=500, y=500)
txt7 = Entry(win, width=10)
txt7.place(x=600, y=500)
btn7 = Button(win, text='Выполнить', command=func_5, bg='grey', fg='white')
btn7.place(x=680, y=500)
ot7 = Label(win, text='Ответ: ')
ot7.place(x=760, y=500)
ans7 = Label(win, text='', font=('Times New Roman', 10, 'bold'), width='13', bg='grey')
ans7.place(x=800, y=500)

win.mainloop()