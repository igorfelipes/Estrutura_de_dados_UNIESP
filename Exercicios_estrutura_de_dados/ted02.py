def calcMetabolico(pesoMetabolico, k_const_group, flagId):
    flags = {"e": 0.25, "b": 0.75}

    k_constants = {
                     1: 129,
                     2: 78,
                     3: 70,
                     4: 49,
                     5: 10
    }

    return (pesoMetabolico ** flags[flagId]) * k_constants[k_const_group]


def main():
    pesoAnimal = float(input("Digite o peso do animal em quilogramas: "))
    groupId = int(input("Digite o codigo do grupo ao qual esse animal pertence: "))
    input_flag = input("Digite 'e' para saber a taxa metabolica especifica e 'b' para taxa metabolica basaal: ")

    print("TME:" if input_flag == 'e' else "TMB:", end='')
    print(' %.2f' % calcMetabolico(pesoAnimal, groupId, input_flag))


if __name__ == '__main__':
    main()
