import pickle
import os.path
book = {
    "Abc": "123",
    "Alex": "88005553535",
    "Bob": "8900",
    "Michael": "9000"
}


class ab:
    def book(self):
        print("Текущая книга:\n")
        for name, adr in book.items():
            print("Имя: {0} - Номер: {1}".format(name, adr))

    def inc(self, book):
        book[input("Введите имя пользователя: ")] = str(
            input("Введите номер пользователя: "))

    def delete(self, book):
        deleted = str(input(
            "Введите имя удаляемого пользователя или введите 'exit' для возврата в меню выбора\n"))
        if deleted == "exit":
            ch()
        while deleted not in book:
            print("Введено неверное имя пользователя\nПопробуйте снова\n")
            deleted = str(
                input("Введите имя удаляемого пользователя или введите 'exit' для возврата в меню:  "))
            if deleted == "exit":
                ch()
        del book[deleted]

    def change(self, book):
        name = str(
            input("Введите имя пользователя, номер которого вы хотите изменить или введите 'exit' для возврата в меню выбора\n"))
        if name == "exit":
            ch()
        while name not in book:
            print("Введено неверное имя пользователя\nПопробуйте снова\n")
            name = str(
                input("Введите имя пользователя или введите 'exit' для возврата в меню: "))
            if name == "exit":
                ch()
        book[name] = str(input("Введите новый номер пользователя: "))

    def find(self, book):
        a = str(input())
        for name, adr in book.items():
            if a in name or a in adr:
                print("Имя: {0} - Номер: {1}".format(name, adr))

    def save(self, book):
        bookt = r"E:\Coding\Python\Library\Adresses.txt"
        f = open(bookt, "wb")
        pickle.dump(book, f)
        f.close()
        print("\nКнига успешно сохранена в: ", bookt)

    def load(self):
        global book
        bookt = r"E:\Coding\Python\Library\Adresses.txt"
        if not os.path.exists(bookt):
            ab().save(book)
        f = open(bookt, "rb+")
        book = pickle.load(f)
        f.close()
        print("\nКнига успешно загружена из:", bookt)


def ch():

    while True:
        print("\nВыберите действие:\n1 - посмотреть книгу\n2 - добавить элемент\n3 - удалить элемент\n4 - изменить номер\n5 - поиск элементов\n6 - сохранить книгу\n7 - загрузить книгу\nВведите 'exit' для завершения работы")
        choice = str(input())
        if choice not in ["1", "2", "3", "4", "5", "6", "7", "exit"]:
            print("Введено неверное значение\nПопробуйте снова")
            ch()
        if choice == "1":
            print("")
            ab().book()
        elif choice == "2":
            print("")
            ab().inc(book)
            ab().book()
        elif choice == "3":
            ab().delete(book)
            ab().book()
        elif choice == "4":
            ab().change(book)
            ab().book()
        elif choice == "5":
            ab().find(book)
        elif choice == "6":
            ab().save(book)
        elif choice == "7":
            ab().load()
            ab().book()
        elif choice == "exit":
            exit()


ch()
