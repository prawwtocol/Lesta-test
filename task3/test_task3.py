import task3
import random
from typing import Any


def test_empty_list() -> None:
    assert task3.timsort([]) == []


def test_single_element() -> None:
    assert task3.timsort([1]) == [1]


def test_two_elements_fwd() -> None:
    assert task3.timsort([1, 2]) == [1, 2]


def test_two_elements_bck() -> None:
    assert task3.timsort([2, 1]) == [1, 2]


def test_multiple_elements() -> None:
    assert task3.timsort([1, 2, 6, 4]) == [1, 2, 4, 6]
    assert task3.timsort([4, 3, 2, 1]) == [1, 2, 3, 4]  # Reverse sorted
    assert task3.timsort([1, 3, 2, 4]) == [1, 2, 3, 4]  # Unsorted
    assert task3.timsort([1, 1, 1, 1]) == [1, 1, 1, 1]  # All same elements
    assert task3.timsort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]  # Already sorted
    assert task3.timsort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]  # Reverse sorted
    assert task3.timsort([1, 2, 3, 5, 4]) == [1, 2, 3, 4, 5]  # Unsorted
    assert task3.timsort([1, 1, 2, 2, 3, 3]) == [
        1,
        1,
        2,
        2,
        3,
        3,
    ]  # Sorted with duplicates
    assert task3.timsort([3, 2, 1, 1, 2, 3]) == [
        1,
        1,
        2,
        2,
        3,
        3,
    ]  # Reverse sorted with duplicates
    assert task3.timsort([2, 2, 1, 1, 3, 3]) == [
        1,
        1,
        2,
        2,
        3,
        3,
    ]  # Unsorted with duplicates
    assert task3.timsort([5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == [
        1,
        1,
        2,
        2,
        3,
        3,
        4,
        4,
        5,
        5,
    ]  # Mixed

    # Test cases with large input
    assert task3.timsort(list(range(1000, 0, -1))) == list(
        range(1, 1001)
    )  # Reverse sorted
    assert task3.timsort(list(range(1, 1001))) == list(
        range(1, 1001)
    )  # Already sorted
    assert task3.timsort([1] * 1000) == [1] * 1000  # All same elements

    # Test cases with negative numbers
    assert task3.timsort([-4, -3, -2, -1]) == [
        -4,
        -3,
        -2,
        -1,
    ]  # Reverse sorted
    assert task3.timsort([-1, -3, -2, -4]) == [-4, -3, -2, -1]  # Unsorted
    assert task3.timsort([-1, -1, -1, -1]) == [
        -1,
        -1,
        -1,
        -1,
    ]  # All same elements
    assert task3.timsort([-1, -2, -3, -4, -5]) == [
        -5,
        -4,
        -3,
        -2,
        -1,
    ]  # Already sorted
    assert task3.timsort([-5, -4, -3, -2, -1]) == [
        -5,
        -4,
        -3,
        -2,
        -1,
    ]  # Reverse sorted
    assert task3.timsort([-1, -2, -3, -5, -4]) == [
        -5,
        -4,
        -3,
        -2,
        -1,
    ]  # Unsorted
    assert task3.timsort([-1, -1, -2, -2, -3, -3]) == [
        -3,
        -3,
        -2,
        -2,
        -1,
        -1,
    ]  # Sorted with duplicates
    assert task3.timsort([-3, -2, -1, -1, -2, -3]) == [
        -3,
        -3,
        -2,
        -2,
        -1,
        -1,
    ]  # Reverse sorted with duplicates
    assert task3.timsort([-2, -2, -1, -1, -3, -3]) == [
        -3,
        -3,
        -2,
        -2,
        -1,
        -1,
    ]  # Unsorted with duplicates
    assert task3.timsort([-5, -4, -3, -2, -1, -1, -2, -3, -4, -5]) == [
        -5,
        -5,
        -4,
        -4,
        -3,
        -3,
        -2,
        -2,
        -1,
        -1,
    ]  # Mixed


def sort_rand_array(n: int = 10000) -> bool:
    random_array = random.sample(range(-10 * n, 10 * n), n)
    return task3.timsort(random_array) == sorted(random_array)


def test_random_elements_l() -> None:
    assert sort_rand_array(1000)


def test_random_elements_xl() -> None:
    assert sort_rand_array(10000)


def test_random_elements_xxl() -> None:
    assert sort_rand_array(50000)


def test_benchmark(benchmark: Any) -> None:
    benchmark(sort_rand_array, 40000)
