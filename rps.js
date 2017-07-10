/*
Rock Paper Scissors

Let's play! You have to return which player won!
In case of a draw return Draw!.

Examples:

rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!
*/

const rps = (p1, p2) => {
    var p1Win = "Player 1 won!";
    var p2Win = "Player 2 won!"

    if (p1 === "scissors" && p2 === "paper"){
        return p1Win;
    } else if (p1 === "paper" && p2 === "scissors"){
        return p2Win;
    } else if (p1 === "scissors" && p2 === "rock"){
        return p2Win;
    } else if (p1 === "rock" && p2 === "scissors"){
        return p1Win;
    } else if (p1 === "paper" && p2 === "rock"){
        return p1Win;
    } else if (p1 === "rock" && p2 === "paper"){
        return p2Win;
    } else {
        return "Draw!";
    }
};
