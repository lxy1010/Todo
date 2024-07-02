from Do import Do

import json


class TodoList:
    """待办列表"""
    def __init__(self):
        self.List: list[Do] = [Do('ss', 'ss', 2024, 10, 10, 10, 10, 10),
                               Do('aaaas', '7231894718920734073204987123471073274072309742749017238749812374897309874098372482893y7huejny7cjpeewsr439qah79weuhyarfdoq34EW7UE3098QE7DU9Q38Y90HRQERDss', 2024, 10, 10, 10, 10, 10)]

    def add_todo(self, name, describe, year, month, day, hour, minute, second):
        self.List.append(Do(name, describe, year, month, day, hour, minute, second))

    def print_out(self):
        for i in range(len(self.List)):
            print(f"待办 {i + 1}")
            self.List[i].print_out()

    def read(self, user):
        with open('data/data.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            return json_data

