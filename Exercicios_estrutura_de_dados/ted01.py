def calcMetabolico(pesoMetabolico, k_const_group):

    k_constants = {
                     1: 129,
                     2: 78,
                     3: 70,
                     4: 49,
                     5: 10
    }

    return (pesoMetabolico ** 0.75) * k_constants[k_const_group]


def main():
    pesoAnimal = float(input("Digite o peso do animal em quilogramas: "))
    print()
    groupId = int(input("Digite o codigo do grupo ao qual esse animal pertence: "))

    print("TMB: %.2f" % calcMetabolico(pesoAnimal, groupId))


if __name__ == '__main__':
    main()
