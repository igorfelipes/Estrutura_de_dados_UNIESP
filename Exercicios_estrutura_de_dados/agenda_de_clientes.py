"""
Crie um dicionário que será a agenda de clientes que compraram fiado na bodega de dona Chica.
Essa agenda contém três informações principais: nome, o quanto deve em reais, telefone e endereço. Crie interações que façam:
a - O cadastro dos clientes
b - A atualização dos valores em dívida
c - A remoção dos clientes que não devem mais
d - Uma busca por nome
"""


class Bodega:
    def __init__(self):
        self.agenda = {
            'José': {'divida': '2341,00', 'telefone': '(83) 98888-9999', 'endereco': 'Rua pedro freire'}

        }
        self.nome = 'Padrao'

    def clienteIsValid(self):
        if not self.buscarCliente():
            return False
        else:
            return True

    def cadastrarCliente(self):
        nome = input('Digite o nome do usuário: ')
        divida = input('Digite o valor da dívida: ')
        telefone = input('Digite o número do telefone: ')
        endereco = input('Digite o endereco do devedor: ')

        self.agenda[nome] = {'divida': divida, 'telefone': telefone, 'endereco': endereco}
        print(f'Cliente {nome} cadastrado com sucesso')

    def atualizarDivida(self):
        self.setName()
        if not self.clienteIsValid():
            return False
        else:
            cliente, dados = self.buscarCliente()
            dados['divida'] = input('Digite o novo valor da dívida: ')

    def removerCliente(self):
        self.setName()
        if not self.clienteIsValid():
            return False
        else:
            cliente, dados = self.buscarCliente()
            del(self.agenda[cliente])
            print(f'Cliente {cliente} deletado com sucesso!')

    def buscarCliente(self):
        try:
            for cliente, dados in self.agenda.items():
                if self.nome == cliente:
                    return cliente, dados
            else:
                print('Cliente não encontrado ou não cadastrado!')
                return False

        except:
            print('Cliente não encontrado ou não cadastrado!')
            return False

    def showCliente(self):
        self.setName()
        if not self.buscarCliente():
            return False
        else:
            cliente, dados = self.buscarCliente()
            print('Nome: ', cliente)
            for key, value in dados.items():
                print(key, ':', value)
                
    def setName(self):
        nome = input('Digite o nome do devedor: ')
        self.nome = nome
        return self.nome
        


def main():
    loop = True
    bodega = Bodega()
    while loop:
        print('----------------------- SERASA DA DONA CHICA-------------------------')
        print('1.Cadastrar Novo devedor   2. Consultar Cliente   3. Atualizar Divida do Cliente   4. Remover Devedor ')
        choice = input('Digite sua opção: ')
        if choice == '1':
            bodega.cadastrarCliente()
        elif choice == '2':
            bodega.showCliente()
        elif choice == '3':
            bodega.atualizarDivida()
        elif choice == '4':
            bodega.removerCliente()
        else:
            print('Opção inválida, tente novamente!')
            continue


if __name__ == '__main__':
    main()
