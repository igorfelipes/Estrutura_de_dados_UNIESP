class SheldonGame:
    def __init__(self, sheldonOption=None, rajOption=None):
        self.successCases = {'pedra': ['lagarto', 'tesoura'],
                             'papel': ['pedra', 'spock'],
                             'tesoura': ['papel', 'lagarto'],
                             'lagarto': ['spock', 'papel'],
                             'spock': ['tesoura', 'pedra']}
        self.attemptCounter = 0
        self.MAX_ATTEMPTS = 100
        self.sheldonOption = sheldonOption
        self.rajOption = rajOption

    def tieCase(self, sheldonOption, rajOption):
        if sheldonOption == rajOption:
            print(f'Caso #{self.attemptCounter}: De novo!')
            options = input('Digite suas opções novamente: ')
            self.attemptCounter += 1
            return options

        return False

    def separateOptions(self, options):

        separateOptions = options.split()
        self.sheldonOption = separateOptions[0].lower()
        self.rajOption = separateOptions[1].lower()

    def checkAttempts(self):

        if self.attemptCounter < self.MAX_ATTEMPTS:

            returnTieCase = self.tieCase(self.sheldonOption, self.rajOption)

            if returnTieCase:
                options = returnTieCase
                self.separateOptions(options)
                return self.checkAttempts()

            if self.rajOption in self.successCases[self.sheldonOption]:
                return print(f'Caso #{self.attemptCounter}: Bazinga!')
            else:
                return print(f'Caso #{self.attemptCounter}: Raj trapaceuou!')
        else:
            print('Você ultrapassou o máximo de tentativas!')


def main():
    sheldonGame = SheldonGame()
    print('--------------------GAME---------------------')
    options = input('Digite suas opções: ')
    sheldonGame.separateOptions(options)
    sheldonGame.checkAttempts()


if __name__ == '__main__':
    main()