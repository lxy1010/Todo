import datetime


class Do:
    """一条待办"""
    def __init__(self, name, describe, year, month, day, hour, minute, second):
        self.name = name
        self.describe = describe
        self.deadline = datetime.datetime(year, month, day, hour, minute, second)
        self.isDone = False

    def is_dead(self):
        """是否截止"""
        dead = self.deadline > datetime.datetime.now()
        if dead:
            self.isDone = True
        else:
            self.isDone = False
        return dead

    def re_name(self, name):
        """重命名"""
        self.name = name

    def re_describe(self, describe):
        """重命名描述"""
        self.describe = describe

    def re_deadline(self, deadline: datetime.datetime):
        """重新设置起止日期"""
        self.deadline = deadline
        self.is_dead()

    def print_out(self):
        print(f"名称\t{self.name}\n"
              f"描述\t{self.describe}\n"
              f"截止日期\t{self.deadline}\n"
              f"是否截止\t{self.isDone}\n")