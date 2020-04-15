def main():
    matriz = [[int(input(f'Digite o valor da posição {sizeI+1} da {sizeJ+1}º linha: ')) for sizeJ in range(4)]
              for sizeI in range(4)]

    for line in matriz:
        for value in line:
            print(value, end='') if value > 10 else print('', end='')


if __name__ == '__main__':
    main()
