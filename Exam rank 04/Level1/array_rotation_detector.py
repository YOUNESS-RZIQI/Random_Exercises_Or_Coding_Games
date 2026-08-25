# def array_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
#     if arr1 is None and arr2 is None:
#         return True
#     elif arr1 == arr2:
#         return True
#     elif len(arr1) != len(arr2):
#         return False

#     n: int = len(arr1)

#     # range from 1, because -0 is error and omits arr2
#     for i in range(1, n):
#         if (arr1[-i:] + arr1[:-i]) == arr2:
#             return True
#     return False




"""
Write a function that determines if one array is a rotation
of another array.
A rotation means the array has been shifted circularly left
or right.

Your function must be declared as follows:

def array_rotation_detector(arr1: list[int], arr2: list[int])
-> bool:

The function should:
- Check if arr2 is a rotation of arr1
- Handle arrays of different lengths (return False)
- Handle empty arrays (two empty arrays are rotations)
- A rotation can be 0 positions (same array)
- Consider both left and right rotations

Examples:

Input: array_rotation_detector([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
Output: True

Input: array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3])
Output: True

Input: array_rotation_detector([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
Output: True

Input: array_rotation_detector([1, 2, 3, 4, 5], [2, 3, 4, 5, 1])
Output: True

Input: array_rotation_detector([1, 2, 3], [1, 3, 2])
Output: False

Input: array_rotation_detector([1, 2, 3], [1, 2])
Output: False

Input: array_rotation_detector([], [])
Output: True

Input: array_rotation_detector([1, 1, 1], [1, 1, 1])
Output: True
"""


def array_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
    if len(arr1) != len((arr2)):
        return False
    if (not arr1 and not arr2) or arr1 == arr2:
        return True
    n = len(arr1)
    new_arr = arr1 + arr1
    for i in range(n):
        if new_arr[i:i+n] == arr2:
            return True
    return False



print(f"True: {array_rotation_detector([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])}")
print(f"True: {array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3])}")
print(f"True: {array_rotation_detector([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])}")
print(f"True: {array_rotation_detector([1, 2, 3, 4, 5], [2, 3, 4, 5, 1])}")
print(f"False: {array_rotation_detector([1, 2, 3], [1, 3, 2])}")
print(f"False: {array_rotation_detector([1, 2, 3], [1, 2])}")
print(f"True: {array_rotation_detector([], [])}")
print(f"True: {array_rotation_detector([1, 1, 1], [1, 1, 1])}")
