"""
Leetcode #692. Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]

Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]

Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

Algorithm/DS used: max_heap

O(n*log(n)) worst case time

O(n) worst case space

"""

import collections
from typing import List
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_frequencies = collections.Counter()
        list_of_word_freq = []
        for word in words:
            word_frequencies[word] -= 1
        list_of_word_freq = [(value, key)
                             for key, value in word_frequencies.items()]
        heapq.heapify(list_of_word_freq)
        return [heapq.heappop(list_of_word_freq)[1] for _ in range(k)]


def test_solution():
    s = Solution()
    input = ["the", "day", "is", "sunny", "the",
             "the", "the", "sunny", "is", "is"]
    print("Expected result from input ([\"the\", \"day\", \"is\", \"sunny\", \"the\", \"the\", \"the\", \"sunny\", \"is\", \"is\"], 4) is [\"the\",\"is\",\"sunny\",\"day\"] and the Actual result is: " +
          str(s.topKFrequent(input, 4)))
    assert s.topKFrequent(input, 4) == ["the", "is", "sunny", "day"]


if __name__ == "__main__":
    test_solution()
