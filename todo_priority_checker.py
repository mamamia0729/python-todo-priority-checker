# To-Do List Priority Checker
# A tool to input tasks, assign priorities, and display them in order

print("Welcome to the To-Do List Priority Checker!")
print("Enter tasks and their priorities (high, medium, or low).")

# Get the number of tasks
num_tasks = int(input("How many tasks do you want to enter? "))

# Lists to store tasks and priorities
tasks = []
priorities = []

# Collect tasks and priorities
for i in range(num_tasks):
    task = input("Enter task " + str(i + 1) + ": ")
    priority = input("Enter priority for task " + str(i + 1) + " (high, medium, low): ").lower()
    
    # Validate priority using if statements
    if priority == "high" or priority == "medium" or priority == "low":
        priorities.append(priority)
    else:
        print("Invalid priority! Setting to 'low' by default.")
        priorities.append("low")
    
    tasks.append(task)

# Display tasks grouped by priority
print("\n=== Your To-Do List ===")
print("High Priority Tasks:")
for index, task in enumerate(tasks):
    if priorities[index] == "high":
        print(str(index + 1) + ". " + task)

print("\nMedium Priority Tasks:")
for index, task in enumerate(tasks):
    if priorities[index] == "medium":
        print(str(index + 1) + ". " + task)

print("\nLow Priority Tasks:")
for index, task in enumerate(tasks):
    if priorities[index] == "low":
        print(str(index + 1) + ". " + task)
