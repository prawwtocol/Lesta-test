from collections import deque
from typing import List, Any


class EmptyBufferError(Exception):
    """
    Exception raised when trying to dequeue from an empty buffer.
    """

    pass


class CircularBufferList:
    """
    Circular Buffer implementation with lists.

    This class provides a circular buffer data structure using a
    list as the underlying storage.
    The buffer has a fixed capacity and supports
    enqueue and dequeue operations.

    Attributes:
        buffer (List[Any]): The underlying list used to store the buffer items.
        capacity (int): The maximum number of items the buffer can hold.
        head (int): The index of the first item in the buffer.
        tail (int): The index where the next item will be added.
        occupancy (int): The number of items currently in the buffer.
    """

    def __init__(self, capacity: int):
        """
        Initialize the CircularBufferList with the given capacity.

        Args:
            capacity (int): The maximum number of items the buffer can hold.
        """
        self.buffer: List[Any] = [None] * capacity
        self.capacity: int = capacity
        self.head: int = 0
        self.tail: int = 0
        self.occupancy: int = 0

    def is_empty(self) -> bool:
        """
        Check if the buffer is empty.

        Returns:
            bool: True if the buffer is empty, False otherwise.
        """
        return self.occupancy == 0

    def is_full(self) -> bool:
        """
        Check if the buffer is full.

        Returns:
            bool: True if the buffer is full, False otherwise.
        """
        return self.occupancy == self.capacity

    def enqueue(self, item: Any) -> None:
        """
        Add an item to the buffer.

        Args:
            item (Any): The item to be added to the buffer.
        """
        if not self.is_full():
            self.occupancy += 1
        else:
            self.head = (self.head + 1) % self.capacity
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity

    def dequeue(self) -> Any:
        """
        Remove an item from the buffer and return its value.

        Returns:
            Any: The value of the item removed from the buffer.

        Raises:
            IndexError: If the buffer is empty.
        """
        if self.is_empty():
            raise EmptyBufferError("Trying to dequeue from empty buffer")
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.occupancy -= 1
        return item

    def size(self) -> int:
        """
        Return the current size of the buffer.

        Returns:
            int: The current size of the buffer.
        """
        return self.occupancy


class CircularBufferDeque:
    """
    Circular Buffer implementation with deques.

    This class provides a circular buffer data structure
    using a deque as the underlying storage.
    The buffer has a fixed capacity and supports
    enqueue and dequeue operations.

    Attributes:
        capacity (int): The maximum number of items the buffer can hold.
        buffer (deque[Any]): The underlying deque
            used to store the buffer items.
    """

    def __init__(self, capacity: int) -> None:
        """
        Initialize the CircularBufferDeque with the given capacity.

        Args:
            capacity (int): The maximum number of items the buffer can hold.
        """
        self.capacity = capacity
        self.buffer: deque[Any] = deque(maxlen=capacity)

    def enqueue(self, item: Any) -> None:
        """
        Add an item to the buffer.

        Args:
            item (Any): The item to be added to the buffer.
        """
        self.buffer.append(item)

    def dequeue(self) -> Any:
        """
        Remove an item from the buffer and return its value.

        Returns:
            Any: The value of the item removed from the buffer.

        Raises:
            IndexError: If the buffer is empty.
        """
        if self.is_empty():
            raise EmptyBufferError("Trying to dequeue from empty buffer")
        else:
            return self.buffer.popleft()

    def is_empty(self) -> bool:
        """
        Check if the buffer is empty.

        Returns:
            bool: True if the buffer is empty, False otherwise.
        """
        return self.size() == 0

    def is_full(self) -> bool:
        """
        Check if the buffer is full.

        Returns:
            bool: True if the buffer is full, False otherwise.
        """
        return self.size() == self.capacity

    def size(self) -> int:
        """
        Return the current size of the buffer.

        Returns:
            int: The current size of the buffer.
        """
        return len(self.buffer)
