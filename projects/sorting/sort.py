from timeit import timeit
from queue import Queue
from typing import TypeVar, Callable
import random
import math

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


def merge_sort_iterative_queue(arr: list[T]) -> list[T]:
    q = Queue()
    for i in range(len(arr)):
        q.put((i, i + 1))

    ax = arr.copy()

    while q.qsize() > 1:
        (start_a, end_a) = q.get()
        if end_a - start_a == 2:
            if arr[start_a] > arr[end_a - 1]:
                arr[start_a], arr[end_a - 1] = arr[end_a - 1], arr[start_a]

        if end_a == len(arr):
            q.put((start_a, end_a))
            continue

        (start_b, end_b) = q.get()
        if end_b - start_b == 2:
            if arr[start_b] > arr[end_b - 1]:
                arr[start_b], arr[end_b - 1] = arr[end_b - 1], arr[start_b]

        i, j = start_a, start_b
        k = start_a

        while i < end_a and j < end_b:
            if arr[i] <= arr[j]:
                ax[k] = arr[i]
                i += 1
            elif arr[i] > arr[j]:
                ax[k] = arr[j]
                j += 1
            k += 1

        while i < end_a:
            ax[k] = arr[i]
            i += 1
            k += 1

        while j < end_b:
            ax[k] = arr[j]
            j += 1
            k += 1

        arr[start_a:end_b] = ax[start_a:end_b]
        q.put((start_a, end_b))

    return arr


def merge_sort_iterative_stack(arr: list[T]) -> list[T]:
    s = [(0, len(arr) // 2, len(arr))]
    i = 0
    while i < len(s):
        (lo, mid, hi) = s[i]
        if (lo, mid, hi) == (lo, lo, lo + 1):
            i += 1
            continue

        s.append((lo, (lo + mid) // 2, mid))
        s.append((mid, (mid + hi) // 2, hi))
        i += 1

    ax = arr.copy()
    for (lo, mid, hi) in reversed(s):
        if hi - lo == 1:
            continue
        elif hi - lo == 2:
            if arr[lo] > arr[lo + 1]:
                arr[lo], arr[lo + 1] = arr[lo + 1], arr[lo]
            continue

        i, j = lo, mid
        k = lo

        while i < mid and j < hi:
            if arr[i] <= arr[j]:
                ax[k] = arr[i]
                i += 1
            elif arr[i] > arr[j]:
                ax[k] = arr[j]
                j += 1
            k += 1

        while i < mid:
            ax[k] = arr[i]
            i += 1
            k += 1

        while j < hi:
            ax[k] = arr[j]
            j += 1
            k += 1

        arr[lo:hi] = ax[lo:hi]
    return arr


def merge_sort_iterative_none(arr: list[T]) -> list[T]:
    ax = arr.copy()

    def merge(lo, mid, hi):
        a, b = lo, mid
        k = lo

        while a < mid and b < hi:
            if arr[a] <= arr[b]:
                ax[k] = arr[a]
                a += 1
            elif arr[a] > arr[b]:
                ax[k] = arr[b]
                b += 1
            k += 1

        while a < mid:
            ax[k] = arr[a]
            a += 1
            k += 1

        while b < hi:
            ax[k] = arr[b]
            b += 1
            k += 1

        arr[lo:hi] = ax[lo:hi]

    i = 1
    while i < len(arr):
        for j in range(0, len(arr) - 1, 2*i):
            lo, hi = j, min(j + 2*i, len(arr))
            mid = min(lo + i, hi)
            merge(lo, mid, hi)
        i *= 2

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
    ints = generate_random_integers(20)
    return list(sorted(ints)) == sorting_fn(ints)


if __name__ == '__main__':
    sort = merge_sort_iterative_none
    print(f'{str(sort)}')
    print(f'Fast Test Result: {fast_test(sort)}')
    print(time_sort(10000, sort))
