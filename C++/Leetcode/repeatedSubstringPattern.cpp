#include <iostream>
#include <string>
#include <functional>
using namespace std;

class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        return (s+s).substr(1,2*s.size()-2).find(s)!=-1;
    }
};

int main() {  
  Solution a1;
  string word1 = "ABAABA";

  cout << a1.repeatedSubstringPattern(word1);

  return 0;
};
