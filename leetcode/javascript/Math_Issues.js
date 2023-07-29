// Oh no, our Math object was
// "accidently" reset. Can you
// re-implement some of those 
// functions? We can assure, that
// only non-negative numbers are
// passed as arguments. So you 
// don't have to consider things
// like undefined, null, NaN,
// negative numbers, strings 
// and so on.

// Here is a list of functions,
// we need:

// Math.round()
// Math.ceil()
// Math.floor()

Math.round = function(number) {
  var decimal = number % 1;
  if (decimal !== 0){
    if (decimal < 0.5){
      number = number - decimal;
    } else {
      number = number - decimal + 1;
    }
  }
  return number;
};

Math.ceil = function(number) {
  var decimal = number % 1;
  if (decimal !== 0){
    number = number - decimal + 1;
  }
  return number;
};

Math.floor = function(number) {
  var decimal = number % 1;
  if (decimal !== 0){
    number = number - decimal;
  }
  return number;
};