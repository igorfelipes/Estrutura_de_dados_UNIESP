class SheldonGame:
    def __init__(self, sheldonOption=None, rajOption=None):
        self.successCase = {'pedra': ['lagarto', 'tesoura'],
                            'papel': ['pedra', 'spock'],
                            'tesoura': ['papel', 'lagarto'],
                            'lagarto': ['spock', 'papel'],
                            'spock': ['tesoura', 'pedra']}
        self.attemptCounter = 0
        self.MAX_ATTEMPTS = None
        self.sheldonOption = sheldonOption
        self.rajOption = rajOption

    def checkMaxAttempts(self, maxAttempts):
        if maxAttempts.isnumeric():
            self.MAX_ATTEMPTS = int(maxAttempts)
        else:
            maxAttempts = input('Invalid Number, Digite a novamente a quantidade de casos que deseja tentar:')
            return self.checkMaxAttempts(maxAttempts)
        if self.MAX_ATTEMPTS > 100:
            self.MAX_ATTEMPTS = 100
            print('Seu número de tentativas ultrapassou o limite, reformatamos o limite para 100')

    def handlingInputErrors(self):
        if self.sheldonOption and self.rajOption not in self.successCase:
            options = input('Entradas inválidas, Digite novamente suas opções: ')
            self.separateOptions(options)
            return self.handlingInputErrors()
        return True

    def checkTieCase(self):
        if self.sheldonOption == self.rajOption:
            print(f'Caso #{self.attemptCounter}: De novo!')
            return True
        return False

    def checkSuccessCase(self):
        if self.rajOption in self.successCase[self.sheldonOption]:
            print(f'Caso #{self.attemptCounter}: Bazinga!')
            return True
        else:
            print(f'Caso #{self.attemptCounter}: Raj trapaceou!')
            return False

    def separateOptions(self, options):
        separateOptions = options.split()
        self.sheldonOption = separateOptions[0].lower()
        self.rajOption = separateOptions[1].lower()

    def checkAttempts(self):

        if self.attemptCounter < self.MAX_ATTEMPTS:
            self.enterOptions()
            self.handlingInputErrors()

            if self.checkTieCase():
                return self.checkAttempts()
            elif self.checkSuccessCase():
                return self.checkAttempts()
            else:
                return self.checkAttempts()
        else:
            print('Você ultrapassou o máximo de tentativas!')

    def enterOptions(self):
        options = input('Digite suas opções: ')
        self.separateOptions(options)
        self.attemptCounter += 1


def main():
    sheldonGame = SheldonGame()
    print('--------------------GAME---------------------')
    print('Pedra - Papel - Tesoura - Lagarto - Spock')
    print()
    attempts = input('Digite a quantidade de casos que deseja tentar: ')
    sheldonGame.checkMaxAttempts(attempts)
    sheldonGame.checkAttempts()


if __name__ == '__main__':
    main()
