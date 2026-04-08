from pathlib import Path
import json



def read_data(file_name, field):
    path = Path(__file__).parent / file_name
    with open(file_name, "r") as f:
        data = json.load(f)

        if field not in data:
            return None

    return data[field]

def main():
    sequential_data = read_data("sequential.json","unordered_numbers" )
    print(sequential_data)





def linear_search(seznam, hledane_cislo):
    pozice = []
    pocet = 0

    for i, hodnota in enumerate(seznam):
        if hodnota == hledane_cislo:
            pozice.append(i)
            pocet += 1

    return {
        "positions" : pozice,
        "count" : pocet
    }

def main():
    seznam = read_data("sequential.json","unordered_numbers")
    hledane_cislo = 5
    vysledek = linear_search(seznam, hledane_cislo)
    print(vysledek)


def binary_search(seznam_cisel, hledane_cislo):
    levy = 0
    pravy = len(seznam_cisel) -1

    while levy <= pravy:
        stred = (levy + pravy) // 2

        if seznam_cisel[stred] == hledane_cislo:
            return stred

        elif seznam_cisel[stred] < hledane_cislo:
            levy += 1
        else:
            pravy = stred - 1

    return None

def main():
    seznam_cisel =  read_data("sequential.json","ordered_numbers")
    hledane_cislo = 45
    index = binary_search(seznam_cisel, hledane_cislo)

    print(index)
if __name__ == "__main__":
    main()