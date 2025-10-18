def age_number(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age has to be positive!")
        if age%2==0:
            print("Age is even")
        else:
            print("Age is odd")
    except ValueError as e:
        print("Exception", e)
user_age=input("Enter your age") 
age_number(user_age)       