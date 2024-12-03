#num = int(input("ENter a  number"))
j=1
#print("Using a for loop")
#for i in range(1,11):
#    print(f"{num} X {i} = {num*i}")

print("using while loop")
while(j<=20): 
    if(j%2==0):
        print(f"EVEN {j}")
        print()
    else:
        print(f"ODD {j}",end='\t\t ')
    j+=1
