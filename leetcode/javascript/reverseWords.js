// Write a reverseWords function
// that accepts a string a 
// parameter, and reverses each
// word in the string. Every 
// space should stay, so you 
// cannot use words from 
// Prelude.

// Example:

// reverseWords("This is an example!"); 
// // returns  "sihT si na !elpmaxe"


function reverseWords(str) {
	var wordArray = str.split(' ');
	var reversedStr = "";
	var reversedWord = "";
	var reversedArray = new Array();

	for (var word of wordArray){
		for (var i = word.length-1; i >= 0; i--){
  			reversedWord += word.charAt(i);
  		}
  		reversedArray.push(reversedWord);
  		reversedWord = "";
  	}

  	reversedStr = reversedArray.join(' ');

  	return reversedStr;
}