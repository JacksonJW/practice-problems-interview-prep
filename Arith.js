/*
Add two English words together!

Implement a class Arith such that

  var k = new Arith("three");
  k.add("seven"); //this should return "ten"

Input - Will be between zero and ten
and will always be in lower case

Output - Word representation of the result of
the addition. Should be in lower case
*/
function Arith (word) {
    this.getStr = function (int) {
      	if (int === 0){
          return "zero";
        } else if (int === 1){
          return "one";
        } else if (int === 2){
          return "two";
        } else if (int === 3){
          return "three";
        } else if (int === 4){
          return "four";
        } else if (int === 5){
          return "five";
        } else if (int === 6){
          return "six";
        } else if (int === 7){
          return "seven";
        } else if (int === 8){
          return "eight";
        } else if (int === 9){
          return "nine";
        } else if (int === 10){
          return "ten";
        } else if (int === 11){
          return "eleven";
        } else if (int === 12){
          return "twelve";
        } else if (int === 13){
          return "thirteen";
        } else if (int === 14){
          return "fourteen";
        } else if (int === 15){
          return "fifteen";
        } else if (int === 16){
          return "sixteen";
        } else if (int === 17){
          return "seventeen";
        } else if (int === 18){
          return "eighteen";
        } else if (int === 19){
          return "nineteen";
        } else if (int === 20){
          return "twenty";
        } else {
          return "out of bounds"
        }
    }

    this.getNum = function () {
      	if (word === "zero"){
          return 0;
        } else if (word === "one"){
          return 1;
        } else if (word === "two"){
          return 2;
        } else if (word === "three"){
          return 3;
        } else if (word === "four"){
          return 4;
        } else if (word === "five"){
          return 5;
        } else if (word === "six"){
          return 6;
        } else if (word === "seven"){
          return 7;
        } else if (word === "eight"){
          return 8;
        } else if (word === "nine"){
          return 9;
        } else if (word === "ten"){
          return 10;
        } else {
          return NaN;
        }
	}

	this.add = function (newWord) {
        var newWord = new Arith(newWord);
        return this.getStr(newWord.getNum() + this.getNum());
    }

}
