def main():
    matriz = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]

    numbers = input('Digite os  dois números separados por um espaço em branco: ')
    numbers = numbers.split()
    for index, line in enumerate(matriz):
        line.append(int(numbers[index]))

    print(matriz)


if __name__ == '__main__':
    main()
