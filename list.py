def show_team_info():
    project_name = "LogiChain Web App"
    developers = [
        {"name": "Serhii Petryk", "role": "Team Lead / Backend"},
        {"name": "Maria Kovalenko", "role": "UI/UX Designer"},
        {"name": "Oleksander Lyhuta", "role": "Full-stack Developer"},
        {"name": "Svitlana Bodnar", "role": "QA Engineer"}
    ]

    print(f"Проєкт: {project_name}\n" + "-"*30)
    print("Склад команди розробників:")
    for dev in developers:
        print(f"- {dev['name']} ({dev['role']})")

if __name__ == "__main__":
    show_team_info()
