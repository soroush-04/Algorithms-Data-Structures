from __future__ import annotations
from typing import List, Optional


# ----
def sort_bubble(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


print(sort_bubble([2, 5, 5, 1, 4, 8, -3]))


# ----
def sort_selection(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print(sort_selection([2, 5, 5, 1, 4, 8, -3]))


# ----
def sort_insertion(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

    return arr


print(sort_insertion([2, 5, 5, 1, 4, 8, -3]))


# ----
def sort_merge(arr):
    n = len(arr)

    if n == 1:
        return arr

    middle = n // 2

    left = arr[:middle]
    right = arr[middle:]

    left = sort_merge(left)
    right = sort_merge(right)

    l, r = 0, 0

    m = 0
    merged = [0] * n

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged[m] = left[l]
            l += 1
        else:
            merged[m] = right[r]
            r += 1
        m += 1

    while l < len(left):
        merged[m] = left[l]
        l += 1
        m += 1

    while r < len(right):
        merged[m] = right[r]
        r += 1
        m += 1

    return merged


print(sort_merge([2, 5, 5, 1, 4, 8, -3]))


# ----
def sort_quick(arr):
    n = len(arr)

    if n <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    left = sort_quick(left)
    right = sort_quick(right)

    return left + [pivot] + right


print(sort_quick([2, 5, 5, 1, 44, 8, -3]))


# ----
def sort_counting(arr):
    k = max(arr)
    counts = [0] * (k + 1)

    for i in range(len(arr)):
        counts[arr[i]] += 1

    i = 0
    for c in range(len(counts)):
        while counts[c] > 0:
            arr[i] = c
            counts[c] -= 1
            i += 1

    return arr


print(sort_counting([2, 5, 5, 1, 14, 2]))
