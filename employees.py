myfile=open(r"C:\Users\ASUS\Downloads\employees.csv","r")
data=myfile.readlines()
# print(data)
nlist=[]
avg=0
len=0
for i in data[1:]:
    #print(i)
    temp=i.strip().split(",")
    #print(temp[0]+" " +temp[4]+" "+temp[7])
    nlist.append(temp[0])
    nlist.sort()
    avg=avg+int(temp[4])
    len+=1
    avgs=avg/len
    if(int(temp[4])>avgs):
        print(temp[0])
#     if(temp[7]=="Product" or temp[7]=="Engineering"):
#         print(i)
print(nlist)
    
