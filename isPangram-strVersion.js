// A pangram is a sentence that contains every
// single letter of the alphabet at least 
// once. For example, the sentence "The quick
// brown fox jumps over the lazy dog" is a 
// pangram, because it uses the letters A-Z
// at least once (case is irrelevant).

// Given a string, detect whether or not it
// is a pangram. Return True if it is, False
// if not. Ignore numbers and punctuation.





function isPangram(string){
  //...
  var reformedString = string.toLowerCase().split(' ').join('');
  var alphabet = "abcdefghijklmnopqrstuvwxyz";

  for (var i = 0; i < reformedString.length; i++){
  	for (var j = 0; j < alphabet.length; j++){
  		if (reformedString.charAt(i) === alphabet.charAt(j)){
  			alphabet = alphabet.split(reformedString.charAt(i)).join('');
  			break;
  		}
  	}
  }

  if (alphabet.length === 0){
  	return true;
  } else {
  	return false;
  }
}