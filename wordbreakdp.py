'''
Give a non-empty string s and a dictionary wordDict containing a list of 
non-empty words, determine if s can be segmented into a space-separated 
sequence of one or more dictionary words.
Note: 
The same word in the dictionary may be reused multiple times in the 
segmentation.
You may assume the dictionary does not contain duplicate words

Examples:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: True

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: True

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: False
'''
#s = "leetcode"    wordDict = ["leet", "code"]
#dp = [[0], [0], [0], [0], [0], [0], [0], [0]]
def wordbreak(s, wordDict):
    dp = [[0]] * len(s)
    for i in range(len(s)):
        for j in range(len(dp[i])):
            if s[dp[i][j]:i + 1] in wordDict:
                dp[i].append(i + 1)
    return dp[-1][-1] == len(s)
