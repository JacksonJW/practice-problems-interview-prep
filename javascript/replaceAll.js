/*
Write function replaceAll (Python: replace_all)
that will replace all occurrences of an item
with another.

Javascript: The function has to work for strings and
lists.

Example: replaceAll [1,2,2] 1 2 -> in list
[1,2,2] we replace 1 with 2 to get new list
[2,2,2]

replaceAll(replaceAll(array: [1,2,2], old: 1, new: 2)
// [2,2,2]
*/

function replaceAll(seq, find, replace) {
    var builder;
    if (typeof seq === 'object'){
        builder = [];
        for (var i = 0; i < seq.length; i++){
            if (seq[i] === find){
                builder.push(replace);
            } else {
                builder.push(seq[i]);
            }
        }
    } else {
        builder = "";
        for (var i = 0; i < seq.length; i++){
            if (seq[i] === find){
                builder += replace;
            } else {
                builder += seq.charAt(i);
            }
        }
    }
    return builder;
}
