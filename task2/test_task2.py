import pytest
from task2 import CircularBufferList, CircularBufferDeque
from typing import Any


def test_circular_buffer_list() -> None:
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
