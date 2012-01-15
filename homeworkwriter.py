agenda=open("agenda.txt","a") #open the notepad file
def choice(): #pick the period
    choice=input("type write, read, or clear\n")
    
    if choice=="read":
        read()
    elif choice=="write":
        write()
    elif choice=="clear":
        clear()
    else:
        print("Invalid Choice")
        
    
def write(): #write the homework
    per=input("What period is it")
    hw=input("What is the homework")
    if per.isdigit() && len(per)==1:
        agenda.write("Period "+per+":"
        agenda.write(hw)
        agenda.write("\n")
    else:
        print("Non existant period")
    again=input("Would you like to read the homework, clear, or read again? (yes or no)")
    if again=="yes":
        choice()
    elif again=="no":
        print("\n")
    
    

def clear():#clear the whole thing
   ajenda = open('agenda.txt', 'r+')
   ajenda.truncate()
   again=input("Would you like to read the homework, clear, or read again? (yes or no)")
   if again=="yes":
       choice()
   elif again=="no":
       print("\n")
   
def read():#read the homework
    read=open("agenda.txt","r")
    readf=read.read()
    print(readf)
    read.close
    again=input("Would you like to read the homework, clear, or read again? (yes or no)")
    if again=="yes":
        choice()
    elif again=="no":
        print("\n")
    
choice()
agenda.close()

    
    
