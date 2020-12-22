import csv
from UserMode import User_MainFunction
from AdminMode import Admin_MainFunction
from Doctors import DoctorDictionary
from Patients import PatientsDictionary


#*************************  Try to Read From Doctor Data Base  *******************************************
try :
     
    with open("Doctors_DataBase.csv","r",newline="") as file:
        Reader=csv.reader(file)
        for ROW in Reader:
           DoctorDictionary[ROW[0]]={"DEPARTMENT":ROW[1],"NAME":ROW[2],"PHONE":ROW[3],"EMAIL":ROW[4]} 


except:
    with open("Doctors_DataBase.csv","w",newline="") as file:
        Data=csv.writer(file)

#************************* #************************* #************************* #************************* 





#*************************  Try to Read From Patients Data Base  *******************************************
try :
     
    with open("Patients_DataBase.csv","r",newline="") as file:
        Reader=csv.reader(file)
        for ROW in Reader:
           PatientsDictionary[ROW[0]]={"DEPARTMENT":ROW[1],"DOCTORNAME":ROW[2],"PATIENTNAME":ROW[3],"ROOMNUMBER":ROW[4]} 


except:
    with open("Patients_DataBase.csv","w",newline="") as file:
        Data=csv.writer(file)

#************************* #************************* #************************* #************************* 




print("\n\nAdmin Mode Password is 1234")




while 1:

    print("\n\n\n\n\n\n\n")
    print("//////////////////////////////////////")
    print("**************************************")
    print("To Select User  Mode Press 1")
    print("To Select Admin Mode Press 2")
    print("**************************************")
    print("//////////////////////////////////////")
    Choice=input("Your Choice >> ")
    
    if Choice =="1":
        User_MainFunction()
    elif Choice =="2":
        Admin_MainFunction()
    else:
        print("Invalied Choice")
