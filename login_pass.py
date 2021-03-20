from tkinter import *
from tkinter import messagebox
from textwrap import wrap
import pickle

root = Tk()
root.geometry("300x500")
root.title('Войти в систему')


def registration():
    text = Label(text="Для входа в систему зарегистрируйтесь !")
    text_login = Label(text="Введите логин : ")
    registr_login = Entry()
    text_password1 = Label(text="Введите пароль : ")
    registr_password1 = Entry()
    text_password2 = Label(text="Повторите пароль : ")
    registr_password2 = Entry(show="*")
    button_registr = Button(text="Зарегистрироваться", command=lambda: save())
    text.pack()
    text_login.pack()
    registr_login.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()

    def save():
        login_pass_save = {}
        login_pass_save[registr_login.get()] = registr_password1.get()
        f = open('login_pass.txt', 'wb')
        pickle.dump(login_pass_save, f)
        f.close()
        login()


def login():
    text_log = Label(text="Поздравляем!")
    text_enter_login = Label(text="Введите логин : ")
    enter_login = Entry()
    text_enter_pass = Label(text="Введите пароль : ")
    enter_password = Entry(show="*")
    text_log.pack()
    button_login = Button(text="Войти", command=lambda: log_pass())
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_password.pack()
    button_login.pack()

    def log_pass():
        if enter_password.get() == "admin" and enter_login.get()== "admin" :
            Admin=Tk()
            Admin.title("Администратор")
            Admin.geometry('1100x400')
            
            label1 = Label(Admin, text="Добро пожаловать Админ!", font=("Impact", 25))   
            label1.grid(row=0, column=0)
            btn1 = Button(Admin, text="Хорошего вам дня")  
            btn1.grid(column=1, row=0)
            Admin.mainloop()
        else:
            
            f = open('login_pass.txt', 'rb')
            a = pickle.load(f)
            f.close()
            if enter_login.get() in a:
                if enter_password.get() == a[enter_login.get()]:
                    okno=Tk()
                    okno.title("Приложение")
                    okno.geometry('600x400')

                    text="Добро пожаловать Пользователь!Чтобы войти как Админ, закройте это окно и введите (логин:admin пароль:admin)"
                    
                    label = Label(okno, text=text, font=("Arial Black", 19))   
                    label.grid(row=0, column=0)

                    okno.update()

                    width = label.winfo_width()

                    if width > 600:
                        char_width = width / len(text)
                        wrapped_text = '\n'.join(wrap(text, int(600 / char_width)))
                        label['text'] = wrapped_text
                    okno.mainloop()
                else:
                    messagebox.showerror("Ошибка!", "Вы вели неверный логин или пароль. ")
            else:
                messagebox.showerror("Ошибка!", "Неверный логин.")


registration()
root.mainloop()