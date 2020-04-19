class HashGame:

    def __init__(self):
        self.array = [[], [], []]
        self.INDEX_MAX = 3
        self.player1 = []
        self.player2 = []
        self.symbolO = 'O'
        self.symbolX = 'X'

    def setPlayers(self):
        self.player1.append(input('Digite o nome do primeiro jogador: '))
        self.player2.append(input('Digite o nome do segundo jogador: '))

    def setSymbol(self):
        print()
        print(' ----------PLAYER 1 ------------ ')
        option = input('1- O     2- X')
        if option.upper() == self.symbolO:
            self.player1.append(self.symbolO)
            self.player2.append(self.symbolX)
        else:
            self.player1.append(self.symbolX)
            self.player2.append(self.symbolO)

    def setPositions(self):
        pass

    def verifyPositions(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
