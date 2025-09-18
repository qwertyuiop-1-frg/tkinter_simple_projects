import customtkinter as ctk
from tkinter import messagebox, Button, Frame


def username_getter():
    while True:
        username = ctk.CTkInputDialog(text='Enter your username: ').get_input()
        if username:
            return username
        else:
            messagebox.showerror("Ошибка", "Некорректный ввод!")

def user_text(username):
    try:
        user_inputted_text = entry.get()
        if user_inputted_text == '':
            raise ValueError
    except ValueError:
        print('Пустая строка!')
    else:
        entry.delete(0, ctk.END)
        with open('user_messages.txt', 'a') as messages:
            messages.write(f'{username} > {user_inputted_text}\n')

def changes():
    with open('user_messages.txt', 'r') as messages_reading:
        text = messages_reading.read()
    usr_text.configure(text=text)
    scrollable_frame.after(1000, changes)
#Main window
window = ctk.CTk()
window.geometry('432x768')
window.title('A beautiful chat _["]_')

#Creating a frame of Window
frame = Frame(window, padx=10, pady=10)
frame.pack(expand=True)

#Getting Username
username = username_getter()

#Create Labels, Buttons
scrollable_frame = ctk.CTkScrollableFrame(frame, width=400, height=668)
scrollable_frame.grid()
entry = ctk.CTkEntry(frame, placeholder_text="Enter Text")
entry.grid()
usr_text = ctk.CTkLabel(scrollable_frame, text='')
usr_text.pack()
changes()
some_button = Button(frame, text='Tap me!', command=lambda: user_text(username))
some_button.grid()
window.mainloop()
