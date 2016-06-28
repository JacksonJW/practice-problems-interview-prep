function isIsogram(str){
  //indexOf
  if (str === "") {
    return true;
  } else{
  
    var strLCase = str.toLowerCase();
    
    for (var i = 0; i < strLCase.length; i++){
      if (strLCase.indexOf(strLCase.charAt(i)) !== strLCase.lastIndexOf(strLCase.charAt(i))){
          return false;
      } 
    } return true;
  }
}