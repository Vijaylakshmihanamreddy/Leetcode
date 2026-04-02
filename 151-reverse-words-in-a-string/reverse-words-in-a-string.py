class Solution(object):
    def reverseWords(self, s):
        words = s.split()        # removes extra spaces
        words.reverse()          # reverse list
        return " ".join(words)   # join with single space