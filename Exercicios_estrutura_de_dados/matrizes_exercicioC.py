def main():
    matriz = [[39, 14, 27],
              [21, 83, 92],
              [21, 83, 43]]

    print('Matriz antiga: ', matriz)
    for array in matriz:
        array.pop()

    print('Matriz nova: ', matriz)


if __name__ == '__main__':
    main()
