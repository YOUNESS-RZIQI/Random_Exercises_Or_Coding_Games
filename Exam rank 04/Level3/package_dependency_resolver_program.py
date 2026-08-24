import sys
import json


def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    if not packages or len(packages) == 0:
        return []

    graph: dict[str, list[str]] = {}
    indegrees: dict[str, int] = {}

    for pkg in packages:
        graph[pkg] = []
        indegrees[pkg] = 0

    for pkg, deps in packages.items():
        in_value: int = 0
        for dep in deps:
            if dep in packages:
                in_value += 1
                graph[dep].append(pkg)
        indegrees[pkg] = in_value

    queue = []

    res_list = []

    for pkg in packages:
        if indegrees[pkg] == 0:
            queue.append(pkg)
    queue.sort()

    while len(queue) > 0:
        next_queue = []
        for curr in queue:
            res_list.append(curr)
            for pkg in graph[curr]:
                indegrees[pkg] -= 1
                if indegrees[pkg] == 0:
                    next_queue.append(pkg)
        next_queue.sort()
        queue = next_queue

    if len(packages) == len(res_list):
        return res_list
    else:
        return []


if __name__ == "__main__":
    if len(sys.argv) == 2:
        raw_input = sys.argv[1]
        curr_dict = json.loads(raw_input)
        print(f"Received {curr_dict}")
        res = package_dependency_resolver(curr_dict)
        print(f"output: {" ".join(res)}\n")
    else:
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
