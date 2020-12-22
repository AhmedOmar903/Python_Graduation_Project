import csv
from Doctors import DoctorDictionary

PatientsDictionary=dict()


#***********************************   ADD Patients ********************************************************************

def StaticFunction_UsedToCheckIfTheDepartmentFound(DoctorDepartmentName):
    flag=0
    for ID in DoctorDictionary:
        if DoctorDepartmentName==DoctorDictionary[ID]["DEPARTMENT"]:
            flag=1
            break
    if flag==1:
        DoctorName=StaticFunction_PrintAllTheAssignedDoctors(DoctorDepartmentName)
        return DoctorName,flag
    else:
        print("There is no Department Called "+str(DoctorDepartmentName)+" in the Hospital .")
        return "NO",flag


    
def StaticFunction_PrintAllTheAssignedDoctors(DepartmentName):
    ChossenDoctorList=list()
    i=1 
    print("\n\n")
    for ID in DoctorDictionary :
        if DoctorDictionary[ID]["DEPARTMENT"]==DepartmentName:
            print("Press "+str(i)+" to Choose Doctor  "+DoctorDictionary[ID]["NAME"])
            ChossenDoctorList.append(DoctorDictionary[ID]["NAME"])
            i+=1       
    Choice=input("\n\nPlease Choose The Assigned Doctor : ")
    while int(Choice)<=0 or int(Choice)>=(i):
        Choice=input("\nPlease Choose The Correct Index of The Assigned Doctor : ")
    Choice=ChossenDoctorList[(int(Choice)-1)]
    ChossenDoctorList.clear()
    return Choice


def Patients_FunctionUsedToAddAnewPatientToTheDataBase():

    Department=input("Please Enter the Department Which The Patient is Assigned to : ")
    Department=Department.upper()
    DoctorName,flag=StaticFunction_UsedToCheckIfTheDepartmentFound(Department)
    if flag==1:
        ID=input("Please Enter the Patient ID : ")
        while ID in PatientsDictionary:
            ID=input("Please Enter another ID for the Patient : ")
        PatientName=input("Please Enter the Patient Name : ")
        RoomNumber=input("Please Enter the Room Number : ")
        
        PatientsDictionary[ID]={"DEPARTMENT":Department,"DOCTORNAME":DoctorName,"PATIENTNAME":PatientName,"ROOMNUMBER":RoomNumber}
        
        with open("Patients_DataBase.csv","a",newline="") as file:
            DATA=csv.writer(file)
            DATA.writerow([ID,Department,DoctorName,PatientName,RoomNumber])
    
#***********************************#***********************************#***********************************#*************    
    
    

def staticFunction_PatientEditOrDelete():
        
    with open("Patients_DataBase.csv","w",newline="") as file:
            DATA=csv.writer(file)
            for ID in PatientsDictionary:
                DATA.writerow([ID,PatientsDictionary[ID]["DEPARTMENT"],PatientsDictionary[ID]["DOCTORNAME"],PatientsDictionary[ID]["PATIENTNAME"],PatientsDictionary[ID]["ROOMNUMBER"]]) 




def Patient_FunctionEditThePatientsInformations():
    ID=input("Please Enter The Patient ID to Edit : ")
    if ID in PatientsDictionary :
       Department=input("Please Enter the Department Which The Patient is Assigned to : ")
       Department=Department.upper()
       DoctorName,flag=StaticFunction_UsedToCheckIfTheDepartmentFound(Department)
       if flag==1:
         RoomNumber=input("Please Enter the new Room Number of the patient "+str(PatientsDictionary[ID]["PATIENTNAME"])+" : ")
         PatientsDictionary[ID]["ROOMNUMBER"]=RoomNumber
         staticFunction_PatientEditOrDelete()   
    else:
        print("Wrong ID")



def Patient_FunctionDisplayThePatientInformation():
    ID=input("Please Enter The Patient ID to Display : ")
    if ID in PatientsDictionary:
        print("\n\n\n\n\n")
        print("Patient Department          : "+PatientsDictionary[ID]["DEPARTMENT"])
        print("Patient Assigned Doctor     : "+PatientsDictionary[ID]["DOCTORNAME"])
        print("Patient Name                : "+PatientsDictionary[ID]["PATIENTNAME"])
        print("Patient ROOM Number         : "+PatientsDictionary[ID]["ROOMNUMBER"])
    else:
        print("Wrong ID")







def Patient_FunctionDeletePatientInformation():
    ID=input("Please Enter The Patient ID to Delete : ")
    
    if ID in PatientsDictionary:
       print("Patient "+PatientsDictionary[ID]["PATIENTNAME"]+" Data Was successufully Deleted .")
       PatientsDictionary.pop(ID)
       staticFunction_PatientEditOrDelete()
    else:
        print("Wrong ID") 






def Patients_MainFunction():
    while 1:
      print("\n\n\n\n\n\n\n\n")
      print("//////////////////////////////////////")
      print("**************************************")
      print("To Add     Patient  Press 1")
      print("To Edit    Patient  Press 2")
      print("To Delete  Patient  Press 3")
      print("To Display Patient  Press 4")
      print("To       Exit       Press 0")
      print("**************************************")
      print("//////////////////////////////////////")
      Choice=input("Your Choice >> ")
      
      if Choice =="1":
        Patients_FunctionUsedToAddAnewPatientToTheDataBase()
      elif Choice =="2":  
        Patient_FunctionEditThePatientsInformations()
      elif Choice=="3":
       Patient_FunctionDeletePatientInformation()
      elif Choice=="4":
        Patient_FunctionDisplayThePatientInformation()
      elif Choice =="0":
        break
    



