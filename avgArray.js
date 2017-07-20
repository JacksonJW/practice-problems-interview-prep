/*
ASC Week 1 Challenge 5 (Medium #2)

Create a function that takes a 2D array as an input,
and outputs another array that contains the average
values for the numbers in the nested arrays at the
corresponding indexes.

For Example:

avgArray([[1, 2, 3, 4], [5, 6, 7, 8]]);
// => [3, 4, 5, 6]
avgArray([[2, 3, 9, 10, 7], [12, 6, 89, 45, 3],
[9, 12, 56, 10, 34], [67, 23, 1, 88, 34]]);
// => [22.5, 11, 38.75, 38.25, 19.5]

This function should also work with negative numbers.
*/

function avgArray(arr) {
    var arrayOfAvg = [];
    var sum = 0;
    for (var j = 0; j < arr[0].length; j++){
        sum = 0;
        for (var i = 0; i < arr.length; i++){
            sum += arr[i][j]
        }
        arrayOfAvg.push(sum/arr.length);
    }
    return arrayOfAvg;
}
