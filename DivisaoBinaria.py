while True:
    def pesquisa_binaria(lista, item):
        baixo = 0
        alto = len(lista) - 1
        tentativas = 0

        while baixo <= alto:
            meio = (baixo + alto) // 2
            chute = lista[meio]
            if chute == item:
                return tentativas
            elif chute < item:
                baixo = meio + 1
            else:
                alto = meio - 1
            tentativas += 1

        return -1

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    item = int(input("Digite o numero da lista:"))
    tentativas = pesquisa_binaria(lista, item)

    if tentativas != -1:
        print(f"Item encontrado após {tentativas} tentativas.")
    else:
        print("Item não encontrado.")

