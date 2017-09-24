// Write function hexToDec which
// converts hex number 
// (given as a string) to 
// decimal number.

function hexToDec(hexString){
	var pow = 0;
	var sum = 0;
	if (hexString.charAt(0) === '-'){
    pow = hexString.length - 2;
		for (var i = 1; i < hexString.length; i++){
			if (hexString.charAt(i).toUpperCase() === 'A'){
				sum -= 10 * Math.pow(16,pow);
				pow--;
			} else if (hexString.charAt(i).toUpperCase() === 'B'){
				sum -= 11 * Math.pow(16,pow);
				pow--;
			} else if (hexString.charAt(i).toUpperCase() === 'C'){
				sum -= 12 * Math.pow(16,pow);
				pow--;
			} else if (hexString.charAt(i).toUpperCase() === 'D'){
				sum -= 13 * Math.pow(16,pow);
				pow--;
			} else if (hexString.charAt(i).toUpperCase() === 'E'){
				sum -= 14 * Math.pow(16,pow);
				pow--;
			} else if (hexString.charAt(i).toUpperCase() === 'F'){
				sum -= 15 * Math.pow(16,pow);
				pow--;
			} else {
				sum -= parseInt(hexString.charAt(i)) * Math.pow(16,pow);
				pow--;
			}
    	}
	} else {
    	pow = hexString.length - 1;
		for (var i = 0; i < hexString.length; i++){
			if (hexString.charAt(i).toUpperCase() === 'A'){
				sum += 10 * Math.pow(16,pow);
				pow--;
			} else if (hexString.charAt(i).toUpperCase() === 'B'){
				sum += 11 * Math.pow(16,pow);
				pow--;
			} else if (hexString.charAt(i).toUpperCase() === 'C'){
				sum += 12 * Math.pow(16,pow);
				pow--;
			} else if (hexString.charAt(i).toUpperCase() === 'D'){
				sum += 13 * Math.pow(16,pow);
				pow--;
			} else if (hexString.charAt(i).toUpperCase() === 'E'){
				sum += 14 * Math.pow(16,pow);
				pow--;
			} else if (hexString.charAt(i).toUpperCase() === 'F'){
				sum += 15 * Math.pow(16,pow);
				pow--;
			} else {
				sum += parseInt(hexString.charAt(i)) * Math.pow(16,pow);
				pow--;
			}
		}
	}
	return sum;
}