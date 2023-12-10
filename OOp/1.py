class User:
    username=""

    def __init__(self,usname,password):
        self.__password=password
        self.username=usname

    def get_password(self):
        return self.__password

    def set_password(self,new_pass):
        self.__password=new_pass
        print("Пароль успешно сменен")

class CSuser(User):
    storona=""
    skin=""

    def __init__(self,username,password,storona,skin):
        super().__init__(username,password)
        self.storona=storona
        self.skin=skin

cs1=CSuser("Ahmad","123","Specnaz","SWAG")
print(cs1.username)
