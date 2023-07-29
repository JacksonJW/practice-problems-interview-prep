// Task

// Given an integral number, 
// determine if it's a square
// number:

// In mathematics, a square
// number or perfect square
// is an integer that is the
// square of an integer; in 
// other words, it is the 
// product of some integer 
// with itself.

var isSquare = function(n){
  if (n<0){
    return false;
  } else if (Math.sqrt(n) % 1 === 0){
    return true;
  } else{
    return false;
  }
}