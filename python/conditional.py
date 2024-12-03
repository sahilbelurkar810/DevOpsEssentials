age2 = int(input("enter age of second person:  "))
age1 = int(input("enter age of first person:  "))


if(age1>=18):
    print(f"yay! first person is  eligible")
else:
    print(f"first person is not eligible , you will be eligible after {18-age1}")
if age2 >= 18:
    print(f"yay! second person is  eligible")
else:
    print(f"second person is not eligible , you will be eligible after {18-age2}")
