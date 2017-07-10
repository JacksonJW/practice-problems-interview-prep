// Return the number (count) of vowels
// in the given string.
// We will consider a, e, i, o, and u
// as vowels for this Kata.

function getCount(str) {
  var vowelsCount = 0;
  
  // enter your majic here
  var vowels = ['a','e','i','o','u'];
  var strSplitted = str.toLowerCase().split(' ').join('').split('');
  
  for (var letter of strSplitted) {
    for (var vowel of vowels){
      if (vowel === letter){
        vowelsCount++;
      }
    }
  }
  return vowelsCount;
}