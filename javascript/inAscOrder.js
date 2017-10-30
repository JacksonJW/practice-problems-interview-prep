// Are the numbers in order?

// In this Kata, your 
// function receives an array
// of positive integers as 
// input. Your task is to 
// determine whether the 
// numbers are in ascending
// order.

// For the purposes of this
// Kata, you may assume 
// that all inputs are 
// valid (i.e. arrays 
// containing only positive
// integers with a length
// of at least 2).

// For example:

function inAscOrder(arr) {
  // Code your algorithm here :)
  for (var i = 0; i < arr.length-1; i++){
    if (arr[i] > arr[i+1]){
      return false;
    }
  } return true;
}