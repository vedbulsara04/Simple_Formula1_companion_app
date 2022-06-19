from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
import mysql.connector


window = Tk()
window.title('Formula 1 companion')
frame = Frame(master = window)
frame.grid(row=0, column=0)

#------------------MySQL---------------------#
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'formula_1'
)
if mydb:
    print('Yes')
else:
    print('No')

#-------------------------------------------------#
def driver_champ(event):
    wdc = Tk()
    wdc.title("World Driver's Championship") 
    wdc_cur = mydb.cursor()
    wdc_cur.execute('SELECT * FROM wdc limit 0,20')
    i = 0
    for wdc_points in wdc_cur:
        for j in range(len(wdc_points)):
            e1 = Entry(wdc, width = 50, fg = 'blue')
            e1.grid(row = i, column = j)
            e1.insert(END, wdc_points[j])
        i = i+1

def construct_champ(event):
    wcc = Tk()
    wcc.title("World Constructor's Championship")
    wcc_cur = mydb.cursor()
    wcc_cur.execute('SELECT * FROM wcc limit 0,10')
    i = 0
    for wcc_points in wcc_cur:
        for j in range(len(wcc_points)):
            e2 = Entry(wcc, width = 50, fg = 'blue')
            e2.grid(row = i, column = j)
            e2.insert(END, wcc_points[j])
        i = i+1

def race_calendar(event):
    rcal = Tk()
    rcal.title("Race Calendar")
    rcal_cur = mydb.cursor()
    rcal_cur.execute('SELECT * FROM rcal limit 0,22')
    i = 0
    for rcalendar in rcal_cur:
        for j in range(len(rcalendar)):
            e2 = Entry(rcal, width = 50, fg = 'blue')
            e2.grid(row = i, column = j)
            e2.insert(END, rcalendar[j])
        i = i+1
#-------------------------------------------------#

small_font = Font(
    family = 'Helvetica',
    size = 3,
    weight = 'bold',
    slant = 'italic',
    underline = 0,
    overstrike = 0

)
big_font = Font(
    family = 'Times',
    size = 15,
    weight = 'bold',
    slant = 'roman',
    underline = 0,
    overstrike = 0
)
#-------------------------------------------------#

lbl_title = Label(master=frame, text = 'Formula 1 companion app',font = big_font )
lbl_title.grid(row = 0, column = 0,padx=3)

btn_latest_news = Button(master = frame, text = 'Latest News')
btn_latest_news.grid(row = 0, column = 1,padx = 3,pady = 0)

btn_driver_champ = Button(master = frame, text="World Driver's Championship")
btn_driver_champ.grid(row = 0, column = 2,padx = 3,pady = 0)
btn_driver_champ.bind('<Button-1>',driver_champ)

btn_construct_champ = Button(master = frame, text="World Constructor's Championship")
btn_construct_champ.grid(row = 0, column = 3,padx = 3,pady = 0)
btn_construct_champ.bind('<Button-1>',construct_champ)

btn_circuit = Button(master = frame, text = 'Race Circuit Info')
btn_circuit.grid(row = 0, column = 4,padx = 3,pady = 0)

btn_calendar = Button(master=frame, text= 'Race Calendar')
btn_calendar.grid(row = 0, column = 5,padx = 3,pady = 0)
btn_calendar.bind('<Button-1>',race_calendar)
#-----------------------Images-----------------------------------#
f1_logo_raw = Image.open('f1_logo.png')
f1_logo_resized = f1_logo_raw.resize((100,80), Image.ANTIALIAS)
f1_logo = ImageTk.PhotoImage(f1_logo_resized)
l_f1_logo = Label(master = window, image = f1_logo)
l_f1_logo.grid(row = 0, column = 6)

f1_front_page_raw = Image.open('f1_front_page.png')
f1_front_page_resized = f1_front_page_raw.resize((1175,700), Image.ANTIALIAS)
f1_front_page = ImageTk.PhotoImage(f1_front_page_resized)
l_f1_frontpage = Label(master = window, image = f1_front_page)
l_f1_frontpage.grid(row = 2, column = 0)

win_logo = PhotoImage(file = 'D:\\COLLEGE\\1.Programming_In_Python\\Formula_1_mini_project\\f1_logo.png')
window.iconphoto(False, win_logo)

#----------------------------------------------------------------#
window.mainloop()
