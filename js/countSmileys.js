// Description:
// Given an array (arr) as an argument complete the
// function countSmileys that should return the total
// number of smiling faces.
//
// Rules for a smiling face:
// -Each smiley face must contain a valid pair of eyes.
// Eyes can be marked as : or ;
// -A smiley face can have a nose but it does not have
// to. Valid characters for a nose are - or ~
// -Every smiling face must have a smiling mouth that
// should be marked with either ) or D.
// Valid smiley face examples:
// :) :D ;-D :~)
// Invalid smiley faces:
// ;( :> :} :]

function countSmileys(arr) {
    var smileyCount = 0;

    for (var element of arr){

        if (element.charAt(0) === ':' || element.charAt(0) === ';'){
            if (element.charAt(1) === '-' || element.charAt(1) === '~'){
                if (element.charAt(2) === 'D' || element.charAt(2) === ')'){
                    smileyCount++;
                }
            } else if (element.charAt(1) === ')' || element.charAt(1) === 'D'){
                smileyCount++;
            } else {
            }
        }

    }
    return smileyCount;
}

//Assumes that there is no char that exists after the mouth of the smiley face
