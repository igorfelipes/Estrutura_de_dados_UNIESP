class Schedule:

    def __init__(self):
        self.arrayFriends = []
        self.arrayBirthday = []

    def insertFriend(self, name, birthday):

        if name in self.arrayFriends:
            return print("Contato já cadastrado!")

        self.arrayFriends.append(name)
        self.arrayBirthday.append(birthday)
        return print("Contato salvo com sucesso!")

    def deleteFriend(self, name=None, position=999):

        if name is None and position == 999:
            return print("Contato já excluído ou não existe")

        if name is not None:
            if name not in self.arrayFriends:
                return print("Contato já excluído ou não existe")
            index = self.arrayFriends.index(name)
            self.arrayFriends.remove(name)
            self.arrayBirthday.pop(index)

        if position != 999:
            self.arrayFriends.pop(position)
            self.arrayBirthday.pop(position)

        return print("Deletado com sucesso! ")

    def printSchedule(self):
        print()
        try:
            for i in range(len(self.arrayFriends)+1):
                print(self.arrayFriends[i], ':',  self.arrayBirthday[i])
        except IndexError:
            print()


def main():
    schedule = Schedule()

    loop = True

    while loop:
        print("----------------------- AGENDA --------------------------------")
        print('1- Adicionar contato')
        print('2- Deletar contato')
        print('3- Visualizar')
        print('4- Sair')
        option = input('Digite a sua opção: ')

        if option == '1':
            name = input('Digite o nome do contato: ')
            date = input('Digite a data de aniversário do contato: ')

            validateDate = schedule.insertFriend(name, date)
            if validateDate is False:
                print('Utilize datas como por exemplo: 06/01/99 , 07/03/79, seguindo este formato dd/mm/aa')
                print('Você irá voltar ao menu principal...')
                print()
                continue

        if option == '2':
            contato = input('Digite o nome do contato ou a posição: ')
            schedule.deleteFriend(position=int(contato)) if contato.isnumeric() else schedule.deleteFriend(name=contato)

        if option == '3':
            schedule.printSchedule()

        if option == '4':
            break

        print()
        print('Deseja adicionar mais algum contato ou visualizar sua agenda? ')
        print('1-SIM')
        print('2-NÃO')
        print('Obs: qualquer tecla será considerado como Não')
        loop = input('Digite a sua opção: ')

        if loop == '1':
            continue
        else:
            loop = False


if __name__ == '__main__':
    main()
