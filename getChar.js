/*
Get character from ASCII Value

Write a function getChar which
takes a number and returns the
corresponding ASCII char for
that value.

Example:

getChar(65) # => 'A'
For ASCII table, you can
refer to http://www.asciitable.com/
*/

function getChar(c)
    return String.fromCharCode(c);
}
