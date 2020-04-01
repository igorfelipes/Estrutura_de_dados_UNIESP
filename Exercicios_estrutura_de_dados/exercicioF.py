def main():
    registers = []

    for reg in range(5):
        registers.append(input('Digite o nome que deseja inserir no registro: '))

    name = input('Digite o seu nome: ')
    registers[registers.index(name)] = input('Digite seu sobrenome: ')

    print(registers)


if __name__ == "__main__":
    main()
