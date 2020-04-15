def main():
    matriz = [[39, 14, 27],
              [21, 83, 92],
              [21, 83, 43]]

    matrizVezesSete = [[number * 7 for number in array] for array in matriz]
    print(matrizVezesSete)

    # print([[number * 7 for number in array] for array in matriz])  - Metodo alternativo


if __name__ == '__main__':
    main()
