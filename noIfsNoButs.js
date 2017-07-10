// Write a function that accepts two parameters
// (a and b) and says whether a is smaller than,
// bigger than, or equal to b.
//
// Here is an example code:
//
// var noIfsNoButs = function (a,b) {
//   if(a > b) return a + " is greater than " + b
//   else if(a < b) return a + " is smaller than " + b
//   else if(a == b) return a + " is equal to " + b
// }
// There's only one problem...
//
// You can't use if statements, and you can't use 
// shorthands like (a < b)?true:false;
//
// in fact the word "if" and the character "?" are not
// allowed in the code.
//
// Inputs are guarenteed to be numbers

var noIfsNoButs = function (a,b) {
    var resultStr = "";
    switch ((a-b).toString().charAt(0)) {
        case ("0"):
            resultStr += a + " is equal to " + b;
            break;

        case ("-"):
            resultStr += a + " is smaller than " + b;
            break;

        default:
            resultStr += a + " is greater than " + b;
            break;
    }
    return resultStr;
}
