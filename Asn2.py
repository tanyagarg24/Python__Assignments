#C to F using map function

cel=[87,12,0]
far=list(map(lambda c:((c*9/5)+32),cel))
print(far)


#print users with starting alphabet vowel using filter function

users=['Angela','Frances','Louise','Julie','Brandon','Gary','Kimberly','Lillian','Jeremy',
       'Shawn','Diana','Donna','Lois','Matthew','Joshua']
vowels = "AaEeIiOoUu"
res=list(filter(lambda x:x[0] in vowels,users))
print(res)


#sort data of cars according to year

CarList=['1985 Toyota Camry (622-VRX)','1993 Honda Civic (883-RS9)', 
         '1996 Dodge Neon (G74-LLC)','1966 Ford Mustang (AZUCAR)','1980 Chevrolet Chevette (J43-SMB)']
l= []
for i in CarList:
    i = i.split()
    l.append(i)
#print(l)
def func(elem):
    return elem[0]
l.sort(key=func)
#print(l)
for i in l:
    print(*i)


