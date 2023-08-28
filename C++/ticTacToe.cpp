#include <iostream> 
#include <string> 
using namespace std;

void printBoard(char board[8]) {
    cout << endl << " " << board[0] << " |";
    cout << " " << board[1] << " |";
    cout << " " << board[2] << endl;
    cout << "-----------" << endl;
    cout << " " << board[3] << " |";
    cout << " " << board[4] << " |";
    cout << " " << board[5] << endl;
    cout << "-----------" << endl;
    cout << " " << board[6] << " |";
    cout << " " << board[7] << " |";
    cout << " " << board[8] << endl;
}

void addMove(char player, int position, char board[9]) {
    board[position] = player;
}

int main() {
    char board[9] {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
    cout << "welcome:";
    printBoard(board);
    addMove('X', 2, board);
    printBoard(board);
    return 0;
}