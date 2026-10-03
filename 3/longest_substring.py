def length_of_longest_substring(s: str) -> int:
    max_len = 0
    start = 0
    chars = {}

    for end in range(len(s)):
        if s[end] in chars:
            start = max(start, chars[s[end]] + 1)

        chars[s[end]] = end
        max_len = max(max_len, end - start + 1)

    return max_len
