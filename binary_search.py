import random


#fazer vector,num
def BinarySearch(vector,num,count=0):
    vector = sorted(vector)
    print(f"Vetor atual: {vector}")
    index = (len(vector)//2)

    if vector[index] == num:
        print(f"Número de iterações: {count}")
        print(f"O item {num} foi encontrado no índice: {index}")
    elif vector[index]>num:
        count += 1
        vector = vector[:index]
        BinarySearch(vector,num,count)
    elif vector[index]<num:
        count += 1
        vector = vector[index:]
        BinarySearch(vector,num,count)
    else:
        print("Item Não encontrado")

def main():
    lista = [9]

    for i in range(0,9):
        n = random.randint(0,20)
        if n != 9:
            lista.append(n)
        else:
            continue

    print(lista)
    BinarySearch(lista,9)

if __name__ == "__main__":
    main()