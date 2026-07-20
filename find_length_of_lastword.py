class Solution(object):
    def lengthOfLastWord(self, s):  # s = "   fly me   to   the moon"
        arr = list(filter(None, s.split(" ")))
        return len(arr[-1])
        
