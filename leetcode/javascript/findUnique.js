/*Write a function called findUnique which
returns the only unique number from an array.

All numbers in the unsorted array are present
twice, except the one you have to find. The
numbers are always valid integer values between
1 and 2147483647, so no need for type and error
checking. The array contains at least one number
and may contain millions of numbers. So make
sure your solution is optimized for speed.

Example

Input:

[ 1, 8, 4, 4, 6, 1, 8 ]
Expected output:

6*/

function findUnique(nums) {
    var isUnique;
    for (var i = 0; i < nums.length; i++){
        isUnique = true;
        for (var j = 0; j < nums.length; j++){
            if (i === j){
                continue;
            } else if (nums[i] === nums[j]){
                isUnique = false;
            }
        }
        if (isUnique){
            return nums[i];
        }
    }
}


/* Other solutions:

function findUnique(){
    var numsAndCounts = [];
    var currNum = 0
    while (numbers.length>0){
        currNum = numbers[numbers.length-1];
        if (numbers.indexOf(numbers.pop()) === -1){
            return currNum;
        } else {
            numbers.splice(numbers.indexOf(currNum), 1);
        }
    }
    return null;
}

function findUnique(){
    var checkArr = [];
    for (var num of numbers){
        if (checkArr.indexOf(num) === -1){
            checkArr.push(num);
        } else {
            checkArr.splice(checkArr.indexOf(num),1);
        }
    }
    return checkArr[0];
}*/
