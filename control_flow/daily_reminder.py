# daily_reminder.py

# Prompt the user for a task description
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide a reminder based on priority using a Match Case statement
match priority:
    case "high":
        priority_message = "high priority task"
    case "medium":
        priority_message = "medium priority task"
    case "low":
        priority_message = "low priority task"
    case _:
        priority_message = "unknown priority"

# Modify the reminder based on time sensitivity
if time_bound == "yes":
    reminder_message = f"Reminder: '{task}' is a {priority_message} that requires immediate attention today!"
else:
    reminder_message = f"Note: '{task}' is a {priority_message}. Consider completing it when you have free time."

# Print the customized reminder
print(reminder_message)
