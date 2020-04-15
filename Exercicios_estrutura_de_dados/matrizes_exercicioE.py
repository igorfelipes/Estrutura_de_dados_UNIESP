def main():
    matriz = [[int(input(f'Digite o valor da posição {sizeI+1} da {sizeJ+1}º linha: ')) for sizeJ in range(4)]
              for sizeI in range(4)]

    print(matriz)


if __name__ == '__main__':
    main()
