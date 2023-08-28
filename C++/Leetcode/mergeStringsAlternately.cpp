#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string word;
        int same;
        int difference1 = -1;
        int difference2 = -1;

        if (word1.length() == word2.length()) {
            same = word1.length();
        }

        else if (word1.length() > word2.length()) {
            same = word2.length();
            difference1 = (word1.length() - word2.length());
        }
        else {
            same = word1.length();
            difference2 = (word2.length() - word1.length());
        }

        for (int i = 0; i < same; i++) {                 
            word += word1[i];                
            word += word2[i];
        }

        for (int j = same; j < (difference1 + same); j++) {                
            word += word1[j];
        }

        for (int k = same; k < (difference2 + same); k++) {                
            word += word2[k];
        }

        return word;
    }
};

int main() {  
  Solution a1;
  string word1 = "24"; 
  string word2 = "13567";
  cout << a1.mergeAlternately(word1,word2);

  return 0;
};
