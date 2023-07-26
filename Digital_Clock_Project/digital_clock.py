from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am_pm = time.strftime('%p')
    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')

    hour_window.config(text=hr)
    min_window.config(text=mi)
    sec_window.config(text=sec)
    am_window.config(text=am_pm)
    date_window.config(text=date)
    month_window.config(text=month)
    year_window.config(text=year)
    day_window.config(text=day)

    hour_window.after(200, date_time)


clock = Tk()

clock.title('Digital Clock ')

clock.geometry('1000x500')

clock.config(bg='black')

# Hour
hour_window = Label(clock, text='00',
                    font=('Time New Roman', 60, 'bold'),
                    bg='white',
                    fg='black')
hour_window.place(x=120, y=50, height=110, width=100)

hour_label = Label(clock, text='Hour',
                   font=('Time New Roman', 20, 'bold'),
                   bg='white',
                   fg='black')
hour_label.place(x=120, y=190, height=40, width=100)

# Minutes
min_window = Label(clock, text='00',
                   font=('Time New Roman', 60, 'bold'),
                   bg='white',
                   fg='black')
min_window.place(x=340, y=50, height=110, width=100)

min_label = Label(clock, text='Min.',
                  font=('Time New Roman', 20, 'bold'),
                  bg='white',
                  fg='black')
min_label.place(x=340, y=190, height=40, width=100)

# Seconds
sec_window = Label(clock, text='00',
                   font=('Time New Roman', 60, 'bold'),
                   bg='white',
                   fg='black')
sec_window.place(x=560, y=50, height=110, width=100)

sec_label = Label(clock, text='Sec.',
                  font=('Time New Roman', 20, 'bold'),
                  bg='white',
                  fg='black')
sec_label.place(x=560, y=190, height=40, width=100)

# AM/PM
am_window = Label(clock, text='00',
                  font=('Time New Roman', 50, 'bold'),
                  bg='white',
                  fg='black')
am_window.place(x=780, y=50, height=110, width=100)

am_label = Label(clock, text='AM/PM',
                 font=('Time New Roman', 20, 'bold'),
                 bg='white',
                 fg='black')
am_label.place(x=780, y=190, height=40, width=100)

# Date
date_window = Label(clock, text='00',
                    font=('Time New Roman', 60, 'bold'),
                    bg='white',
                    fg='black')
date_window.place(x=120, y=270, height=110, width=100)

date_label = Label(clock, text='Date',
                   font=('Time New Roman', 20, 'bold'),
                   bg='white',
                   fg='black')
date_label.place(x=120, y=410, height=40, width=100)

# Month
month_window = Label(clock, text='00',
                     font=('Time New Roman', 60, 'bold'),
                     bg='white',
                     fg='black')
month_window.place(x=340, y=270, height=110, width=100)

month_label = Label(clock, text='Month',
                    font=('Time New Roman', 20, 'bold'),
                    bg='white',
                    fg='black')
month_label.place(x=340, y=410, height=40, width=100)

# Year
year_window = Label(clock, text='00',
                    font=('Time New Roman', 60, 'bold'),
                    bg='white',
                    fg='black')
year_window.place(x=560, y=270, height=110, width=100)

year_label = Label(clock, text='Year',
                   font=('Time New Roman', 20, 'bold'),
                   bg='white',
                   fg='black')
year_label.place(x=560, y=410, height=40, width=100)

# Day
day_window = Label(clock, text='00',
                   font=('Time New Roman', 35, 'bold'),
                   bg='white',
                   fg='black')
day_window.place(x=780, y=270, height=110, width=100)

day_label = Label(clock, text='Day',
                  font=('Time New Roman', 20, 'bold'),
                  bg='white',
                  fg='black')
day_label.place(x=780, y=410, height=40, width=100)

date_time()
clock.mainloop()
