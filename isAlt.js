/*
Create a function isAlt() that accepts
a string as an argument and validates
whether the vowels (a, e, i, o, u) and
consonants are in alternate order.

isAlt("amazon")
// true
isAlt("apple")
// false
isAlt("banana")
// true
*/

function isAlt(word) {
    if (word.length < 2){
        return true;
    }
    var match = /([a|e|i|o|u|y][^a|e|i|o|u|y])+|([^a|e|i|o|u|y][a|e|i|o|u|y])+/g;

    if (word.match(match) !== null){
        return word.match(match).join('') === word;
    }
    return false;
}
