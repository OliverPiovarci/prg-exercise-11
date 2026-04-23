class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, pocet):
        indexy = []
        for i in range(len(self.scores)):
            if self.scores[i] == pocet:
                indexy.append(i)
        return indexy

    def get_sorted(self):
        scores = self.scores.copy()
        for i in range(len(scores)):
            for j in range(0, len(scores) - 1- i):
                if scores[j] > scores[j+1]:
                    scores[j], scores[j+1] = scores[j+1], scores[j]

        return scores

from sorting import random_numbers

def main():
    vysledky = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print("Počet studentů:", vysledky.count())

    for i in range(vysledky.count()):
        points = vysledky.get_by_index(i)
        grade = vysledky.get_grade(i)
        print(f"Student {i}: {points} bodů–{grade}")

    print("Studenti se 100 body:", vysledky.find(100))
    print("Seřazené výsledky:", vysledky.get_sorted())
    print("Původní data:", vysledky.scores)
    print("Náhodná data")
    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print("Počet studentů:", random_results.count())
    print("Seřazené výsledky:", random_results.get_sorted())

if __name__ == "__main__":
    main()
    # results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    #
    # print(results.count())  # 9
    # print(results.get_by_index(2))  # 91
    # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]