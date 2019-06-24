import datetime
print('Hello world!')
print('*' * 25)
print("Python-3.7.3")
print("*" * 25)


def print_python():

    print("__")
    print("L"), print("__")
    print("I"), print("__")
    print("N"), print("__")
    print("U"), print("__")
    print("X"), print("__")


print_python()

now = datetime.datetime.now()

if now.hour < 12:
    print("Good Morning!")
else:
    if 12 <= now.hour < 17:
        print("Good Afternoon!")
    else:
        if now.hour >= 17:
            print("Good Evening!")

name = input("Hi! What's your name? ")
colour = input("What's your favourite colour? ")

print(name.capitalize() + " likes " + colour.casefold())

birth_year = input("What's your birth year? ")
age = now.year - int(birth_year)
print(name.capitalize() + " is " + str(age))

if age <= 12:
    print(name.capitalize() + " is a child~ ")
else:
    if 12 < age <= 18:
        print(name.capitalize() + " is a teenager~ ")
    else:
        if 18 < age <= 21:
            print(name.capitalize() + " is a young adult~ ")
        else:
            if age > 21:
                print(name.capitalize() + " is an adult~ ")

weight_kg = input("How many kg(s) do you weight? ")
weight_pound = int(weight_kg) * 2.205
print(str(weight_pound) + " lbs ")

height_cm = input("What's your height(cm)? ")
height_m = int(height_cm) / 100
print(str(height_m) + " m ")

BMI = int(weight_kg) / (height_m * height_m)
print("BMI: " + str(BMI))

if BMI < 18.5:
    print("-Underweight-")
else:
    if 25.0 < BMI < 30.0:
        print("-Overweight-")
    else:
        if BMI >= 30.0:
            print("-Obese-")
        else:
            print("-Healthy-")
