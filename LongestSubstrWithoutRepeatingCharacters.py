"""
Busra Yasar
Given a string, find the length of the longest substring without repeating
character:
Maintain a sliding window, updating the start whenever we see a character
repeated.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        s:str
        rtype: int
        """
        last_seen = {} #mapping from character to its last seen index in s
        start = 0 # start index of current substring
        longest = 0
        for i,c in enumerate(s):
            if c in last_seen and last_seen[c] >= start:
                #start a new substring after the previous sighting of c
                start = last_seen[c] + 1
            else:
                longest = max(longest, i-start+1)
            last_seen[c] =i #update the last sighting index
        return longest
def main():
    strn = str(input("Enter a string:"))
    print(Solution().lengthOfLongestSubstring(strn))
if __name__ == "__main__":
    main()
