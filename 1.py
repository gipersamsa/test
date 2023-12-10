l=[]
num=int(input("Введите количество паролей\n"))
for i in range(num):
    passw=input("Введите пароль \n")
    l.append(passw)

passw=input("Введите ваш пароль\n")
if passw in l:
    print("Пароль найден")
else:
    print("Не найден пароль")