"""
功能需求
用户注册与登录（可选，增加复杂度）
用户可以注册新账户
用户可以登录自己的账户
用户登录后可以查看自己的待办事项
待办事项管理
用户可以添加新的待办事项，包括标题、描述和截止日期（可选）
用户可以编辑已存在的待办事项
用户可以删除待办事项
用户可以标记待办事项为已完成或未完成
待办事项列表
显示所有待办事项的列表，区分已完成和未完成的任务
可以按照截止日期、标题等字段对列表进行排序
搜索功能（可选，增加复杂度）
用户可以通过关键词搜索待办事项
提醒功能（可选，增加复杂度）
当待办事项的截止日期临近时，发送提醒通知（如邮件、应用内通知等）

添加闹钟
添加GUI
"""

import datetime


class Do:
    """一条待办"""
    def __init__(self, name, describe, year, month, day, hour, minute, second):
        self.name = name
        self.describe = describe
        self.deadline = datetime.datetime(year, month, day, hour, minute, second)

    def is_dead(self):
        """If deadline > now return True, else return False"""
        return self.deadline > datetime.datetime.now()


class TodoList:
    """待办列表"""
    def __init__(self):
        self.todoList: list[Do] = []

    def add_todo(self, todo: Do):
        self.todoList.append(todo)


class User:
    """用户"""
    def __init__(self, name):
        self.name = name


class Todo:
    """应用程序"""
    def __init__(self):
        pass
