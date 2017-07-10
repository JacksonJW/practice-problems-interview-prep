// I would like to be able to pass 
// an array with two elements to my 
// swapValues function to swap the 
// values. However it appears that 
// the values aren't changing.

// Can you figure out what's wrong 
// here?

function swapValues(arguments) {
  var swappedNum = 0;
  swappedNum = arguments[1];
  arguments[1] = arguments[0];
  arguments[0] = swappedNum;
  return arguments;
}