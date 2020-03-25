def createArrayCountries():
    arrayCountries = []
    sizeArray = int(input("Digite a quantidade de Países que deseja armazenar: "))
    for size in range(sizeArray):
        arrayCountries.append(input("Digite o nome do %dº país: " % (size + 1)))
    return arrayCountries


def createArrayCities():
    arrayCities = []
    sizeArray = int(input("Digite a quantidade de cidades que deseja armazenar: "))
    for size in range(sizeArray):
        arrayCities.append(input("Digite o nome da %dª cidade: " % (size + 1)))
    return arrayCities


def main():
    countries = createArrayCountries()
    cities = createArrayCities()
    print(countries)
    print(cities)


if __name__ == '__main__':
    main()
