// Speed is a crucial measure of success
// for any aspiring warrior, so let's write 
// a function to calculate it.

// Average Speed is calculated by dividing 
// distance by time. Given two strings as 
// input the first of which indicates a 
// codewarrior's distance travelled 
// (in metres or kilometres) and the second
// indicating the time it takes them to 
// travel (in seconds or minutes), return 
// a string indicating their speed in miles 
// per hour rounded to the nearest integer.

// For the purposes of this kata one metre 
// per second is defined as 2.23694 miles 
// per hour.

// So for example given the input values of 
// distance & time "3km" and "5min" we 
// should return a speed value of "22mph".

function calculateSpeed(distance, time) {
	var distanceStr = "";
	var distanceNum = 0;
	var timeStr = "";
	var timeNum = 0;
	var km = false;
	var min = false;
	var metersPerSecond = 0;
	var milesPerHour = 0;
	
	for (var i of distance.split('')){
		if (isNaN(parseInt(i)) === false){
			distanceStr += i;
		} else if (i === 'k'){
			km = true;
		}
	}
  

	for (var j of time.split('')){
		if (isNaN(parseInt(j)) === false){
			timeStr += j;
		} else if (j === 'm'){
			min = true;
		}
	}

	distanceNum = parseInt(distanceStr);
	timeNum = parseInt(timeStr);

	if (km === true) {
		distanceNum *= 1000;
	}
	if (min === true) {
		timeNum *= 60;
	}

	metersPerSecond = distanceNum / timeNum;
	milesPerHour = Math.round(metersPerSecond * 2.23694);
  

	return milesPerHour + "mph";
}
