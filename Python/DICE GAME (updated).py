#Daniyaal Dar NEA project

import mysql.connector
import os
import random
import time

#Dice images 
dice1 = (' _____ \n|     |\`n|  ■  |\n|     |\n ¯¯¯¯¯ ')
dice2 = (' _____ \n|■    |\n|     |\n|    ■|\n ¯¯¯¯¯ ')
dice3 = (' _____ \n|■    |\n|  ■  |\n|    ■|\n ¯¯¯¯¯ ')
dice4 = (' _____ \n|■   ■|\n|     |\n|■   ■|\n ¯¯¯¯¯ ')
dice5 = (' _____ \n|■   ■|\n|  ■  |\n|■   ■|\n ¯¯¯¯¯ ')
dice6 = (' _____ \n|■   ■|\n|■   ■|\n|■   ■|\n ¯¯¯¯¯ ')

#Arrays
DiceList = [dice1,dice2,dice3,dice4,dice5,dice6]
Numbers = ['0','1','2','3','4','5','6','7','8','9']
Positions = ['0','1st','2nd','3rd','4th','5th']
InvalidChars = ['(',')',',','[',']',"'"]

mydb1 = mysql.connector.connect (
    host = '2-12.co.uk',
    port = '3306',
    user = 'ddar',
    password = 'tjwa1234',
    database = 'DiceGameDB_Dani'
)

mydb2 = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'DiceGameDB'
)

mycursor = mydb1.cursor()

#Asks the user if they want to play again with the same users
def PlayAgainSamePlayers():

    global RoundNumber
    global Player1Score
    global Player2Score

    RoundNumber = 1
    Player1Score = 0
    Player2Score = 0

    decision = input('\nDo you want to play again with the same players (yes/no) ')
    decision = decision.lower()
    decision = decision.strip()

    if decision == 'yes': 
        Main(Player1)
    elif decision == "no": 
        Start()
    else: 
        print("That is not a valid input. Please try again")
        PlayAgainSamePlayers()

#Asks the user if they would like to play again
def PlayAgain():

    #time.sleep(1)
    decision = input('\nDo you want to play again? (yes/no) ')
    decision = decision.lower()
    decision = decision.strip()

    if decision == 'yes': 
        PlayAgainSamePlayers()
    elif decision == "no": 
        print('\nThank you for playing.')
    else: 
        print("That is not a valid input. Please try again")
        PlayAgain()

#Function prints out the leaderboard. If none found then nothing is printed.
def ViewLeaderboard():

    CurrentPosition = 1
    EndOfTable = False
    while CurrentPosition <= 5 and EndOfTable != True:

        sql = "SELECT Winner FROM LeaderboardData WHERE Position = %s"
        adr = (CurrentPosition, )
        mycursor.execute(sql,adr)

        myresult = mycursor.fetchall()

        Winner = ''

        for character in str(myresult):
            if character not in InvalidChars:
                Winner = str(Winner) + str(character)

        if Winner != '' and CurrentPosition == 1:
            #time.sleep(1)
            print('\n        Leaderboard\n----------------------------')


        if Winner != '':
            sql = "SELECT Loser FROM LeaderboardData WHERE Position = %s"
            adr = (CurrentPosition, )
            mycursor.execute(sql,adr)

            myresult = mycursor.fetchall()

            Loser = ''

            for character in str(myresult):
                if character not in InvalidChars:
                    Loser = str(Loser) + str(character)

            sql = "SELECT WinnerScore FROM LeaderboardData WHERE Position = %s"
            adr = (CurrentPosition, )
            mycursor.execute(sql,adr)

            myresult = mycursor.fetchall()

            WinnerScore = ''

            for character in str(myresult):
                if character not in InvalidChars:
                    WinnerScore = str(WinnerScore) + str(character)

            sql = "SELECT LoserScore FROM LeaderboardData WHERE Position = %s"
            adr = (CurrentPosition, )
            mycursor.execute(sql,adr)

            myresult = mycursor.fetchall()

            LoserScore = ''

            for character in str(myresult):
                if character not in InvalidChars:
                    LoserScore = str(LoserScore) + str(character)

            print(Positions[CurrentPosition] + ' place: ' + str(Winner) + ' vs ' + str(Loser) + ' (' + str(WinnerScore) + '-' + str(LoserScore) + ')')
            CurrentPosition += 1

        else:
            EndOfTable = True

