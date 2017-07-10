// You need to write a function 
// that reverses the words in a 
// given string. If this is not 
// clear enough, here are some 
// examples:

// Your solution should also 
// work for double spaces:

// Happy coding!

function reverse(string){
	var strArr = string.split(' ');
	var reverseArr = [];
	for (var i = strArr.length - 1; i >= 0; i--){
		reverseArr.push(strArr[i]);
	}
	return reverseArr.join(' ');
}