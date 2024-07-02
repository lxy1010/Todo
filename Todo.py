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

import customtkinter
import json

from User import User
from greeting import rand_greeting


class Todo:
    def __init__(self):
        self.data = self.read()
        self.users: list[User] = []
        self.user = None

        self.flag = {'login': True, 'register': False, 'main': False}

        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')

        self.root = customtkinter.CTk()
        self.root.geometry('1024x720')

        self.tk_init()

    def read(self):
        with open('data/data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def run(self):
        self.root.mainloop()

    def update(self):
        self.body.destroy()
        self.body = customtkinter.CTkFrame(master=self.root)
        self.body.pack(padx=20, pady=10, fill='both', expand=True)
        if self.flag['login']:
            self.tk_login()
        if self.flag['register']:
            self.tk_register()
        if self.flag['main']:
            self.tk_todo()

    def change(self, chance=None):
        try:
            if chance is None:
                for k, v in self.flag.items():
                    self.flag[k] = False
                self.update()
                return
            self.flag[chance] = True
            for k, v in self.flag.items():
                self.flag[k] = False
            self.flag[chance] = True
            self.update()
        except KeyError:
            print("Error: Key is wrong")

    def tk_init(self):
        self.head = customtkinter.CTkFrame(master=self.root)
        self.head.pack(padx=20, pady=10, fill='both', expand=True)

        self.title = customtkinter.CTkLabel(master=self.head, text='Todo System', font=('Times New Roman', 72), text_color='#555555')
        self.title.pack(padx=12, pady=20)

        self.logined = customtkinter.CTkLabel(master=self.head, text='Unlogged', font=('Times New Roman', 30), text_color='#8888BB')
        self.logined.pack(padx=12, pady=20)

        self.greeting = customtkinter.CTkLabel(master=self.head, text=f'{rand_greeting()}', font=('Times New Roman', 18), text_color='#BBBBDD')
        self.greeting.pack(padx=12, pady=10)

        self.loginButton = customtkinter.CTkButton(master=self.head, text='Login', font=('Times New Roman', 20), command=lambda : self.change('login'))
        self.loginButton.pack(side=customtkinter.LEFT, padx=20, pady=20)

        self.registerButton = customtkinter.CTkButton(master=self.head, text='Register', font=('Times New Roman', 20), command=lambda : self.change('register'))
        self.registerButton.pack(side=customtkinter.LEFT, padx=20, pady=20)

        self.mainButton = customtkinter.CTkButton(master=self.head, text='Todo', font=('Times New Roman', 20), command=lambda : self.change('main'))
        self.mainButton.pack(side=customtkinter.LEFT, padx=20, pady=20)

        self.returnButton = customtkinter.CTkButton(master=self.head, text='Return', font=('Times New Roman', 20), command=lambda : self.change())
        self.returnButton.pack(side=customtkinter.LEFT, padx=20, pady=20)

        """Body"""
        self.body = customtkinter.CTkFrame(master=self.root)
        self.body.pack(padx=20, pady=10, fill='both', expand=True)

    def tk_login(self):
        self.loginText = customtkinter.CTkLabel(master=self.body, text=f'Login', font=('Times New Roman', 50), text_color='#555555')
        self.loginText.pack(padx=12, pady=20)

        self.loginName = customtkinter.CTkEntry(master=self.body, placeholder_text='Enter Your UserName', font=('Times New Roman', 30), width=500)
        self.loginName.pack(padx=40, pady=20)

        self.loginPassword = customtkinter.CTkEntry(master=self.body, placeholder_text='Enter Your Password', font=('Times New Roman', 30), width=500)
        self.loginPassword.pack(padx=40, pady=20)

        self.bodyLoginButton = customtkinter.CTkButton(master=self.body, text='Login', font=('Times New Roman', 20), command=self.login)
        self.bodyLoginButton.pack(padx=20, pady=20)

    def tk_register(self):
        self.registerSuccess = customtkinter.CTkLabel(master=self.body, text=f'Register', font=('Times New Roman', 50), text_color='#555555')
        self.registerSuccess.pack(padx=12, pady=20)

        self.registerName = customtkinter.CTkEntry(master=self.body, placeholder_text='Enter Your UserName', font=('Times New Roman', 30), width=500)
        self.registerName.pack(padx=40, pady=20)

        self.registerPassword = customtkinter.CTkEntry(master=self.body, placeholder_text='Enter Your Password',  font=('Times New Roman', 30), width=500)
        self.registerPassword.pack(padx=40, pady=20)

        self.bodyRegisterButton = customtkinter.CTkButton(master=self.body, text='Register', font=('Times New Roman', 20), command=self.create_user)
        self.bodyRegisterButton.pack(padx=20, pady=20)

    def tk_todo(self):
        self.grid = customtkinter.CTkTextbox(master=self.body, width=950, height=200, font=('Times New Roman', 20))
        self.grid.pack(padx=20, pady=20)
        for i in range(len(self.user.todolist.List)):
            self.grid.insert(customtkinter.END, text=f'Todo {i + 1}:  {self.user.todolist.List[i].name}\t\t{self.user.todolist.List[i].describe}\n')
            # do = customtkinter.CTkLabel(master=self.body, text=f'odo {i + 1}:  {self.user.todolist.List[i].name}', font=('Times New Roman', 20), text_color='#FFFFFF')
            # do.pack(padx=20, pady=10, fill='both', expand=True)
        self.createNew = customtkinter.CTkButton(master=self.body, text='Create New', font=('Times New Roman', 30), command=self.tk_create_new_todo)
        self.createNew.pack(padx=5, pady=5)

    def tk_create_new_todo(self):
        self.grid.destroy()
        self.createNew.destroy()
        self.NewFrame = customtkinter.CTkFrame(master=self.body)
        self.NewFrame.pack(padx=5, pady=5, fill='both', expand=True)

        self.nameText = customtkinter.CTkLabel(master=self.NewFrame, text='Name', font=('Times New Roman', 30))
        self.nameText.grid(row=0, column=0, padx=5, pady=5)
        self.newName = customtkinter.CTkEntry(master=self.NewFrame, placeholder_text='Enter Name', font=('Times New Roman', 30), width=400)
        self.newName.grid(row=0, column=1, padx=5, pady=5)

        self.describeText = customtkinter.CTkLabel(master=self.NewFrame, text='Description', font=('Times New Roman', 30))
        self.describeText.grid(row=1, column=0, padx=5, pady=5)
        self.newDescription = customtkinter.CTkTextbox(master=self.NewFrame, width=600, height=100, font=('Times New Roman', 20))
        self.newDescription.grid(row=1, column=1, padx=5, pady=5)

        self.setTimeFrame = customtkinter.CTkFrame(master=self.body)
        self.setTimeFrame.pack(fill='both')

        self.newYearText = customtkinter.CTkLabel(master=self.setTimeFrame, text='Year', font=('Times New Roman', 30))
        self.newYearText.grid(row=0, column=0, padx=5, pady=5)
        self.newYear = customtkinter.CTkOptionMenu(master=self.setTimeFrame, values=[str(i) for i in range(2024, 2050)])
        self.newYear.grid(row=0, column=1, padx=5, pady=5)

        self.newMonthText = customtkinter.CTkLabel(master=self.setTimeFrame, text='Month', font=('Times New Roman', 30))
        self.newMonthText.grid(row=0, column=2, padx=5, pady=5)
        self.newMonth = customtkinter.CTkOptionMenu(master=self.setTimeFrame, values=[str(i) for i in range(1, 13)])
        self.newMonth.grid(row=0, column=3, padx=5, pady=5)

        self.newDayText = customtkinter.CTkLabel(master=self.setTimeFrame, text='Day', font=('Times New Roman', 30))
        self.newDayText.grid(row=0, column=4, padx=5, pady=5)
        self.newDay = customtkinter.CTkOptionMenu(master=self.setTimeFrame, values=[str(i) for i in range(1, 32)])
        self.newDay.grid(row=0, column=5, padx=5, pady=5)

        self.newHourText = customtkinter.CTkLabel(master=self.setTimeFrame, text='Hour', font=('Times New Roman', 30))
        self.newHourText.grid(row=1, column=0, padx=5, pady=5)
        self.newHour = customtkinter.CTkOptionMenu(master=self.setTimeFrame, values=[str(i) for i in range(0, 24)])
        self.newHour.grid(row=1, column=1, padx=5, pady=5)

        self.newMinuteText = customtkinter.CTkLabel(master=self.setTimeFrame, text='Minute', font=('Times New Roman', 30))
        self.newMinuteText.grid(row=1, column=2, padx=5, pady=5)
        self.newMinute = customtkinter.CTkOptionMenu(master=self.setTimeFrame, values=[str(i) for i in range(0, 60)])
        self.newMinute.grid(row=1, column=3, padx=5, pady=5)

        self.newSecondText = customtkinter.CTkLabel(master=self.setTimeFrame, text='Second', font=('Times New Roman', 30))
        self.newSecondText.grid(row=1, column=4, padx=5, pady=5)
        self.newSecond = customtkinter.CTkOptionMenu(master=self.setTimeFrame, values=[str(i) for i in range(0, 60)])
        self.newSecond.grid(row=1, column=5, padx=5, pady=5)

        self.commitTime = customtkinter.CTkButton(master=self.body, text='Commit', font=('Times New Roman', 30), command=self.create_new_todo)
        self.commitTime.pack(padx=5, pady=5)
    def create_new_todo(self):
        self.user.todolist.add_todo(self.newName.get(), self.newDescription.get('1.0'), int(self.newYear.get()), int(self.newMonth.get()), int(self.newDay.get()), int(self.newHour.get()), int(self.newMinute.get()), int(self.newSecond.get()))
        print(self.newName.get(), self.newDescription.get('1.0', customtkinter.END), int(self.newYear.get()), int(self.newMonth.get()), int(self.newDay.get()), int(self.newHour.get()), int(self.newMinute.get()), int(self.newSecond.get()))
        print('Done')

    def create_user(self):
        assert self.flag['register']
        name = self.registerName.get()
        password = self.registerPassword.get()
        self.users.append(User(name, password))
        self.data[name] = {"password": password, "todo":[]}
        print(self.users)
        self.bodyRegisterButton.destroy()
        registerSuccess = customtkinter.CTkLabel(master=self.body, text=f'Success', font=('Times New Roman', 40), text_color='#EEEEEE')
        registerSuccess.pack(padx=12, pady=20)

    def login(self):
        if self.flag['login']:
            name = self.loginName.get()
            password = self.loginPassword.get()
            for user in self.users:
                if name == user.name and password == user.password:
                    self.user = user
                    self.bodyLoginButton.destroy()
                    loginSuccess = customtkinter.CTkLabel(master=self.body, text='Success', font=('Times New Roman', 40), text_color='#EEEEEE')
                    loginSuccess.pack(padx=12, pady=20)
                    self.logined.configure(text=f'Welcome,{self.user.name}!')
                    print(user)
                else:
                    loginFailed = customtkinter.CTkLabel(master=self.body, text='UserName or Password isnt right, please try again', font=('Times New Roman', 40), text_color='#EEEEEE')
                    loginFailed.pack(padx=12, pady=20)
                    print("failed")
        else:
            print("Not login")


if __name__ == '__main__':
    todo = Todo()
    todo.run()
