// Life isn't always easy as a small word
// amongst big words. If only they had a 
// code warrior to help them out...

// Your task is to make all words which 
// are 3 characters or less into capital 
// letters. You should also remove any 
// vowels from 'long' 
// (4 characters or more) words.

// For example:

// "The quick brown fox jumps over the 
// lazy dog"

// Should become:

// "THE qck brwn FOX jmps vr THE 
// lzy DOG"

function smallWordHelper(sentence){
	var wordsOfSentence = sentence.split(' ');
	var resultSentence = "";
	var arrayBuilder = [];

	for (var i = 0; i < wordsOfSentence.length; i++) {
		if (wordsOfSentence[i].length <= 3){
			arrayBuilder.push(wordsOfSentence[i].toUpperCase());
		}
		else if (wordsOfSentence[i].length >= 4) {
			arrayBuilder.push(wordsOfSentence[i].replace(/[aeiou]/ig,''));
		} else {
			arrayBuilder.push(wordsOfSentence[i]);
		}
	}
  
    resultSentence = arrayBuilder.join(' ');
  	return resultSentence;
}
