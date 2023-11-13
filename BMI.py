height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI=weight/(height*height)
a=round(BMI)

if BMI < 18.5:
    print("Your BMI is {}, you are underweight.".format(a))
elif BMI < 25:
    print("Your BMI is {}, you have a normal weight.".format(a))
elif BMI < 30:
    print("Your BMI is {}, you are slightly overweight.".format(a))
elif BMI < 35:
    print("Your BMI is {}, you are obese.".format(a))
else:
    print("Your BMI is {}, you clinically obese.".format(a))