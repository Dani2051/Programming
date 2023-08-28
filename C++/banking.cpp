#include <iostream>
#include <string> 
#include <iomanip>
#include <vector>
using namespace std;

class Account {
    private:
        float accBalance;
        int accNo;
        string accName;
        string accPassword;

    public: 
        static int numOfAccounts;

    // constructor
    public: Account(string name, string password) {
        accName = name;
        accPassword = password;
        numOfAccounts++; 
        accNo = numOfAccounts + rand();
        cout << endl << "Account created" << endl;
        cout << "Account Number: " << setfill('0') << setw(8) << accNo << endl;
        cout << "Name: " << accName << endl << "Password: " << accPassword << endl;
    }

    // methods
    public: double balance(){
        return accBalance;
    }

    // setters and getters
    public: double deposit(double depositAmount) {
        if (depositAmount > 1000) {
            cout << "Too much in one go!" << endl;
        }

        else {
            accBalance += depositAmount;
            cout << depositAmount << " has been sucessfully deposited to account " << accNo << " your new balance is " << accBalance << endl;
        }   
        return 0;
    }

    public: int setAccNo(int accNo) {
        return 0;
    }

    public: double withdraw(double withdrawAmount) {
        if (accBalance >= withdrawAmount) {
            accBalance -= withdrawAmount;
            cout << withdrawAmount << " withdrawn. Your balance is now " << accBalance << endl;
        }

        else {
            cout << "You do not have enough in your account to withdraw " << withdrawAmount << ". Your balance is " << accBalance;
        }

        return 0;
    }

    public: int accountInfo() {
        cout << accBalance << endl << accNo << endl;
        return 0; 
    }
};

int Account::numOfAccounts = 0;

void registerAccount() {
    string name;
    string password;
    cout << "Name: ";
    cin >> name;
    cout << "Password:";
    cin >> password;
    Account account1(name, password);
}

void loginAccount() {
}

int main()
{
    string decision; 
    cout << endl << "Do you want to register for an account or login? (register/login) " << endl << endl;
    cin >> decision;

    if (decision == "register"){
        registerAccount();
    }

    else if (decision == "login") {
        loginAccount();
    }

    else {
        cout << endl << "That is an invalid input. Please try again" << endl;
        main();
    }
    
    return 0;
}










