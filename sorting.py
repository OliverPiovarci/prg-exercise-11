import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(values):
    zoradeny = values.copy()
    for i in range(len(zoradeny)):
        minimum = i
        for j in range(i + 1, len(zoradeny)):
            if zoradeny[j] < zoradeny[minimum]:
                minimum = j

        zoradeny[i], zoradeny[minimum] = zoradeny[minimum], zoradeny[i]
    return zoradeny

def bubble_sort(seznam):
    novy = seznam.copy()
    for i in range(len(novy)):
        for j in range(0, len(novy)-1-i):
            if novy[j] > novy[j+1]:
                novy[j], novy[j+1] = novy[j+1], novy[j]
    return novy

if __name__ == "__main__":
    values = random_numbers(20)
    print(values)
    test = [5, 1, 4, 2, 8]
    print(selection_sort(random_numbers(20)))
    print(selection_sort(test))
    print(bubble_sort(test))
    print(selection_sort(random_numbers(20)))