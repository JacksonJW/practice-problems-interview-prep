from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        min_distance = float('inf')
        word1_index = -1
        word2_index = -1
        for i in range(len(words)):
            if words[i] == word1:
                word1_index = i
            elif words[i] == word2:
                word2_index = i

            if word1_index != -1 and word2_index != -1:
                min_distance = min(min_distance, abs(
                    word1_index - word2_index))

        return min_distance


def main():
    s = Solution()
    result = s.shortestDistance(["practice", "makes", "perfect",
                                 "coding", "makes"], "coding", "practice")
    print("Expected Result is 3. Actual result is: " + str(result))


if __name__ == "__main__":
    main()
