
def main_menu():
    print("1: Calculate BMI")
    print("2: View Membership Rates")
    print("3: Exit")
main_menu()
option=int(input('Enter the option of your choice:'))
while(option == 1):
    print('Welcome to the BMI calculation!')
    height=float(input("Enter your height:"))
    weight=int(input("Enter your weight"))
    height_m2=height**2
    print('Your height is meter square is:',height_m2)
    BMI=weight/height_m2
    print('Your BMI calculated is:',BMI)
    if(BMI < 18.5):
        print('You are underweight')
    elif(BMI <= 18.5 and BMI >= 25):
        print('You are normal')
    elif(BMI <= 25 and BMI >= 30):
        print('You are overweight')
    elif(BMI > 30):
        print('You are obese')
    else:
        print('Invalid option')       

    while(option == 2):
        print('Welcome to membership rates!')
        type=input('Enter the type of membership you would like:')
        if(type == 'Basic'):
            rate1 = 1000
            print('The rates for weekly membership are:',rate1)
            print('The rates for monthly membership are:',rate1*4)
        elif(type == 'Regular'):
            rate2 = 1500
            print('The rates for weekly membership are:',rate2)
            print('The rates for monthly membership are:',rate2*4)
        elif(type == 'Premium'):
            rate3 = 2000
            print('The rates for weekly membership are:',rate3)
            print('The rates for monthly membership are:',rate3*4)
        else:
            print('Invalid option')

    while(option == 3):
        print("Thank you for your visit user!!!")                         