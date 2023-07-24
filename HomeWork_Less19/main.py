from HomeWork_Less19.tasks import add_task, list_tasks, mark_tasks_as_completed, delete_task


def invalid_input(*args, **kwargs):
    print("Nu exista asa valoare in meniu")


def main_menu(path):
    # Meniul principal a programului
    # Se afiseaza de fieare data
    while True:
        print(
            """
    1. Add task
    2. List all uncompleted tasks
    3. List completed tasks
    4. Mark task as complete
    5. Mark task as deleted
    0. To end program
            """
        )
        # Verificam input-ul utilizatorului pentru optiunea selectata
        # Si actionam in cazul fiecarii optiuni
        match input('Selected Option: '):
            case "1":
                add_task(path)
            case "2":
                list_tasks(path)
            case "3":
                list_tasks(path, True)
            case "4":
                mark_tasks_as_completed(path)
            case "0":
                delete_task(path)
            case "5":
                break
            case _:
                # Optiunea selectata nu este nici una din cele de mai de sus
                # Astfel rulam functia de mai jos pentur a afisa o eroare
                invalid_input()


if __name__ == '__main__':
    # Rulam Programul
    path = input('Path to file:')
    main_menu(path)