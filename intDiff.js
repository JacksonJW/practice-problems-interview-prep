// Write a function that accepts 
// two arguments: an array of 
// integers and another integer n.

// Determine the number of times 
// where two integers in the array
//  have a difference of n.

// For example:

// int_diff([1, 1, 5, 6, 9, 16, 27],
//  4) # 3 ([1, 5], [1, 5], [5, 9])

// int_diff([1, 1, 3, 3], 2) # 4 
// ([1, 3], [1, 3], [1, 3], [1, 3])

const intDiff = (arr, n) => {
  // your code goes here
  var diffCount = 0;
  for (var i = 0; i < arr.length-1; i++){
    for (var j = i + 1; j < arr.length; j++){
      if (Math.abs(arr[j] - arr[i]) === n){
        diffCount++;
      }
    }
  }
  return diffCount;
}