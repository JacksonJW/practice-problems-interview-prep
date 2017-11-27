/*
Given an array containing only zeros and ones,
find the index of the zero that, if converted
to one, will make the longest sequence of ones.

For instance, given the array

[1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1],

replacing the zero at index 10 (counting from 0)
forms a sequence of 9 ones.

Your task is to write the function replaceZero()
that determines where to replace a zero with a
one to make the maximum length subsequence.

Note:

If the're multiple results, return the last
[1,1,0,1,1,0,1,1] //=> 5

The array will always contain zeros and ones.
Can you do this in one pass ?
*/

function replaceZero(arr){
  let i = 0;
  let numberOf1s = 0;
  let longestSequence = 0;
  let resultIndex = -1;
  let encounteredZero = false;
  let replaceIndex = -1;
  while (i <= arr.length){
    if (i === arr.length){
      if (numberOf1s >= longestSequence){
        longestSequence = numberOf1s;
        resultIndex = replaceIndex;
      }
    } else if (arr[i] === 0 && encounteredZero === false){
      arr[i] = 1;
      replaceIndex = i;
      numberOf1s++;
      encounteredZero = true;
    } else if (arr[i] === 0 && encounteredZero === true){
      if (numberOf1s >= longestSequence){
        longestSequence = numberOf1s;
        resultIndex = replaceIndex;
      }
      i = replaceIndex;
      numberOf1s = 0;
      encounteredZero = false;
    } else {
      numberOf1s++
    }
      i++;
  }
  return resultIndex;
}
