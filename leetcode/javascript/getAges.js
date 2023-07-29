/*
Create a function that takes in the sum
and age difference of two people,
calculates their individual ages and
returns the result as an array of the
following format: [olderAge, youngerAge].
Return null if:

1. sum < 0
2. difference < 0
3. either of the calculated ages come out
    to be negative
*/

function getAges(sum, difference){
    if (sum < 0 || difference < 0){
        return null;
    }

    var olderAge = (sum/2) + (difference/2);
    var youngerAge = (sum/2) - (difference/2);

    if (olderAge < 0 || youngerAge < 0){
        return null;
    }

    return [olderAge, youngerAge];
}
