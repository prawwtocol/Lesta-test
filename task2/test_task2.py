import pytest
from task2 import CircularBuffer, CircularBuffer2


def test_circular_buffer() -> None:
    # Test initialization
    buffer = CircularBuffer(3)
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


def test_circular_buffer2() -> None:
    # Test initialization
    buffer = CircularBuffer2(3)
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
