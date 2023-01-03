def enter(): 
  import csv
file=open("student.csv","w",newline='')
    
student=csv.writer(file)

student.writerow(["Studentid","Name","Roll","Batch"])
data=int(input("Enter the details of the student"))
for i in range(data):
    studentid=int(input("Student id"))
    Name=input("Name")
    Rollnumber=int(input(("Roll number")))
    Batchname=input("Batch:")
    student.writerow(Studentid,Name,roll,Batch)
    file.close() 
   
    def update():
      import pandas as pd
      df=pd.read_csv("student.csv")
      a=input("Enter the student id:")
      if s== "CSE2201":
        print("1. To update the name")       
        print("2.. To update the class roll number")
        print("3 To update the batch name")
        ch= int(input("Enter your choice:"))
        if ch==1:
          b=input("Enter the name")
          df.loc[]1,[name]=b
        
elif ch==2:
x=input("Enter the roll number")
df.loc[1,roll number]=x

elif ch==3:
d=input("Enter the batch name")
df.loc[1,d]
else:
   print ("Invalid choice")
   
   def generate():
total marks = 0
total subjects = 0
marks=input()
subjects=input()
      total marks=+marks
      total subjects=+subjects
       
      percentage=total marks/total subjects
