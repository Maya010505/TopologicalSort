import random


def generate_acyclic_graph_file(filename, numberV, numberE):
    def creates_cycle(listE, v1, v2):

        visitedV = set()

        def dfs(vertex):
            visitedV.add(vertex)
            for neighbor in [v for u, v in listE if u == vertex]:
                if neighbor == v2 or (neighbor not in visitedV and dfs(neighbor)):
                    return True
            return False

        return dfs(v1)

    listV = list(range(1, numberV + 1))
    listE = []

    while len(listE) < numberE:
        v1 = random.choice(listV)
        v2 = random.choice(listV)
        if v1 != v2 and (v1, v2) not in listE:
            if creates_cycle(listE, v1, v2):
                raise ValueError("Добавление ребра ({}, {}) создает цикл".format(v1, v2))
            listE.append((v1, v2))

    with open(filename, "w") as f:
        f.write(f"{numberV} {numberE}\n")
        for e in listE:
            f.write(f"{e[0]} {e[1]}\n")


i = 1
while i < 51:
    filename = "test" + str(i) + ".txt"
    numberV = random.randint(100, 4000)
    numberE = random.randint(round(numberV / 1.5), round(numberV * 1.5))
    try:
        generate_acyclic_graph_file(filename, numberV, numberE)
        i += 1
    except ValueError:
        continue
