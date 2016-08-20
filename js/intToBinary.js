function intToBinary(number){
	var highestBase2Exp = Math.floor(Math.log2(number));
	var binaryStr = "";
	while (highestBase2Exp >= 0){
		if (number >= Math.pow(2,highestBase2Exp)) {
			number = number - Math.pow(2,highestBase2Exp);
      alert(number);
			binaryStr = binaryStr + "1";
		} else {
			binaryStr = binaryStr + "0";
		}
		highestBase2Exp--;
	}
  
		return binaryStr;
}