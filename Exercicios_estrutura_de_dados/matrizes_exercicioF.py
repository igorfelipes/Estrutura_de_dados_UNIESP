def main():
    matriz = [[input(f'Digite o nome, matricula e data do aluno {number+1} em cada linha respectivamente: ').strip() for _ in range(3)] for number in range(3)]
    print(matriz)


if __name__ == '__main__':
    main()
