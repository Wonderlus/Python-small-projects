import time
import os
source = "Library"
target_dir = r"E:\Coding\Python\Library\Backup"
now = time.strftime("%H_%M_%S")
today = target_dir + os.sep + time.strftime("%d_%m_%Y")
if not os.path.exists(today):
    os.mkdir(today)
    print("Создан каталог - ", today)
comm = input("Введите комментарий: ")
if len(comm) == 0:
    target = today + os.sep + now + ".zip"
else:
    target = today + os.sep + now + "_" + comm.replace(" ", "_") + ".zip"
zip_com = "zip -r {0} {1}".format(target, source)
if os.system(zip_com) == 0:
    print("Бэкап завершен")
else:
    print("Не удалось создать резервную копию")
