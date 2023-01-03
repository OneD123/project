def enter():
    import csv
    with open("course.csv","w") as file:
        writer=csv.writer(file)
        write.writerow(["Course Id","Course Name","Marksheet"])
    noofdata=int(input("Enter the number of data:"))
    for i in range(noofdata):
        
        CourseID=input("Enter the course ID:")
        CourseName=input("Enter the course name:")
        marksobtained=input("Enter the Mark Obtained:")
        writer.writerow(CourseID,CourseNamwe,Marksobtained)
        
        def performance():
            import csv
            with open("innovators.csv","r") as file:
                      reader=csv.reader(file)
                      for row in reader:
                      print(row)

                      def show():
                          import pandas as pd
                          database1=pd.read_csv("course.csv")
                          database2=pd.read_csv("student.csv")
                          data1=database1.iloc[:,1:3].values
                          data2=database1.iloc[:,1:2].values
                          data3=database2.iloc[:,1:2].values
                          print(data1,data2,data3)
                          def histo():
                              import pandas as pd
                              import matplotlib.pyplot as plt
                              import    
                          
                        
    