#Function adds a new score to the leaderboard
#If there is a score with the same score achived in the recent game, the recent game score goes above the one in the leaderboard
#This is done to keep the leaderboard fresh and full of the best and most recent scores
def WritingLeaderboard(Winner,Loser,WinnerScore,LoserScore):
    
    WinnerScore = 66
    LoserScore = 40
    
    with open('LeaderboardData.txt', 'r') as leaderboardread:
        firstchar = leaderboardread.read(1)
        if not firstchar: #Checks to see if leaderboard is empty. If it is then it will write the score achieved in the current match into it 
            with open("LeaderboardData.txt","a") as leaderboardwrite:
                leaderboardwrite.write(str(Winner) + ' ' + str(Loser) + ' ' + str(WinnerScore) + ' ' + str(LoserScore))
                leaderboardwrite.flush()
        else:
            Replaced = False
            open("BUFFER.txt", "w") #Opens a buffer file  

            count = 1

            for line in open("LeaderboardData.txt","r").readlines(): #Reads each line in the file
                LogData = line.split() #Differenciates each component based on the space between them e.g Daniyaal Bob 46 23 would show that Daniyaal VS bob (46-23)
                with open("BUFFER.txt","a") as bufferwrite:
                    if WinnerScore > int(LogData[2]) and Replaced == False:
                        Replaced = True 
                        bufferwrite.write(str(Winner) + ' ' + str(Loser) + ' ' + str(WinnerScore) + ' ' + str(LoserScore) + "\n")
                        bufferwrite.write(LogData[0] + " " + LogData[1] + " " + LogData[2] + " " + LogData[3] + "\n")
                        bufferwrite.flush()
                    elif WinnerScore == int(LogData[2]) and LoserScore == int(LogData[3]) and Replaced == False:
                        Replaced = True 
                        bufferwrite.write(str(Winner) + ' ' + str(Loser) + ' ' + str(WinnerScore) + ' ' + str(LoserScore) + "\n")
                        bufferwrite.write(LogData[0] + " " + LogData[1] + " " + LogData[2] + " " + LogData[3] + "\n")
                        bufferwrite.flush()    
                    else:
                        bufferwrite.write(LogData[0] + " " + LogData[1] + " " + LogData[2] + " " + LogData[3] + "\n")
                        bufferwrite.flush()

                count += 1

            if count <= 5 and Replaced == False:
                with open("BUFFER.txt","a") as bufferwrite:
                    bufferwrite.write(str(Winner) + ' ' + str(Loser) + ' ' + str(WinnerScore) + ' ' + str(LoserScore))

            open("LeaderboardData.txt", "w") #This is done to clear the text file 
            count = 1
            
            for line in open("BUFFER.txt","r").readlines(): 
                LogData = line.split()
                if count <= 5:
                    with open("LeaderboardData.txt","a") as leaderboardwrite:
                        leaderboardwrite.write(LogData[0] + " " + LogData[1] + " " + LogData[2] + " " + LogData[3] + "\n")
                        leaderboardwrite.flush()
                        count += 1

            leaderboardwrite.close()        
            os.remove("BUFFER.txt") #Deletes the buffer file

    ViewLeaderboard()

def GameFinished():

    #time.sleep(2)

    if Player1Score == Player2Score:
        print('\nThe game has ended and the scores are tied at ' + str(Player1Score) + '.\ntime for sudden death!')
        SuddenDeath()
    elif Player1Score > Player2Score:
        print('\nThe game has ended. The winner is ' + str(Player1) + ' with a score of ' + str(Player1Score) + '!')
        #time.sleep(1)
        WritingLeaderboard(Player1,Player2,Player1Score,Player2Score)
    elif Player1Score < Player2Score:
        print('\nThe game has ended. The winner is ' + str(Player2) + ' with a score of ' + str(Player2Score) + '!')
        #time.sleep(1)
        WritingLeaderboard(Player2,Player1,Player2Score,Player1Score)  

    PlayAgain()

def SuddenDeath():

    global Player1Score
    global Player2Score

    #time.sleep(1)
    print('\n' + str(Player1) + ("'s turn... "))
    DeathRoll1 = random.randint(1,6)
    print(DiceList[DeathRoll1 - 1])
    #time.sleep(2)
    print('You rolled a ' + str(DeathRoll1))
    #time.sleep(1)

    print('\n' + str(Player2) + ("'s turn... "))
    DeathRoll2 = random.randint(1,6)
    print(DiceList[DeathRoll2 - 1])
    #time.sleep(2)
    print('You rolled a ' + str(DeathRoll2))
    #time.sleep(1)

    Player1Score += DeathRoll1
    Player2Score += DeathRoll2
    #time.sleep(1)

    if DeathRoll1 == DeathRoll2:
        print("\nIt's a tie again. Re-roll")
        SuddenDeath()
    elif Player1Score > Player2Score:
        print('\n' + str(Player1) + ' has won in the sudden death. Congratulations!')
    elif Player1Score < Player2Score:  
        print('\n' + str(Player2) + ' has won in the sudden death. Congratulations!')

    GameFinished()

