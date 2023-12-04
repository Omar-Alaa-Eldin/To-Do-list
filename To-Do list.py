# 1 - add tasks to a list
# 2 - mark task as complete
# 3 - view tasks
# 4 - Quit

tasks_list = []

def main():
    #user = input("What is your name? ")
    message = """1 - add tasks to a list
2 - mark task as complete
3 - view tasks
4 - Quit"""
    while True:
      print(message)
      choice = input("Enter your choice: ")
      if choice == "1":
        #add task to tasks list
        add_task(tasks_list)
      elif choice == "2":
        #mark task as complete
        mark_task_complete(tasks_list)
      elif choice == "3":
        #view all tasks
        view_tasks(tasks_list)
      elif choice == "4":
        #quit
        break
      else:
        print("Invalid choice, please enter a number between 1 and 4")


#"pass" order make pass to the function to run the program without produce error becauce the function is not defined.


def add_task(tasks):
  #get the task from the user
  task = input("Enter the task: ")
  note = input("Enter the task note: ")
  #define task statuse
  task_info = {"task": task, "completed": False, "note":note}
  #assing the task to the list
  tasks.append(task_info)
  print("Task added to the list sucsessfully")


def mark_task_complete(tasks):
  #get list of non compleat tasks
  incomplete_tasks = [task for task in tasks if task["completed"] is False]
  if incomplete_tasks:
    #show the non compleated tasks
    print("The non completed tasks are: ")
    for i, task in enumerate(incomplete_tasks):
        print(f"{i+1}) {task['task']}   ->  {task['note']}")
        print("_."*30)
    #get the index of the task to
    try:
      index = int(input("Enter the index of the task to mark as complete: "))
      if index < 1 or index > len(incomplete_tasks):
        raise IndexError
      #mark the task as compleated
      task = incomplete_tasks[index-1]
      task["completed"] = True
      #print a messsage to the user
      print(f"Task {task['task']} marked as complete")
    except IndexError:
      print("Invalid index, please enter a number in the list")
    except ValueError:
      print("Invalid index, please enter a number")
  else:
      print("There are no incomplete tasks")

def view_tasks(tasks):
  #the "..." = "pass" order
  #if there are no tasks, print message and return.
  if tasks:
    #print the tasks
    print("The tasks are: ")
    for i,task in enumerate(tasks):
      status = "✔" if task["completed"] else "❌"
      print(f"{i+1}. {task['task']} = {status}")
    try:
      #get the index of the task to view
      index = int(input("Enter the index of the task to view: "))
      if index < 1 or index > len(tasks):
        raise IndexError
      #print the task
      task = tasks[index-1]
      status = "✔" if task["completed"] else "❌"
      print(f"Task: {task['task']} = {status}")
      print(f"Note: {task['note']}")
    except IndexError:
      print("Invalid index, please enter a number in the list")
    except ValueError:
      print("Invalid index, please enter a number")
  else:
    print("There are no tasks")

#print(__name__)
if __name__ == "__main__":
  main()
