import math
def main_menu():
    print("1: Calculate BMI")
    print("2: View Membership rates")

main_menu()
option = input("Enter Your BMI ") 
while option == "BMI":
    print(option)
    print("BMI Calculation Started")
    weight = int(input("Enter Your Weight: "))
    height = int(input("Enter Your Height: "))
    heightSquare = math.pow (height,2)
    BMI = weight / heightSquare
    print(BMI)
    pass
    if BMI < 18.5:
        print("Underweight")
    elif BMI > 18.5 and BMI < 25:
        print("Normal")
    elif BMI > 25 and BMI < 30:
        print("Overweight")
    elif BMI > 30:
        print("Obese")
    else:
        print("Wrong BMI!")



    break
while option == 2:
    def membership_menu():
        print("The Membership rates options are as follows:\n1. Basic\n2. Regular\n3. Premium ")
        Basic = 1000
        Regular = 1500
        Premium = 2000
    membership_menu()    
    MR = int(input("Please select Membership option: "))
    if MR == 1000:
            monthlyBasic = 4000
            print("Your monthly membership rate is: ",monthlyBasic)
    elif MR == 1500:
            monthlyRegular = 6000
            print("Your monthly membership rate is: ",monthlyRegular)
    elif MR == 2000:
            monthlyPremium = 8000
            print("Your monthly membership rate is: ",monthlyPremium)
    else:
            print("Try Again")   
    break         
