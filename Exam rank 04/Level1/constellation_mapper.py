"""
Write a function that maps a constellation of stars onto a grid
and returns the visual representation as a list of strings.

Your function must be declared as follows:

def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:

The function should:
- Take a list of star coordinates as tuples (row, col)
    and grid size as integer
- Return a list of strings representing the grid
- Stars are represented by '*' and empty spaces by '.'
- Grid coordinates start from (0, 0) at top-left
- Ignore coordinates outside the grid boundaries
- Handle duplicate coordinates (star appears only once)

Examples:

Input: constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)
Output: ['*..', '.*.', '..*']

Input: constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3)
Output: ['.*.', '***', '.*.']

Input: constellation_mapper([], 2)
Output: ['..', '..']

Input: constellation_mapper([(0, 0), (0, 0), (1, 1)], 2)
Output: ['*.', '.*']

Input: constellation_mapper([(0, 0), (5, 5)], 3)
Output: ['*..', '...', '...']

Input: constellation_mapper([(1, 0), (1, 1), (1, 2)], 3)
Output: ['...', '***', '...']
"""


def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    star_set = set(stars)
    return ["".join("*" if (r, c) in star_set else "." for c in range(size))
            for r in range(size)]


print("['*..', '.*.', '..*']" == f"{constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)}")
print("['.*.', '***', '.*.']" == f"{constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3)}")
print("['..', '..']" == f"{constellation_mapper([], 2)}")
print("['*.', '.*']" == f"{constellation_mapper([(0, 0), (0, 0), (1, 1)], 2)}")
print("['*..', '...', '...']" == f"{constellation_mapper([(0, 0), (5, 5)], 3)}")
print("['...', '***', '...']" == f"{constellation_mapper([(1, 0), (1, 1), (1, 2)], 3)}")
