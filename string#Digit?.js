/*
Implement String#digit? (in
Java StringUtils.isDigit(String)), which
should return true if given object is a
digit (0-9), false otherwise.
*/

String.prototype.digit = function() {
    if (this.length === 1){
        return this.match(/\b\d\b/) !== null;
    }
    return false;
};
