function binaryToInt(binaryStr){
	var base2Exp = 0;
	var sum = 0;
	for (var i = binaryStr.length - 1; i >= 0; i--) {
		if (parseInt(binaryStr.charAt(i)) === 1) {
			sum += Math.pow(2, base2Exp);
		}

		base2Exp++;
	}
	return sum;
}