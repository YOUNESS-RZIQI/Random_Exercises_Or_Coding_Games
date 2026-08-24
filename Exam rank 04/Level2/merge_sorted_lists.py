# """
# Solutions

# 1) The Algorithmic Upgrade (if imports were allowed):
# Using a Min-HeapIf your exam allows you to import standard
# Python libraries, the absolute best tool for merging
# $K$ sorted lists is heapq.
# Instead of sorting everything at the end,
# heapq.merge looks at the first element of each list,
# picks the smallest one, and moves forward.
# This drops the time complexity down to $O(N \\log K)$
# (where $K$ is the number of lists), which is significantly
# faster for massive datasets.

# Solution:
# import heapq

# def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
#     if not lists:
#         return []

#     # heapq.merge takes unpacked lists and merges them on the fly
#     # It returns an iterator, so we wrap it in list()
#     return list(heapq.merge(*lists))



# 2) Optimization (without extra imports)
# Even if you have to sort at the end,
# you can drastically speed up your flattening process.
# In Python, looping through items one-by-one with .append() is slow.
# Using .extend() pushes the looping down to the C-level,
# which executes much faster.
# Chosen solution below:
# """


# def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
#     if not lists:
#         return []

#     temp_list: list[int] = []
#     for item in lists:
#         # for n in item:
#         #   temp_list.append(n) - very slow solution
#         # use extend()
#         temp_list.extend(item)

#     return sorted(temp_list)

"""
Write a function that merges multiple sorted lists
into one sorted list while maintaining the sort order efficiently.

Your function must be declared as follows:

def merge_sorted_lists(lists: list[list[int]]) -> list[int]:

The function should:
- Take a list of sorted integer lists as input
- Return a single merged list in ascending order
- Preserve all duplicate elements in the final result
- Handle empty lists and empty input gracefully
- Maintain optimal efficiency for large inputs

Rules:
- All input lists are guaranteed to be sorted in ascending order
- Empty lists should be ignored during merging
- Return empty list if no valid input is provided
- Preserve duplicates across different lists
- Handle negative numbers correctly

Examples:

Input: merge_sorted_lists([[1, 3, 5], [2, 4, 6]])
Output: [1, 2, 3, 4, 5, 6]

Input: merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]])
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

Input: merge_sorted_lists([[5], [1, 3], [2, 4]])
Output: [1, 2, 3, 4, 5]

Input: merge_sorted_lists([[1, 1, 2], [2, 3, 3]])
Output: [1, 1, 2, 2, 3, 3]

Input: merge_sorted_lists([[], [1, 2, 3]])
Output: [1, 2, 3]

Input: merge_sorted_lists([])
Output: []

Input: merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]])
Output: [-5, -3, -1, 0, 2, 4]

Input: merge_sorted_lists([[10], [10], [10]])
Output: [10, 10, 10]

Edge cases to handle:
- Empty input list: return empty list
- Lists containing only empty lists: return empty list
- Single list input: return copy of that list
- All duplicate elements: preserve all instances
- Negative numbers: handle correctly in sort order
"""



print(f"[1, 2, 3, 4, 5, 6] : {merge_sorted_lists([[1, 3, 5], [2, 4, 6]])}")
print(
    "[1, 2, 3, 4, 5, 6, 7, 8, 9] : "
    f"{merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]])}")
print(f"[1, 2, 3, 4, 5] : {merge_sorted_lists([[5], [1, 3], [2, 4]])}")
print(f"[1, 1, 2, 2, 3, 3] : {merge_sorted_lists([[1, 1, 2], [2, 3, 3]])}")
print(f"[1, 2, 3] : {merge_sorted_lists([[], [1, 2, 3]])}")
print(f"[] : {merge_sorted_lists([])}")
print("[-5, -3, -1, 0, 2, 4] : "
      f"{merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]])}")
print(f"[10, 10, 10] : {merge_sorted_lists([[10], [10], [10]])}")
