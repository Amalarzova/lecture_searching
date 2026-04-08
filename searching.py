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

import time
import matplotlib.pyplot as plt
from generators import ordered_sequence


def measure_time(funkce, *argumenty):
    start = time.perf_counter()
    funkce(*argumenty)
    end= time.perf_counter()

    return end - start

def main():
    velikosti = [100, 500, 1000, 5000,  10000 ]

    casy_linear=[]
    casy_binary=[]

    for n in velikosti:
        seznam_cisel = ordered_sequence(n)
        hledane_cislo = seznam_cisel[-1]

        cas_linear = measure_time(linear_search, seznam_cisel, hledane_cislo)
        casy_linear.append(cas_linear)

        cas_binary = measure_time(binary_search, seznam_cisel, hledane_cislo)
        casy_binary.append(cas_binary)

        print(len(velikosti))
        print(len(casy_linear))
        print(len(casy_binary))

        plt.plot(velikosti, casy_linear, label="lineqarni vyhledavani")
        plt.plot(velikosti, casy_binary, label= "binarni vyhledavani")

        plt.xlabel("Velikost vstupu")
        plt.ylabel("Čas [s]")
        plt.title("mereni casu behem algoritmu")
        plt.legend()
        plt.show()






if __name__ == "__main__":
    main()