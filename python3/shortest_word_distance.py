from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_index = -1
        word2_index = -1
        shortest = float('inf')
        for i, e in enumerate(wordsDict):
            if e == word1:
                word1_index = i
            elif e == word2:
                word2_index = i
            if word1_index > -1 and word2_index > -1:
                shortest = min(shortest, abs(word1_index - word2_index))
        return shortest


def main():
    s = Solution()
    result = s.shortestDistance(["practice", "makes", "perfect",
                                 "coding", "makes"], "coding", "practice")
    print("Expected Result is 3. Actual result is: " + str(result))


if __name__ == "__main__":
    main()
