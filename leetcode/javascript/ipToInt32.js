// ipToInt32
// Instructions
// Output
// Take the following IPv4 address:
//  128.32.10.1 This address has 4 
//  octets where each octet is a 
//  single byte (or 8 bits).

// 1st octet 128 has the binary
//  representation: 10000000
// 2nd octet 32 has the binary
//  representation: 00100000
// 3rd octet 10 has the binary
//  representation: 00001010
// 4th octet 1 has the binary
//  representation: 00000001
// So 128.32.10.1 == 
// 10000000.00100000.
// 00001010.00000001

// Because the above IP address
// has 32 bits, we can represent
// it as the 32 bit number: 
// 2149583361.

// Write a function 
// ip_to_int32(ip) 
// ( JS: ipToInt32(ip) ) that
// takes an IPv4 address and 
// returns a 32 bit number.

//   ipToInt32("128.32.10.1") 
//   => 2149583361

function ipToInt32(ip){
  var ipArray = ip.split(".");
  var binaryIp = "";
  var bit32number;
  for (var octet of ipArray) {
    binaryIp = binaryIp + intToBinary(parseInt(octet));
	}
	bit32number =  binaryToInt(binaryIp);
	
	return bit32number;
}

function intToBinary(number){
	var highestBase2Exp = Math.floor(Math.log2(number));
	var binaryStr = "";
	var leadingZero = "0";
	while (highestBase2Exp >= 0){
		if (number >= Math.pow(2,highestBase2Exp)) {
			number = number - Math.pow(2,highestBase2Exp);
			binaryStr = binaryStr + "1";
		} else {
			binaryStr = binaryStr + "0";
		}
		highestBase2Exp--;
	}

	while (binaryStr.length < 8){
		binaryStr = leadingZero + binaryStr;
	}
  
		return binaryStr;
}

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