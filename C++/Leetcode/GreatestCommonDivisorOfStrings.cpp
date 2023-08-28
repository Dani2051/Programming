#include <iostream>
#include <string>
#include <functional>
using namespace std;

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        string result = "";
        int count = 1;
        return str1.substr(0, gcd(str1.length(),str2.length()));;
    }
};

int main() {  
  Solution a1;
  string word1 = "ABABAB"; 
  string word2 = "ABAB";

  cout << a1.gcdOfStrings(word1,word2);

  return 0;
};
