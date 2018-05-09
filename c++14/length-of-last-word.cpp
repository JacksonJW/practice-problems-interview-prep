// From leetcode.com -
// https://leetcode.com/problems/length-of-last-word/description/

// Given a string s consists of upper/lower-case alphabets and empty space
// characters ' ', return the length of last word in the string.
//
// If the last word does not exist, return 0.
//
// Note: A word is defined as a character sequence consists of non-space
// characters only.
//
// Example:
//
// Input: "Hello World"
// Output: 5

#include <string>
#include <stdio.h>
#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(std::string& s) {
        deleteTrailingSpaces(s);
        if (s.length() == 0){
            return 0;
        }
        int i = s.length()-1;
        string lastWord = "";
        while (s[i] != ' ' && i >= 0){
            lastWord = s[i] + lastWord;
            i--;
        }
        return lastWord.length();
    }
private:
    void deleteTrailingSpaces(std::string& s){
        int i = s.length()-1;
        while (s[i] == ' ' && i >= 0) {
            s.erase(i, 1);
            i--;
        }
    }
};
