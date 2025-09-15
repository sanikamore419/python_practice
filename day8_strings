def firstUniqChar(s: str) -> int:
    freq = {}

    # Step 1: Count frequency of each character
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Step 2: Find first character with frequency 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1


# 🔹 Test Cases
print(firstUniqChar("leetcode"))      # 0
print(firstUniqChar("loveleetcode"))  # 2
print(firstUniqChar("aabb"))          # -1
