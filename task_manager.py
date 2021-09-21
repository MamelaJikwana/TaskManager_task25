import re
import datetime
log_in = False

#==================== REGISTER USER ==================================

#register a user that does not have an account
#if the username exists or the password is incorrect call reg_user()
#if the username does not exit it should be append to the user.txt

def reg_user():
    file = open("user.txt","r")
    name = input("Please create a username: ")  
    password = input("Please create a password: ")
    confirm_password = input("Please confirm your password: ")
    d = {}
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        d[a] = b

        if password != confirm_password:
            print("Passwords do not match. Please re-enter")
            reg_user()
        else:
            if name in d:
                print(name,"aleady exists")
                reg_user()
            else:
                file = open("user.txt","a")
                file.write("\n" + name + "," + password)
                file.close()
    file.close()
    
#==================== USER LOGIN ======================================
    
#if login under begin() was selected. The user should enter their details
#if the user logs in successfully choice() will be called
#if the user logs in successfully and is admin admin_newMenu() will be called
#if the username or password is incorrect the login() will be called
#if the username does not exit the reg_user() will be called
    
def login():
    file = open("user.txt","r")
    name = input("Please enter your username: ")
    password = input("Please enter your password: ")
       
    if not len(name or password) < 1:
        d = {}
        for i in file:
            a,b = i.split(",")
            b = b.strip()
            d[a] = b
        try:
            if d[name]:
                try:
                    if password == d[name]:
                        print("Login successful!")
                        print("Great to have you back,", name)
                        log_in =True
                    else:
                        print("Username or Password incorrect.")
                        login()
                except:
                    print("Username or Password incorrect.")
                    login()
            else:
                print("Username does not exist")
                reg_user()
        except:
            print("Username does not exist")
            reg_user() 
    else:
        print("Please enter an option")
        
    if log_in == True and name == "admin":
        admin_newMenu()
    elif log_in == True:
        choice()
        
#==================== CHOOSE TO REGISTER OR LOGIN =========================
        
#choose to register or login
#if register is chosen call reg_user()
#if login is chosen call login()
#if no selection is made call begin()
        
def begin(option = None):
    option = input("Register or login: ")                            
    if option.lower() == "register":
        reg_user()
    elif option.lower() == "login":
        login()
    else:
        print("Please make a selection")
        begin()
        
#==================== ADD TASK ============================================
        
# all the new tasks (from selection.lower() == "a") are appended to tasks.txt
#to append these tasks open the file in append "a" mode

def add_task(task_info):
    file = open("tasks.txt","a")    
    file.write("\n" + task_info)
    file.close()
    
#==================== VIEW ALL TASKS ======================================
    
#if selection.lower() == "va" is selected. The user requests to see all the tasks allocated to people
#to read these tasks open the file in read "r" mode
    
def view_all():
    file = open("tasks.txt", "r")
    tasks = file.readlines()
    for lines in tasks:
        person_allocated, task, task_description, start_date, due_date, task_completed = lines.split(", ")
        print(f'''
Allocated person:{person_allocated}
Task            :{task}
Task Description:{task_description}
Start Date      :{start_date}
Due Date        :{due_date}
Task Completion :{task_completed}''')
    file.close()
    
#==================== VIEW MY TASKS ======================================
    
#verify username and password of the user
#if password and username match with stored details in 'user.txt' allow user to view their tasks which are stored in 'task.txt'
#allow user to edit a task if task completion is 'No'
#write changes on a temporary text file (temp.txt)
#if they want to go back to the main menu call choice()
    
