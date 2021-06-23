import pickle
book = ["Fast", "Fun", "Run", "123"]


class ab:
    def book(self):
        print("\nТекущий список:")
        print(book)

    def inc(self, book):
        book.append(input())

    def delete(self, book):
        x = int(input())
        for i in range(len(book)):
            if i == x - 1:
                del book[i]

    def find(self, book):
        a = str(input())
        for i in book:
            if a in i:
                print(i)

    def save(self, book):
        bookt = r"E:\Coding\Python\Library\ook.txt"
        f = open(bookt, "wb")
        pickle.dump(book, f)
        print("\nСписок успешно сохранен в: ", bookt)

    def load(self):
        bookt = r"E:\Coding\Python\Library\ook.txt"
        f = open(bookt, "rb+")
        global book
        book = pickle.load(f)
        print("\nСписок успешно загружен из:", bookt)


def ch():

    while True:
        print("Выберите действие:\n1 - посмотреть книгу\n2 - добавить элемент\n3 - удалить элемент\
        \n4 - поиск элементов\n5 - сохранить список\n6 - загрузить список")
        choice = int(input())
        if choice == 1:
            ab().book()
        elif choice == 2:
            print("\nВведите название добавляемого элемента:")
            ab().inc(book)
            ab().book()
        elif choice == 3:
            print("\nВведите номер элемента, который хотите удалить:")
            ab().delete(book)
            ab().book()
        elif choice == 4:
            ab().find(book)
        elif choice == 5:
            ab().save(book)
        elif choice == 6:
            ab().load()
        else:
            exit()


ch()
