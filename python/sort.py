var = [1,2,3,4,5,6,7,10,1,1]
hi = sorted(var)
print(f"{var} \n {hi}")
var.sort(reverse=True)
print(var)
var.reverse()
print(var)


keys=["name","age","address"]
values =["Sahil",22,"Bangalore"]

data = dict(zip(keys,values))
print(data)
data2 = {keys[i]: values[i] for i in range(len(keys))}
print(type(data2))