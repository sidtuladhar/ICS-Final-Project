import tkinter as tk
import tkinter.messagebox

lan = "english"
getData = []


def signUp(usrName, usrPwd):
    with open('data.txt', 'a') as usrFile:
        usrFile.writelines("{}\n{}\n".format(usrName, usrPwd))


def compare():
    name = var_usr_name.get()
    pwd = var_usr_pwd.get()
    usrName, usrPwd = name, pwd
    getData = removeN()
    g = 0
    while (g < (len(getData) - 1)):
        if usrName == getData[g] and g % 2 == 0 and usrPwd == getData[g + 1]:
            tk.messagebox.showinfo(title='login',
                                   message='Welcome, {}. You have successfully logged in.'.format(usrName))
            break
        g = g + 1
    if g == len(getData) - 1:
        tk.messagebox.showwarning(title="error", message="The user name and password are incorrect.")


def removeN():
    asd = " "
    c = ""
    bd = []
    de = 0
    fg = "\n"
    with open('data.txt', 'r') as usrFile:
        asd = usrFile.readlines()
        for j in range(len(asd)):
            er = asd[j]
            pos = er.index(fg)
            cex = er[0:pos]
            bd.append(cex)
            de = 0
            cex = ""
        return bd


def language():
    global lan
    answer = False
    if lan == "english":
        answer = tk.messagebox.askquestion(title='language changing', message='Do you want to switch to Chinese?')
        if answer == "yes":
            lan = "spanish"
            d_name.set("选择语言")
            e_name.set("用户名")
            f_name.set("密码")
        else:
            pass
    elif lan == "中文":
        answer = tk.messagebox.askquestion(title='language changing', message='Do you want to switch to English?')
        if answer == "yes":
            lan = "english"
            d_name.set("select language")
            e_name.set("user name")
            f_name.set("password")
        else:
            pass


window = tk.Tk()
window.title('Fake PowerSchool Help Students!')
window.geometry('500x500')
z = tk.Label(window, anchor='w', bg='white',
             justify='center', width=500, height=500)
z.place(x=0, y=0)
a = tk.Label(window, anchor='w', text="PowerSchool SIS",
             fg='white', bg='darkblue', font=('TimesNewRoman', 30),
             justify='center', width=20, height=1)
a.place(x=50, y=100)

b = tk.Label(window, anchor='nw', text="Student and Parent Sign In",
             fg='black', bg='white', font=('TimesNewRoman', 12),
             justify='center', width=50, height=20)
b.place(x=50, y=150)

c = tk.Button(window, text='language', width=15,
              height=2, command=language)
c.place(x=270, y=200)

d_name = tk.StringVar()
d_name.set("select language")
d = tk.Label(window, anchor='nw', textvariable=d_name,
             fg='black', bg='white', font=('TimesNewRoman', 12),
             justify='center', width=20, height=2)
d.place(x=50, y=210)

e_name = tk.StringVar()
e_name.set("user name")
e = tk.Label(window, anchor='nw', textvariable=e_name,
             fg='black', bg='white', font=('TimesNewRoman', 12),
             justify='center', width=50, height=1)
e.place(x=50, y=290)

f_name = tk.StringVar()
f_name.set("password")
f = tk.Label(window, anchor='nw', textvariable=f_name,
             fg='black', bg='black', font=('TimesNewRoman', 12),
             justify='center', width=50, height=1)
f.place(x=50, y=350)

g = tk.Button(window, text='login', width=4,
              height=1, command=compare)
g.place(x=330, y=410)

var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=270, y=290)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=270, y=350)

window.mainloop()

