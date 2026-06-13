"""PRACTICES/arrays.py

10 basic array (list) questions with simple, readable solutions.
Run: python PRACTICES/arrays.py
"""

from __future__ import annotations


def q1_sum_of_array(arr: list[int]) -> int:
    """Q1: Find the sum of all elements in an array."""
    return sum(arr)


def q2_find_max(arr: list[int]) -> int:
    """Q2: Find the maximum element in an array."""
    return max(arr)


def q3_find_min(arr: list[int]) -> int:
    """Q3: Find the minimum element in an array."""
    return min(arr)


def q4_reverse_array(arr: list[int]) -> list[int]:
    """Q4: Reverse an array."""
    return list(reversed(arr))


def q5_count_occurrences(arr: list[int], x: int) -> int:
    """Q5: Count occurrences of an element x."""
    return sum(1 for v in arr if v == x)


def q6_sort_array(arr: list[int]) -> list[int]:
    """Q6: Sort the array in ascending order."""
    return sorted(arr)


def q7_second_largest_distinct(arr: list[int]) -> int | None:
    """Q7: Find the second largest distinct element.

    Returns None if it doesn't exist.
    """
    distinct = sorted(set(arr))
    if len(distinct) < 2:
        return None
    return distinct[-2]


def q8_move_zeros_to_end(arr: list[int]) -> list[int]:
    """Q8: Move all zeros to the end while maintaining relative order of non-zero elements."""
    non_zeros = [v for v in arr if v != 0]
    zeros = [0] * (len(arr) - len(non_zeros))
    return non_zeros + zeros


def q9_remove_duplicates_preserve_order(arr: list[int]) -> list[int]:
    """Q9: Remove duplicates while preserving the original order."""
    seen = set()
    out = []
    for v in arr:
        if v not in seen:
            seen.add(v)
            out.append(v)
    return out


def q10_rotate_right(arr: list[int], k: int) -> list[int]:
    """Q10: Rotate array by k steps to the right."""
    n = len(arr)
    if n == 0:
        return []
    k %= n
    return arr[-k:] + arr[:-k]


if __name__ == "__main__":
    a = [1, 3, 0, 2, 3, 0, 4]
    x = 3

    print("Q1 Sum:", q1_sum_of_array(a))
    print("Q2 Max:", q2_find_max(a))
    print("Q3 Min:", q3_find_min(a))
    print("Q4 Reverse:", q4_reverse_array(a))
    print("Q5 Count", x, ":", q5_count_occurrences(a, x))
    print("Q6 Sorted:", q6_sort_array(a))
    print("Q7 Second largest distinct:", q7_second_largest_distinct(a))
    print("Q8 Zeros to end:", q8_move_zeros_to_end(a))
    print("Q9 Remove duplicates:", q9_remove_duplicates_preserve_order(a))
    print("Q10 Rotate right by 2:", q10_rotate_right(a, 2))

