from tkinter import *

window = Tk()
window.geometry('400x300')
window.title('Body Mass Index')
#Creating frame on a whole window to place elements
frame = Frame(window)
frame.pack(expand=True)

#BMI counter function without return? only print()
def b_m_counter():
    #Exception checker
    try:
        kg = float(weight_text_frame.get())
        m = int(height_text_frame.get()) / 100
    except ValueError:
        print('Были введены цифры, неверный формат!')
    else:
        bmi = kg/(m*m)
        bmi = round(bmi, 1)
        if bmi < 18.5:
            print('Недостаток веса')
        elif 18.5 <= bmi < 24.9:
            print('Средний вес все ок')
        elif 24.9 <= bmi < 29.9:
            print('Чуть больше среднего но ок')
        else: print('Ожирение')

#Text labels
height_l = Label(frame, text='Your height(cm):')
height_l.grid(row=2, column=1)
weight_l = Label(frame, text='Your weight(kg):')
weight_l.grid(row=3, column=1)

#Input text frames
height_text_frame = Entry(frame)
height_text_frame.grid(row=2, column=2)
weight_text_frame = Entry(frame)
weight_text_frame.grid(row=3, column=2)

#Button
counter_button = Button(frame, text='Рассчитать!', command=b_m_counter, bg='#1142AA', )
counter_button.grid(row=4, column=2)

window.mainloop()
