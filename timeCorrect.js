function timeCorrect(timestring) {
  if (timestring == null){
    return null;
  }
  if (timestring == ''){
    return '';
  }
  var timestringArr = timestring.split(':');
  var strToNum = 0;
  var newtimestring = "";
  var hours = 0;
  var minutes = 0;
  var seconds = 0;
  var hoursStr = "";
  var minutesStr = "";
  var secondsStr = "";
  
  if (timestringArr.length !== 3 || timestringArr[0].match(/[a-z]/i)  
          || timestringArr[1].match(/[a-z]/i) || timestringArr[2].match(/[a-z]/i)){
    return null;
  }
  
  for (var i = timestringArr.length - 1; i >= 0; i--){
    strToNum = parseInt(timestringArr[i]);
    if(i === 2){
      seconds +=strToNum;
      if (seconds >= 60){
        seconds %= 60;
        minutes+=1;
      }
    } else if(i === 1){
      minutes +=strToNum;
      if (minutes >= 60){
        minutes %= 60;
        hours+=1;
      }
    } else {
      hours +=strToNum;
      if (hours >= 24){
        hours %= 24;
      }
    }
  }
  
  if (String(hours).length < 2){
    hoursStr += '0'+ String(hours);
  } else {
    hoursStr = String(hours);
  }
  
  if (String(minutes).length < 2){
    minutesStr += '0'+ String(minutes);
  } else {
    minutesStr = String(minutes);
  }
  
  if (String(seconds).length < 2){
    secondsStr += '0'+ String(seconds);
  } else {
    secondsStr = String(seconds);
  }

  return "" + hoursStr + ':' + minutesStr + ':' + secondsStr;
}