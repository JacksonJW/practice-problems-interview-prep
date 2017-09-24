// altERnaTIng cAsE <=> ALTerNAtiNG CaSe

// Define String.prototype.toAlternatingCase (StringUtils.toAlternatingCase(String) in Java)
// such that each lowercase letter
// becomes uppercase and each uppercase
// letter becomes lowercase. For example:

// Note to no Java langs

// You must NOT alter the original string.

String.prototype.toAlternatingCase = function () {
  // Define your method here :)
  var newStr = "";
  for (var i = 0; i < this.length; i++){
    if (this.charAt(i).toUpperCase() === this.charAt(i)){
       newStr += this.charAt(i).toLowerCase();
    } else {
       newStr += this.charAt(i).toUpperCase();  
    }
  }
  return newStr;
}