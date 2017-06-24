/*
When given a string of space separated words,
return the word with the longest length. If
there are multiple words with the longest length,
return the last instance of the word with the
longest length.

Example:

'red white blue' //returns string value of white

'red blue gold' //returns gold
*/

function longestWord(stringOfWords){
    var longestLength = 0;
    var longestIndex = 0;
    var arrOfWords = stringOfWords.split(' ');
    for (var i = 0; i < arrOfWords.length; i++){
        if (arrOfWords[i].length >= longestLength){
            longestLength = arrOfWords[i].length;
            longestIndex = i;
        }
    }
    return arrOfWords[longestIndex];
}
