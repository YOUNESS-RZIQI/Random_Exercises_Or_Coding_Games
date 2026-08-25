# def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
#     if not lists:
#         return []

#     temp_list: list[int] = []
#     for item in lists:
#         temp_list.extend(item)

#     return sorted(temp_list)

"""
Write a function that merges multiple sorted lists
into one sorted list while maintaining the sort order efficiently.

Your function must be declared as follows:

def merge_sorted_lists(lists: list[list[int]]) -> list[int]:

The function should:
- Take a list of sorted integer lists as input
- Return a single merged list in     order
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

def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    merged = []
    for ls in lists:
        merged.extend(ls)
    merged.sort()
    return merged


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
