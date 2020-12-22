from Doctors import Doctor_MainFunction
from Patients import Patients_MainFunction



#This Function Is used to Check wherether The Password Right or Wrong
def Admin_FunctionThatCheckThePassword():
    RealPassword="1234"
    Vaildation=0
    Index=0
    InputPassword=input("Please Enter The Password : ")
    while Index <2 :
        if(InputPassword==RealPassword) :
            Vaildation=1
            break;
        else:
            InputPassword=input("Wrong Password Try Again : ")
        Index+=1
    if Vaildation ==0:    
        print("Try Again Later !!!")
    return Vaildation
    
    
    
    

def Admin_MainFunction():
    
    ValidatePassword=Admin_FunctionThatCheckThePassword()
    
    if(ValidatePassword==1):
        while 1:
            print("\n\n\n\n\n\n\n\n")
            print("//////////////////////////////////////")
            print("**************************************")
            print("To Mange The Doctors      Press 1")
            print("To Mange The Patients     Press 2")
            print("To       Exit         Press 0")
            print("**************************************")
            print("//////////////////////////////////////")
            Choice=input("Your Choice >> ")
            if Choice =="1":
                Doctor_MainFunction()
            elif Choice=="2":
                Patients_MainFunction()
            elif Choice =="0":
                break
    
    
    

