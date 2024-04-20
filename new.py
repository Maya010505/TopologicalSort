import time


def inputGraph(filename):
    r = open(filename)
    n, m = map(int, r.readline().split())
    graph = {i + 1: set() for i in range(n)}
    for i in range(m):
        u, v = map(int, r.readline().split())
        graph[u].add(v)
    return graph


# Топологическая сортировка методом Тарьяна (работает эффективно при маленьких данных)
# def topologicalSort(v, graph, visitedV, sortedV):
#     for u in graph[v]:
#         if u not in visitedV:
#             topologicalSort(u, graph, visitedV, sortedV)
#     visitedV.add(v)
#     sortedV.append(v)


def topologicalSort(graph):
    degreeI = {v: 0 for v in graph}
    for v in graph:
        for adjacentV in graph[v]:
            degreeI[adjacentV] += 1

    stack = [v for v in graph if degreeI[v] == 0]
    sortedV = []

    iteration_count = 0
    while stack:
        iteration_count += 1
        node = stack.pop(0)
        sortedV.append(node)
        for adjacentV in graph[node]:
            degreeI[adjacentV] -= 1
            if degreeI[adjacentV] == 0:
                stack.insert(0, adjacentV)

    return sortedV, iteration_count


for i in range(1, 51):
    filename = "test" + str(i) + ".txt"

    graph = inputGraph(filename)

    start_time = time.perf_counter()

    sorted_V, iterations = topologicalSort(graph)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    # print(f"Тест {i}: {elapsed_time:.6f} секунд")
    # print(f"Тест {i}: {iterations} итераций")
    # print()

# Код ниже: Для топологической сортировки методом Тарьяна
    # sortedV = []
    # remainingV = set(range(1, len(graph) + 1))
    # visitedV = set()
    # while remainingV:
    #     v = remainingV.pop()
    #     topologicalSort(v, graph, visitedV, sortedV)
    #     remainingV -= visitedV
    # print(' '.join(map(str, sortedV[::-1])))