def Main(PlayerPlaying):

    global RoundNumber
    global Player1Score
    global Player2Score

    ScoreOfPlayerPlaying = 0
    #time.sleep(1)

    if PlayerPlaying == Player1:
        #time.sleep(1)
        print('\nGet ready for round for round ' + str(RoundNumber) + '!')

    #time.sleep(1)
    print('\n' + PlayerPlaying + "'s" + ' turn...')
    #time.sleep(1)
    enter = input('\nPress enter to roll the dice ')

    if PlayerPlaying == Player1:
        ScoreOfPlayerPlaying = Player1Score
    elif PlayerPlaying == Player2:
        ScoreOfPlayerPlaying = Player2Score

    Roll1 = random.randint(1,6)
    Roll2 = random.randint(1,6)

    #time.sleep(2)
    print(DiceList[Roll1 - 1])
    #time.sleep(2)
    print(DiceList[Roll2 - 1])
    TotalRoll = Roll1 + Roll2
    #time.sleep(1)
    print('You rolled a ' + str(Roll1) + ' and a ' + str(Roll2) + ' which totals to ' + str(TotalRoll))
    #time.sleep(1)

    if Roll1 == Roll2:
        print('You rolled a double. You get another roll...')
        #time.sleep(1)
        enter = input('\nPress enter to roll the dice ')
        #time.sleep(2)

        Roll3 = random.randint(1,6)
        print(DiceList[Roll3 - 1])
        TotalRoll += Roll3
        #time.sleep(1)
        print('You rolled a ' + str(Roll3) + ' which means you rolled a total of ' + str(TotalRoll))
        #time.sleep(1)

    if TotalRoll % 2 == 0:
        TotalRoll += 10
        ScoreOfPlayerPlaying += TotalRoll
        print('The total of your roll is even so you gain 10 points. Your score is ' + str(ScoreOfPlayerPlaying))
    else:
        ScoreOfPlayerPlaying += TotalRoll
        ScoreOfPlayerPlaying -=5

        if ScoreOfPlayerPlaying < 0: 
            ScoreOfPlayerPlaying = 0

        print('The total of your roll is odd so you lose 5 points. Your score is ' + str(ScoreOfPlayerPlaying))

    if PlayerPlaying == Player1:
        Player1Score = ScoreOfPlayerPlaying
        Main(Player2)
    elif PlayerPlaying == Player2:
        Player2Score = ScoreOfPlayerPlaying
        RoundNumber += 1
        if RoundNumber != 6:
            Main(Player1)
        elif RoundNumber == 6:
            GameFinished() 

def ChangingPassword(player,Username):
    
    Password = input("Create a new password: ")
    Password = Password.strip()
    validuser = False

    for character in Password:
        if character == ' ':
            print("\nUsername cannot contain spaces. Please try again\n")
            ChangingPassword(player,Username)
    
    if len(Password) < 6:
        print("\nPassword is too short, it must be more than 5 characters.\n")
        ChangingPassword(player,Username)
        
    for character in Password:
        if character in Numbers:
            validuser = True
            
    if validuser == True:
        open("BUFFER.txt", "w")

        for line in open("LoginData.txt","r").readlines(): 
            LogData = line.split()
            with open("BUFFER.txt","a") as bufferwrite:
                if Username != LogData[0]:
                    bufferwrite.write(LogData[0] + " " + LogData[1] + "\n")
                else:
                    bufferwrite.write(Username + " " + Password + "\n")
                bufferwrite.flush()

        open("LoginData.txt", "w")

        for line in open("BUFFER.txt","r").readlines(): 
            LogData = line.split()
            with open("LoginData.txt","a") as loginwrite:
                loginwrite.write(LogData[0] + " " + LogData[1] + "\n")
                loginwrite.flush()
        
        loginwrite.close()
        os.remove("BUFFER.txt")
    
        print("\nYour password has been changed!")
        UserDecision(player)
            
    else:
        print("\nPassword is not strong enough, include a number.\n")
        ChangingPassword(player,Username)
        
def ChangePassword(player):
    
    ChangingPasswordOfUser = input("\nPlease enter the username would you like to change the password of: ")
    ChangingPasswordOfUser = ChangingPasswordOfUser.lower()
    ChangingPasswordOfUser = ChangingPasswordOfUser.strip()

    for character in ChangingPasswordOfUser:
        if character == ' ':
            print("\nUsername cannot contain spaces. Please try again")
            ChangePassword(player)

    OldPassword = input("Please enter the old password: ")
    OldPassword = OldPassword.strip()

    for character in OldPassword:
        if character == ' ':
            print("\nPassword cannot contain spaces. Please try again")
            ChangePassword(player)

    Login = False
    for line in open("LoginData.txt","r").readlines(): 
        LogData = line.split()
        if ChangingPasswordOfUser == LogData[0] and OldPassword == LogData[1]:
            login = True
            ChangingPassword(player,ChangingPasswordOfUser)
            
    if Login == False:
        InvalidLogin(player)    
            
