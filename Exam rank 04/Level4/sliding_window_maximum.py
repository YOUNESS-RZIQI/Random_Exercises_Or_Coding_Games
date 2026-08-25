"""
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that finds the maximum element in
each sliding window of size k in an array.
Return a list of maximums for each window position.

Your function must be declared as follows:

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:

The function should:
- Slide a window of size k through the array
- Find the maximum element in each window position
- Return a list of maximum values
- Handle edge cases (empty array, k <= 0, k > array length)
- Return empty list for invalid inputs

Examples:

Input: sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
Output: [3, 3, 5, 5, 6, 7]

Input: sliding_window_maximum([1, 2, 3, 4, 5], 2)
Output: [2, 3, 4, 5]

Input: sliding_window_maximum([5, 4, 3, 2, 1], 1)
Output: [5, 4, 3, 2, 1]

Input: sliding_window_maximum([1, 2, 3], 3)
Output: [3]

Input: sliding_window_maximum([1, 2, 3], 4)
Output: []

Input: sliding_window_maximum([], 2)
Output: []

Input: sliding_window_maximum([1, 2, 3], 0)
Output: []
"""


def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return []

    return [max(nums[i : i + k]) for i in range(len(nums) - k + 1)]



print("[3, 3, 5, 5, 6, 7]" == f"{sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)}")

print("[2, 3, 4, 5]" == f"{sliding_window_maximum([1, 2, 3, 4, 5], 2)}")

print("[5, 4, 3, 2, 1]" == f"{sliding_window_maximum([5, 4, 3, 2, 1], 1)}")


print("[3]" == f"{sliding_window_maximum([1, 2, 3], 3)}")

print("[]" == f"{sliding_window_maximum([1, 2, 3], 4)}")

print("[]" == f"{sliding_window_maximum([], 2)}")

print("[]" == f"{sliding_window_maximum([1, 2, 3], 0)}")
