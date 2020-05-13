from pilha import Pilha

def main():
    pilha = Pilha()

    string = input('Digite as caracters que deseja inserir na pilha: ')

    [pilha.pushPilha(c)for c in string]
    print(pilha.getPilha())


if __name__ == '__main__':
    main()
