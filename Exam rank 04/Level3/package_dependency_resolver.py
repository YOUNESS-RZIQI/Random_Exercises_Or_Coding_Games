"""
Write a function that determines a valid package installation order
by resolving dependencies.
Use topological sorting to ensure dependencies are installed
before the packages that require them.

Your function must be declared as follows:

def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:

The function should:
- Take a dictionary where keys are package names and
    values are lists of dependencies
- Return packages in installation order (dependencies first)
- Return empty list if no valid order exists (circular dependencies)
- Handle empty input and isolated dependency chains
- Ignore references to packages not in the input dictionary

Algorithm requirements:
- Use topological sorting (e.g., Kahn's algorithm)
- Process packages with no remaining dependencies first
- Ensure deterministic output when multiple valid orders exist

Examples:

Input: package_dependency_resolver({
    "app": ["database"],
    "database": ["driver"],
    "driver": []
})
Output: ["driver", "database", "app"]
# Dependencies: driver → database → app

Input: package_dependency_resolver({
    "A": [],
    "B": ["A"],
    "C": ["A", "B"]
})
Output: ["A", "B", "C"]
# A has no deps, B needs A, C needs both A and B

Input: package_dependency_resolver({})
Output: []
# Empty input

Input: package_dependency_resolver({
    "X": ["Y"],
    "Y": ["X"]
})
Output: []
# Circular dependency: X needs Y, Y needs X

Input: package_dependency_resolver({
    "web": [],
    "api": [],
    "frontend": ["web"],
    "backend": ["api"]
})
Output: ["api", "web", "backend", "frontend"]
# Two independent chains: api→backend and web→frontend

Edge cases to handle:
- Empty input: return empty list
- Packages with no dependencies: include in output first
- Multiple independent chains: process all chains
- Circular dependencies: return empty list
- Non-existent dependencies: ignore missing packages
- Self-dependencies: return empty list

Notes:
- For deterministic output, process packages alphabetically
    when choices exist
- A package cannot be installed until all its dependencies
    are installed
- If any circular dependency exists, no valid installation order
    is possible

Testing example:
python3 main.py
'{"app": ["database"], "database": ["driver"], "driver": []}'
# Expected output: driver database app

import json
packages = json.loads(
'{"app": ["database"], "database": ["driver"], "driver": []}')
result = package_dependency_resolver(packages)
print(' '.join(result))  # Output: driver database app
"""


def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    # 1. Filter out missing dependencies and self-dependencies
    deps = {
        p: [d for d in reqs if d in packages and d != p]
        for p, reqs in packages.items()
    }
    
    # 2. Return [] if self-dependencies exist
    if any(p in reqs for p, reqs in packages.items()):
        return []

    result = []
    
    # 3. Kahn's Algorithm loop
    while deps:
        # Find all packages with no remaining dependencies, sorted alphabetically
        ready = sorted([p for p, reqs in deps.items() if not reqs])
        
        if not ready:  # Cycle detected (no package can be processed)
            return []
            
        for p in ready:
            result.append(p)
            del deps[p]
            # Remove processed package from remaining dependencies
            for reqs in deps.values():
                if p in reqs:
                    reqs.remove(p)

    return result


# package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []})

print(["driver", "database", "app"] == package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}))

print(["A", "B", "C"] == package_dependency_resolver({"A": [],"B": ["A"],"C": ["A", "B"]}))

print([] == package_dependency_resolver({}))

print([] == package_dependency_resolver({"X": ["Y"],"Y": ["X"]}))

print(["api", "web", "backend", "frontend"] ==package_dependency_resolver({"web": [],"api": [],"frontend": ["web"],"backend": ["api"]}))
