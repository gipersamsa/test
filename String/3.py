import os

class Aset:
    def __init__(self):
        self.main()

    def main(self):
        while True:
            po = int(input("asdf"))

            if po==1:
                r = self.AsetGETCWD()
                print(r)

            elif po==2:
                r = self.AsetMKDIR()


    def AsetGETCWD(self):
       return os.getcwd()

    def AsetMKDIR(self):
        result = input("введите название папки")
        os.mkdir(result)


aset = Aset()
aset.main()