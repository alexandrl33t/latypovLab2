import hashlib
import threading
from datetime import datetime

hashes = [
    '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad',
    '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b',
    '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f',
]

found = 0


def brute_force(hshs: list, combinations, start_point, step):
    global found
    for hsh in hshs:
        if found == len(hshs):
            return None
        for i in range(start_point, len(combinations), step):
            hash_object = hashlib.sha256(combinations[i][:-1].encode('ascii'))
            if hash_object.hexdigest() == hsh:
                print(hsh)
                print(f'Зашифрованная комбинация: {combinations[i]}')
                found += 1
                break
    return None


with open("combindations.txt", mode='r') as file:
    combinations = file.readlines()

n = input("Введите количество потоков: ")

if n.isdigit() == False:
    print("Ошибка! n должна быть числом")
else:
    start_time = datetime.now()
    n = int(n)
    lenght_of_thread = int(len(combinations) / n)
    threads = [
        threading.Thread(target=brute_force, args=(hashes, combinations, i, n))
        for i in range(0, n)
    ]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print(f"Время выполнения {datetime.now() - start_time}")