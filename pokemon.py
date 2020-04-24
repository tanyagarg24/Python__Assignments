myfile= open(r"C:\Users\ASUS\Downloads\pokemon.csv","r")

data= myfile.readlines()
#data=myfile.read()
print(data)
print("\n")
# for line in data:
#     print(line.strip().split(","))
# for line in data:
#     print(line)
myfile.close()


d = {}
for i in data[1:]:
    temp = i.strip().split(",")
    pokemon = temp[0]
    type_ = temp[1]
    try:
        d[type_].append(pokemon)
    except:
        d[type_] = [pokemon]
print(d)
print("\n")

for k,v in d.items():
    count=0
    count=len(v)
    print(k,count)
    
print("\n")

