// The function should take three arguments
// - operation(string), value1(integer),
// value2(integer). The function should 
// return result of integers after applying 
// chosen operation.

// Examples: 
// Javascript: 
// basicOp('+', 4, 7) // Output: 11 
// basicOp('-', 15, 18) // Output: -3 
// basicOp('*', 5, 5) // Output: 25 
// basicOp('/', 49, 7) // Output: 7 

function basicOp(operation, value1, value2){
	var result = 0;
	if (operation === '+'){
		result = value1 + value2;
	} else if (operation === '-'){
		result = value1 - value2;
	} else if (operation === '*'){
		result = value1 * value2;
	} else {
		result = value1 / value2;
	}
	return result;
}