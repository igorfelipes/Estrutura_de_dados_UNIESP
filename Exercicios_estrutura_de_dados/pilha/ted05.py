from pilha import Pilha


def testaMaisElementos(pilha1, pilha2):
    if len(pilha1.getPilha()) > len(pilha2.getPilha()):
        return True
    else:
        return False

def main():
    pilha1 = Pilha()
    pilha2 = Pilha()

    elementosPilha1 = ['elemento1', 'elemento2', 'elemento3']
    elementosPilha2 = ['elemento1', 'elemento2', 'elemento3', 'elemento4', 'elemento5']

    [pilha1.pushPilha(elemento) for elemento in elementosPilha1]
    [pilha2.pushPilha(elemento) for elemento in elementosPilha2]

    print('Pilha 1 > Pilha 2') if testaMaisElementos(pilha1, pilha2) else print('Pilha 2 > Pilha 1')


if __name__ == '__main__':
    main()