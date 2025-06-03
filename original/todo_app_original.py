tasks = []

def add_task(description):
    tasks.append({'description': description, 'done': False})

def remove_task(index):
    if index < len(tasks):
        tasks.pop(index)

def show_tasks():
    for i in range(len(tasks)):
        print(f"{i}. {tasks[i]['description']} - {'Done' if tasks[i]['done'] else 'Pending'}")

def complete_task(index):
    if index < len(tasks):
        tasks[index]['done'] = True
