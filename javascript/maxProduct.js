// Create a performant solution
// to find the product of the
// largest two integers in a 
// unique array of positive 
// numbers.
// All inputs will be valid.
// Passing [2, 6, 3] should 
// return 18, the product of
// [6, 3].

// maxProduct([2, 1, 5, 0, 4, 3])              // 20
// maxProduct([7, 8, 9])                       // 72
// maxProduct([33, 231, 454, 11, 9, 99, 57])   // 104874

function maxProduct(a) {
	var largestNum = a[0];
	var secondLargestNum = a[0];
	for (num of a){
		if (num > largestNum){
			largestNum = num;
		}
	}

	a.splice(a.indexOf(largestNum),1);

	for (num of a){
		if (num < secondLargestNum){
			secondLargestNum = num;
		}
	}
	return largestNum * secondLargestNum;
}