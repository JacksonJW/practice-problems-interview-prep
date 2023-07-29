/*
Create a function runningAverage() that
returns a callable function object.
Update the series with each given value
and calculate the current average.

rAvg = runningAverage();
rAvg(10) = 10.0;
rAvg(11) = 10.5;
rAvg(12) = 11;
*/

function runningAverage(num) {
    var total;
    var count;

    function average(num){
        if (total === undefined && count === undefined){
            total = num;
            count = 1;
        } else{
        	total += num;
        	count++;
        }
        var avrg = total/count;

        if (avrg.toString().indexOf('.') !== -1 && avrg.toString().split('.')[1].length > 2){
            return avrg.toFixed(2);
        }
        return avrg;
    }
    return average;
}
