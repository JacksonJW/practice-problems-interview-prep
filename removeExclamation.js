/*
Description:

Remove all exclamation marks from sentence but
ensure a exclamation mark at the end of string.
For a beginner kata, you can assume that the
input data is always a non empty string, no
need to verify it.

Examples

remove("Hi!") === "Hi!"
remove("Hi!!!") === "Hi!"
remove("!Hi") === "Hi!"
remove("!Hi!") === "Hi!"
remove("Hi! Hi!") === "Hi Hi!"
remove("Hi") === "Hi!"
*/

function remove(s){
    var resultStr = '';
    for (var i = 0; i < s.length; i++){
        if (s.charAt(i) !== '!'){
            resultStr += s.charAt(i);
        };
    }
    return resultStr + "!";
}
