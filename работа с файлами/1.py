abc = "aboutme.txt"
mes = []

for i in range(4):
    mess = input("ведите что то о себе" + str(i + 1)+":")
    mes.append(mess + '\n')

with open(abc, "w") as file:
    for mess in mes:
        file.write(mess)

print("считанные файлы!!!!!!")
with open(abc, "r") as file:
    for mess in file:
        print(mess, end="")
