// You are given an array strarr of 
// strings and an integer k. Your 
// task is to return the first longest
// string consisting of k consecutive
// strings taken in the array.

// Example:

// longest_consec(["zone", "abigail",
// 	"theta", "form", "libe", "zas", 
// 	"theta", "abigail"], 2) --> 
// 	"abigailtheta"

// n being the length of the string 
// array, if n = 0 or k > n or 
// k <= 0 return "".

function longestConsec(strarr, k) {
	if (strarr.length === 0 || k > strarr.length || k <= 0){
		return "";
	}

	var largestStr = strarr[0];
	var resultStr = "";

	for (var i = 1; i <= k; i++){
		for (var j = 0; j < strarr.length; j++){
			if(strarr[j].length > largestStr.length){
				largestStr = strarr[j];
			}
		}
		resultStr += strarr.splice(strarr.indexOf(largestStr),1);
		largestStr = "";
	}
	return resultStr;	
}