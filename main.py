import hashlib

hashes = [
    '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad',
    '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b',
    '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f',
]

def brute_force(hshs : list, combinations, start_point, step):
    for hsh in hshs:
        for i in range(start_point, len(combinations), step):
            hash_object = hashlib.sha256(combinations[i][:-1].encode('ascii'))
            if hash_object.hexdigest() == hsh:
                print(f'Зашифрованная комбинация: {combinations[i]}')
                break
    return None




with open("combindations.txt", mode='r') as file:
    combinations = file.readlines()

n = input("Введите количество потоков: ")

if n.isdigit() == False:
    print("Ошибка! n должна быть числом")
else:
    n = int(n)
    lenght_of_thread = int(len(combinations)/ n)
    for i in range(n):
        brute_force(hashes, combinations, i, n)