#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string convertToTitle(int columnNumber) {
        string alphabet[] = {"", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
        string result;

        while (columnNumber > 26) {
            if (columnNumber / 26 < 27) {
                result = alphabet[(columnNumber / 26) - 1] + alphabet[columnNumber - 26];
                break;
            }
        }

        return result;
    }
};

int main() {  
  Solution a1;
  int columnNumber = 51;
  cout << a1.convertToTitle(columnNumber);

  return 0;
};
