try:
    weight = float(input('please enter your weight(kg):'))
    height = float(input('please enter your height(m):'))
    BMI = weight / (height**2)
    if BMI >= 18.5 and BMI < 25:
        print("You have normal weight.")
    elif BMI >= 25 and BMI < 30:
        print("You are overweight.")
    elif BMI >= 30 and BMI < 40:
        print("You are seriously overweight.")
    elif BMI >= 40:
        print("You have obesity.")
    else:
        print("You are underweight.")
except:
    print("Error! Please enter legitimate numbers for weight and height.")