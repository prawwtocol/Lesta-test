"""
This module contains unit tests for the CircularBufferList
and CircularBufferDeque classes.

The CircularBufferList class is tested for its initialization,
enqueue, and dequeue methods.
The CircularBufferDeque class is also tested for its
initialization, enqueue, and dequeue methods.

Additionally, benchmark tests are included for both classes to measure
their performance.
"""

import pytest
from task2 import CircularBufferList, CircularBufferDeque
from typing import Any


def test_circular_buffer_list() -> None:
    """
    Test the functionality of the CircularBufferList class.

    This function tests the initialization, enqueue, and dequeue
    operations of the CircularBufferList class.
    It asserts various conditions to ensure that the CircularBufferList
    behaves as expected.
    """
    # Test initialization
    buffer = CircularBufferList(3)
    assert buffer.size() == 0
    assert buffer.is_empty() == True
    assert buffer.is_full() == False

    # Test enqueue
    buffer.enqueue(1)
    assert buffer.size() == 1
    assert buffer.is_empty() == False
    assert buffer.is_full() == False

    buffer.enqueue(2)
    assert buffer.size() == 2
    assert buffer.is_empty() == False
    assert buffer.is_full() == False

    buffer.enqueue(3)
    assert buffer.size() == 3
    assert buffer.is_empty() == False
    assert buffer.is_full() == True

    # Test dequeue
    assert buffer.dequeue() == 1
    assert buffer.size() == 2
    assert buffer.is_empty() == False
    assert buffer.is_full() == False

    assert buffer.dequeue() == 2
    assert buffer.size() == 1
    assert buffer.is_empty() == False
    assert buffer.is_full() == False

    assert buffer.dequeue() == 3
    assert buffer.size() == 0
    assert buffer.is_empty() == True
    assert buffer.is_full() == False

    # Test dequeue from empty buffer
    with pytest.raises(Exception):
        buffer.dequeue()


def test_circular_buffer_deque() -> None:
    """
    Test the functionality of the CircularBufferDeque class.

    This function tests the initialization, enqueue, and dequeue
    operations of the CircularBufferDeque class.
    It asserts various conditions to ensure that the CircularBufferDeque
    behaves as expected.
    """
    # Test initialization
    buffer = CircularBufferDeque(3)
    assert buffer.size() == 0
    assert buffer.is_empty() == True
    assert buffer.is_full() == False

    # Test enqueue
    buffer.enqueue(1)
    assert buffer.size() == 1
    assert buffer.is_empty() == False
    assert buffer.is_full() == False

    buffer.enqueue(2)
    assert buffer.size() == 2
    assert buffer.is_empty() == False
    assert buffer.is_full() == False

    buffer.enqueue(3)
    assert buffer.size() == 3
    assert buffer.is_empty() == False
    assert buffer.is_full() == True

    # Test dequeue
    assert buffer.dequeue() == 1
    assert buffer.size() == 2
    assert buffer.is_empty() == False
    assert buffer.is_full() == False

    assert buffer.dequeue() == 2
    assert buffer.size() == 1
    assert buffer.is_empty() == False
    assert buffer.is_full() == False

    assert buffer.dequeue() == 3
    assert buffer.size() == 0
    assert buffer.is_empty() == True
    assert buffer.is_full() == False

    # Test dequeue from empty buffer
    with pytest.raises(Exception):
        buffer.dequeue()


def test_bench_circular_buffer_list(benchmark: Any) -> None:
    """
    Test function for benchmarking the CircularBufferDeque class.
    """

    def test_circular_buffer_list_200() -> None:
        buffer = CircularBufferList(205)
        for i in range(1, 201):
            buffer.enqueue(i)
            buffer.size()
            buffer.is_empty()
            buffer.is_full()
        for i in range(1, 201):
            buffer.dequeue()
            buffer.size()
            buffer.is_empty()
            buffer.is_full()

    benchmark(test_circular_buffer_list_200)


def test_bench_circular_buffer_deque(benchmark: Any) -> None:
    """
    Test function for benchmarking the CircularBufferList class.
    """

    def test_circular_buffer_deque_200() -> None:
        buffer = CircularBufferDeque(205)
        for i in range(1, 201):
            buffer.enqueue(i)
            buffer.size()
            buffer.is_empty()
            buffer.is_full()
        for i in range(1, 201):
            buffer.dequeue()
            buffer.size()
            buffer.is_empty()
            buffer.is_full()

    benchmark(test_circular_buffer_deque_200)
