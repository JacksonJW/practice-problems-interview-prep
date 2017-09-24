/*
An isogram is a word that has no repeating
letters, consecutive or non-consecutive.
Implement a function that determines whether
a string that contains only letters is an
isogram. Assume the empty string is an
isogram. Ignore letter case.

isIsogram( "Dermatoglyphics" ) == true
isIsogram( "aba" ) == false
isIsogram( "moOse" ) == false // -- ignore letter case
*/

function isIsogram(str){
  if (str === "") {
    return true;
  } else{

    var strLCase = str.toLowerCase();

    for (var i = 0; i < strLCase.length; i++){
      if (strLCase.indexOf(strLCase.charAt(i)) !== strLCase.lastIndexOf(strLCase.charAt(i))){
          return false;
      }
    } return true;
  }
}
