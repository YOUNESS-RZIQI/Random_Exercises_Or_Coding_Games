# def list_intersection_finder_set(lists: list[list[int]]) -> list[int]:
#     # edge case - no input
#     if not lists:
#         return []

#     # use 1st list as the base for intersection
#     running_set = set(lists[0])

#     # iterate through other lists
#     for current_list in lists[1:]:
#         # create new set out of next list
#         current_set = set(current_list)

#         # update the running intersection
#         running_set = running_set.intersection(current_set)

#         # guard rails
#         if not running_set:
#             return []

#     final_list = list(running_set)
#     return sorted(final_list)


# def list_intersection_finder_pointer(lists: list[list[int]]) -> list[int]:
#     # edge case
#     if not lists:
#         return []

#     # set starting point
#     running_result: list = []
#     for num in lists[0]:
#         if not running_result or running_result[-1] != num:
#             running_result.append(num)
#             # running_result[-1] != num: For all subsequent numbers,
#             # this checks the last item in our new list ([-1]).
#             # If the current num is different from the last thing
#             # we added, it is a new, unique number, so we append it.
#             # If they are the same, it is a duplicate,
#             # so the if statement fails and we move on.

#     # compare running_result against other lists
#     for current_list in lists[1:]:
#         temp_intersection: list = []
#         a: int = 0
#         b: int = 0
#         while a < len(running_result) and b < len(current_list):
#             val_A = running_result[a]
#             val_B = current_list[b]
#             if val_A == val_B:
#                 if not temp_intersection or temp_intersection[-1] != val_A:
#                     temp_intersection.append(val_A)
#                 a += 1
#                 b += 1
#             elif val_A < val_B:
#                 # val_A is smaller, move it forward
#                 a += 1
#             else:
#                 b += 1
#         running_result = temp_intersection
#     return running_result



"""
Write a function that finds the intersection of
multiple sorted lists.
Return a new list containing elements that appear in
ALL input lists, in sorted order.

Your function must be declared as follows:

def list_intersection_finder(lists: list[list[int]]) -> list[int]:

The function should:
- Return elements that appear in ALL lists
- Result should be sorted in ascending order
- Remove duplicates from the result
- Handle empty input or empty lists gracefully
- If any list is empty, the intersection is empty

Examples:

Input: list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]])
Output: [2, 3]

Input: list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]])
Output: [4]

Input: list_intersection_finder([[1, 2, 3], [4, 5, 6]])
Output: []

Input: list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]])
Output: [1, 2, 3]

Input: list_intersection_finder([])
Output: []

Input: list_intersection_finder([[1, 2, 3], []])
Output: []

Input: list_intersection_finder([[5]])
Output: [5]
"""

print("set [2, 3] : "
      f"{list_intersection_finder_set(
          [[1, 2, 3], [2, 3, 4], [2, 3, 5]])}")
print("set [4] : "
      f"{list_intersection_finder_set(
          [[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]])}")
print("set [] : "
      f"{list_intersection_finder_set([[1, 2, 3], [4, 5, 6]])}")
print("set [1, 2, 3] : "
      f"{list_intersection_finder_set(
          [[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]])}")
print(f"set [] : {list_intersection_finder_set([])}")
print(f"set [] : {list_intersection_finder_set([[1, 2, 3], []])}")
print(f"set [5] : {list_intersection_finder_set([[5]])}")


print("\n\npointer [2, 3] : "
      f"{list_intersection_finder_pointer(
          [[1, 2, 3], [2, 3, 4], [2, 3, 5]])}")
print("pointer [4] : "
      f"{list_intersection_finder_pointer(
          [[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]])}")
print("pointer [] : "
      f"{list_intersection_finder_pointer([[1, 2, 3], [4, 5, 6]])}")
print("pointer [1, 2, 3] : "
      f"{list_intersection_finder_pointer(
          [[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]])}")
print("pointer [] : "
      f"{list_intersection_finder_pointer([])}")
print("pointer [] : "
      f"{list_intersection_finder_pointer([[1, 2, 3], []])}")
print("pointer [5] : "
      f"{list_intersection_finder_pointer([[5]])}")
