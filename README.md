# To-Do list
#### Video Demo:  <URL https://youtu.be/Vu4qAbgwYU4>
#### Description:
This project is a simple to-do list program to help anyone organize and remember daily tasks.
It's just a simple terminal program written by Python.
when you run the program you will see the allowed options, there are four options:
1 - add tasks to a list
2 - mark task as complete
3 - view tasks
4 - Quit
you need to write an option number from 1 to 4 only and if you write anything else error message will appear and choose again.
The error massage "Invalid choice, please enter a number between 1 and 4" will apear if you writ anything rather than numbers of the option and the option apears again to choose of them.

#### add tasks to a list:
to add task to the task list choos option 1 the program asks you about the task name with this massage "Enter the task: " write the name of the task to save it in the list and then the program ask for task note with this massage "Enter the task note: " write the any information or any not about the task you want to save or you can press enter to leav the task note empty.
after that the task will be added to the list with status not complete as the default status and this massage will apear "Task added to the list sucsessfully".
if you
Then the options list will appear again to choose another option.

#### mark task as complete:
When you finish any task choos option 2 to change its status the program view a list of all noncomplete task only with it's notes, the completed task will not apear in this list, you need to choose the number of the task you want to mark as complete, a message "Task {task_name} marked as complete" will appear and the task status change to completed, the main option list will appear again to choose other option.
if you enter a number not excit in the task list this error message "Invalid index, please enter a number in the list" will apear or if you enter a nonnumber value this error message "Invalid index, please enter a number" will apear and in the two case the main option list will apear.

#### view tasks:
When choosing option 3 the program views a list of all tasks names with its status as a right sign for a completed task and an x sign for a noncomplete task.
if you want to see the information about any task writ the task number and the task will apear with its status and the its note in the second line.
if you enter a number not excit in the task list this error message "Invalid index, please enter a number in the list" will apear or if you enter a nonnumber value this error message "Invalid index, please enter a number" will apear and in the two case the main option list will apear.
after that the main option list will apear to choose another one.


#### Quit:
The last option will exit the program and the tasks list will clear.


