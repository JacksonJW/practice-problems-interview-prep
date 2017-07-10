// You have an array of numbers.
// Your task is to sort ascending odd
// numbers but even numbers must be on
// their places.
//
// Zero isn't an odd number and you don't
// need to move it. If you have an empty
// array, you need to return it.
//
// Example
//
// sortArray([5, 3, 2, 8, 1, 4])
// == [1, 3, 2, 8, 5, 4]

function sortArray(arr) {
    var resultArr = [];

    for (var num of arr){
        if (num % 2 !== 0){
            resultArr.push(num);
        }
    }

    resultArr.sort(function(a, b){return a - b});

    for (var i = 0; i < arr.length; i++){
        if (arr[i] % 2 === 0){
            resultArr.splice(i, 0, arr[i]);
        }
    }

    return resultArr;
}
