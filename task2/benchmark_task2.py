import timeit
from task2 import CircularBufferList, CircularBufferDeque
from typing import Union


def test1(buffer: Union[CircularBufferList, CircularBufferDeque]) -> None:
    # Test initialization
    buffer.size()
    buffer.is_empty()
    buffer.is_full()

    # Test enqueue
    for i in range(1, 201):
        buffer.enqueue(i)
        buffer.size()
        buffer.is_empty()
        buffer.is_full()

    # Test dequeue
    for i in range(1, 201):
        buffer.dequeue()
        buffer.size()
        buffer.is_empty()
        buffer.is_full()


buffer1 = CircularBufferList(205)
buffer2 = CircularBufferDeque(205)

print(
    timeit.timeit(
        "test1(buffer1)",
        number=100000,
        globals={"test1": test1, "buffer1": buffer1, "buffer2": buffer2},
    )
)
print(
    timeit.timeit(
        "test1(buffer2)",
        number=100000,
        globals={"test1": test1, "buffer1": buffer1, "buffer2": buffer2},
    )
)
