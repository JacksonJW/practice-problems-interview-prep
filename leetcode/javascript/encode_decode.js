// Step 1: Create a function called 
// encode() to replace all the 
// lowercase vowels in a given 
// string with numbers according to
//  the following pattern:
// a -> 1
// e -> 2
// i -> 3
// o -> 4
// u -> 5

// For example, encode("hello") 
// would return "h2ll4" There is no
// need to worry about uppercase
// vowels in this kata.

// Step 2: Now create a function 
// called decode() to turn the 
// numbers back into vowels 
// according to the same pattern 
// shown above.

// For example, decode("h3 th2r2")
// would return "hi there"

// For the sake of simplicity, you
// can assume that any numbers 
// passed into the function will
// correspond to vowels.

function encode(str){
  var newStr = "";
  for (var i = 0; i < str.length; i++){
    if (str.charAt(i) == 'a'){
      newStr+='1';
    } else if (str.charAt(i) == 'e'){
      newStr+='2';
    } else if (str.charAt(i) == 'i'){
      newStr+='3';
    } else if (str.charAt(i) == 'o'){
      newStr+='4';
    } else if (str.charAt(i) == 'u'){
      newStr+='5';
    } else {
      newStr+=str.charAt(i);
    }
  }
  return newStr;
}

//turn numbers back into vowels
function decode(str){
  var newStr = "";
  for (var i = 0; i < str.length; i++){
    if (str.charAt(i) === '1'){
      newStr+='a';
    } else if (str.charAt(i) === '2'){
      newStr+='e';
    } else if (str.charAt(i) === '3'){
      newStr+='i';
    } else if (str.charAt(i) === '4'){
      newStr+='o';
    } else if (str.charAt(i) === '5'){
      newStr+='u';
    } else {
      newStr+=str.charAt(i);
    }
  }return newStr;
}
