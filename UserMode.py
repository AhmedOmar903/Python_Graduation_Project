from Doctors import DoctorDictionary
from Patients import PatientsDictionary
from Patients import Patient_FunctionDisplayThePatientInformation


#***********************************   Patients *************************************************************
def UserMode_FunctionDiplayAllThePatientWithTheirRoomNuber():
    UserMode_FunctionUsedToDisplayAllDepartments(PatientsDictionary)
    Department=input("\n\nPlease choose one from The previous Departments To Display its Assigned Patients : ")
    Department=Department.upper()
    i=1
    flag=0
    for ID in PatientsDictionary:
        if PatientsDictionary[ID]["DEPARTMENT"]==Department:
            print("\n\n////*************//************//******")
            print(str(i)+" Patients Name is "+PatientsDictionary[ID]["PATIENTNAME"]+" You can foud him/her at room number "+PatientsDictionary[ID]["ROOMNUMBER"])
            i+=1
            flag=1

    if flag==0:
        print("Sorry There is no Department in the hospital called "+Department)


#***********************************#***********************************#***********************************#*************  







#***********************************   Doctors and Department *************************************************************

def UserMode_FunctionUsedToDisplayAllDepartments(VariableDict):
    DepartmentList=list()
    i=1
    print("\n\n\n\n\n\n\n")
    print("******************** All Departments *********************")
    for ID in VariableDict:
        if VariableDict[ID]["DEPARTMENT"] not in DepartmentList:
            print(str(i)+"- "+str(VariableDict[ID]["DEPARTMENT"]))
            DepartmentList.append(VariableDict[ID]["DEPARTMENT"])
            i+=1
    DepartmentList.clear()


def UserMode_FunctionDisplayAllDepartmentWithItsAssignedDoctors():
    DepartmentList=list()
    for FirstKey in DoctorDictionary:
        if DoctorDictionary[FirstKey]["DEPARTMENT"] not in DepartmentList :
            print("*********************"+DoctorDictionary[FirstKey]["DEPARTMENT"]+"*********************")
            i=1
            for SecandKey in DoctorDictionary:
                if DoctorDictionary[SecandKey]["DEPARTMENT"]==DoctorDictionary[FirstKey]["DEPARTMENT"] :
                    
                    print("\n\n\n")
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print(str(i)+"- Doctor Doctor Name    : "+DoctorDictionary[SecandKey]["NAME"])
                    print(str(i)+"- Doctor Email Address  : "+DoctorDictionary[SecandKey]["EMAIL"])
                    print(str(i)+"- Doctor Phone Number   : "+DoctorDictionary[SecandKey]["PHONE"])
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    i+=1
            DepartmentList.append(DoctorDictionary[FirstKey]["DEPARTMENT"])
    DepartmentList.clear()    

#***********************************#***********************************#***********************************#*************    
  







def User_MainFunction():

    while 1:
        print("\n\n\n\n\n\n\n")
        print("////////////////////////////////////////////////////////////////")
        print("****************************************************************")
        print("To Veiw All the Department Of the Hospital Please        Press 1")
        print("To Veiw All the Doctors Of the Hospital in Details       Press 2")
        print("To Veiw All the Patients Of the Hospital                 Press 3")
        print("To Veiw All the Patients Of the Hospital in Details      Press 4")
        print("To                       EXIT                            Press 0")
        print("****************************************************************")
        print("////////////////////////////////////////////////////////////////")
        Choice=input("Your Choice >> ")
        
        if Choice =="1":
            UserMode_FunctionUsedToDisplayAllDepartments(DoctorDictionary)
        elif Choice =="2":
            UserMode_FunctionDisplayAllDepartmentWithItsAssignedDoctors()
        elif Choice=="3":
            UserMode_FunctionDiplayAllThePatientWithTheirRoomNuber()
        elif Choice=="4":
            Patient_FunctionDisplayThePatientInformation()
        elif Choice =="0":
            break  
    
    