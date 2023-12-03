def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def criar_vetor(tamanho):
    vetor = [2 * i + 1 for i in range(tamanho)]  # Números ímpares
    return vetor

tamanho_vetor = 30
vetor = criar_vetor(tamanho_vetor)

print("Vetor não ordenado:", vetor)
insertion_sort(vetor)
print("Vetor ordenado:", vetor)