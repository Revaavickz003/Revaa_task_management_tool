import matplotlib.pyplot as plt
from collections import defaultdict

# Dummy data for the example
employee_name = "M. Vignesh"
startdate = "June 25, 2024"
enddate = "July 2, 2024"

tasks_by_team_and_project = {
    "Software Development": {
        "RDS SWP002": {
            "Frontend": [
                {"pk": "SDT001", "title": "Task edit page"},
                {"pk": "SDT002", "title": "Task comments section"},
                {"pk": "SDT004", "title": "user details page"}
            ],
            "Backend": [
                {"pk": "SDT005", "title": "Task edit page"},
                {"pk": "SDT006", "title": "Task comments section"},
                {"pk": "SDT007", "title": "Add task details form in task page"},
                {"pk": "SDT010", "title": "user details page"}
            ],
            "Database": [
                {"pk": "SDT009", "title": "Task comments table"}
            ],
            "Planning": [
                {"pk": "SDT004", "title": "user details page task report"}
            ]
        },
        "LCS SWP002": {
            "Frontend": [
                {"pk": "SDT011", "title": "Task edit page"},
                {"pk": "SDT012", "title": "Task comments section"},
                {"pk": "SDT014", "title": "user details page"}
            ],
            "Backend": [
                {"pk": "SDT015", "title": "Task edit page"},
                {"pk": "SDT016", "title": "Task comments section"},
                {"pk": "SDT017", "title": "Add task details form in task page"},
                {"pk": "SDT020", "title": "user details page"}
            ],
            "Database": [
                {"pk": "SDT019", "title": "Task comments table"}
            ],
            "Planning": [
                {"pk": "SDT014", "title": "user details page task report"}
            ]
        }
    }
}

# Generate the report
plt.figure(figsize=(12, 8))

# Plot data
for team, projects in tasks_by_team_and_project.items():
    for project, task_types in projects.items():
        for task_type, tasks in task_types.items():
            x = [task['pk'] for task in tasks]
            y = [task_type] * len(tasks)
            plt.scatter(x, y, label=f"{team} - {project} - {task_type}")

plt.title(f"{employee_name}'s Task Details\nTasks from {startdate} to {enddate}")
plt.xlabel("Task Code (PK)")
plt.ylabel("Task Type")
plt.legend(loc="upper right", bbox_to_anchor=(1.25, 1))
plt.grid(True)
plt.tight_layout()

# Save the report
plt.savefig('/mnt/data/task_report.png')
plt.show()



# Nothing 09-07-24
