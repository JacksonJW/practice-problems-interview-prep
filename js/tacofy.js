/*
If you like Taco Bell, you will be familiar
with their signature doritos locos taco.
They're very good.

Why can't everything be a taco? We're going
to attempt that here, turning every word we
find into the taco bell recipe with each
ingredient.

We want to input a word as a string, and
return a list representing that word as
a taco.

Key

all vowels = beef

t = tomato

l = lettuce

c = cheese

g = guacamole

s = salsa

Note
We do not care about case here. 'S' is
therefore equivalent to 's' in our taco.

Ignore all other letters; we don't want our
taco uneccesarily clustered or else it will
be too difficult to eat.

Note that no matter what ingredients are
passed, our taco will always have a shell.
*/

function tacofy(word) {
    var taco = ["shell"];
    var vowels = /[aeiou]/i;
    for (var i = 0; i < word.length; i++){
        if (vowels.test(word.charAt(i))) {
            taco.push("beef");
        } else if (word.charAt(i).toLowerCase() === "t")  {
            taco.push("tomato");
        } else if (word.charAt(i).toLowerCase() === "l") {
            taco.push("lettuce");
        } else if (word.charAt(i).toLowerCase() === "c"){
            taco.push("cheese");
        } else if (word.charAt(i).toLowerCase() === "g"){
            taco.push("guacamole");
        } else if (word.charAt(i).toLowerCase() === "s"){
            taco.push("salsa");
        }
    }
    taco.push("shell");
    return taco;
}
