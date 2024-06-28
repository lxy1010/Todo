from Do import Do


class TodoList:
    """待办列表"""
    def __init__(self):
        self.todoList: list[Do] = []

    def add_todo(self, name, describe, year, month, day, hour, minute, second):
        self.todoList.append(Do(name, describe, year, month, day, hour, minute, second))

    def print_out(self):
        for i in range(len(self.todoList)):
            print(f"待办 {i + 1}")
            self.todoList[i].print_out()
