#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        int length = s.length() - 1;
        int value = 0;
        bool skip = false;

        for (int i = 0; i <= length; i++) {
            if (skip == false) {
                if (s[i] == 'I') {
                    if (s[i + 1] == 'V') {
                        value += 4;
                        skip = true;
                    } 
                    else if (s[i + 1] == 'X') {
                        value += 9;
                        skip = true;
                    } 
                    else {
                        value += 1;
                    }
                }
                else if (s[i] == 'X') {
                    if (s[i + 1] == 'L') {
                        value += 40;
                        skip = true;
                    } 
                    else if (s[i + 1] == 'C') {
                        value += 90;
                        skip = true;
                    } 
                    else {
                        value += 10;
                    }
                }
                else if (s[i] == 'C') {
                    if (s[i + 1] == 'D') {
                        value += 400;
                        skip = true;
                    } 
                    else if (s[i + 1] == 'M') {
                        value += 900;
                        skip = true;
                    } 
                    else {
                        value += 100;
                    }
                }
                else if (s[i] == 'V') {
                    value += 5;
                }
                else if (s[i] == 'L') {
                    value += 50;
                }
                else if (s[i] == 'C') {
                    value += 100;
                }
                else if (s[i] == 'D') {
                    value += 500;
                }
               else if (s[i] == 'M') {
                    value += 1000;
                };
            }
            else { 
               skip = false;
            };
        }
        return value;
    }
};

int main() {
    Solution test;

    cout << test.romanToInt("MCMXCIV");

    return 0;
};

/*

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
*/