/*
Calculate the product of all elements in an array.

In JavaScript, if the array is null or is empty,
the function should return null.

As a challenge, try writing your method in just one
line of code. It's possible to have only 36
characters within your method.
*/

function product(values) {
    if ( values === null || values.length === 0){
        return null;
    }
    return values.reduce( function (prod, num){
        return prod * num;
    });
}
