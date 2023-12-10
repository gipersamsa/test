librar={

}
def add_book(title,author,year):
    if title not in librar:
        librar[title]={
             'author':author,
              "year":year
        }
        print("Книга успешно добавлена")
    else:
        print("Эта книга уже существует")


def get_info(title):
    print(librar[title])

def remove_book(title):
    if title in librar:
        del librar[title]
        print("Успешно удалена")
    else:
        print("Книги нет")

