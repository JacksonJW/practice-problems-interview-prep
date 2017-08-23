/*
Description:

Remove n exclamation marks in the sentence from left to right. n is positive integer.

Examples

remove("Hi!",1) === "Hi"
remove("Hi!",100) === "Hi"
remove("Hi!!!",1) === "Hi!!"
remove("Hi!!!",100) === "Hi"
remove("!Hi",1) === "Hi"
remove("!Hi!",1) === "Hi!"
remove("!Hi!",100) === "Hi"
remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"
Note

Please don't post issue about difficulty or duplicate.
*/

function remove(s,n){
    var result = '';
    var count = n;
    for (var i = 0; i < s.length; i++){
        if (s.charAt(i) !== '!' || count <= 0){
            result += s.charAt(i);
        } else {
            count--;
        }
    }
    return result;
}