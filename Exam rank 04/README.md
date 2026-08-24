*This project has been created as part of the 42 curriculum by dporhomo*

![42 School](https://img.shields.io/badge/42-school-black?style=for-the-badge)
![Grade](https://img.shields.io/badge/Grade-100%25%20%2F%20100%25-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python&logoColor=white)
![Date](https://img.shields.io/badge/Completed-21%20July%202026-purple?style=for-the-badge)

# Exam 04: Python Algorithmic Challenges

The core constraint of this exam was to solve complex algorithmic problems using **pure, procedural Python**—strictly avoiding external imports, advanced built-in functions (like `collections`, `itertools`, or `math`), and relying entirely on fundamental loops, list manipulations, and manual state tracking.

## 📂 Repository Structure

```text
.
├── Level1
│   ├── array_rotation_detector.py
│   └── constellation_mapper.py
├── Level2
│   ├── list_intersection_finder.py
│   └── merge_sorted_lists.py
├── Level3
│   ├── package_dependency_resolver.py
│   ├── package_dependency_resolver_clean.py
│   ├── package_dependency_resolver_program.py
│   └── palindrome_partitioner.py
└── Level4
    └── sliding_window_maximum.py

```

---

## 📝 Exercise Descriptions

### Level 1

* **`array_rotation_detector.py`**: An algorithm to determine the number of times a sorted array has been rotated, or to find the pivot point in a shifted sequence.
* **`constellation_mapper.py`**: A grid/matrix traversal algorithm to identify and map connected components (constellations) within a 2D space.

### Level 2

* **`list_intersection_finder.py`**: A memory-efficient solution to find common elements (intersections) between two lists with and without relying on Python's built-in `set` operations.
* **`merge_sorted_lists.py`**: Implements the merging phase of Merge Sort. It takes two pre-sorted lists and combines them into a single sorted list strictly using pointer manipulation.

### Level 3

* **`package_dependency_resolver*.py`**: A procedural implementation of Kahn's Algorithm for Topological Sorting. It resolves software dependencies by processing packages in "waves." It ensures that independent packages are processed in strict alphabetical order without relying on standard queue libraries like `collections.deque`. The `_program.py` version includes a CLI wrapper to parse JSON input from `sys.argv`.
* **`palindrome_partitioner.py`**: A Dynamic Programming (DP) solution that calculates the minimum number of cuts required to partition a string such that every resulting substring is a valid, case-sensitive palindrome. It uses a 1D DP array to memoize optimal cuts and avoid redundant checks.

### Level 4

* **`sliding_window_maximum.py`**: Calculates the maximum element in every sliding window of size `k` across an array. Handles all edge cases (empty arrays, zero size, window larger than array) and manually calculates maximums within sliced subarrays to strictly adhere to the "no built-in functions" rule.

---

## 🚀 Instructions

Ensure you have Python 3.13 installed. Since these are pure Python scripts with no external dependencies, they can be executed directly from the terminal.

### Running standard functions

For most scripts, simply execute the file to run the embedded test cases:

```bash
python3 Level4/sliding_window_maximum.py
python3 Level3/palindrome_partitioner.py

```

### Running CLI-enabled programs

For scripts designed to take command-line arguments (like the dependency resolver program), pass the required JSON string as an argument:

```bash
# Example with package dependency resolver
python3 Level3/package_dependency_resolver_program.py '{"app": ["database"], "database": ["driver"], "driver": []}'

```

*Expected Output: `driver database app*`

If run without arguments, the script will default to running a suite of built-in test cases for validation:

```bash
python3 Level3/package_dependency_resolver_program.py

```
