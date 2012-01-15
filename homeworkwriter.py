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
    if per=="1":
        agenda.write("Period 1:")
        agenda.write(hw)
        agenda.write("\n")
    if per=="2":
        agenda.write("Period 2:")
        agenda.write(hw)
        agenda.write("\n")
    if per=="3":
        agenda.write("Period 3:")
        agenda.write(hw)
        agenda.write("\n")
    if per=="4":
        agenda.write("Period 4:")
        agenda.write(hw)
        agenda.write("\n")
    if per=="5":
        agenda.write("Period 5:")
        agenda.write(hw)
        agenda.write("\n")
    if per=="6":
        agenda.write("Period 6:")
        agenda.write(hw)
        agenda.write("\n")
    if per=="7":
        agenda.write("Period 7:")
        agenda.write(hw)
        agenda.write("\n")
    if per=="8":
        agenda.write("Period 8:")
        agenda.write(hw)
        agenda.write("\n")
    

def clear():#clear the whole thing
   ajenda = open('agenda.txt', 'r+')
   ajenda.truncate()
def read():#read the homework
    read=open("agenda.txt","r")
    readf=read.read()
    print(readf)
    read.close
choice()
agenda.close()

    
    
