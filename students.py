d={}
l=[]
N=int(input("enter the no. of students:"))
for i in range(0,N):
    d["Name"]=input("Enter student's Name:")
    d["Roll"]=input("Enter student's roll no.")
    d["Marks1"]=input("Enter the marks of subject 1:")
    d["Marks2"]=input("Enter the marks of subject 2:")
    l.append(d)
    d={}
print(l)