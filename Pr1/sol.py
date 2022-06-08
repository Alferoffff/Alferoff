def number0():
    print("Нет такой задачи)))")

def number1():
    import psutil
    from pprint import pprint
    print("Информация о устройстве:")
    pprint(psutil.disk_partitions())

def number2():
    import string
    import os

    i=input()
    f= open("files.txt","w")
    f.write(i)
    f.close
    with open("files.txt", "r") as f:
        m=f.read()
    print(m)
    os.remove("files.txt")

def number3():
    import json
    import os

    data = input()
    to_json = {'nadpis': data}
    with open('file.json', 'w') as f:
        f.write(json.dumps(to_json))
    with open('file.json') as f:
        print(f.read())
    os.remove('file.json')

def number4():
    import zipfile
    import os
    i=input()
    newzip = zipfile.ZipFile('bdseoru.zip', 'w')
    f = open("fike.txt", "w")
    f.write(i)
    f.close()
    newzip.write('fike.txt')
    os.remove("fike.txt")
    while True:
        x = int(input("Показать содержимое файла:1-да/2-извлечь файл/3-удалить"))
        if x == 0:
            break
        elif x == 1:
            newzip.printdir()
        elif x == 2:
            newzip.extract('fike.txt')
            with open("fike.txt", "r") as f:
                y = f.read()
                print(y)
                f.close()
        elif x == 3:
            newzip.close()
            os.remove("bdseoru.zip")
            try:
                os.remove("fike.txt")
            except FileNotFoundError:
                pass
            else:
                os.remove("fike.txt")
            break

def number5():
    import xml.etree.ElementTree as ET
    import os

    first_name = input("First name: ")
    last_name = input("Last name: ")
    city = input("City: ")

    items = [
        {"first_name": first_name, "last_name": last_name, "city": city},
    ]

    root = ET.Element('root')

    for i, item in enumerate(items, 1):
        person = ET.SubElement(root, 'person' + str(i))
        ET.SubElement(person, 'first_name').text = item['first_name']
        ET.SubElement(person, 'last_name').text = item['last_name']
        ET.SubElement(person, 'city').text = item['city']

    tree = ET.ElementTree(root)
    tree.write('xmlf.xml')

    with open('xmlf.xml') as f:
        print(f.read())

    os.remove('xmlf.xml')
