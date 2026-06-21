def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """

    # iterate over string
    seen = {}
    curr_max, curr_len, curr_idx = 0, 0, 0
    for i, c in enumerate(s):
        # print(f'{c}, {seen}, {curr_len}, {curr_max}')
        
        # if seen twice, reset
        if c in seen:
            tmp_idx = seen[c]
            curr_len -= (tmp_idx+1 - curr_idx)
            for j in range(curr_idx, tmp_idx+1):
                seen.pop(s[j])
            curr_idx = tmp_idx+1

        curr_len += 1
        seen[c] = i # store char x index in dict

        # print(f'{c}, {seen}, {curr_len}, {curr_max}')
        if curr_len > curr_max:
            curr_max = curr_len
    
    return curr_max

print(lengthOfLongestSubstring(None, "abba"))