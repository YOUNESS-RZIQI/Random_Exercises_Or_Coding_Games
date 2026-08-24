"""
My prepared solution 1:

def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:

Input: package_dependency_resolver({
    "app": ["database"],
    "database": ["driver"],
    "driver": []
})
Output: ["driver", "database", "app"]
# Dependencies: driver → database → app

"""


def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    if not packages or len(packages) == 0:
        return []

    graph: dict[str, list[str]] = {}
    indegrees: dict[str, int] = {}

    for pkg in packages:
        graph[pkg] = []
        indegrees[pkg] = 0

    for pkg, deps in packages.items():
        indegree_value: int = 0
        for dep in deps:
            if dep in packages:
                indegree_value += 1
                graph[dep].append(pkg)
        indegrees[pkg] = indegree_value

    queue: list = []
    for pkg in packages:
        if indegrees[pkg] == 0:
            queue.append(pkg)
    queue.sort()

    result: list = []

    while len(queue) > 0:
        next_queue: list = []
        for current in queue:
            result.append(current)
            for pkg in graph[current]:
                indegrees[pkg] -= 1
                if indegrees[pkg] == 0:
                    next_queue.append(pkg)
        next_queue.sort()
        queue = next_queue

    if len(result) == len(packages):
        return result
    else:
        return []


print("# Dependencies: driver → database → app")
res = package_dependency_resolver(
    {"app": ["database"],
     "database": ["driver"],
     "driver": []})
print("expected: [\"driver\", \"database\", \"app\"]")
print(f"output: {res}\n")

print("# A has no deps, B needs A, C needs both A and B")
res = package_dependency_resolver(
    {"A": [],
     "B": ["A"],
     "C": ["A", "B"]})
print("expected: [\"A\", \"B\", \"C\"]")
print(f"output: {res}\n")

print("# Empty input")
res = package_dependency_resolver({})
print("expected: []")
print(f"output: {res}\n")

print("# Circular dependency: X needs Y, Y needs X")
res = package_dependency_resolver(
    {"X": ["Y"],
     "Y": ["X"]})
print("expected: []")
print(f"output: {res}\n")

print("# Two independent chains: api→backend and web→frontend")
res = package_dependency_resolver(
    {"web": [],
     "api": [],
     "frontend": ["web"],
     "backend": ["api"]})
print("expected: [\"api\", \"web\", \"backend\", \"frontend\"]")
print(f"output: {res}")

print("# Multiple dependencies")
res = package_dependency_resolver(
    {
     "A": [],
     "B": [],
     "D": [],
     "E": [],
     "C": ["A", "B"],
     "F": ["D", "E"],
     "J": ["C", "F"],
     "P": ["J"]})
print("expected: [\"A\", \"B\", \"D\", \"E\", \"C\", \"F\", \"J\", \"P\"]")
print(f"output: {res}")
