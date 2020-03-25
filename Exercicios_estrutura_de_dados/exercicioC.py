def main():
    valuesArray = []
    sizeArray = int(input("Digite a quantidade de valores que deseja digitar: "))
    for size in range(sizeArray):
        valuesArray.append(int(input("Digite o %dº valor: " % (size + 1))))
    print(valuesArray)


if __name__ == '__main__':
    main()
