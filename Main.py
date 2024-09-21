"""You are given a non-empty, zero-indexed array A of n (1 � n � 100 000) integers
a0, a1, . . . , an−1 (0 � ai � 1 000). This array represents number of mushrooms growing on the
consecutive spots along a road. You are also given integers k and m (0 � k, m < n).
A mushroom picker is at spot number k on the road and should perform m moves. In
one move she moves to an adjacent spot. She collects all the mushrooms growing on spots
she visits. The goal is to calculate the maximum number of mushrooms that the mushroom
picker can collect in m moves.
For example, consider array A such that:
2 3 7 5 1 3 9
0 1 2 3 4 5 6
The mushroom picker starts at spot k = 4 and should perform m = 6 moves. She might
move to spots 3, 2, 3, 4, 5, 6 and thereby collect 1 + 5 + 7 + 3 + 9 = 25 mushrooms. This is the
maximal number of mushrooms she can collect."""

from typing import List


def prefix_sums(A: List[int]) -> List[int]:
    n = len(A)
    P = [0] * n
    P[0] = A[0]

    for i in range(1, n):
        P[i] = P[i - 1] + A[i]

    return P


def count_total(pref: List[int], left: int, right: int) -> int:
    if left > right:
        return 0
    return pref[right] - (pref[left - 1] if left > 0 else 0)


def mushrooms(A: List[int], k: int, m: int) -> int:
    n = len(A)
    result = 0
    pref = prefix_sums(A)

    # Picking mushrooms from the left
    for p in range(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        result = max(result, count_total(pref, left_pos, right_pos))

    # Picking mushrooms from the right
    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, count_total(pref, left_pos, right_pos))

    return result


A = [2, 3, 7, 5, 1, 3, 9]
k = 4
m = 6
print(mushrooms(A, k, m))
