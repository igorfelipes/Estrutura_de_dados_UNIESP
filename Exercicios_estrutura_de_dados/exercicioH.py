def main():
    ages = []

    for i in range(5):
        ages.append(int(input('Digite o ano de nascimento: ')))

    ages.sort()
    print('Crescente: ', ages)
    ages.sort(reverse=True)
    print('Decrescente: ', ages)


if __name__ == "__main__":
    main()
