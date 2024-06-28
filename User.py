from TodoList import TodoList


class User:
    """用户"""
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.todolist = TodoList()

    def verify(self, password):
        return self.password == password