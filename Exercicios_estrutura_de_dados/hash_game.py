class HashGame:

    def __init__(self):
        self.INDEX_MAX = 3
        self.player1 = []
        self.player2 = []
        self.symbolO = 'O'
        self.symbolX = 'X'
        self.arraySymbol = ['X', 'O']
        self.matrizPrincipal = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.divisoria = '----|----|-----'
        self.counter = 1
        self.col = 0
        self.line = 0
        self.gameEnd = False

    def handlerError(self):
        pass

    def convertPositions(self, value):
        self.col = int(value[0]) - 1
        self.line = int(value[1]) - 1

    def setPlayers(self):
        self.player1.append(input('Digite o nome do primeiro jogador: '))
        self.player2.append(input('Digite o nome do segundo jogador: '))

    def setSymbol(self):
        print()
        print(' ----------PLAYER 1 ------------ ')
        print('1- O     2- X')
        option = input('Opção: ')
        if option.upper() == self.symbolO or option == '1':
            self.player1.append(self.symbolO)
            self.player2.append(self.symbolX)
        else:
            self.player1.append(self.symbolX)
            self.player2.append(self.symbolO)

    def setPositions(self):
        while not self.gameEnd:
            self.printGame()
            if self.counter == 1:
                print()
                print('------PLAYER 1 -------')
                print()
                positions = input('Digite a coluna  e a linha separado por um espaço em branco:  ').split()
                self.convertPositions(positions)
                self.verifyPositions()
                self.counter = 2
                continue

            if self.counter == 2:
                print('------PLAYER 2 -------')
                positions = input('Digite a coluna  e a linha separado por um espaço em branco:  ').split()
                self.convertPositions(positions)
                self.verifyPositions()
                self.counter = 1

    def printGame(self):
        viewLine1 = [' ', ' ', self.matrizPrincipal[0][0], ' ', '|',
                          ' ', ' ', self.matrizPrincipal[0][1], ' ', '|',
                          ' ', ' ', self.matrizPrincipal[0][2], ' ']
        viewLine2 = [' ', ' ', self.matrizPrincipal[1][0], ' ', '|',
                          ' ', ' ', self.matrizPrincipal[1][1], ' ', '|',
                          ' ', ' ', self.matrizPrincipal[1][2], ' ']
        viewLine3 = [' ', ' ', self.matrizPrincipal[2][0], ' ', '|',
                          ' ', ' ', self.matrizPrincipal[2][1], ' ', '|',
                          ' ', ' ', self.matrizPrincipal[2][2], ' ']
        print('\n')
        print(''.join(viewLine1))
        print(self.divisoria)
        print(''.join(viewLine2))
        print(self.divisoria)
        print(''.join(viewLine3))

    def verifyPositions(self):
        if self.matrizPrincipal[self.line][self.col] in self.arraySymbol:
            print('Posição já selecionada por algum jogador, tente novamente')
            self.setPositions()
        else:
            if self.counter == 1:
                self.matrizPrincipal[self.line][self.col] = self.player1[1]
            else:
                self.matrizPrincipal[self.line][self.col] = self.player2[1]

        for index in range(len(self.matrizPrincipal)):
            if all(value == self.player1[1] for value in self.matrizPrincipal[index]) or all(row[index] == self.player1[1] for row in self.matrizPrincipal):
                self.printGame()
                self.gameEnd = True
                return print(self.player1[0], 'Venceu!')
            elif all(value == self.player2[1] for value in self.matrizPrincipal[index]) or all(row[index] == self.player2[1] for row in self.matrizPrincipal):
                self.printGame()
                self.gameEnd = True
                return print(self.player2[0], 'Venceu!')



def main():
    print('-----------------JOGO DA VELHA----------------------')
    hashGame = HashGame()
    hashGame.setPlayers()
    hashGame.setSymbol()
    hashGame.setPositions()


if __name__ == '__main__':
    main()