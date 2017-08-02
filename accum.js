/*
This time no story, no theory. The examples below
show you how to write function accum:

Examples:

accum("abcd");
// "A-Bb-Ccc-Dddd"

accum("RqaEzty");
// "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

accum("cwAt");
// "C-Ww-Aaa-Tttt"
*/

function accum(s) {
    var resultArr = [];
    var resultStr = "";
    for (var i = 0; i < s.length; i++){
        resultStr = "";
        for (var j = 0; j <= i; j++){
            if (j === 0){
                resultStr += s.charAt(i).toUpperCase();
            } else {
                resultStr += s.charAt(i).toLowerCase();
            }
        }
        resultArr.push(resultStr);
    }
    return resultArr.join("-");
}
