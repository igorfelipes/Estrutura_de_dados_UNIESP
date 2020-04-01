def main():
    colors = []

    sizeColors = int(input('Digite a quantidade de cores que deseja adicionar? '))
    for values in range(sizeColors):
        colors.append(input('Digite o cor que deseja inserir: ').lower())

    colors.remove('vermelho')
    print(colors)


if __name__ == "__main__":
    main()
