// Write a function called repeatStr
// which repeats the given string
// tring exactly n times.
//
// repeatStr(6, "I") // "IIIIII"
//
// repeatStr(5, "Hello") //
// "HelloHelloHelloHelloHello"

function repeatStr (num, str) {
    var result = "";
    for (var i = 0; i < num; i++){
        result += str;
    }
    return result ;
}
