#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        bool result[sizeof(candies)] = {"true"};
        for (int i : candies) {
            cout << i << "\n";
        }

        return result[1];
    }
};

int main() {  
  Solution a1;
  bool candies[] = {2,3,5,1,3}; 
  int extraCandies = 3;
  cout << a1.kidsWithCandies(candies, extraCandies);

  return 0;
};
