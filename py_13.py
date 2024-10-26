try:
    age = int(input("Enter a age of the dog : "))
    
    if age < 0:
        print("You must enter a positive age!")
        exit()
    elif age <= 2:
        human_age = age * 10.5
    else:
        human_age = 21 + (age - 2) * 4
    
    print(f"The age of the dog in human age is {human_age}")
except ValueError:
    print("Please enter only a number!")