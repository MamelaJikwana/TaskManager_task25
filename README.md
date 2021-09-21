# TaskManager_task25

For this task I had to create a program for a small business that can help it to manage tasks assigned to each member of the team.
I had to create two text files: user.txt and tasks.txt. 'tasks.txt' stores a list of all the tasks that the team is working on
and the 'user.txt' stores the username and password for each user that has permission to use this program (task_manager.py). Functions
had to be used to achieve this program

* The following should be added to each task:
  * The username of the person to whom the task is assigned;
  * The title of the task;
  * A description of the task;
  * The date that the task was assigned to the user;
  * The due date for the task;
  * Either a 'Yes' or 'No' value that specifies if the task has been completed yet.

* These functions were included in the program:
  * reg_user - that is called when the user selects 'r' to register a user;
  * login - that is called when the user chooses to login;
  * add_task - that is called when a user selects 'a' to add a new task;
  * view_all - that is called when users type 'va' to view all the tasks listed in 'tasks.txt';
  * view_mine — that is called when users type 'vm' to view all the tasks that have been assigned to them

* If the logged in user is 'admin' the following functions should be added:
  * overview - that is called when admin selects 'gr' to generate a report;
  * display_stats - that is called when admin selects 'ds' to display statistics
  
When the admin chooses to generate reports, two text files, called 'task_overview.txt' and 'user_overview.txt', should be generated.

* The following should be added to task_overview.txt:
  * The total number of tasks that have been generated and tracked using the task_manager.py;
  * The total number of completed tasks;
  * The total number of uncompleted tasks;
  * The total number of tasks that haven’t been completed and that are overdue;
  * The percentage of tasks that are incomplete;
  * The percentage of tasks that are overdue.
  
* The following should be added to user_overview.txt:
  * The total number of users registered with task_manager.py;
  * The total number of tasks that have been generated and tracked using the task_manager.py;
  * For each user also describe:
    * The total number of tasks assigned to that user;
    * What percentage of the total number of tasks have been assigned to that user;
    * What percentage of the tasks assigned to that user have been completed;
    * What percentage of the tasks assigned to that user must still be completed;
    * What percentage of the tasks assigned to that user have not yet been completed and are overdue.
