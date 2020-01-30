import sys
def main():
    print("!!!!!!!!!! Welcome !!!!!!!!!!")
    print("Check Your Body Mass Index and Retirement Plan.")
    print()
    print("Choose one of the following: ")
    print("1: Body Mass Index (BMI)")
    print("2: Retirement")
    print("3: Exit")
    while True:
        try:
            option = int(input("Enter 1 for BMI, 2 for Retirement or 3 to exit. "))
            break
        except ValueError:
            print("Invalid value. Please choose the valid options.")
    while(option):
        if(option == 1):
            bmi, category = calc_bmi()
            print()
            print("!!!!!!!!!Details!!!!!!!!!!!!")
            print("Your Body Mass Index is ",bmi)
            print("According to BMI, you're ",category)
            while True:
                try:
                    option = int(input("Do you want to continue? If yes choose option. "))
                    break
                except ValueError:
                    print("Invalid value. Please choose the valid options.")

                    
        elif (option == 2):
            print(calc_retirement())
            while True:
                try:
                    option = int(input("Do you want to continue? If yes choose option. "))
                    break
                except ValueError:
                    print("Invalid value. Please choose the valid options.")

                    
        elif (option == 3):
            sys.exit()
            
        else:
            while True:
                try:
                    option = int(input("Invalid Option. Please select again. "))
                    break
                except ValueError:
                    print("Invalid Option. Integers Only.")
                


def calc_bmi():
    height = input("Enter height in Feet and Inches:(Ex. 5'3\") ")
    feet, inches = height.split("'")
    total_height = 12*int(feet)+int(inches.strip('"'))
    weight = int(input("Enter the weights in pounds. "))
    weight_in_kg = weight*0.45
    height_in_m = total_height*0.025
    bmi = weight_in_kg/(height_in_m*height_in_m)
    bmi = round(bmi,1)
    if(bmi <= 18.5):
        category = "Underweight"
        return bmi, category
    elif(bmi >= 18.5 and bmi <=24.9):
        category = "Normal Weight"
        return bmi, category
    elif(bmi >= 25 and bmi <= 29.9):
        category = "Over Weight"
        return bmi, category
    else:
        category = "Obese"
        return bmi, category
    
def calc_retirement():
    current_age = int(input("Enter your current age: "))
    annual_salary = int(input("Enter your Annual Salary: "))
    percent_save = input("Enter your percentage saving: (Ex. 35%)")
    percent = int(percent_save.strip('%'))
    save_goal = int(input("Enter the retirement savings goal: "))
                    



main()
