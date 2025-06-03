# tests_refactored.py

import pytest
from todo_app_refactored import TaskManager # type: ignore

@pytest.fixture
def manager():
    return TaskManager()

def test_add_task(manager):
    manager.add_task("Do laundry")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].description == "Do laundry"

def test_add_multiple(manager):
    manager.add_task("One")
    manager.add_task("Two")
    assert len(manager.tasks) == 2

def test_remove_task(manager):
    manager.add_task("Delete me")
    manager.remove_task(0)
    assert len(manager.tasks) == 0

def test_remove_invalid(manager):
    manager.add_task("A")
    manager.remove_task(5)
    assert len(manager.tasks) == 1

def test_complete_task(manager):
    manager.add_task("Finish")
    manager.complete_task(0)
    assert manager.tasks[0].done is True

def test_complete_invalid(manager):
    manager.add_task("X")
    manager.complete_task(99)
    assert manager.tasks[0].done is False

def test_task_status_default(manager):
    manager.add_task("T")
    assert manager.tasks[0].done is False

def test_str_representation(manager):
    manager.add_task("Show this")
    assert str(manager.tasks[0]) == "Show this - Pending"

def test_str_after_done(manager):
    manager.add_task("Mark this")
    manager.complete_task(0)
    assert str(manager.tasks[0]) == "Mark this - Done"

def test_show_tasks_output(manager, capsys):
    manager.add_task("Task")
    manager.show_tasks()
    captured = capsys.readouterr()
    assert "Task" in captured.out

# Додаткові 10
def test_unicode_task(manager):
    manager.add_task("Задача 🌍")
    assert manager.tasks[0].description == "Задача 🌍"

def test_empty_description(manager):
    manager.add_task("")
    assert manager.tasks[0].description == ""

def test_remove_first_of_multiple(manager):
    manager.add_task("1")
    manager.add_task("2")
    manager.remove_task(0)
    assert manager.tasks[0].description == "2"

def test_remove_last(manager):
    manager.add_task("1")
    manager.add_task("2")
    manager.remove_task(1)
    assert len(manager.tasks) == 1

def test_complete_middle(manager):
    manager.add_task("A")
    manager.add_task("B")
    manager.add_task("C")
    manager.complete_task(1)
    assert manager.tasks[1].done is True

def test_index_bounds_negative_complete(manager):
    manager.add_task("A")
    manager.complete_task(-1)
    assert manager.tasks[0].done is False

def test_index_bounds_negative_remove(manager):
    manager.add_task("A")
    manager.remove_task(-1)
    assert len(manager.tasks) == 1

def test_complete_first(manager):
    manager.add_task("A")
    manager.add_task("B")
    manager.complete_task(0)
    assert manager.tasks[0].done is True

def test_complete_last(manager):
    manager.add_task("A")
    manager.add_task("B")
    manager.complete_task(1)
    assert manager.tasks[1].done is True

def test_task_order_preserved(manager):
    manager.add_task("A")
    manager.add_task("B")
    assert [t.description for t in manager.tasks] == ["A", "B"]
