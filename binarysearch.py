def maxCalcTimesBinarySearch(N):
    """
    @param N: int 1 ~ N Your search area
    @return : int The maximum times of calculation of binary search with N
    """
    if N == 1:
        return 0
    elif N // 2 == 1:
        return 1
    else:
        return 1 + maxCalcTimesBinarySearch(N // 2 + N % 2)
