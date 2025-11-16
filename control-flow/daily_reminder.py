task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match (priority.lower(), time_bound.lower()):
    case ("high", "yes"):
        print(f"'{task}' is a high priority task that requires immediate attention today!")
    case ("high", "no"):
        print(f"'{task}' is a high priority task. Try to complete it soon.")
    case ("medium", "yes"):
        print(f"'{task}' is a medium priority task with a deadline. Plan accordingly.")
    case ("medium", "no"):
        print(f"'{task}' is a medium priority task. Schedule it when possible.")
    case ("low", "yes"):
        print(f"'{task}' is a low priority task but has a deadline. Don't forget to do it!")
    case ("low", "no"):
        print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid input for priority or time-bound status.")
if priority.lower() == "high" and time_bound.lower() == "yes":
    print(f"'{task}' is a high priority task that requires immediate attention today!")
elif priority.lower() == "low" and time_bound.lower() == "no":
    print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
elif priority.lower() == "medium" and time_bound.lower() == "yes":
    print(f"'{task}' is a medium priority task with a deadline. Plan accordingly.")
elif priority.lower() == "high" and time_bound.lower() == "no":
    print(f"'{task}' is a high priority task. Try to complete it soon.")
elif priority.lower() == "medium" and time_bound.lower() == "no":
    print(f"'{task}' is a medium priority task. Schedule it when possible.")
elif priority.lower() == "low" and time_bound.lower() == "yes":
    print(f"'{task}' is a low priority task but has a deadline. Don't forget to do it!")
else:
    print("Invalid input for priority or time-bound status.")
    