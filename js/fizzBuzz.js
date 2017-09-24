/*
Return an array containing the numbers
from 1 to N, where N is the parametered
value. N will never be less than 1.

Replace certain values however if any of
the following conditions are met:

If the value is a multiple of 3: use the
value 'Fizz' instead
If the value is a multiple of 5: use the
value 'Buzz' instead
If the value is a multiple of 3 & 5: use
the value 'FizzBuzz' instead
*/

function fizzbuzz(n){
    var resultArr = [];
    for (var i = 1; i <= n; i++){
        if (i % 15 === 0){
            resultArr.push("FizzBuzz");
        } else if (i % 5 === 0){
            resultArr.push("Buzz");
        } else if (i % 3 === 0){
            resultArr.push("Fizz");
        } else {
            resultArr.push(i);
        }
    }
    return resultArr;
}
