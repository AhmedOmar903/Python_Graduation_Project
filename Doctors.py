import csv

DoctorDictionary=dict()




#Shared Function

def Doctor_FunctionUpgradeTheInformations():
    
    
    with open("Doctors_DataBase.csv","w",newline="") as file:
        Data=csv.writer(file)
        for ID in DoctorDictionary:
            Data.writerow([ID,DoctorDictionary[ID]["DEPARTMENT"],DoctorDictionary[ID]["NAME"],DoctorDictionary[ID]["PHONE"],DoctorDictionary[ID]["EMAIL"]])
    
    




#Add Function
def Doctor_FunctionUsedToAddAnewDoctorToTheDataBase():
    
    Id=input("Please Enter The ID For The New Doctor : ")
    while Id in DoctorDictionary:
        Id=input("Please Enter The Another ID For The New Doctor : ")
    Department=input("Please Enter The Department Of The New Doctor : ")
    Department=Department.upper()
    Name=input("Please  Enter The Name Of The New Doctor : ")
    Phone=input("Please Enter The Phone Number Of The New Doctor : ")
    Email=input("Please Enter The Email Of The New Doctor : ")
    
    DoctorDictionary[Id]={"DEPARTMENT":Department,"NAME":Name,"PHONE":Phone,"EMAIL":Email}
    with open("Doctors_DataBase.csv","a",newline="") as file:
        Data=csv.writer(file)
        Data.writerow([Id,Department,Name,Phone,Email])


#Edit Function
def Doctor_FunctionEditTheDoctorsInformations():
    ID=input("Please Enter The Doctor ID to Edit : ")
    
    if ID in DoctorDictionary:
       Phone=input("Please Enter The New Phone Number Of  Doctor "+str(DoctorDictionary[ID]["NAME"])+" : ")
       Email=input("Please Enter The Email Of  Doctor "+str(DoctorDictionary[ID]["NAME"])+" : ")
       DoctorDictionary[ID]["PHONE"]=Phone
       DoctorDictionary[ID]["EMAIL"]=Email
       print("Doctor "+DoctorDictionary[ID]["NAME"]+" Data Was successufully Updated .")
       Doctor_FunctionUpgradeTheInformations()
    else:
        print("Wrong ID")


#Delete Function

def Doctor_FunctionDeleteDoctorInformation():
    ID=input("Please Enter The Doctor ID to Delete : ")
    
    if ID in DoctorDictionary:
       print("Doctor "+DoctorDictionary[ID]["NAME"]+" Data Was successufully Deleted .")
       DoctorDictionary.pop(ID)
       Doctor_FunctionUpgradeTheInformations()
    else:
        print("Wrong ID")
    



#Display Function

def Doctor_FunctionDisplayTheDoctorInformation():
    ID=input("Please Enter The Doctor ID to Delete : ")
    if ID in DoctorDictionary:
        print("\n\n\n\n\n")
        print("Doctor Department     : "+DoctorDictionary[ID]["DEPARTMENT"])
        print("Doctor Doctor Name    : "+DoctorDictionary[ID]["NAME"])
        print("Doctor Email Address  : "+DoctorDictionary[ID]["EMAIL"])
        print("Doctor Phone Number   : "+DoctorDictionary[ID]["PHONE"])
    else:
        print("Wrong ID")
    
#Main Function

def Doctor_MainFunction():

    while 1:
      print("\n\n\n\n\n\n\n\n")
      print("//////////////////////////////////////")
      print("**************************************")
      print("To Add     Doctors  Press 1")
      print("To Edit    Doctors  Press 2")
      print("To Delete  Doctors  Press 3")
      print("To Display Doctors  Press 4")
      print("To       Exit       Press 0")
      print("**************************************")
      print("//////////////////////////////////////")
      Choice=input("Your Choice >> ")
      
      if Choice =="1":
        Doctor_FunctionUsedToAddAnewDoctorToTheDataBase()
      elif Choice =="2":  
        Doctor_FunctionEditTheDoctorsInformations()
      elif Choice=="3":
        Doctor_FunctionDeleteDoctorInformation()
      elif Choice=="4":
        Doctor_FunctionDisplayTheDoctorInformation()
      elif Choice =="0":
        break
        