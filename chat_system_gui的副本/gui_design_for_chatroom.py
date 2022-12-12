from tkinter import *
from tkinter.messagebox import *

import fontTools.fontBuilder

from chat_server import *
import json
import threading
import csv
import datetime

class chatroom:
    # constructor method
    def __init__(self, send, recv, sm, s):
        # chat window which is currently hidden
        self.now = datetime.datetime.now()
        self.Window = Tk()
        self.Window.withdraw()
        # self.login_window = Tk()
        # self.login_window.withdraw()
        self.send = send
        self.recv = recv
        self.sm = sm
        self.socket = s
        self.my_msg = ""
        self.system_msg = ""
        self.lan = 0

    # def verify(self):
    #     pass

    def login(self):

        self.login = Toplevel()
        self.login.title('Login')
        self.login.geometry(
            f"{str(500)}x{str(500)}+" +
            f"{int((self.login.winfo_screenwidth() - 500) / 2)}+" +
            f"{int((self.login.winfo_screenheight() - 500) / 2)}"
        )

        self.bg = Label(self.login, anchor='w', bg='white',
                        justify='center', width=500, height=500)
        self.bg.place(x=0, y=0)
        self.label_banner_set = StringVar()
        self.label_banner_set.set('Welcome to Chatroom')
        self.label_banner = Label(self.login,
                                  anchor='w',
                                  textvariable=self.label_banner_set,
                                  fg='black', bg='white',
                                  font=('Times New Roman', 28),
                                  width=18, height=1)
        self.label_banner.place(x=100, y=100)

        self.lang_set = StringVar()
        self.lang_set.set('select language')
        self.label_lang_set = Label(self.login,
                                    anchor='nw', textvariable=self.lang_set,
                                    fg='black', bg='white',
                                    font=('Times New Roman', 15),
                                    width=20, height=2
                                    )
        self.label_lang_set.place(x=50, y=210)

        self.language = StringVar()
        self.language.set('language')
        self.language_button = Button(self.login,
                                      textvariable=self.language,
                                      width=15, height=2,
                                      command=self.language_switch)
        self.language_button.place(x=270, y=210)

        self.user = StringVar()
        self.user.set('User name')
        self.label_user = Label(self.login,
                                anchor='nw', textvariable=self.user,
                                fg='black', bg='white',
                                font=('Times New Roman', 15),
                                justify=CENTER,
                                width=50, height=1)
        self.label_user.place(x=50, y=290)

        self.pwd = StringVar()
        self.pwd.set('Password')
        self.label_pwd = Label(self.login,
                               anchor='nw', textvariable=self.pwd,
                               fg='black', bg='white',
                               font=('Times New Roman', 15),
                               width=50, height=1)
        self.label_pwd.place(x=50, y=350)

        self.var_usr_name = StringVar()
        self.entry_usr_name = Entry(self.login, textvariable=self.var_usr_name)
        self.entry_usr_name.place(x=270, y=290)

        self.var_pwd = StringVar()
        self.entry_pwd = Entry(self.login, textvariable=self.var_pwd, show='*')
        self.entry_pwd.place(x=270, y=350)

        self.entry_usr_name.focus()
        self.entry_pwd.focus()

        self.login_text_set = StringVar()
        self.login_text_set.set('login')
        self.login_button = Button(self.login,
                                   textvariable=self.login_text_set,
                                   width=4, height=1,
                                   command=lambda: self.verify(self.entry_usr_name.get(),
                                                               self.entry_pwd.get()))
        self.login_button.place(x=330, y=410)

        self.reg_text_set = StringVar()
        self.reg_text_set.set('register')
        self.register_button = Button(self.login,
                                      textvariable=self.reg_text_set,
                                      width=4, height=1,
                                      command=lambda: self.register())
        self.register_button.place(x=50, y=410)

        self.Window.mainloop()

    def register(self):
        self.register = Toplevel()
        self.register.title('register')
        self.register.geometry(
            f"{str(500)}x{str(500)}+" +
            f"{int((self.login.winfo_screenwidth() - 300) / 2)}+" +
            f"{int((self.login.winfo_screenheight() - 300) / 2)}"
        )

        self.label_register = Label(self.register,
                                    anchor='w',
                                    text="welcome to the chatroom",
                                    fg='white', bg='gray',
                                    font=('Times New Roman', 28),
                                    justify=CENTER,
                                    width=18, height=1)
        self.label_register.place(x=100, y=100)

        self.create_user = StringVar()
        self.user.set('Set user name')
        self.label_user = Label(self.register,
                                anchor='nw', textvariable=self.user,
                                fg='black', bg='white',
                                font=('Times New Roman', 12),
                                justify='center', width=50, height=1)
        self.label_user.place(x=50, y=210)

        self.pwd = StringVar()
        self.pwd.set('Set password')
        self.label_pwd = Label(self.register,
                               anchor='nw', textvariable=self.pwd,
                               fg='black', bg='white',
                               font=('Times New Roman', 12),
                               justify='center', width=50, height=1)
        self.label_pwd.place(x=50, y=290)

        self.pwd = StringVar()
        self.pwd.set('Repeat password')
        self.label_repeat_pwd = Label(self.register,
                               anchor='nw', textvariable=self.pwd,
                               fg='black', bg='white',
                               font=('Times New Roman', 12),
                               justify='center', width=50, height=1)
        self.label_repeat_pwd.place(x=50, y=350)

        self.create_usr_name = StringVar()
        self.create_usr_name = Entry(self.register, textvariable=self.create_usr_name)
        self.create_usr_name.place(x=270, y=210)

        self.create_pwd = StringVar()
        self.create_pwd = Entry(self.register, textvariable=self.create_pwd, show='*')
        self.create_pwd.place(x=270, y=290)

        self.repeat_pwd = StringVar()
        self.repeat_pwd = Entry(self.register, textvariable=self.repeat_pwd, show='*')
        self.repeat_pwd.place(x=270, y=350)

        self.create_usr_name.focus()
        self.create_pwd.focus()

        self.registration_button = Button(self.register,
                                          text='Finish Registration',
                                          width=10, height=1,
                                          command=lambda: self.registration_verify(self.create_usr_name.get(),
                                                                                   self.create_pwd.get(),
                                                                                   self.repeat_pwd.get()))
        self.registration_button.place(x=330, y=410)

        self.back_button = Button(self.register,
                                  text='back',
                                  width=4, height=1,
                                  command=lambda: self.login())
        self.back_button.place(x=50, y=410)
        self.Window.mainloop()

    def verify(self, name, key):
        # print(name)
        # print(key)
        if len(name) > 0:
            msg = json.dumps({"action": "login", "name": name, "password": key})
            self.send(msg)
            response = json.loads(self.recv())
            if response['status'] == 'notexist':
                showwarning(title="No account", message="Can't find your account, please register first")
            elif response['status'] == 'wrong':
                showwarning(title="Wrong password", message="your enter a wrong password, please enter again")
            # elif response["status"] == 'ok':
            else:
                self.login.destroy()
                # self.register.destroy()
                self.sm.set_state(S_LOGGEDIN)
                self.sm.set_myname(name)
                self.main_layout(name)
                self.textCons.config(state=NORMAL)
                self.textCons.insert(END, "hello" + "\n\n")
                self.textCons.insert(END, menu + "\n\n")
                self.textCons.config(state=DISABLED)
                self.textCons.see(END)
                process = threading.Thread(target=self.proc)
                process.daemon = True
                process.start()

    def registration_verify(self, name, key, repeat_key):
        # self.reg_signal = False
        if name == "" or key == "":
            showwarning(title="Invalid input", message="User name or password is empty")
            return
        elif key != repeat_key:
            showwarning(title="Invalid input", message="Different password input")
            return
        else:
            self.register.destroy()
            # self.login.destroy()
            msg = json.dumps({'action': 'register', 'name': name, 'password': key})
            self.send(msg)
            response = json.loads(self.recv())
            if response['status'] == 'duplicate':
                showerror(title="Error", message="you have already logged in. Do not register again.")
            elif response['status'] == 'ok':
                showinfo("success", "you have your account now!")
                self.verify(name, key)  # 创建账号之后直接登录
                self.reg_signal = True

                headers = ['users', 'passwords']
                user = {'users': name, 'passwords': key}
                with open('user.csv', 'w', encoding='utf8', newline='') as f:
                    dict_writer = csv.DictWriter(f, fieldnames=headers)
                    dict_writer.writerow(user)

    def language_switch(self):  # 后续需要修改所有button显示; need to fix all texts' variable

        if self.lan == 0:
            answer = askquestion(title='language changing', message='Do you want to switch to Chinese?')
            if answer == "yes":
                self.lan = 1
                self.lang_set.set("选择语言")
                self.user.set("用户名")
                self.pwd.set("密码")
                self.language.set('语言')
                self.reg_text_set.set('注册')
                self.login_text_set.set('登录')
                self.label_banner_set.set('   欢迎来到聊天室')
            else:
                pass
        elif self.lan == 1:
            answer = askquestion(title='语言切换', message='你确定要切换到英文吗?')
            if answer == "yes":
                self.lan = 0
                self.lang_set.set("select language")
                self.user.set("user name")
                self.pwd.set("password")
                self.language.set('language')
                self.reg_text_set.set('register')
                self.login_text_set.set('login')
                self.label_banner_set.set('Welcome to Chatroom')
            else:
                pass

    def update_time(self):
        self.timeLabel = Label(self.Window,
                               bg="#17202A",
                               fg="#EAECEE",
                               font="Helvetica 13 bold",
                               pady=7,
                               text='showme'
                               )
        self.timeLabel.place(relwidth=1)
        self.now = datetime.datetime.now()
        self.timeLabel.configure(text=self.now.strftime("%Y-%m-%d %H:%M:%S"))
        self.Window.after(1000, self.update_time)
        pass

    def main_layout(self, name):  # 优化图形界面
        self.update_time()
        self.name = name
        # to show chat window
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width=False,
                              height=False)
        self.Window.configure(width=470,
                              height=700,
                              bg="#210337")
        self.labelHead = Label(self.Window,
                               bg="#210337",
                               fg="#EAECEE",
                               text='Welcome, ' + self.name + '!',
                               font="Helvetica 13 bold",
                               pady=5)

        self.labelHead.place(relwidth=1)
        self.line = Label(self.Window,
                          width=450,
                          bg="#ABB2B9")

        self.line.place(relwidth=1,
                        rely=0.1,
                        relheight=0.012)

        self.textCons = Text(self.Window,
                             width=20,
                             height=2,
                             bg="#210337",
                             fg="#EAECEE",
                             font="Helvetica 14",
                             padx=5,
                             pady=5)

        self.textCons.place(relheight=0.745,
                            relwidth=1,
                            rely=0.08)

        self.labelBottom = Label(self.Window,
                                 bg="#ABB2B9",
                                 height=80)

        self.labelBottom.place(relwidth=1,
                               rely=0.825)

        self.entryMsg = Entry(self.labelBottom,
                              bg="#562B73",
                              fg="#EAECEE",
                              font="Helvetica 13")

        # place the given widget
        # into the gui window
        self.entryMsg.place(relwidth=0.74,
                            relheight=0.06,
                            rely=0.008,
                            relx=0.011)

        self.entryMsg.focus()

        self.entryMsg.bind('<Return>',
                           lambda event: self.sendButton(self.entryMsg.get()))  # type return to send message, it works!

        # create a Send Button
        self.buttonMsg = Button(self.labelBottom,
                                text="Send",
                                font="Helvetica 10 bold",
                                width=20,
                                bg="#ABB2B9",
                                command=lambda: self.sendButton(self.entryMsg.get()))

        self.buttonMsg.place(relx=0.77,
                             rely=0.008,
                             relheight=0.06,
                             relwidth=0.22)

        self.textCons.config(cursor="arrow")

        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)

        # place the scroll bar
        # into the gui window
        scrollbar.place(relheight=1,
                        relx=0.974)

        scrollbar.config(command=self.textCons.yview)

        self.textCons.config(state=DISABLED)

        # function to basically start the thread for sending messages

    def sendButton(self, msg):
        # self.textCons.config(state=DISABLED)
        self.my_msg = msg
        # print(msg)
        self.entryMsg.delete(0, END)
        self.textCons.config(state=NORMAL)
        self.textCons.insert(END, msg + "\n")
        self.textCons.config(state=DISABLED)
        self.textCons.see(END)
        if msg == 'q':
            showwarning(title='exit', message='you are exiting the chat system')
            self.Window.destroy()

    def proc(self):
        # print(self.msg)
        while True:
            read, write, error = select.select([self.socket], [], [], 0)
            peer_msg = []
            # print(self.msg)
            if self.socket in read:
                peer_msg = self.recv()
            if len(self.my_msg) > 0 or len(peer_msg) > 0:
                # print(self.system_msg)
                self.system_msg = self.sm.proc(self.my_msg, peer_msg)
                self.my_msg = ""
                self.textCons.config(state=NORMAL)
                self.textCons.insert(END, self.system_msg + "\n\n")
                self.textCons.config(state=DISABLED)
                self.textCons.see(END)

    def run(self):
        self.login()


if __name__ == '__main__':
    win = Tk()
    print(font.families())
