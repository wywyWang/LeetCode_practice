class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lcs = [[0 for col in range(len(word2)+1)] for row in range(len(word1)+1)]
        
        for row in range(1, len(word1)+1):
            for col in range(1, len(word2)+1):
                if word1[row-1] == word2[col-1]:
                    lcs[row][col] = 1 + lcs[row-1][col-1]
                else:
                    lcs[row][col] = max(lcs[row][col-1], lcs[row-1][col])
                        
        return len(word1) + len(word2) - 2 * lcs[-1][-1]