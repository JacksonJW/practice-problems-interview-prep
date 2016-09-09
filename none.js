// Create a method none? 
// (JS none) that accepts 
// an array and a block 
// (JS: a function), and 
// returns true if the 
// block (/function) 
// returns true for none of 
// the items in the array. 
// An empty list should 
// return true.

function none(arr, fun){
	if (arr.length === 0){
		return true;
	}
	var flag = true;
	for (var i = 0; i < arr.length; i++){
		if (fun(arr[i])){
			flag = false;
		}
	}
	return flag;
}