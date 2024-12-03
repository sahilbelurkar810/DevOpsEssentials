# var = 10
# var +=30
# var -= 1
# var /= 12
# var *= 45
# print(var)

# num1 = int(input("enter an number : "))
# # num2 = int(input("enter another number"))
# # # choice = input("enter your choice")
# # print(f"Entered numbers are {num1} and {num2}\n the sum is {num1+num2}")
# i = 1
# print(f"{num1} * {i} = {num1*i}")
# i+=1
# print(f"{num1} * {i} = {num1*i}")
# i+=1
# print(f"{num1} * {i} = {num1*i}")
# i+=1
# print(f"{num1} * {i} = {num1*i}")
# i+=1
# print(f"{num1} * {i} = {num1*i}")
# i+=1
# print(f"{num1} * {i} = {num1*i}")
# i+=1
# print(f"{num1} * {i} = {num1*i}")
# i+=1
# print(f"{num1} * {i} = {num1*i}")
# i+=1
# print(f"{num1} * {i} = {num1*i}")
# i+=1
# print(f"{num1} * {i} = {num1*i}")


var1 = 10
var2 = 20
print(f"\nBefore swapping var1:{var1} and var2:{var2}")
temp = var1
var1 = var2
var2 = temp
print(f"\nAfter swapping var1: {var1} and var2: {var2}")
print("\nRESWAPPING")
var1,var2=var2,var1
print(f"\nAfter swapping var1: {var1} and var2: {var2}")
print("\nRESWAPPING")

var1 += var2
var2 = var1 - var2
var1 = var1 - var2
print(f"\nAfter swapping var1: {var1} and var2: {var2}")


print("using xor")
var1 = var1 ^ var2
var2 = var1 ^ var2
var1 = var1 ^ var2
print(f"\nAfter swapping var1: {var1} and var2: {var2}")

# for i in range(1,11):
#     print(f"{num1} * {i} = {num1*i}")


