/*
Remember the spongebob meme that is meant to make fun
of people by repeating what they say in a mocking way?

You need to create a function that converts the input
into this format, with the output being the same string
expect there is a pattern of uppercase and lowercase
letters.

Examples:

spongeMeme("stop Making spongebob Memes!")
    // => 'StOp mAkInG SpOnGeBoB MeMeS!'
*/

function spongeMeme(sentence) {
    return sentence.split('').map( function(element, index){
        return index % 2 === 0 ? element.toUpperCase() : element.toLowerCase();
    }).join('');
}
