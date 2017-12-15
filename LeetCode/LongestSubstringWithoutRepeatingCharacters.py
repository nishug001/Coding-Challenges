# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_list = list(s)
        char_map = {}
        max_len = 0
        i = 0
        for j in range(0, len(char_list)):
            if char_list[j] in char_map:
                i = max(i, char_map[char_list[j]])
            max_len = max(max_len, j - i + 1)
            char_map[char_list[j]] = j + 1

        return max_len
