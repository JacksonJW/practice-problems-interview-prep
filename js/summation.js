//Write a program that finds the 
//summation of every number between
//1 and num. The number will always
//be a positive integer greater 
//than 0.

var summation = function (num) {
  var sum = 0;
  while (num > 0 ) {
    sum += num + num - 1
    num -= 2;
  }
  return sum;
}