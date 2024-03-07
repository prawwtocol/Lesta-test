

# it is timsort
from typing import List

# from numbers import Number


def getMinRun(arr: List[int]) -> int:
    return 32
    # r = 0
    # while n >= 64:
    #     r |= n & 1
    #     n >>= 1
    # return n + r


# todo generalize list int
def foo(arr: List[int], minrun: int) -> None:
    """
    Changes arr in place like timsort would
    """
    st = []

    if len(arr) <= 1:
        return

    def gen_run(arr: List[int], p1: int) -> int:
        p1_start = p1
        run = []

        run_start, run_end = -1, -1
        if arr[p1] <= arr[p1 + 1]:  # todo bug
            run_start = p1
            run_end = p1 + 1
            keep_going = True
            while keep_going:
                # Your code here
                run.append(arr[p1])

                run_end += 1  # run end points to el after last element in run
                if not (p1 + 1 < len(arr)) or not (arr[p1] <= arr[p1 + 1]):
                    keep_going = False
                p1 += 1
        else:
            run_start = p1
            run_end = p1 + 1

            keep_going = True
            while keep_going:
                # Your code here
                run.append(arr[p1])

                run_end += 1  # run end points to el after last element in run
                if not (p1 + 1 < len(arr)) or not (arr[p1] > arr[p1 + 1]):
                    keep_going = False
                p1 += 1
            arr[run_start:run_end] = arr[run_start:run_end][::-1]  # O(n)

        if len(run) < minrun:
            run_end = min(len(arr), run_start + minrun)
            # run += arr[p1 : p1 + minrun - len(run)]
            p1 = min(len(arr), p1 + minrun - len(run))
        # we get array `run` which is partly or totally ascending

        arr[run_start:run_end] = sorted(arr[run_start:run_end])
        # todo use insertion sort here, performs well on almost-sorted data
        st.append((p1_start, run_end - run_start))
        return p1

    # runs = [[]]

    import copy

    def timsort_merge(p1: int, l1: int, p2: int, l2: int) -> (int, int):

        if p1 > p2:
            p1, l1, p2, l2 = p2, l2, p1, l1
        # p_leftmost = p1 if p1 < p2 else p2
        p_leftmost = p1
        p1_start = p_leftmost
        # l1 is smaller array now
        tmp = copy.deepcopy(arr[p1 : p1 + l1])

        pt = 0  # pointer temporary
        pb = p2  # pointer biggfer
        while pt < l1 and pb - p2 < l2:
            if tmp[pt] > arr[pb]:
                arr[p_leftmost] = arr[pb]
                pb += 1
                p_leftmost += 1
            else:
                arr[p_leftmost] = tmp[pt]
                pt += 1
                p_leftmost += 1
        # copy remaining to
        a1 = tmp[pt :]
        a2 = arr[pb : p2 + l2]
        for a in a1:
            arr[p_leftmost] = a
            p_leftmost += 1
        for a in a2:
            arr[p_leftmost] = a
            p_leftmost += 1
        return (p1_start, l1 + l2)
        pass

    p = 0
    while p < len(arr):
        p = gen_run(arr, p)
        # todo fix

        # whenever hits 3 elements
        if len(st) > 2:
            xp, x = st[-1]
            yp, y = st[-2]
            zp, z = st[-3]
            if not (x > y + z) or not (y > z):
                # merge y with min(x,z)
                if x < z:
                    # pop y, x
                    # push new
                    st.pop()
                    st.pop()
                    st.append(timsort_merge(yp, y, xp, x))
                    # merge y with x

                else:
                    st.pop(-3)
                    st.pop(-2)
                    st.append(timsort_merge(yp, y, zp, z))
                    # merge y with z

        if len(st) > 1:
            xp, x = st[-1]
            yp, y = st[-2]
            if not y > x:
                st.pop()
                st.pop()
                st.append(timsort_merge(yp, y, xp, x))
                # merge x,y
    if len(st) > 1:
        # reempty stack to 1 element
        xp, x = st[-1]
        yp, y = st[-2]
        st.pop()
        st.pop()
        st.append(timsort_merge(yp, y, xp, x))
        # merge x,y


def timsort(arr: List[int]) -> List[int]:
    foo(arr, 32)
    return arr


def main() -> None:
    arr = [2, 1]
    minrun = getMinRun(arr)
    foo(arr, minrun)  # sorts arr inplace
    print(arr)


if __name__ == "__main__":
    main()
