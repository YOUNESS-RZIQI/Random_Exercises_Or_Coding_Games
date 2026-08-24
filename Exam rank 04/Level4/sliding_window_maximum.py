# def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
#     # edge cases
#     n = len(nums)
#     if n == 0 or k <= 0 or k > n:
#         return []

#     # slidig window of size k across the array
#     # valid start = n - k or
#     # valid range = range(n - k + 1)

#     result = []
#     for i in range(n - k + 1):
#         # extract current window chunk
#         window = nums[i:i+k]

#         # find max in window
#         max_value: int = max(window)
#         """
#         max_value: int = window[0]
#         for num in window:
#             if num > max_value:
#                 max_value = num
#         """
#         result.append(max_value)

#     return result


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

print("expected: [3, 3, 5, 5, 6, 7]")
print(f"output: {sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)}")

print("expected: [2, 3, 4, 5]")
print(f"output: {sliding_window_maximum([1, 2, 3, 4, 5], 2)}")

print("expected: [5, 4, 3, 2, 1]")
print(f"output: {sliding_window_maximum([5, 4, 3, 2, 1], 1)}")

print("expected: [3]")
print(f"output: {sliding_window_maximum([1, 2, 3], 3)}")

print("expected: []")
print(f"output: {sliding_window_maximum([1, 2, 3], 4)}")

print("expected: []")
print(f"output: {sliding_window_maximum([], 2)}")

print("expected: []")
print(f"output: {sliding_window_maximum([1, 2, 3], 0)}")
