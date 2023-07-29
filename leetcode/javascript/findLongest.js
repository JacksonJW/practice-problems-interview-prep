// Find the number with the most digits.
//
// If two numbers in the argument array
// have the same number of digits,
// return the first one in the array.

function findLongest(array){
    var longest = "";
    for (var element of array){
        var count = 0;
        if(element.toString().length > longest.length){
            longest = element.toString();
        }
    }
    return array[array.indexOf(parseInt(longest))];
}