def view_mine():                                                          
    username = input("Verify your username: ")                            
    password = input("Verify your password: ")
    log_in = False
    file = open("user.txt","r")
    for i in file:
        a,b = i.split(", ")
        b = b.strip()
        if a == username and b == password:
            log_in = True   
            taskfile = open("tasks.txt", "r")
            s = " "
            while s:
                s = taskfile.readline()
                L = re.split(", |- ",s)
                if len(s) > 0:
                    if L[1]  == username:
                        print("Allocated person: " + L[0] + "- " + L[1])
                        print("Task            :",L[2])
                        print("Task Description:",L[3])
                        print("Start Date      :",L[4])
                        print("Due Date        :",L[5])
                        print("Task Completion :",L[6])

                    if L[6] == "N":
                        task_number = input("Please enter the task number you would like to edit: ")
                        if L[0]  == task_number:
                            print(L[0] + "&" + task_number)
                            print("1:edit task")
                            print("2:task completion (Y/N)")
                            selection = input("Please make a selection (-1 to return to main menu): ")

                            if selection == "1":
                                person_allocated = input("Please enter the username of the person the task is assigned too: ")              
                                due_date = input("Enter the due date in the format (dd/mm/yyyy): ")
                                task = str(L[0]) + "- " + person_allocated + ", " + L[2] + ", " + L[3] + ", " + L[4] + ", " + due_date + ", " + L[6]
                                temp_file = open("temp.txt", "w")
                                temp_file.write("\n" +task)
                                temp_file.close()
                            elif selection == "2":
                                task_completed = input("Is the task completed? (Y/N)")                    
                                task = str(L[0]) + "- " + L[1] + ", " + L[2] + ", " + L[3] + ", " + L[4] + ", " + L[5] + ", " + task_completed                    
                                temp_file = open("temp.txt", "w")
                                temp_file.write("\n" +task)   
                                temp_file.close()
                            else:
                                temp_file = open("temp.txt", "w")
                                temp_file.write(s)
                                temp_file.close()
                        else:
                            task_number == "-1"
                            break
                            choice()                           
    file.close()
    taskfile.close()  
   
#==================== GENERATE REPORTS ======================================
    
#generate task and user overview report
#determine the number of tasks completed,incomplete and overdue
#determine the number of tasks completed,incomplete and overdue for each user
#if the users wishes to edit their task(incomplete) allow them too
#write to 'task_overview.txt' and 'user_overview.txt'
    
def overview():
    task_number = 0
    completed_tasks = 0
    incomplete_tasks = 0
    overdue = 0
    total_users = 0
    assigned_perUser = 0
    total_tasks = 0
    userCompleted_tasks = 0
    userIncomplete_tasks = 0
    user_overdue = 0

    file = open("tasks.txt", "r", encoding='utf-8')
    file.seek(0)
    s = " "
    while s:
        s = file.readline()
        L = s.strip()
        L = re.split(", |- ",L)

        if len(s) > 0:          
            if L[0]:
                task_number += 1                
            if L[6] == "Y":
                completed_tasks += 1
            if L[6] == "N":
                incomplete_tasks += 1
            datetime_object = datetime.datetime.strptime(L[5], '%d/%m/%Y') # 'strptime()' parses a string representing a time according to a format.
            if datetime_object < datetime.datetime.today() and 'N' == L[6]: # 'today()' method of date class under datetime module returns a date object which contains the value of Today's date.
                overdue += 1                   
    percentage_incomplete = round(float((incomplete_tasks / task_number) *100),2)
    percentage_overdue = round(float((overdue / task_number) *100),2)

    task_overviewFile = open("task_overview.txt","w")    
    task_overviewFile.write(f"Total number of tasks: {task_number}\n")
    task_overviewFile.write(f"The total number of completed tasks is:{completed_tasks}\n")
    task_overviewFile.write(f"The total number of incomplete tasks is:{incomplete_tasks}\n")   
    task_overviewFile.write(f"Percentage of incomplete tasks:{percentage_incomplete}\n")
    task_overviewFile.write(f"Percentage of overdue tasks:{percentage_overdue}\n")

    username = input("Verify your username: ")
    userfile = open("user.txt","r")
    d = {}
    for i in userfile:
        a,b = i.split(",")
        b = b.strip()
        d[a] = b
        if d[a]:
            total_users += 1
        if a == username:  
            taskfile = open("tasks.txt", "r")
            r = " "
            while r:
                r = taskfile.readline()
                L1 = r.strip()
                L1 = re.split(", |- ",L1)
                if len(r) > 0:
                    if L1[0]:
                        total_tasks += 1
                    percentage_assigned = round(float((assigned_perUser / total_tasks) *100),2)
                    if L1[1]  == username:
                        assigned_perUser += 1

                        if L1[6] == "Y":                        
                            userCompleted_tasks += 1
                            percentage_userCompleted = round(float((userCompleted_tasks / assigned_perUser) *100),2)

                        if L1[6] == "N":                        
                            userIncomplete_tasks += 1
                        percentage_userInomplete = round(float((userIncomplete_tasks / assigned_perUser) *100),2)

                        datetime_object = datetime.datetime.strptime(L1[5], '%d/%m/%Y')
                        if datetime_object < datetime.datetime.today() and 'N' == L1[6]: 
                            user_overdue += 1

                        percentage_userOverdue = round(float((user_overdue / assigned_perUser) *100),2)

    user_overviewFile = open("user_overview.txt","w")
    user_overviewFile.write(f"\nTotal number of registered users:{total_users}\n")
    user_overviewFile.write(f"Total number of tasks: {total_tasks}\n")
    user_overviewFile.write(f"Total number of tasks assigned to {username} is {assigned_perUser}\n")
    user_overviewFile.write(f"Percentage assigned to {username} is {percentage_assigned}\n")
    user_overviewFile.write(f"Percentage of tasks assigned to {username} which have been completed {percentage_userCompleted}\n")
    user_overviewFile.write(f"Percentage of tasks assigned to {username} which are incomplete {percentage_userInomplete}\n")
    user_overviewFile.write(f"Percentage of overdue tasks assigned to {username} is {percentage_userOverdue}\n")

    file.close()
    task_overviewFile.close()
    userfile.close()
    taskfile.close()
    user_overviewFile.close()
    
