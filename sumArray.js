// Sum all the numbers of the 
// array except the highest 
// and the lowest element.
// (Only one element at each 
// edge, even if there are 
// more than one with the 
// same value!)

// Example: 
// { 6, 2, 1, 8, 10 } => 16



// If array is empty or null,
// or if only 1 Element 
// exists, return 0.
// Note: in C++ instead null
// an empty vector is used. 


// Have fun coding it and 
// please don't forget to 
// vote and rank this kata! 
// :-)

// I have created other katas.
// Have a look if you like 
// coding and challenges.

function sumArray(array) {
	if (array === null){
		return 0;
	}
	if (array.length === 0 || array.length === 1){
		return 0;
	}

	var sum = 0;
	var sortedArray = array.sort(function(a,b){return a-b;});

	for (var i = 1; i < sortedArray.length - 1; i++){
		sum += sortedArray[i];
	}

	return sum;
}