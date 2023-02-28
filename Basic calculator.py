#Our project target is build a basic calculator

# taking the value from the input 
number1=int(input("Enter the first number for calculate : "))
sign=input("Enter the sign for calculate . Between (+ - * / %) : ")
number2=int(input("Enter the second number for calculate : "))

#funtional parts 

if sign=="+":
    print(f"The sum is {number1+number2}")
elif sign=="-":
    print(f"The subtruction is {number1-number2}")
elif sign =="*":
    print(f"The multiplication is {number1*number2}")
elif sign =="/":
    print(f"The Division is {number1/number2}")
elif sign =="%":
    print(f"The remindar is {number1%number2}")
else:
    print("Invalid Calculation.Try again")






#coded by Shougot mollik

