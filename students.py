d={}
l=[]
N=int(input("enter the no. of students:"))
for i in range(0,N):
    d["Name"]=input("Enter student's Name:")
    d["Roll"]=input("Enter student's roll no.")
    d["Marks1"]=input("Enter the marks of subject 1:")
    d["Marks2"]=input("Enter the marks of subject 2:")
    d["branch"]=input("enter branch name:")
    l.append(d)
    d={}
print(l)
search=input("Enter a roll no. to search students:")
for d in l:
    if d["Roll"]==search:
        print("student found")
        print(d)
        break
search_del=input("enter a roll no. for delete the details:")
for d in l:
    if d["Roll"]==search_del:
        l.remove(d)
        print("details have deleted")
        print(l)
        break
old_Roll=input("enter a student old roll no.")
for d in l:
    if d["Roll"]==old_Roll:
        New_Roll=input("enter a roll no to update:")
        d["Roll"]=New_Roll
        print("roll no. updated successfully")
        print(d)
        print(l)
        break