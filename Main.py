"""Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000]."""


def solution(A):
    seen = set(A)
    temp = 1

    while temp in seen:
        temp += 1

    return temp


array = [1, 5, 3, 2, 8, 7, 0]
print(solution(array))
