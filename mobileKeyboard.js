/*
Mobile Display Keystrokes

Do you remember the old mobile display keyboards?
Do you also remember how inconvenient it was to
write on it?
Well, here you have to calculate how much
keystrokes you have to do for a specific word.

This is the layout:



Return the amount of keystrokes of input str
(! only letters, digits and special characters
in lowercase included in layout without
whitespaces !)

e.g:

mobileKeyboard("123") => 3 (1+1+1)
mobileKeyboard("abc") => 9 (2+3+4)
mobileKeyboard("codewars")
    => 26 (4+4+2+3+2+2+4+5)
*/

function mobileKeyboard(str){
    var keystrokes = function (letter) {
        var strokeNum = { 1: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "#", "*"],
        2: ["a", "d", "g", "j", "m", "p", "t", "w"], 3: ["b", "e", "h", "k", "n", "q", "u", "x"],
        4: ["c", "f", "i", "l", "o", "r", "v", "y"], 5: ["s", "z"] };

        for (var key in strokeNum){
            if (strokeNum[key].indexOf(letter) !== -1){
                return parseInt(key);
            }
        }
    }

    return str.split('').reduce(    function (sum, element){
        return sum + keystrokes(element);
    }, 0);
}
