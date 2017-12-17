# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example:
#
# Input: "babbabade"baa
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
# Example:
#
# Input: "cbbd"
#
# Output: "bb"

import math


class Solution(object):
    def __init__(self):
        self.lo = 0
        self.maxLen = 0

    def longestPalindrome(self, s):
        """babbabade
        :type s: str
        :rtype: str
        """
        char_list = list(s)
        no_of_characters = len(char_list)
        if no_of_characters is 1:
            return s
        for i in range(0, no_of_characters - 1):
            self.getLongestPalindrom(char_list, i, i)
            self.getLongestPalindrom(char_list, i, i + 1)

        return ''.join(char_list[self.lo: self.lo + self.maxLen])

    def getLongestPalindrom(self, char_list, start, end):
        while start >= 0 and end < len(char_list) and char_list[start] == char_list[end]:
            start -= 1
            end += 1
        if self.maxLen < end - start - 1:
            self.lo = start + 1
            self.maxLen = end - start - 1


obj = Solution()
print(obj.longestPalindrome('madamm'))
