// You'll be passed an array of objects - you must sort them in descending order based on the value of an arbitrarily specified property. For example, when sorted by a, this:

// [
//   {a: 1, b: 3},
//   {a: 3, b: 2},
//   {a: 2, b: 40},
//   {a: 4, b: 12}
// ]
// should return:

// [
//   {a: 4, b: 12},
//   {a: 3, b: 2},
//   {a: 2, b: 40},
//   {a: 1, b: 3}
// ]
// your function must take the form function sortList (sortBy, list)

function sortList (sortBy, list) {
  var listOfNumbers = new Array();
  var sortedListOfNumbers = new Array();
  var sortedListOfObj = new Array();

    for (var obj of list){
      if (sortBy === 'a'){
        listOfNumbers.push(obj.a);
      } else {
        listOfNumbers.push(obj.b);
      }
    }

  
    sortedListOfNumbers = 
      listOfNumbers.sort(function(a,b){return b-a});
    
    for (var i = 0; i < sortedListOfNumbers.length; i++){
      for (var obj of list){
        if (sortBy === 'a'){
          if (obj.a === sortedListOfNumbers[i]){
            sortedListOfObj.push(obj);
            break;
          }      
        }else {
          if (obj.b === sortedListOfNumbers[i]){
            sortedListOfObj.push(obj);
            break;
          }  
        }
      }
    }
    
    
    return sortedListOfObj;
}