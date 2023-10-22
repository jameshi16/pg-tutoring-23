from timeit import timeit
from typing import TypeVar, Callable
import random

T = TypeVar('T')

# Sorting methods


def bubble_sort(arr: list[T]) -> list[T]:
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
    return arr


def insertion_sort(arr: list[T]) -> list[T]:
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr


def selection_sort(arr: list[T]) -> list[T]:
    for i in range(len(arr)):
        min_ind, min_num = min(enumerate(arr[i:]), key=lambda x: x[1])
        arr[i], arr[min_ind + i] = arr[min_ind + i], arr[i]
    return arr


def merge_sort(arr: list[T]) -> list[T]:
    if len(arr) == 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    a = merge_sort(arr[:len(arr) // 2])
    b = merge_sort(arr[len(arr) // 2:])
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[i + j] = a[i]
            i += 1
        elif a[i] > b[j]:
            arr[i + j] = b[j]
            j += 1

    while i < len(a):
        arr[i + j] = a[i]
        i += 1

    while j < len(b):
        arr[i + j] = b[j]
        j += 1

    return arr


def quick_partition(arr: list[T]) -> T:
    i = 1
    j = len(arr) - 1

    while i < j:
        while i < len(arr) - 1 and arr[i] <= arr[0]:
            i += 1

        while j > 0 and arr[j] >= arr[0]:
            j -= 1

        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]

    arr[0], arr[j] = arr[j], arr[0]
    return j


def quick_sort(arr: list[T]) -> list[T]:
    if len(arr) == 0 or len(arr) == 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    k = quick_partition(arr)

    a = quick_sort(arr[:k])
    b = quick_sort(arr[k + 1:])

    return a + [arr[k]] + b


# Helper functions

def generate_random_integers(n: int) -> list[int]:
    res = [random.randint(-9999, 9999) for _ in range(n)]
    return res


def time_sort(n: int, sorting_fn: Callable[[list[T]], list[T]]) -> float:
    ints = generate_random_integers(n)
    return timeit(lambda: sorting_fn(ints),
                  number=5, globals=globals())


def fast_test(sorting_fn: Callable[[list[T]], list[T]]) -> bool:
    """
    Checks if the sorting function is sane
    """
    ints = generate_random_integers(10)
    return list(sorted(ints)) == sorting_fn(ints)


if __name__ == '__main__':
    sort = quick_sort
    print(f'{str(sort)}')
    print(f'Fast Test Result: {fast_test(sort)}')
    print(time_sort(10000, sort))
