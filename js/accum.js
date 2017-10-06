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
    return s.split('').map(function(currentValue, index){
      let j = 0;
      let value = '';
      while (j <= index){
        if (j === 0){
          value += currentValue.toUpperCase();
        } else{
          value += currentValue.toLowerCase();
        }
        j++;
      }
      return value;
    }).join('-');
}
