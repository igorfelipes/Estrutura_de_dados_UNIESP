def main():
    registros = []

    for reg in range(5):
        registros.append(input('Digite o nome que deseja inserir no registro: '))

    for reg in registros:
        print('Nomes inseridos: ', end='')
        print(reg)

    registros.append(input('Digite o nome que deseja inserir no final do registro: '))
    registros.insert(2, input('Digite o nome que deseja inserir na segunda posição do registro: '))

    print(registros)


if __name__ == "__main__":
    main()
