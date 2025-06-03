from typing import List

class Task:
    def __init__(self, description: str):
        self.description = description
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "Done" if self.done else "Pending"
        return f"{self.description} - {status}"

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, description: str):
        self.tasks.append(Task(description))

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()

    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")
