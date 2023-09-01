import codewars_test as test


def capitalize(s):
    result = ["", ""]
    for i, l in enumerate(s):
        if i % 2 == 0:
            result[0] += l.upper()
            result[1] += l
        else:
            result[0] += l
            result[1] += l.upper()
    return result


test.it("Basic tests")
test.assert_equals(capitalize("abcdef"), ["AbCdEf", "aBcDeF"])
test.assert_equals(capitalize("codewars"), ["CoDeWaRs", "cOdEwArS"])
test.assert_equals(capitalize("abracadabra"), ["AbRaCaDaBrA", "aBrAcAdAbRa"])
test.assert_equals(capitalize("codewarriors"), ["CoDeWaRrIoRs", "cOdEwArRiOrS"])
