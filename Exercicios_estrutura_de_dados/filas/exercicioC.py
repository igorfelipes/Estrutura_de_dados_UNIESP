from filaLib import Infos


def main():

    values = ['UNIESP', 'ED', '2020.1', 'João Pessoa', 'Estágio 2']
    infos = Infos()

    print('Antes: ', infos.getInfos())

    [infos.insertInfo(value) for value in values]
    print('Depois: ', infos.getInfos())


if __name__ == '__main__':
    main()