#==================== DISPLAY STATISTICS =============================================
    
#print the data in task_overview.txt and user_overview.txt
#if these two text files do not exit overview() should be called
# open task_overview.txt and user_overview.txt in read mode and print

def display_stats():
    if not os.path.exists("task_overview.txt") and not os.path.exists("user_overview.txt"):
        overview()

    tasks = open("task_overview.txt", "r", encoding="utf-8")
    for i in tasks:
        i = i.strip()
        print(i)

    users = open("user_overview.txt", "r", encoding="utf-8")
    for line in users:
        line = line.strip()
        print(line)
        
    tasks.close()
    users.close()
    
#==================== MENU ============================================================
    
#if the user is logged in display this menu print the different options to choose from
    
def  choice():
    while True:
        print("*"*140)
        print("MAIN MENU".center(140))
        print(" "*45+"Please select one of the following options:")
        print(" "*45+"r\t-register user")
        print(" "*45+"a\t-add task")
        print(" "*45+"va\t-view all tasks")
        print(" "*45+"vm\t-view my tasks")
        print(" "*45+"e\t-exit")
        print("*"*140)
        selection = input("Please make a selection: ")
        
#==================== MENU: IF REGISTER USER IS SELECTED ==============================
        
# if selection.lower() == "r" is selected reg_user() will be called
# enter the username and password

        if selection.lower() == "r":
            reg_user()
            
#==================== MENU: IF ADD TASK IS SELECTED ===================================
            
#if selection.lower() == "a" is selected the user should enter the name of the person allocated to the task,
#task, task description, start and due date and whether the task is completed or not
#create new text file for primary key(unique identity) for each task
#call the function add_task(task_info) where all the tasks will be start to 'tasks.txt'
            
        elif selection.lower() == "a":
            file = open("primary_key.txt","r")
            s = file.read()
            if s == "":
                primary_key = 1
                file.close()
                file = open("primary_key.txt","w")
                file.write(str(primary_key))
                file.close()
            else:
                primary_key = int(s) + 1
                file.close()
                file = open("primary_key.txt","w")
                file.write(str(primary_key))
                file.close()           

            person_allocated = input("Please enter the username of the person the task is assigned too: ")              
            task = input("Please enter the title of the task: ")
            task_description = input("Please enter the description of the task: ")
            start_date = input("Enter the start date of the task in the format (dd/mm/yyyy) : ")
            due_date = input("Enter the due date in the format (dd/mm/yyyy): ")
            task_completed = input("Is the task completed? (Y/N)")
            task_info = str(primary_key) + "- " + person_allocated + ", " + task + ", " + task_description + ", " + start_date + ", " + due_date + ", " + task_completed
            add_task(task_info)
            
#==================== MENU: IF VIEW ALL TASKS IS SELECTED ==============================
            
#if selection.lower() == "va" is selected call the function view_all()
#allow the user to view all the tasks in 'tasks.txt'
            
        elif selection.lower() == "va":           
            view_all()

#==================== MENU: IF VIEW MY TASKS IS SELECTED ===============================
            
#if selection.lower() == "vm" is selected call the function view_mine()
#allow the user to view only tasks allocated to them
#allow them to edit the tasks. if the tasks are not completed
            
        elif selection.lower() == "vm":
            view_mine()
            
