    #"UPDATE LeaderboardData SET WinnerScore = 100 and LoserScore = 82 WHERE Position = 1;"
    #ViewLeaderboard()
import mysql.connector

mydb1 = mysql.connector.connect (
    host = '2-12.co.uk',
    port = '3306',
    user = 'ddar',
    password = 'tjwa1234',
    database = 'DiceGameDB_Dani'
)

mycursor = mydb1.cursor()

def ChangingPassword(player,Username):#Use Update
    
    Password = input("Create a new password: ")
    Password = Password.strip()
    validuser = False

    for i in Password:
        if i == ' ':
            print("\nUsername cannot contain spaces. Please try again\n")
            ChangingPassword(player,Username)
    
    if len(Password) < 6:
        print("\nPassword is too short, it must be more than 5 characters.\n")
        ChangingPassword(player,Username)
        
    for i in Password:
        if i in numbers:
            validuser = True
            
    if validuser == True:
        open("BUFFER.txt", "w")##############################################################

        for line in open("LoginData.txt","r").readlines(): ##################################
            LogData = line.split()###########################################################
            with open("BUFFER.txt","a") as bufferwrite:######################################
                if Username != LogData[0]:###################################################
                    bufferwrite.write(LogData[0] + " " + LogData[1] + "\n")##################
                else:########################################################################
                    bufferwrite.write(Username + " " + Password + "\n")######################
                bufferwrite.flush()##########################################################

        open("LoginData.txt", "w")###########################################################

        for line in open("BUFFER.txt","r").readlines(): #####################################
            LogData = line.split()###########################################################
            with open("LoginData.txt","a") as loginwrite:####################################
                loginwrite.write(LogData[0] + " " + LogData[1] + "\n")#######################
                loginwrite.flush()###########################################################
        
        loginwrite.close()###################################################################
        os.remove("BUFFER.txt")##############################################################
    
        print("\nYour password has been changed!")
        UserDecision(player)
            
    else:
        print("\nPassword is not strong enough, include a number.\n")
        ChangingPassword(player,Username)

def ChangePassword(player):#
    
    ChangingPasswordOfUser = input("\nPlease enter the username would you like to change the password of: ")
    ChangingPasswordOfUser = ChangingPasswordOfUser.lower()
    ChangingPasswordOfUser = ChangingPasswordOfUser.strip()

    for i in ChangingPasswordOfUser:
        if i == ' ':
            print("\nUsername cannot contain spaces. Please try again")
            ChangePassword(player)

    OldPassword = input("Please enter the old password: ")
    OldPassword = OldPassword.strip()

    for i in OldPassword:
        if i == ' ':
            print("\nPassword cannot contain spaces. Please try again")
            ChangePassword(player)

    Login = False
    for line in open("LoginData.txt","r").readlines(): ###############################
        LogData = line.split()########################################################
        if ChangingPasswordOfUser == LogData[0] and OldPassword == LogData[1]:########
            login = True
            ChangingPassword(player,ChangingPasswordOfUser)
            
    if Login == False:
        InvalidLogin(player)    

def WritingLeaderboard(Winner,Loser,WinnerScore,LoserScore):#
    
    sql = "UPDATE LeaderboardData SET WinnerScore = %s, LoserScore = %s WHERE Position = %s"
    val = (WinnerScore, LoserScore, 3)
    #sql = "INSERT INTO LeaderboardData (Position, Winner, Loser, WinnerScore, LoserScore) VALUES (%s, %s, %s,%s, %s) WHERE Position = 3"
    #val = (3, Winner, Loser, WinnerScore, LoserScore)

    mycursor.execute(sql, val)
    mydb1.commit()
    #ViewLeaderboard()

WritingLeaderboard('Dani123','Steve20', 39 , 24)