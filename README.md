# ✅ To-Do List (Python CLI Application)
#### Video Demo:  <URL https://youtu.be/Vu4qAbgwYU4>


![To-Do List Cover](https://github.com/Omar-Alaa-Eldin/To-Do-list/blob/main/ChatGPT%20Image%20Aug%2019%2C%202025%2C%2003_39_22%20PM.png)


A simple and interactive **Command-Line To-Do List Application** built in **Python**.  
This program helps users manage their tasks by allowing them to add new tasks with notes, mark tasks as complete, and view the entire task list with status indicators.  

---

## 📖 Program Description

This To-Do List application was created as a **productivity tool** to practice working with **lists, dictionaries, user input handling, and modular programming** in Python.  

It features a **menu-driven interface** that runs in the terminal, making it lightweight and simple to use.  

### Features
- ➕ **Add tasks** with custom notes.  
- ✔ **Mark tasks as complete** with error handling for invalid inputs.  
- 📋 **View tasks** with clear status indicators:  
  - `✔` Completed tasks  
  - `❌` Incomplete tasks  
- 🛡️ **Robust input validation** (handles invalid indexes and empty lists).  
- 🔄 Continuous menu loop until the user chooses to quit.  

---

## ⚙️ Program Flow

1. **Main Menu Options**
   - `1` → Add a new task.  
   - `2` → Mark an existing task as complete.  
   - `3` → View all tasks.  
   - `4` → Quit the program.  

2. **Adding a Task**
   - Prompts the user for:
     - Task name
     - Task note/description  
   - Saves the task with default status `❌ Incomplete`.

3. **Marking a Task as Complete**
   - Displays a list of all incomplete tasks.  
   - Prompts the user to select a task by index.  
   - Marks the selected task as `✔ Complete`.

4. **Viewing Tasks**
   - Shows all tasks with their status (`✔` or `❌`).  
   - Allows the user to view task details (task name + note).  

---

## 🖥️ Example Run

```bash
1 - add tasks to a list
2 - mark task as complete
3 - view tasks
4 - Quit
Enter your choice: 1
Enter the task: Study Python
Enter the task note: Read chapter 5
Task added to the list successfully

1 - add tasks to a list
2 - mark task as complete
3 - view tasks
4 - Quit
Enter your choice: 3
The tasks are:
1. Study Python = ❌
Enter the index of the task to view: 1
Task: Study Python = ❌
Note: Read chapter 5
#### Quit:
The last option will exit the program and the tasks list will clear.





