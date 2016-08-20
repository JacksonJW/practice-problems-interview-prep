// You are given two arrays a1
// and a2 of strings. Each 
// string is composed with 
// letters from a to z. Let x
// be any string in the first
// array and y be any string
// in the second array.

// Find 
// max(abs(length(x) − length(y)))

// If a1 or a2 are empty 
// return -1 in each 
// language except in Haskell 
// where you will return Nothing.

// Example:

// s1 = ["hoqq", "bbllkw", 
// 	"oox", "ejjuyyy", "plmiis",
//  	"xxxzgpsssa", "xxwwkktt",
//  	"znnnnfqknaz", 
//  	"qqquuhii", "dvvvwz"]

// s2 = ["cccooommaaqqoxii",
//  "gggqaffhhh", "tttoowwwmmww"]

// mxdiflg(s1, s2) --> 13

function mxdiflg(a1, a2) {
    // your code
    var maxDiff = 0;
    if (a1.length === 0 || a2.length === 0){
    	return -1;
    } else {
    	for (var x of a1){
    		for (var y of a2){
    			if (Math.abs(x.length - y.length) > maxDiff){
    				maxDiff = Math.abs(x.length - y.length);
    			}
    		}
    	}
    	return maxDiff;
    }
}