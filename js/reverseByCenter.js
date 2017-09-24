// You and your friends want
// to play undercover agents.
// In order to exchange your
// secret messages, you've
// come up with the following
// system: you take the word,
// cut it in half, and place
// the first half behind 
// the latter. If the word 
// has an uneven number of 
// characters, you leave the
// middle at its previous 
// place:

// retsec examples

// That way, you'll be able to
// exchange your messages in
// private.

// Task

// You're given a single word.
// Your task is to swap the 
// halves. If the word has an
// uneven length, leave the
// character in the middle at
// that position and swap the
// chunks around it.

// Examples

// reverseByCenter("agent")
// 	== "nteag" 
// // center character is e

// reverseByCenter("secret")
// 	== "retsec" 
// // no center character

function reverseByCenter(s){
	var newStr = "";

  	if (s.length % 2 === 0){
  		for (var i = s.length/2; i < s.length; i++){
  			newStr += s.charAt(i);
  		}
  		for (var i = 0; i< s.length/2; i++){
  			newStr += s.charAt(i);
  		}
  	} else {
  		for (var i = Math.ceil(s.length/2); i < s.length; i++){
			newStr += s.charAt(i);
		}

		newStr += s.charAt(Math.floor(s.length/2));

		for (var i = 0; i < Math.floor(s.length/2); i++){
			newStr+=s.charAt(i);
		}
  	}
  	return newStr;
}
