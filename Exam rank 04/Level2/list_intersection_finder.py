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


def list_intersection_finder_set(lists: list[list[int]]) -> list[int]:
      if not lists:
            return []
      if len(lists) == 1:
            return lists[0]

      # inter = set(lists[0].copy())

      # for num in lists[0]:
      #       for ls in lists:
      #             if num not in ls and num in inter:
      #                   inter.remove(num)

      # inter = list(inter)
      # inter.sort()
      # return inter
      inter = set()
      sets_list = [set(ls) for ls in lists]


      for st in sets_list[1:]:
            val = sets_list[0].intersection(st)
            for el in val:
                  inter.add(el)
      inter = list(inter)
      inter.sort()
      return inter



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


# print("\n\npointer [2, 3] : "
#       f"{list_intersection_finder_pointer(
#           [[1, 2, 3], [2, 3, 4], [2, 3, 5]])}")
# print("pointer [4] : "
#       f"{list_intersection_finder_pointer(
#           [[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]])}")
# print("pointer [] : "
#       f"{list_intersection_finder_pointer([[1, 2, 3], [4, 5, 6]])}")
# print("pointer [1, 2, 3] : "
#       f"{list_intersection_finder_pointer(
#           [[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]])}")
# print("pointer [] : "
#       f"{list_intersection_finder_pointer([])}")
# print("pointer [] : "
#       f"{list_intersection_finder_pointer([[1, 2, 3], []])}")
# print("pointer [5] : "
#       f"{list_intersection_finder_pointer([[5]])}")
