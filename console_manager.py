import os
import shutil
import victory
import getpass

#1
def make_dir(name_dir):
    os.mkdir(name_dir)
#2
def del_dir(name_dir):
    if os.path.exists(name_dir):
        os.rmdir(name_dir)
    else:
        print('такой папки нет')
#3
def file_copy(file_name,new_file_name):
    shutil.copy(file_name,new_file_name)
#4
def dir_veiw(name_dir):
    print(os.listdir(name_dir))
#7
def os_info():
   print(os.name)
#8
def owner_unit():
    print(getpass.getuser())

#9 Викторина

#11
def change_dir(path_dir):
    os.chdir(path_dir)

while True:
    print('меню:')
    print(' 1 - создать папку\n 2 - удалить (файл/папку)\n 3 - копировать (файл/папку)\n 4 - просмотр содержимого рабочей директории \n 5 - посмотреть только папки')
    print(' 6- посмотреть только файлы\n 7 - просмотр информации об операционной системе\n 8 - создатель программы \n 9 - играть в викторину\n 10 - мой банковский счет')
    print(' 11 - смена рабочей директории \n 12 - выход')
    user_action = int(input('выберите команду'))

    if user_action == 1:
        name_dir = input('Введите имя папки')
        make_dir(name_dir)
    elif user_action == 2:
        name_dir = input('Введите имя папки/файла для удаления')
        del_dir(name_dir)
    elif user_action == 3:
        file_name = input('Введите имя файла для копирования')
        new_file_name = input('Введите новое имя файла')
        file_copy(file_name, new_file_name)
    elif user_action == 4:
        name_dir = input('Введите имя папки для просмотра содержимого')
        dir_veiw(name_dir)
    elif user_action == 7:
        os_info()
    elif user_action == 8:
        owner_unit()
    elif user_action == 9:
        victory.year_verify()
    elif user_action == 11:
        path_dir = input('Введите полный путь до новой папки')
        change_dir(path_dir)
    elif user_action == 12:
        exit()