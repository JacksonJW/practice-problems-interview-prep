"""
Leetcode #1268 Search Suggestions System

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from
products after each character of searchWord is typed. Suggested
products should have common prefix with searchWord. If there are
more than three products with a common prefix return the three
lexicographically minimums products.

Return a list of lists of the suggested products after each
character of searchWord is typed.



Example 1:
Input: products = ["mobile","mouse","moneypot","monitor",
"mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]

Explanation: products sorted lexicographically = ["mobile",
"moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user
["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse",
"mousepad"]


Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],
["havana"]]

Example 3:
Input: products = ["bags","baggage","banner","box","cloths"],
searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],
["baggage","bags"],["bags"]]


Constraints:
 - 1 <= products.length <= 1000
 - 1 <= products[i].length <= 3000
 - 1 <= sum(products[i].length) <= 2 * 104
 - All the strings of products are unique.
 -  products[i] consists of lowercase English letters.
 - 1 <= searchWord.length <= 1000
 - searchWord consists of lowercase English letters.

Algorithm/DS used: Trie using dictionary to catalog products

O(N) worst case time where N is the # of characters for all products

O(N) worst case space where N is the # of characters for all products

"""
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str)\
            -> List[List[str]]:
        catalog = {}
        catalog_ptr = catalog
        for product in products:
            for letter in product:
                if letter not in catalog_ptr:
                    catalog_ptr[letter] = [[product], {}]
                elif letter in catalog_ptr:
                    catalog_ptr[letter][0].append(product)
                    catalog_ptr[letter][0] = sorted(catalog_ptr[letter][0])[:3]
                catalog_ptr = catalog_ptr[letter][1]
            catalog_ptr = catalog
        result, is_in_catalog = [], True
        for letter in searchWord:
            if not is_in_catalog:
                result.append([])
            elif letter not in catalog_ptr:
                result.append([])
                is_in_catalog = False
            elif letter in catalog_ptr:
                result.append(catalog_ptr[letter][0])
                catalog_ptr = catalog_ptr[letter][1]
        return result


def test_solution():
    s = Solution()
    print("Expected result from input [\"mobile\", \"mouse\", \"moneypot\",\
     \"monitor\", \"mousepad\"], \"mouse\" is \
 [[\"mobile\", \"moneypot\", \"mon itor\"], [\"mobile\", \"moneypot\", \
     \"monitor\"],[\"mouse\", \"mousepad\"], [\"mouse\", \"mousepad\"],\
 [\"mouse\", \"mousepad\"]] and the Actual result is: " +
          str(s.suggestedProducts(["mobile", "mouse", "moneypot",
                                   "monitor", "mousepad"], "mouse")))
    assert s.suggestedProducts(["mobile", "mouse", "moneypot",
                                "monitor", "mousepad"], "mouse")\
        == [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"]
    ]


if __name__ == "__main__":
    test_solution()