#==================== MENU: IF EXIT IS SELECTED ========================================
            
#if selection.lower() == "e" is selected. Allow the user to exit the program
            
        elif selection.lower() == "e":
            break
        
#==================== MENU: IF NO SELECTION MADE =======================================
        
#if no selection is made, call choice() menu
        
        else:
            print("Invalid selection")
            choice()
            
#==================== ADMIN MENU =======================================================
            
#if the logged in user is admin display this menu. Print the different options to choose from
            
def admin_newMenu():
    while True:    
        print("*"*140)
        print("MAIN MENU".center(140))
        print(" "*45+"Please select one of the following options:")
        print(" "*45+"r\t-register user")
        print(" "*45+"a\t-add task")
        print(" "*45+"va\t-view all tasks")
        print(" "*45+"vm\t-view my tasks")
        print(" "*45+"gr\t-generate reports")
        print(" "*45+"ds\t-display statistics")   
        print(" "*45+"e\t-exit")
        print("*"*140)
        selection = input("Please make a selection: ")
        
#==================== ADMIN MENU: IF REGISTER USER IS SELECTED ==============================
        
# if selection.lower() == "r" is selected reg_user() will be called
# enter the username and password

        if selection.lower() == "r":
            reg_user()
            
#==================== ADMIN MENU: IF ADD TASK IS SELECTED ===================================
            
#if selection.lower() == "a" is selected the user should enter the name of the person allocated to the task,
#task, task description, start and due date and whether the task is completed or not
#create new text file for primary key(unique identity) for each task
#call the function add_task(task_info) where all the tasks will be start to 'tasks.txt'
            
        elif selection.lower() == "a":            
            file = open("primary_key.txt","r")
            s = file.read()
            if s == "":
                primary_key = 1
                file.close()
                file = open("primary_key.txt","w")
                file.write(str(primary_key))
                file.close()
            else:
                primary_key = int(s) + 1
                file.close()
                file = open("primary_key.txt","w")
                file.write(str(primary_key))
                file.close()            

            person_allocated = input("Please enter the username of the person the task is assigned too: ")              
            task = input("Please enter the title of the task: ")
            task_description = input("Please enter the description of the task: ")
            start_date = input("Enter the start date of the task in the format (dd/mm/yyyy) : ")
            due_date = input("Enter the due date in the format (dd/mm/yyyy): ")
            task_completed = input("Is the task completed? (Y/N)")
            task_info = str(primary_key) + ". " + person_allocated + ", " + task + ", " + task_description + ", " + start_date + ", " + due_date + ", " + task_completed
            add_task(task_info)
            
#==================== ADMIN MENU: IF VIEW ALL TASKS IS SELECTED ==============================
            
#if selection.lower() == "va" is selected call the function view_all()
#allow the user to view all the tasks in 'tasks.txt'
            
        elif selection.lower() == "va":           
            view_all()

#==================== ADMIN MENU: IF VIEW MY TASKS IS SELECTED ===============================
            
#if selection.lower() == "vm" is selected call the function view_mine()
#allow the user to view only tasks allocated to them
#allow them to edit the tasks. if the tasks are not completed
            
        elif selection.lower() == "vm":
            view_mine()
            
#==================== ADMIN MENU: IF GENERATE REPORT IS SELECTED =============================
            
#only admin can generate a report
#if selection.lower() == "gr" is selected, call overview()
#generate task and user overview report
#determine the number of tasks completed,incomplete and overdue
#determine the number of tasks completed,incomplete and overdue for each user
#if the users wishes to edit their task(incomplete) allow them too
#write to 'task_overview.txt' and 'user_overview.txt'

        elif selection.lower() == "gr":
            overview()

#==================== ADMIN MENU: IF DISPLAY STATISTICS IS SELECTED ==========================
            
#only admin can display statistics
#if selection.lower() == "ds" is selected, call display_stats()
#print the data in task_overview.txt and user_overview.txt
#if these two text files do not exit overview() should be called
# open task_overview.txt and user_overview.txt in read mode and print

        elif selection.lower() == "ds":
            display_stats()

#==================== MENU: IF NO SELECTION MADE =============================================
            
#if selection.lower() == "e" is selected. Allow the user to exit the program
            
        else:
            selection.lower() == "e"
            break     
begin()
reg_user()
login()
choice()
admin_newMenu()
add_task(task_info)
view_all()
view_mine()
overview()
display_stats()










