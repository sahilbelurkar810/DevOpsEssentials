

i=1
while(i<=50):
    if(i%2==0 and i%3==0):
        print(" FIZZ BUZZ")
        i+=1
    elif(i%2==0):
        print(" FIZZ")
        i+=1
    elif(i%3==0):
        print(" BUZZ")
        i+=1
    else:
        print(f"{i}")
        i+=1
