#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        string lastWord = "";
        int i = s.length() - 1;
        while (s[i] != ' ') {
            lastWord = s[i] + lastWord;
            i--;
        }
        return lastWord.length();
    }
};