def MakingPassword(player,Username):#
    
    Password = input("Create a new password: ")
    Password = Password.strip()

    validuser = False

    for character in Password:
        if character == ' ':
            print("\nPassword cannot contain spaces. Please try again\n")
            MakingPassword(player,Username)
    
    if len(Password) < 6:
        print("\nPassword is too short, it must be more than 5 characters.\n")
        MakingPassword(player,Username)
        
    for character in Password:
        if character in Numbers:
            validuser = True
            
    if validuser == True:
        sql = "INSERT INTO LoginData (Username, Password) VALUES (%s, %s)"
        val = (Username, Password)
        mycursor.execute(sql, val)
        mydb.commit()
        #time.sleep(1)
        print("\nYour Account has been created!")
        UserDecision(player)
    else:
        print("\nPassword is not strong enough, include a number.\n")
        MakingPassword(player,Username)

def NewUser(player):

    validuser = False
    Username = input("\nCreate a new username: ")
    Username = Username.strip()

    for character in Username:
        if character == ' ':
            print("\nUsername cannot contain spaces. Please try again")
            NewUser(player)
    
    if len(Username) < 6:
        print("\nUsername is too short, it must be more than 5 characters!")
        NewUser(player)
        
    for character in Username:
        if character in Numbers:
            validuser = True         
            
    if validuser != True:
        print("\nUsername is not strong enough, include a number!")
        NewUser(player)
    
    sql = "SELECT Username FROM LoginData WHERE Username = %s"
    adr = (Username, )
    mycursor.execute(sql,adr)

    FetchedResult = mycursor.fetchall()
    FetchedUsername = ''

    for character in str(FetchedResult):
        if character not in InvalidChars:
            FetchedUsername = str(FetchedUsername) + str(character)

    if Username == FetchedUsername:
        print("\nUser already exists please try again.")
        NewUser(player)
    else:
        MakingPassword(player,Username)
        
def InvalidLogin(player):

    decision = input("\nIncorrect username or password. Do you want to log in, change your password or create a new account? (1/2/3) ")
    decision = decision.strip()

    if decision == "1":
        OldUser(player)
    elif decision == "2":
        ChangePassword(player)
    elif decision == "3":
        NewUser(player)
    else: 
        print("\nThat is not a valid input. Please try again.")
        InvalidLogin(player)

def UserAlreadyLogged(player):

    decision = input('\nThat user is already logged in. Do you want to sign in with a differnt user or create a new account? (1/2) ')
    decision = decision.strip()

    if decision == "1":
        OldUser(player)
    elif decision == "2":
        NewUser(player)
    else: 
        print("\nThat is not a valid input. Please try again.")
        UserAlreadyLogged(player)

def OldUser(player):
    
    global Player1 
    global Player2
    global UsersLogged

    Username = input("\nUsername: ")
    Username = Username.strip()

    for character in Username:
        if character == ' ':
            print("\nUsername cannot contain spaces. Please try again")
            OldUser(player)

    if Username == Player1:
        UserAlreadyLogged(player)

    Password = input("Password: ")
    Password = Password.strip()

    for character in Password:
        if character == ' ':
            print("\nPassword cannot contain spaces. Please try again")
            OldUser(player)

    sql = "SELECT Password FROM LoginData WHERE Username = %s"
    adr = (Username, )

    mycursor.execute(sql,adr)

    result = mycursor.fetchall()

    FetchedPassword = ''

    for character in str(result):
        if character not in InvalidChars:
            FetchedPassword = str(FetchedPassword) + str(character)

    #time.sleep(1)

    if str(FetchedPassword) == str(Password):
        print("\n" + player + " login successful!")
        UsersLogged += 1
    else:
        InvalidLogin(player)

    if UsersLogged == 1:
        Player1 = Username
        player = "Player2"
        UserDecision(player)
    else:
        Player2 = Username
        Main(Player1)
                    
def UserDecision(player):

    #time.sleep(1)
    decision = input("\n" + (player) + ", do you already have an account? (Yes/No) ")
    decision = decision.lower()
    decision = decision.strip()

    if decision == 'yes': 
        OldUser(player) 
    elif decision == "no": 
        NewUser(player)
    else: 
        print("That is not a valid input. Please try again")
        UserDecision(player)

def Start():

    global RoundNumber
    global Player1Score
    global Player2Score
    global UsersLogged
    global Player1
    global Player2

    UsersLogged = 0
    RoundNumber = 1
    Player1Score = 0
    Player2Score = 0
    UsersLogged = 0
    Player1 = ''
    Player2 = ''
    
    UserDecision('Player1')

#time.sleep(0.5)
print("Welcome to Danis dice game.")

ViewLeaderboard()
Start()                                                                                                                       
