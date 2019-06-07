def groupAnagrams(strs):
    set_lookup = {}
    for word in strs:
        sorted_word = tuple(sorted(word))
        if sorted_word in set_lookup:
            set_lookup[sorted_word].append(word)
        else:
            set_lookup[sorted_word] = [word]
    return list(set_lookup.values())


actual_result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
expected_result = [
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
]
print(
    "Epected value of group anagrams given [\"eat\", \"tea\", \"tan\", \"ate\", \"nat\", \"bat\"] is: \n"+str(expected_result))

print(
    "Actual value of group anagrams given [\"eat\", \"tea\", \"tan\", \"ate\", \"nat\", \"bat\"] is: \n"+str(actual_result))
