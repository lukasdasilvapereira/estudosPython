def lista():

    try:
        arr = [10, 20, 30, 40, 50]
        print(arr)

        indice = int(input("Digite o indice: "))
        print(f"Elemento no índice {indice}: {arr[indice]}")

    except IndexError as err:
        print(err)
    except ValueError as err:
        print(err)    


lista()