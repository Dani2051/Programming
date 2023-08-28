import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'DiceGameDB'
)

mycursor = mydb.cursor()

InvalidChars = ['(',')',',','[',']',"'"]
Positions = ['0','1st','2nd','3rd','4th','5th']

CurrentPosition = 1

while CurrentPosition <= 5:

    sql = "SELECT Winner FROM LeaderboardData WHERE Position = %s"
    adr = (CurrentPosition, )
    mycursor.execute(sql,adr)

    myresult = mycursor.fetchall()

    Winner = ''

    for character in str(myresult):
        if character not in InvalidChars:
            Winner = str(Winner) + str(character)

    if Winner != '' and CurrentPosition == 1:
        time.sleep(1)
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