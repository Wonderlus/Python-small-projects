import time
import os
source = "Library"
target_dir = r"E:\Coding\Python\Library\Backup"
now = time.strftime("%H_%M_%S")
target = target_dir + os.sep + time.strftime("%d_%m_%Y")
zip_com = "zip -qr {0} {1}".format(target + os.sep + now + ".zip", source)
if not os.path.exists(target):
    os.mkdir(target)
    print("Каталог", target, "успешно создан")
print(zip_com)
if os.system(zip_com) == 0:
    print("Бэкап создан в", target)
else:
    print("Не удалось создать резервную копию")
