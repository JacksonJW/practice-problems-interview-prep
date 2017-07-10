/*
Mr. Safety loves numeric locks and his
Nokia 3310. He locked almost everything
in his house. He is so smart and he
doesn't need to remember the combinations.
He has an algorithm to generate new
passcodes on his Nokia cell phone.

Task

Can you crack his numeric locks?
Mr. Safety's treasures wait for you. Write
an algorithm to open his numeric locks. Can
you do it without his Nokia 3310?

Input

The str or message (Python) input string
consists of lowercase and upercase
characters. It's a real object that you want
to unlock.

Output

Return a string that only consists of digits.
Example

unlock("Nokia")  // => 66542
unlock("Valut")  // => 82588
unlock("toilet") // => 864538
*/


function unlock(str){
    return str.split('').map(function(letter) {
        if (/[abc]/i.test(letter)){
            return 2;
        } else if (/[def]/i.test(letter)){
            return 3;
        } else if (/[ghi]/i.test(letter)){
            return 4;
        } else if (/[jkl]/i.test(letter)){
            return 5;
        } else if (/[mno]/i.test(letter)){
            return 6;
        } else if (/[pqrs]/i.test(letter)){
            return 7;
        } else if (/[tuv]/i.test(letter)){
            return 8;
        } else if (/[wxyz]/i.test(letter)){
            return 9;
        } else {
            return 1;
        }
    }).join('');
}
