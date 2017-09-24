// Given some points 
// (cartesian coordinates),
// return true if all of 
// them lie on a line.

// onLine([[1,2], [7, 4], [22, 9]]);                 
// // returns true
// onLine([[1,2], [-3, -14], [22, 9]]);              
// // returns false

function onLine(points) {
	var x1 = points[0][0];
	var y1 = points[0][1];
	var x2 = points[1][0];
	var y2 = points[1][1];
	var x3 = points[2][0];
	var y3 = points[2][1];

	var slope1 = (y2 - y1) / (x2 - x1);
	var slope2 = (y3 - y1) / (x3 - x1);

	if (slope1 === slope2){
		return true;
	}else {
		return false;
	}
}
