"""
This module provides a Python implementation of the Timsort algorithm.

The module contains a main function `timsort` which sorts an input list
using the Timsort algorithm.

It also contains a helper class `TimsortHelper` which provides methods
for generating runs, merging runs, and sorting the input list using the
Timsort algorithm.
"""

from typing import List, Tuple
import copy


def timsort(arr: List[int]) -> List[int]:
    """
    Sorts the input list using the timsort algorithm.

    The timsort algorithm is a hybrid sorting algorithm derived from
    merge sort and insertion sort.
    It is designed to perform well on many kinds of real-world data.

    Args:
        arr: A list of integers to be sorted.

    Returns:
        The sorted list.
    """
    return TimsortHelper(arr).sort()


class TimsortHelper:
    """
    Helper class for performing timsort algorithm.

    This class provides methods for generating runs, merging runs,
    and sorting the input list using the timsort algorithm.

    Args:
        arr: A list of integers to be sorted.

    Attributes:
        arr: The input list to be sorted.
        arr_len: The length of the input list.
        stack: A stack to store information about runs.
        min_run: The minimum run size for timsort algorithm.
    """

    def __init__(self, arr: List[int]) -> None:
        self.arr = arr
        self.arr_len = len(arr)
        self.stack: List[Tuple[int, int]] = []
        self.min_run = self.get_min_run()

    def get_min_run(self) -> int:
        """
        Returns the minimum run size for timsort algorithm.

        The minimum run size is calculated based on the length
        of the input list.
        It is used as a parameter in the timsort algorithm.

        Returns:
            The minimum run size.
        """
        # Implementation details:
        # https://web.archive.org/web/20160128232837/https://hg.python.org/cpython/file/tip/Objects/listsort.txt
        bit_cardinality = 0
        N = self.arr_len
        while N >= 64:
            bit_cardinality |= N & 1
            N >>= 1
        return N + bit_cardinality

    def generate_run(self, start_index: int) -> int:
        """
        Generates a run in the input list.

        A run is a subsequence of the input list that is already sorted.
        This function generates a run starting from the given index
        and returns the next index to start generating the next run.

        Args:
            start_index: The starting index of the run.

        Returns:
            The next index to start generating the next run.
        """
        run = []

        run_start_index, run_end_index = start_index, start_index + 1
        rsi, rei = run_start_index, run_end_index

        is_ascending = self.arr[start_index] <= self.arr[start_index + 1]
        keep_going = True
        while keep_going:
            run.append(self.arr[start_index])
            rei += 1
            if not (start_index + 1 < self.arr_len) or not (
                (self.arr[start_index] <= self.arr[start_index + 1])
                == is_ascending
            ):
                keep_going = False
            start_index += 1
        if not is_ascending:
            self.arr[rsi:rei] = self.arr[rsi:rei][::-1]

        if len(run) < self.min_run:
            rei = min(self.arr_len, rsi + self.min_run)
            start_index = min(
                self.arr_len, start_index + self.min_run - len(run)
            )

        self.arr[rsi:rei] = sorted(self.arr[rsi:rei])
        self.stack.append((rsi, rei - rsi))
        return start_index

    def merge_runs(
        self, p1: int, l1: int, p2: int, l2: int
    ) -> Tuple[int, int]:
        """
        Merges two runs in the input list.

        This function merges two runs in the input list and
        returns the starting index and length of the merged run.

        Args:
            p1: The starting index of the first run.
            l1: The length of the first run.
            p2: The starting index of the second run.
            l2: The length of the second run.

        Returns:
            A tuple containing the starting index and length of the merged run.
        """
        if p1 > p2:
            p1, l1, p2, l2 = p2, l2, p1, l1

        # copy leftmost array to tmp arr
        tmp_arr = copy.deepcopy(self.arr[p1 : p1 + l1])

        # main pointer iterates over arr, overwriting it with
        # min(tmp_arr[lp],self.arr[rp])
        main_pointer = p1

        # save p1 position to push on stack later
        saved_p1 = p1

        # left_pointer iterates over the leftmost run
        left_pointer = 0
        lp = left_pointer
        # right_pointer iterates over the rightmost run
        right_pointer = p2
        rp = right_pointer
        while lp < l1 and rp - p2 < l2:
            if tmp_arr[lp] > self.arr[rp]:
                self.arr[main_pointer] = self.arr[rp]
                rp += 1
                main_pointer += 1
            else:
                self.arr[main_pointer] = tmp_arr[lp]
                lp += 1
                main_pointer += 1

        a1 = tmp_arr[lp:]
        a2 = self.arr[rp : p2 + l2]
        for a in a1:
            self.arr[main_pointer] = a
            main_pointer += 1
        for a in a2:
            self.arr[main_pointer] = a
            main_pointer += 1

        # push new stack info onto stack
        return (saved_p1, l1 + l2)

    def sort(self) -> List[int]:
        """
        Sorts the input list using the timsort algorithm.

        Returns:
            The sorted list.
        """
        if self.arr_len <= 1:
            # Nothing to sort
            return self.arr

        # Go with pointer from left to right to divide arr in runs:
        pointer = 0
        while pointer < self.arr_len:
            pointer = self.generate_run(pointer)

            if len(self.stack) > 2:
                xp, x = self.stack[-1]
                yp, y = self.stack[-2]
                zp, z = self.stack[-3]
                if not (x > y + z) or not (y > z):
                    if x < z:
                        self.stack.pop()
                        self.stack.pop()
                        self.stack.append(self.merge_runs(yp, y, xp, x))
                    else:
                        self.stack.pop(-3)
                        self.stack.pop(-2)
                        self.stack.append(self.merge_runs(yp, y, zp, z))

            if len(self.stack) > 1:
                xp, x = self.stack[-1]
                yp, y = self.stack[-2]
                if not y > x:
                    self.stack.pop()
                    self.stack.pop()
                    self.stack.append(self.merge_runs(yp, y, xp, x))

        if len(self.stack) > 1:
            xp, x = self.stack[-1]
            yp, y = self.stack[-2]
            self.stack.pop()
            self.stack.pop()
            self.stack.append(self.merge_runs(yp, y, xp, x))
        return self.arr
