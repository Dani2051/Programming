#include <string>
#include <iostream>
#include <sstream>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        string word;
        istringstream(x) >> word;
        cout << word;
        /*int length = word.length() - 1

        for (int i = length; i > 0; i++) {
            string += x[i]
        }*/
        return true;
    }
};

int main() {
    Solution test;

    test.isPalindrome(123);

    return 0;
};