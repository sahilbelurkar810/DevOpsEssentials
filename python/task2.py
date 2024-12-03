# Calculator
print("Simple Calculator \n")
num1 = int(input("Enter first Operand : "))
num2 = int(input("Enter first Operand : "))

choice = input("What wouyld you like to do\n + : add \n - :substract \n * : Multiply \n / : Divide \n % : modulo \n // : Floor Division \n ^ : Power\n : ")

if (choice == "+"):
    print(f"RESULT is : {num1+num2}")
elif(choice=="-"):
    print(f"RESULT is : {num1-num2}")
elif(choice=="*"):
    print(f"RESULT is : {num1*num2}")
elif(choice=="/"):
    if(num2 == 0):
        print("Division by zero is not possible")
    else:
        print(f"RESULT is : {float(num1)/float(num2)}")
elif(choice=="%"):
    print(f"RESULT is : {num1%num2}")
elif(choice=="//"):
    print(f"RESULT is : {float(num1)//float(num2)}")
elif(choice=="^"):
    print(f"RESULT is : {num1**num2}")
