# def is_polindrome(s: str) -> bool:
#     return s == s[::-1]


# def palindrome_partitioner(s: str) -> int:
#     # determine length of s
#     n: int = len(s)

#     # edge case
#     if n == 0:
#         return 0

#     # build worst-case min_cuts,
#     # assuming every single letter requires cut

#     min_cuts: list[int] = []
#     for i in range(n):
#         min_cuts.append(i)

#     for i in range(n):
#         for j in range(i + 1):
#             chunk: str = s[j:i+1]

#             if is_polindrome(chunk):
#                 # entire string is polindrome
#                 if j == 0:
#                     min_cuts[i] = 0
#                 else:
#                     pre_cuts: int = min_cuts[j - 1] + 1
#                     if pre_cuts < min_cuts[i]:
#                         min_cuts[i] = pre_cuts
#     return min_cuts[-1]

"""
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that finds the minimum number of cuts needed
to partition a string so that every substring is a palindrome.

Your function must be declared as follows:

def palindrome_partitioner(s: str) -> int:

The function should:
- Find minimum cuts to make all parts palindromes
- Return the number of cuts needed (not the number of parts)
- Handle empty strings (return 0)
- Single characters are palindromes
- Case-sensitive palindrome checking

Examples:

Input: palindrome_partitioner("aab")
Output: 1
# Cut: "a|ab" -> "a" and "ab" (but "ab" is not palindrome)
# Cut: "aa|b" -> "aa" and "b" (both palindromes) - 1 cut

Input: palindrome_partitioner("aba")
Output: 0
# "aba" is already a palindrome - 0 cuts

Input: palindrome_partitioner("abcba")
Output: 0
# "abcba" is already a palindrome - 0 cuts

Input: palindrome_partitioner("abcd")
Output: 3
# "a|b|c|d" -> 3 cuts needed

Input: palindrome_partitioner("aabaa")
Output: 0
# "aabaa" is already a palindrome - 0 cuts needed

Input: palindrome_partitioner("abac")
Output: 1
# "aba|c" -> 1 cut needed ("aba" and "c" are palindromes)

Input: palindrome_partitioner("")
Output: 0



Implementation - Dynamic Programming (DP)

2. The Solution Strategy: Dynamic Programming
To find the minimum cuts, we must try multiple combinations.
The easiest way to do this without getting lost in
complex recursion is to keep a running scoreboard of the best cuts
for every prefix of the string.

This is a classic technique called Dynamic Programming (DP).

Dynamic Programming (DP) is a computer science term that sounds
intimidating, but it essentially means solving a large, complex
problem by remembering the answers to its smaller subproblems so
you never have to calculate them twice.

A problem is solved using DP when it has two specific
characteristics, both of which are central to our
palindrome_partitioner() logic:

1. Overlapping Subproblems (The Need for Memory)
If you try to solve this problem without DP (a "brute force"
approach), the algorithm does massive amounts of repetitive work.

For example, to evaluate "abac", a brute-force algorithm might try
slicing off "a" and then calculating the cuts for "bac".
Later, it might slice off "ab" and calculate the cuts for "ac".
Notice that in both scenarios, it is evaluating the letter "c".
As the string gets longer, it calculates the exact same smaller
chunks hundreds or thousands of times.

DP fixes this by giving the algorithm a memory—our min_cuts array.
Once we calculated that "aba" takes exactly 0 cuts, we wrote it
down on the scoreboard. We never had to calculate "aba" from
scratch again.

2. Optimal Substructure (Building the Big Answer)
This means the absolute best solution for the entire string is
built directly by combining the absolute best solutions of its
smaller pieces.

When our loop reached the very end of "abac", it recognized that
"c" was a palindrome. To find the minimum cuts for the whole string,
 it didn't rethink the whole word. It simply asked: "What was the
 optimal score for everything that came right before 'c'?"

Python
# This single line is the essence of Dynamic Programming
min_cuts[i] = min_cuts[j - 1] + 1
It looked backwards into its memory at min_cuts[2]
(the optimal score for "aba"), saw that the score was 0,
and simply added 1.

Because the algorithm builds its final answer by dynamically
referencing a table of its own previously optimized answers,
it falls under the umbrella of Dynamic Programming.


Create a min_cuts list. min_cuts[i] will store the lowest number
of cuts needed for the substring from the beginning up to index i.

Assume the worst-case scenario first: s[0:i] requires i cuts (e.g.,
"abcd" requires 3 cuts).

Loop through the string. For every ending index i, look backwards
with a starting index j.

If the chunk between j and i is a palindrome, update the scoreboard.

"""

print(f"a = 0: {palindrome_partitioner("a")}")
print(f"ab = 1: {palindrome_partitioner("ab")}")
print(f"aba = 0: {palindrome_partitioner("aba")}")
print(f"aab = 1: {palindrome_partitioner("aab")}")
print(f"abcba = 0: {palindrome_partitioner("abcba")}")
print(f"abcd = 3: {palindrome_partitioner("abcd")}")
print(f"aabaa = 0: {palindrome_partitioner("aabaa")}")
print(f"abac = 1: {palindrome_partitioner("abac")}")
print(f"\"\" = 0: {palindrome_partitioner("")}")
