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

from User import User
from greeting import rand_greeting


class Todo:
    """应用程序"""
    def __init__(self):
        self.users: list[User] = []
        self.user = None

        self.flag = {'login': True, 'register': False, 'main': False}

        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')

        self.root = customtkinter.CTk()
        self.root.geometry('1024x720')

        self.head = customtkinter.CTkFrame(master=self.root)
        self.head.pack(padx=20, pady=10, fill='both', expand=True)

        self.title = customtkinter.CTkLabel(master=self.head, text='Todo System', font=('Times New Roman', 72), text_color='#555555')
        self.title.pack(padx=12, pady=20)

        self.greeting = customtkinter.CTkLabel(master=self.head, text=f'{rand_greeting()}', font=('Times New Roman', 18), text_color='#BBBBDD')
        self.greeting.pack(padx=12, pady=10)

        self.loginButton = customtkinter.CTkButton(master=self.head, text='Login', font=('Times New Roman', 20), command=lambda: self.change('login'))
        self.loginButton.pack(side=customtkinter.LEFT, padx=20, pady=20)

        self.registerButton = customtkinter.CTkButton(master=self.head, text='Register', font=('Times New Roman', 20), command=lambda: self.change('register'))
        self.registerButton.pack(side=customtkinter.LEFT, padx=20, pady=20)

        self.mainButton = customtkinter.CTkButton(master=self.head, text='Todo', font=('Times New Roman', 20), command=lambda: self.change('main'))
        self.mainButton.pack(side=customtkinter.LEFT, padx=20, pady=20)

        self.returnButton = customtkinter.CTkButton(master=self.head, text='Return', font=('Times New Roman', 20), command=lambda : self.change())
        self.returnButton.pack(side=customtkinter.LEFT, padx=20, pady=20)

        """Body"""
        self.body = customtkinter.CTkFrame(master=self.root)
        self.body.pack(padx=20, pady=10, fill='both', expand=True)


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

        self.loginbutton = customtkinter.CTkButton(master=self.body, text='Login', font=('Times New Roman', 20), command=self.update)
        self.loginbutton.pack(padx=20, pady=20)

    def tk_register(self):
        self.registerText = customtkinter.CTkLabel(master=self.body, text=f'Register', font=('Times New Roman', 50), text_color='#555555')
        self.registerText.pack(padx=12, pady=20)

        self.registerName = customtkinter.CTkEntry(master=self.body, placeholder_text='Enter Your UserName', font=('Times New Roman', 30), width=500)
        self.registerName.pack(padx=40, pady=20)

        self.registerPassword = customtkinter.CTkEntry(master=self.body, placeholder_text='Enter Your Password',  font=('Times New Roman', 30), width=500)
        self.registerPassword.pack(padx=40, pady=20)

        self.registerbutton = customtkinter.CTkButton(master=self.body, text='Register', font=('Times New Roman', 20), command=self.create_user)
        self.registerbutton.pack(padx=20, pady=20)


    def create_user(self):
        if self.flag['register']:
            name = self.registerName.get()
            password = self.registerPassword.get()
            self.users.append(User(name, password))
            print(self.users)
        else:
            print('Not Login')

    def login(self):
        for i in range(3):
            name = input("输入用户名 ")
            password = input("输入密码 ")
            for user in self.users:
                if user.name == name and user.password == password:
                    print(f"登陆成功!\n你好,{user.name}")
                    return user
            print(f"不是一个有效的用户名或密码, 你还有 {2 - i} 次机会")
        return None


if __name__ == '__main__':
    todo = Todo()
    todo.run()
