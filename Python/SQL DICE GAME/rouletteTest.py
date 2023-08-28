import random 

bet = 0.39

a = random.randint(0,36)
x = 0
while x <100 :
    x +=1 
    a = random.randint(0,36)
    if a%2 == 0:
        print(a)