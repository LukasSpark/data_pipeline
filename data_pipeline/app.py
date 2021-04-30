import pipeline as pp

FILE_NAME = 'techcrunch.csv'


def main():
    result = pp.load_data(FILE_NAME)
    for dict_ in result:
        print("=> ", dict_)


if __name__ == "__main__":
    main()
x = 2