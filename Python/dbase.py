import mysql.connector


alphabet = ['(',')',',','[',']',"'"]
mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'DiceGameDB'
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE LoginData (Username varchar(255) UNIQUE NOT NULL, Password varchar(255) NOT NULL)")
InvalidChars = ['(',')',',','[',']',"'"]

def insert(Username,Password):
    sql = "INSERT INTO LoginData (Username, Password) VALUES (%s, %s)"
    val = (Username, Password)
    mycursor.execute(sql, val)
    mydb.commit()

def delete(Username):
    sql = "DELETE FROM LeaderboardData WHERE Position = 2"
    adr = (Username, )
    mycursor.execute(sql,adr)
    mydb.commit()

    if Name != Username:
        print('Username not found')


def find(Username):

    global myresult

    sql = "SELECT Username FROM LoginData WHERE Username = %s"
    adr = (Username, )
    mycursor.execute(sql,adr)

    myresult = mycursor.fetchall()

    for x in myresult:
        Name = ''
        for a in str(myresult):
            if a not in alphabet:
                Name = str(Name) + str(a)

    if str(Name) == str(UNAME):
        print('Account found')

    else:
        print('Account not found')

def all():
    global myresult
    mycursor.execute("SELECT *  FROM LoginData")

    myresult = mycursor.fetchall()
    
    for x in myresult:
        removechars(x)

UNAME = 'Dani123'
PWORD = 'Testing'

#find(UNAME)
#delete(UNAME)
#all()
#insert(UNAME,PWORD)

#"UPDATE LeaderboardData SET WinnerScore = 100 and LoserScore = 82 WHERE Position = 1;"

"ADD PlayerID varchar(100);"


sql = "SELECT * FROM LeaderboardData ORDER BY WinnerScore"

mycursor.execute(sql)

myresult = mycursor.fetchall()

Winner = ""

for character in myresult:
    if character not in InvalidChars:
        Winner = str(Winner) + str(character)

print(Winner)