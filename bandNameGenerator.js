/*
My friend wants a new band name for her band.
She like bands that use the formula: 'The' +
a noun with first letter capitalized.

dolphin -> The Dolphin

However, when a noun STARTS and ENDS with the
same letter, she likes to repeat the noun
twice and connect them together with the first
and last letter, combined into one word like
so (WITHOUT a 'The' in front):

alaska -> Alaskalaska

europe -> Europeurope

Can you write a function that takes in a noun
as a string, and returns her preferred band
name written as a string?
*/

function bandNameGenerator(str) {
    var resultStr = "";
    if (str.charAt(0) === str.charAt(str.length - 1)){
        resultStr += str.charAt(0).toUpperCase() + str.slice(1) + str.slice(1);
    } else {
        resultStr += "The " + str.charAt(0).toUpperCase() + str.slice(1);
    }
    return resultStr;
}
