# """
# Solution strategy:

# """

# # Strategy A: The Blank Canvas (List of Lists)
# # This approach focuses on building the grid in memory,
# # updating the specific coordinates, and then formatting it
# # at the very end.


# def constellation_mapper_canvas(
#         stars: list[tuple[int, int]], size: int) -> list[str]:

#     # Prep the canvas
#     canvas: list[list] = []
#     for _ in range(size):
#         canvas.append(['.'] * size)

#     # Paint the starts
#     for row, col in stars:
#         if row >= 0 and row < size and col >= 0 and col < size:
#             canvas[row][col] = '*'
#             # duplicate coordinates overwite safely each other

#     # Format output
#     final_result: list = []
#     for raw_list in canvas:
#         final_result.append(''.join(raw_list))

#     return final_result


# """
# Strategy B: The Scanner (Row by Row)
# This approach focuses on generating the final strings directly
# by asking "Should this specific pixel be a star or a dot?"
# as it scans across the grid.
# """


# def constellation_mapper_scanner(
#         stars: list[tuple[int, int]], size: int) -> list[str]:

#     # Optimize the stars by using a set,
#     # to remove duplicates and for instant lookups

#     star_set = set(stars)

#     # Scan the grid and build strings

#     final_result: list = []

#     for row in range(size):
#         current_row: str = ""
#         for col in range(size):
#             if (row, col) in star_set:
#                 current_row += '*'
#             else:
#                 current_row += '.'
#         final_result.append(current_row)
#     return final_result



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

    # ignore cords outside grid !
    # skeep duplicates.

    table = [["." for _ in range(size)] for _ in range(size)]

    

    return table


for row in constellation_mapper([(0, 0), (1, 1), (2, 2)], 3):
    for i in range(3):
        print(row[i] + " ", end="")
    print()

# print(
#     "canvas: ['*..', '.*.', '..*'] : "
#     f"{constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)}")
# print(
#     "canvas: ['.*.', '***', '.*.'] : " 
#     f"{constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3)}")
# print(
#     "canvas: ['..', '..'] : "
#     f"{constellation_mapper([], 2)}")
# print(
#     "canvas: ['*.', '.*'] : "
#     f"{constellation_mapper([(0, 0), (0, 0), (1, 1)], 2)}")
# print(
#     "canvas: ['*..', '...', '...'] : "
#     f"{constellation_mapper([(0, 0), (5, 5)], 3)}")
# print(
#     "canvas: ['...', '***', '...'] : "
#     f"{constellation_mapper([(1, 0), (1, 1), (1, 2)], 3)}")

