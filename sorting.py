import random
import matplotlib.pyplot as plt

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
    plt.ion()
    plt.show()
    for i in range(len(novy)):
        for j in range(0, len(novy)-1-i):
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(novy)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(novy)), novy, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if novy[j] > novy[j+1]:
                novy[j], novy[j+1] = novy[j+1], novy[j]
    plt.ioff()
    plt.show()
    return novy

if __name__ == "__main__":
    values = random_numbers(20)
    print(values)
    test = [5, 1, 4, 2, 8]
    print(selection_sort(random_numbers(20)))
    print(selection_sort(test))
    print(bubble_sort(test))
    print(selection_sort(random_numbers(20)))