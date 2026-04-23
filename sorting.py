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

if __name__ == "__main__":
    values = random_numbers(20)
    print(values)
    test = [5, 1, 4, 2, 8]
    print(selection_sort(random_numbers(20)))
    print(selection_sort(test))
