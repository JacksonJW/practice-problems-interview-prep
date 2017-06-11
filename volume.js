/*
Find the volume of a cone whose radius and height are
provided as parameters to the function volume. Use the
value of PI provided by your language
(for example: Math.PI in JS, math.pi in Python or
	Math::PI in Ruby)
and round down the volume to an Interger.
*/

function volume(r,h) {
	return Math.floor((Math.PI * Math.pow(r,2)) * (h/3));
}
