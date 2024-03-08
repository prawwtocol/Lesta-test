from typing import List, Tuple
import copy


def get_min_run(n: int) -> int:
    """
    Returns the minimum run size for timsort algorithm.

    The minimum run size is calculated based on the length of the input list.
    It is used as a parameter in the timsort algorithm.

    Args:
        n: An integer representing the length of the input list.

    Returns:
        The minimum run size.

    """
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1

    return n + r


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
    min_run = get_min_run(len(arr))

    stack = []

    if len(arr) <= 1:
        return arr  # quit

    def gen_run(arr: List[int], p1: int) -> int:
        """
        Generates a run in the input list.

        A run is a subsequence of the input list that is already sorted.
        This function generates a run starting from the given index
        and returns the next index to start generating the next run.

        Args:
            arr: A list of integers.
            p1: The starting index of the run.

        Returns:
            The next index to start generating the next run.

        """
        p1_start = p1
        run = []

        run_start, run_end = -1, -1

        dir_ascending = arr[p1] <= arr[p1 + 1]
        run_start = p1
        run_end = p1 + 1
        keep_going = True
        while keep_going:
            run.append(arr[p1])
            run_end += 1
            if not (p1 + 1 < len(arr)) or not (
                (arr[p1] <= arr[p1 + 1]) == dir_ascending
            ):
                keep_going = False
            p1 += 1
        if not dir_ascending:
            arr[run_start:run_end] = arr[run_start:run_end][::-1]

        if len(run) < min_run:
            run_end = min(len(arr), run_start + min_run)
            p1 = min(len(arr), p1 + min_run - len(run))

        arr[run_start:run_end] = sorted(arr[run_start:run_end])
        stack.append((p1_start, run_end - run_start))
        return p1

    def timsort_merge(p1: int, l1: int, p2: int, l2: int) -> Tuple[int, int]:
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
        p_leftmost = p1
        p1_start = p_leftmost
        tmp = copy.deepcopy(arr[p1 : p1 + l1])

        pt = 0
        pb = p2
        while pt < l1 and pb - p2 < l2:
            if tmp[pt] > arr[pb]:
                arr[p_leftmost] = arr[pb]
                pb += 1
                p_leftmost += 1
            else:
                arr[p_leftmost] = tmp[pt]
                pt += 1
                p_leftmost += 1

        a1 = tmp[pt:]
        a2 = arr[pb : p2 + l2]
        for a in a1:
            arr[p_leftmost] = a
            p_leftmost += 1
        for a in a2:
            arr[p_leftmost] = a
            p_leftmost += 1
        return (p1_start, l1 + l2)

    p = 0
    while p < len(arr):
        p = gen_run(arr, p)

        if len(stack) > 2:
            xp, x = stack[-1]
            yp, y = stack[-2]
            zp, z = stack[-3]
            if not (x > y + z) or not (y > z):
                if x < z:
                    stack.pop()
                    stack.pop()
                    stack.append(timsort_merge(yp, y, xp, x))
                else:
                    stack.pop(-3)
                    stack.pop(-2)
                    stack.append(timsort_merge(yp, y, zp, z))

        if len(stack) > 1:
            xp, x = stack[-1]
            yp, y = stack[-2]
            if not y > x:
                stack.pop()
                stack.pop()
                stack.append(timsort_merge(yp, y, xp, x))

    if len(stack) > 1:
        xp, x = stack[-1]
        yp, y = stack[-2]
        stack.pop()
        stack.pop()
        stack.append(timsort_merge(yp, y, xp, x))
    return arr
