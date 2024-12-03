overdue_days = int(input("Enter the number of overdue days: "))

if overdue_days == 0:
    fine = 0
elif 1 <= overdue_days <= 5:
    fine =  50
elif 6 <= overdue_days <= 10:
    fine =  100
elif overdue_days > 10:
    fine = 500
else:
    fine = 0

print(f"The fine for {overdue_days} overdue days is: {fine} Rs")
