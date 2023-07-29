/*
Given a set of numbers, return the additive
inverse of each. Each positive becomes
negatives, and the negatives become
positives.

Python/JS/PHP/Java:

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers
(and for C/C++: that all values are greater
than INT_MIN).
*/

function invert(array) {
  var resultArr = array.map(function(num){
        if (Math.sign(num) === -1){
            return Math.abs(num);
        } else if (Math.sign(num) === 0){
            return 0;
        } else {
            return -Math.abs(num);
        }
    });
    return resultArr;
}
