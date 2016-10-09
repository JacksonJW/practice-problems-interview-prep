function removeExclamationMarks(s) {
	var resultStr = "";
	for (var char of s.split('')){
		if (char !== "!"){
			resultStr += char;
		}
	}
	return resultStr;
}