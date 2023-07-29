/*
In mathematics, the factorial of integer 'n'
is written as 'n!'. It is equal to the product
of n and every integer preceding it. For
example: 5! = 1 x 2 x 3 x 4 x 5 = 120

Your mission is simple: write a function that
takes an integer 'n' and returns 'n!'.

You are guaranteed an integer argument. For any
values outside the positive range, return null,
nil, None or throw a suitable exception.

Note: 0! is always equal to 1. Negative values
should return null;
*/

function factorial (n) {
    if (n < 0){
        return null;
    }
    if (n === 0){
        return 1;
    }

    var product = 1;
    for (var i = n; i > 0; i--){
        product = product * i;
    }
    return product;
}
