// Your are given a string. You must replace
// the word(s) coverage by covfefe, however,
// if you don't find the word coverage in the
// string, you must add it at the end of the
// string with a leading space.

function covfefe(str){
    if(!str.includes("coverage")){
        return str + " covfefe";
    }
    var regexp = /coverage/gi;
    return str.replace(regexp,"covfefe");
}
