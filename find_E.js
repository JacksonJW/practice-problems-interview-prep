/*
Is it possible to write a book without the
letter 'e' ?

Task

Given String str, return:

How much "e" does it contains
(case-insensitive) - return number as
String.
If given String doesn't contain any "e",
return: There is no "e".
If given String is empty, return empty
String.
If given String is null, return null
*/

function find_E(str){
    var eCount = 0;
    if (str === null){
        return null;
    }
    if (str.length === 0){
        return "";
    }

    for (var i = 0; i < str.length; i++){
        if (str.charAt(i).toLowerCase() === 'e'){
            eCount++;
        }
    }

    if (eCount === 0){
        return "There is no \"e\".";
    } else {
        return eCount.toString();
    }
}
