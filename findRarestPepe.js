/*
The pepe market is on the verge of collapse.
In a last ditch attempt to make some quick
cash, you decide to sift through the thousands
of pepes on the Internet in order to identify
the rarest, which are worth more. Since this
would be tedious to do by hand, you decide to
use your programming skills to streamline the
process.

Your task in this kata is to implement a
function that, given a list of pepes (pepes),
returns the rarest pepe in the list. If two or
more pepes are equally rare, return a list of
these pepes, sorted in alphabetical order. Also,
if the rarest pepe (or pepes) has a frequency of
5 or more, then it is not really a rare pepe, so
your function should return 'No rare pepes!'.
*/

/*Trying to do this at O(n) runtime*/
function findRarestPepe(pepes){
    var isRarePepeObj = {};
    var rarePepeArr = [];
    var lowestNumberOfPepes = 0;

    for (var i = 0; i < pepes.length; i++){
        if (isRarePepeObj[pepes[i]] === undefined){
            isRarePepeObj[pepes[i]] = 0;
        } else {
            isRarePepeObj[pepes[i]] += 1;
        }
    }

    for (var rarePepe in isRarePepeObj){
        lowestNumberOfPepes = isRarePepeObj[rarePepe];
    }

    for (var rarePepe in isRarePepeObj){
        if (isRarePepeObj[rarePepe] < lowestNumberOfPepes){
            lowestNumberOfPepes = isRarePepeObj[rarePepe];
        }
    }

    for (var rarePepe in isRarePepeObj){
        if (isRarePepeObj[rarePepe] === lowestNumberOfPepes){
            rarePepeArr.push(rarePepe);
        }
    }

    rarePepeArr.sort();

    if (rarePepeArr.length >= 5 || lowestNumberOfPepes >= 5){
        return "No rare pepes!";
    } else if (rarePepeArr.length === 1){
        rarePepeArr = rarePepeArr.join('');
    }

    return rarePepeArr;
}
