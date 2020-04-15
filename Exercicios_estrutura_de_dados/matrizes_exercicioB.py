def main():
    matriz = [[39, 14, 27],
              [21, 83, 92],
              [21, 83, 43]]

    matrizVezesSete = [[number * 7for number in array] for array in matriz]
    print(matrizVezesSete)


if __name__ == '__main__':
    main()
