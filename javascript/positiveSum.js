/*
You get an array of numbers, return
the sum of all of the positives ones.

Example [1, -4, 7, 12] => 1 + 7 + 12 = 20

Note: array may be empty, in this
case return 0.
*/

function positiveSum(arr) {
    if (arr.length === 0){
        return 0;
    }

    var newArr = arr.filter(function (num) {
        return Math.sign(num) === 1;
    });

    if (newArr.length === 0){
        return 0;
    }

    return newArr.reduce(function (sum, posNum) {
            return sum + posNum;
    });
}
