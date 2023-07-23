import os
import sys

file = os.path.isfile("todo_list.txt")
if file:
    None
else:
    with open("todo_list.txt", "w") as fp:
        pass


def insert(a):
    file_object = open("todo_list.txt", "a+")
    file_object.seek(0)
    data = file_object.read()
    if len(data) > 0:
        file_object.write("\n")
    file_object.write(a)
    file_object.close()


def read():
    f = open("todo_list.txt", "r")
    if f.mode == "r":
        content = f.read()
        print(content)
    f.close()


def delete(d):
    a_file = open("todo_list.txt", "r")
    lines = a_file.readlines()
    a_file.close()
    s = d - 1
    del lines[s]
    new_file = open("todo_list.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()


def clear():
    file = open("todo_list.txt", "a+")
    for line in file:
        if not line.isspace():
            file.write(line)


while True:
    print("1. insert task")
    print("2. read")
    print("3. delete/remove task")
    print("4. exit")
    z = input("enter the option you want: ")
    if "1" in z or "insert" in z or "enter" in z:
        a = input("enter the task you want to add: ")
        insert(a)
    elif "2" in z or "read" in z or "display" in z:
        read()
    elif "3" in z or "delete" in z or "remove" in z:
        d = int(input("enter the task number you want to delete: "))
        delete(d)
        clear()
    elif "4" in z or "exit" in z or "close" in z:
        sys.exit()
