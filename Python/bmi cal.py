#bmi calculator 3

name = input("What is your name? ")
weight_kg = input("How much do you weigh in KG? ")
height_m = input("What is your height in meters?")

def bmi_calculator (name, weight_kg, height_m):
    bmi = int(weight_kg) / (int(height_m) ** 2)
    print('bmi: ')
    print(bmi)
     
    if bmi < 18.5:
        print('underwight')
    elif bmi <= 24.9:
        print('healthy')
    elif bmi <= 30:
        print('overweight')
    elif bmi <= 40:
        print('obese')
    elif bmi > 40:
        print('morbidly obese')


bmi_calculator (name, weight_kg, height_m)







