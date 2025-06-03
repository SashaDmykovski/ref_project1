# tests_original.py

import pytest
import todo_app_original as app

@pytest.fixture(autouse=True)
def reset_tasks():
    app.tasks.clear()

def test_add_task():
    app.add_task("Task 1")
    assert len(app.tasks) == 1
    assert app.tasks[0]['description'] == "Task 1"

def test_add_multiple_tasks():
    app.add_task("Task A")
    app.add_task("Task B")
    assert len(app.tasks) == 2

def test_complete_task():
    app.add_task("Finish me")
    app.complete_task(0)
    assert app.tasks[0]['done'] == True

def test_remove_task():
    app.add_task("Delete me")
    app.remove_task(0)
    assert len(app.tasks) == 0

def test_remove_invalid_index():
    app.add_task("Task 1")
    app.remove_task(5)
    assert len(app.tasks) == 1

def test_complete_invalid_index():
    app.add_task("Task X")
    app.complete_task(99)
    assert app.tasks[0]['done'] == False

def test_show_tasks_output(capsys):
    app.add_task("Task Show")
    app.show_tasks()
    captured = capsys.readouterr()
    assert "Task Show" in captured.out

def test_task_done_status():
    app.add_task("Task to finish")
    app.complete_task(0)
    assert app.tasks[0]['done'] is True

def test_task_pending_by_default():
    app.add_task("Unfinished")
    assert app.tasks[0]['done'] is False

def test_add_empty_description():
    app.add_task("")
    assert app.tasks[0]['description'] == ""

# Додаткові
def test_index_bounds_negative_complete():
    app.add_task("Do something")
    app.complete_task(-1)
    assert app.tasks[0]['done'] == False

def test_index_bounds_negative_remove():
    app.add_task("Try remove")
    app.remove_task(-1)
    assert len(app.tasks) == 1

def test_multiple_task_states():
    app.add_task("1")
    app.add_task("2")
    app.complete_task(1)
    assert app.tasks[1]['done'] is True
    assert app.tasks[0]['done'] is False

def test_add_unicode_task():
    app.add_task("Привіт 🌟")
    assert app.tasks[0]['description'] == "Привіт 🌟"

def test_add_numeric_description():
    app.add_task("123")
    assert app.tasks[0]['description'] == "123"

def test_remove_last():
    app.add_task("A")
    app.add_task("B")
    app.remove_task(1)
    assert len(app.tasks) == 1

def test_remove_first():
    app.add_task("A")
    app.add_task("B")
    app.remove_task(0)
    assert app.tasks[0]['description'] == "B"

def test_remove_middle():
    app.add_task("A")
    app.add_task("B")
    app.add_task("C")
    app.remove_task(1)
    assert app.tasks[1]['description'] == "C"

def test_complete_first():
    app.add_task("X")
    app.add_task("Y")
    app.complete_task(0)
    assert app.tasks[0]['done'] == True

def test_complete_last():
    app.add_task("X")
    app.add_task("Y")
    app.complete_task(1)
    assert app.tasks[1]['done'] == True
