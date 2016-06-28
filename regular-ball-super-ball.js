/*Create a class Ball.

Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

ball1 = new Ball();
ball2 = new Ball("super");

ball1.ballType     //=> "regular"
ball2.ballType     //=> "super"
*/

var Ball = function (ballType) {
     if (ballType === undefined || ballType === "regular") {
          this.ballType = "regular";
     } else if (ballType === "super") {
          this.ballType = "super";
     } else {
          this.ballType = "Please choose a valid ball type.";
     }
}

ball1 = new Ball("super");
alert(ball1.ballType);

//Expected: Will output super
//Result: Outputted Super