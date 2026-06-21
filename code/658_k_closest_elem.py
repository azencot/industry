def findClosestElements(self, arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """

    # find x in arr or closest to it
    jj = -1
    if x < arr[0]:
        jj = 0
    elif x > arr[-1]:
        jj = len(arr) - 1
    else:
        last_dist = abs(x - arr[0])
        jj = 0
        for i in range(1, len(arr)):
            curr_dist = abs(x - arr[i])

            if curr_dist < last_dist:
                last_dist = curr_dist
                jj = i

            if curr_dist > last_dist:
                break

    # expand at most k neighbors around x
    jl, jr = jj, jj
    while jr+1-jl < k:
        print(f'{jl}, {jr}')

        if jl < 1:
            jr += 1
        elif jr+1 == len(arr):
            jl -= 1
        elif abs(arr[jl-1] - x) <= abs(arr[jr+1] - x):
            jl -= 1
        else:
            jr += 1

    return arr[jl:jr+1]

print(findClosestElements(None, [0,0,0,1,3,5,6,7,8,8], 2, 2))

        