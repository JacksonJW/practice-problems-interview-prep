// Bob is preparing to pass
// IQ test. The most frequent
// task in this test is to 
// find out which one of the
// given numbers differs from
// the others. Bob observed
// that one number usually
// differs from the others
// in evenness. Help Bob —
// to check his answers, he
// needs a program that among
// the given numbers finds 
// one that is different in
// evenness, and return a 
// position of this number.

// ! Keep in mind that your
// task is to help Bob solve
// a real IQ test, which
// means indexes of the 
// elements start from 
// 1 (not 0)

function iqTest(numbers){
  // ...
  var evenNumCount = 0;
  var oddNumCount = 0;
  var numsArray = numbers.split(' ');
  var evensPlace = 0;
  var oddsPlace = 0;

  for (var num of numsArray){
  	if (num % 2 === 0){
  		evenNumCount++;
  		evensPlace = numsArray.indexOf(num) + 1;
  	} else {
  		oddNumCount++
  		oddsPlace = numsArray.indexOf(num) + 1;
  	}
  }

  if (evenNumCount > oddNumCount){
  	return numToStr(oddsPlace) + " number is odd. The rest are even."
  } else {
	return numToStr(evensPlace) + " number is even. The rest are odd."
  }
}

function numToStr(number){
	if (number === 1){
		return "first";
	} else if (number === 2){
		return "second";
	} else if (number === 3){
		return "third";
	} else if (number === 4){
		return "fourth";
	} else if (number === 5){
		return "fifth";
	} else{
		return '';
	}
}