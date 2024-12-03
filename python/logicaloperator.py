x = 22
y=12

print(f"{x} < {y} AND {x} > {y} = {(x<y) and (x>y)}")
print(f"{x}  {y} OR {x} > {y} = {(x<y) or (x>y)}")
print(f"{x} > {y} OR {x} > {y} = {(x<y) and (x>y)}")
print(f"{x} > {y} OR {x} > {y} = {(x<y) or (x>y)}")
print(f"{x} Not equal to 22 {not(x==22)}")
