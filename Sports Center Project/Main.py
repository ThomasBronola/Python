import tkinter as tk
from tkinter import *
import tkinter.messagebox
import sqlite3

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

def connection():
    try:
        conn = sqlite3.connect("SportsCenter.db")
    except:
        print("cannot connect to the database")
    return conn

def clear():
    txtName.delete(0, END)
    txtMonth.delete(0, END)
    txtDay.delete(0, END)
    txtYear.delete(0, END)
    txtFacility.delete(0, END)
    txtType.delete(0, END)
    txtTime.delete(0, END)
    txtDuration.delete(0, END)
    txtPtype.delete(0, END)
    txtAmount.delete(0, END)
    txtArea.delete(1.0, END)
    txtArea.insert(END, "When Adding all Parameters are Required\n")
    txtArea.insert(END, "When Editing only The Facility, Transaction, Time, Duration, Payment Type and Amount will be Updated.\n")
    txtArea.insert(END, "When Deleting Name, Month, Day and Year are Required\n\n")

def verify():
    if not txtName.get():
        txtArea.insert(END, "\n\nName is Required\n")
    if not txtMonth.get():
        txtArea.insert(END, "Month is Required\n")
    if not txtDay.get():
        txtArea.insert(END, "Day is Required\n")
    if not txtYear.get():
        txtArea.insert(END, "Year is Required\n")
    if not txtFacility.get():
        txtArea.insert(END, "Facility is Required\n")
    if not txtType.get():
        txtArea.insert(END, "Tansaction Type is Require\n")
    if not txtDuration.get():
        txtArea.insert(END, "Duration is Required\n")
    if not txtName.get():
        txtArea.insert(END, "Name is Required\n")
    if not txtPtype.get():
        txtArea.insert(END, "Payment Type is Required\n")
    else:
        return 1

def night():
    conn = connection()
    cur = conn.cursor()
    durasyon = txtDuration.get()
    dur = int(durasyon)
    cur.execute("SELECT night_price from PRICE where Facility = ?", [txtFacility.get()])
    presyo = cur.fetchall()
    for x in presyo:
        tagal = x[0] * dur
        return tagal

def day():
    conn = connection()
    cur = conn.cursor()
    durasyon = txtDuration.get()
    dur = int(durasyon)
    cur.execute("SELECT day_price from PRICE where Facility = ?", [txtFacility.get()])
    presyo = cur.fetchall()
    for x in presyo:
        tagal = x[0] * dur
        return tagal

def exclusive():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT day_price from PRICE where Facility = ?", [txtFacility.get()])
    presyo = cur.fetchall()
    for x in presyo:
        tagal = x[0]
        return tagal

def chkexclusive():
    if txtFacility.get() == "Comference rooms(2 boxes equipment, 8 hours use)":
        return 1
    if txtFacility.get() == "Basketball gym covered court(8 hours use)":
        return 1
    if txtFacility.get() == "Oval, Open courts(8 hours use)":
        return 1
    if txtFacility.get() == "Swimming Pool(8 hours use)":
        return 1
    if txtFacility.get() == "Lawntennis(8 hours use)":
        return 1
    if txtFacility.get() == "Badminton(8 hours use/ 3 courts)":
        return 1
    if txtFacility.get() == "Table tennis(8 hours use/ 4 courts)":
        return 1
    if txtFacility.get() == "Sepak Takraw(8 hours use)":
        return 1
    if txtFacility.get() == "Boxing ring set(3 1/2 hrs/session)":
        return 1
    if txtFacility.get() == "Running track(3 1/2 hrs/session)":
        return 1
    else:
        return 0

def add():
    conn = connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS TRANSACT (NAME TEXT, MONTH TEXT, DAY INT, YEAR INT, FACILITY TEXT, "
                "TTYPE TEXT, TIME TEXT , DURATION TEXT , PTYPE TEXT, AMOUNT INT)")
    i = verify()
    if i == 1:
        if txtDuration.get() == "EXCLUSIVE":
            total = exclusive()
            cur.execute("INSERT INTO TRANSACT VALUES(?,?,?,?,?,?,?,?,?,?)", (
                txtName.get(), txtMonth.get(), txtDay.get(), txtYear.get(), txtFacility.get(),
                txtType.get(),
                txtTime.get(),
                txtDuration.get(), txtPtype.get(), total))
            conn.commit()
            conn.close()
            t = str(total)
            s = "Transaction Added!" + "\n" + "Total Amount is: " + t
            tkinter.messagebox.showinfo("Alert", s)
            clear()
        else:
            chk = chkexclusive()
            if chk == 1:
                total = exclusive()
                cur.execute("INSERT INTO TRANSACT VALUES(?,?,?,?,?,?,?,?,?,?)", (
                    txtName.get(), txtMonth.get(), txtDay.get(), txtYear.get(), txtFacility.get(),
                    txtType.get(),
                    txtTime.get(),
                    txtDuration.get(), txtPtype.get(), total))
                conn.commit()
                conn.close()
                t = str(total)
                s = "Transaction Added!" + "\n" + "Total Amount is: " + t
                tkinter.messagebox.showinfo("Alert", s)
                clear()
            else:
                araw = txtTime.get()
                if araw == "NIGHT":
                    total = night()
                    cur.execute("INSERT INTO TRANSACT VALUES(?,?,?,?,?,?,?,?,?,?)", (
                        txtName.get(), txtMonth.get(), txtDay.get(), txtYear.get(), txtFacility.get(),
                        txtType.get(),
                        txtTime.get(),
                        txtDuration.get(), txtPtype.get(), total))
                    conn.commit()
                    conn.close()
                    t = str(total)
                    s = "Transaction Added!" + "\n" + "Total Amount is: " + t
                    tkinter.messagebox.showinfo("Alert", s)
                    clear()
                else:
                    total = day()
                    cur.execute("INSERT INTO TRANSACT VALUES(?,?,?,?,?,?,?,?,?,?)", (
                        txtName.get(), txtMonth.get(), txtDay.get(), txtYear.get(), txtFacility.get(),
                        txtType.get(),
                        txtTime.get(),
                        txtDuration.get(), txtPtype.get(), total))
                    conn.commit()
                    conn.close()
                    t = str(total)
                    s = "Transaction Added!" + "\n" + "Total Amount is: " + t
                    tkinter.messagebox.showinfo("Alert", s)
                    clear()

def view():
    clear()
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM TRANSACT")
    data = cur.fetchall()
    conn.close()
    txtArea.insert(END, "LIST OF TRANSACTIONS:\n")
    for i in data:
        txtArea.insert(END, str(i) + "\n")

def delete():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(name) FROM TRANSACT WHERE name = ? and month = ? and day = ? and year = ?",
                (txtName.get(), txtMonth.get(), txtDay.get(), txtYear.get()))
    validate = cur.fetchall()
    for i in validate:
        if i[0] == 0:
            tkinter.messagebox.showerror("Error!", "Name Does Not Match With Any Of The Records.")
        else:
            cur.execute("DELETE FROM TRANSACT WHERE name = ? and month = ? and day = ? and year = ?",
                        (txtName.get(), txtMonth.get(), txtDay.get(), txtYear.get(),))
            conn.commit()
            conn.close()
            tkinter.messagebox.showinfo("Alert", "Transaction Deleted!")
            clear()

def update():
    conn = connection()
    cur = conn.cursor()
    i = verify()
    if i == 1:
        if txtDuration.get() == "EXCLUSIVE":
            total = exclusive()
            cur.execute(
                "UPDATE TRANSACT SET facility=?, ttype=?, time=?, duration=?, ptype=?, amount=? where name=? and month=? and year=?",
                (txtFacility.get(), txtType.get(), txtTime.get(), txtDuration.get(), txtPtype.get(), total,
                 txtName.get(), txtMonth.get(), txtYear.get()))
            conn.commit()
            tkinter.messagebox.showinfo("Information", "Transaction Successfully Updated.")
            conn.close()
            t = str(total)
            s = "Transaction Added!" + "\n" + "Total Amount is: " + t
            tkinter.messagebox.showinfo("Alert", s)
            clear()
        else:
            chk = chkexclusive()
            if chk == 1:
                total = exclusive()
                cur.execute(
                    "UPDATE TRANSACT SET facility=?, ttype=?, time=?, duration=?, ptype=?, amount=? where name=? and month=? and year=?",
                    (txtFacility.get(), txtType.get(), txtTime.get(), txtDuration.get(), txtPtype.get(), total,
                     txtName.get(), txtMonth.get(), txtYear.get()))
                conn.commit()
                tkinter.messagebox.showinfo("Information", "Transaction Successfully Updated.")
                conn.close()
                t = str(total)
                s = "Transaction Added!" + "\n" + "Total Amount is: " + t
                tkinter.messagebox.showinfo("Alert", s)
                clear()
            else:
                araw = txtTime.get()
                if araw == "NIGHT":
                    total = night()
                    cur.execute(
                        "UPDATE TRANSACT SET facility=?, ttype=?, time=?, duration=?, ptype=?, amount=? where name=? and month=? and year=?",
                        (txtFacility.get(), txtType.get(), txtTime.get(), txtDuration.get(), txtPtype.get(), total,
                         txtName.get(), txtMonth.get(), txtYear.get()))
                    conn.commit()
                    tkinter.messagebox.showinfo("Information", "Transaction Successfully Updated.")
                    conn.close()
                    t = str(total)
                    s = "Transaction Added!" + "\n" + "Total Amount is: " + t
                    tkinter.messagebox.showinfo("Alert", s)
                    clear()
                else:
                    total = day()
                    cur.execute(
                        "UPDATE TRANSACT SET facility=?, ttype=?, time=?, duration=?, ptype=?, amount=? where name=? and month=? and year=?",
                        (txtFacility.get(), txtType.get(), txtTime.get(), txtDuration.get(), txtPtype.get(), total,
                         txtName.get(), txtMonth.get(), txtYear.get()))
                    conn.commit()
                    tkinter.messagebox.showinfo("Information", "Transaction Successfully Updated.")
                    conn.close()
                    t = str(total)
                    s = "Transaction Added!" + "\n" + "Total Amount is: " + t
                    tkinter.messagebox.showinfo("Alert", s)
                    clear()

def danalysis():
    txtArea.delete(1.0, END)
    conn = connection()
    cur = conn.cursor()
    txtArea.insert(END, "DATA ANALYSIS\n")

    cur.execute("SELECT count(name) FROM TRANSACT")
    number = cur.fetchall()
    for row in number:
        txtArea.insert(END, "\nTOTAL VISITORS: ")
        txtArea.insert(END, row[0])

    cur.execute("SELECT count(TIME) FROM TRANSACT where TIME='DAY'")
    td = cur.fetchall()
    for rows in td:
        txtArea.insert(END, "\nTOTAL DAY TIME VISITORS: ")
        txtArea.insert(END, rows[0])
        totalday = 100 * (rows[0] / row[0])

    cur.execute("SELECT count(TIME) FROM TRANSACT where TIME='NIGHT'")
    tn = cur.fetchall()
    for rowss in tn:
        txtArea.insert(END, "\nTOTAL NIGHT TIME VISITORS: ")
        txtArea.insert(END, rowss[0])
        totalnight = 100 * (rowss[0] / row[0])

    cur.execute("SELECT count(TTYPE) FROM TRANSACT where TTYPE='WALK IN'")
    tw = cur.fetchall()
    for twi in tw:
        totwalkin = twi[0]
        percentwalkin = 100 * (totwalkin / row[0])

        cur.execute("SELECT count(TTYPE) FROM TRANSACT where TTYPE='RESERVATION'")
        td = cur.fetchall()
        for twd in td:
            totreservation = twd[0]
            percentreservation = 100 * (totreservation / row[0])

        #PERCENTAGES
        txtArea.insert(END, "\n\nPERCENTAGE OF DAY TIME VISITORS: ")
        txtArea.insert(END, totalday)
        txtArea.insert(END, "%")
        txtArea.insert(END, "\nPERCENTAGE OF NIGHT TIME VISITORS: ")
        txtArea.insert(END, totalnight)
        txtArea.insert(END, "%")
        txtArea.insert(END, "\n\nPERCENTAGE OF WALK IN VISITORS: ")
        txtArea.insert(END, percentwalkin)
        txtArea.insert(END, "%")
        txtArea.insert(END, "\nPERCENTAGE OF RESERVE VISITORS: ")
        txtArea.insert(END, percentreservation)
        txtArea.insert(END, "%")
        txtArea.insert(END, "\n\n")

    txtArea.insert(END, "WALK IN")
    cur.execute("SELECT FACILITY, count(FACILITY) FROM TRANSACT  WHERE TTYPE='WALK IN' GROUP by FACILITY ORDER by count(facility) DESC LIMIT 1")
    data = cur.fetchall()
    for i in data:
        txtArea.insert(END,"\nThe Most Frequently Used Facility is the ")
        txtArea.insert(END, i[0])

    cur.execute("SELECT count(FACILITY) FROM TRANSACT  WHERE TTYPE='WALK IN' AND FACILITY = ? GROUP by FACILITY ORDER by count(facility) DESC",[i[0]])
    rec = cur.fetchall()
    for j in rec:
        txtArea.insert(END, "\nNumber Of Walk In's: ")
        txtArea.insert(END, j[0])

    cur.execute("SELECT FACILITY, count(FACILITY) FROM TRANSACT  WHERE TTYPE='WALK IN' GROUP by FACILITY ORDER by count(facility) ASC LIMIT 1")
    one = cur.fetchall()
    for k in one:
        txtArea.insert(END, "\nThe Least Used Facility is the ")
        txtArea.insert(END, k[0])

    cur.execute("SELECT count(FACILITY) FROM TRANSACT  WHERE TTYPE='WALK IN' AND FACILITY = ? GROUP by FACILITY ORDER by count(facility) ASC LIMIT 1",[k[0]])
    rec = cur.fetchall()
    for l in rec:
        txtArea.insert(END, "\nNumber Of Walk In's: ")
        txtArea.insert(END, l[0])

    cur.execute("SELECT count(FACILITY) from TRANSACT where TTYPE='WALK IN'")
    tots = cur.fetchall()
    totsa = l[0] + j[0]
    for u in tots:
        otherW = u[0] - totsa
        txtArea.insert(END, "\nNumber of Walk In in Other Facilities: ")
        txtArea.insert(END, otherW)
        txtArea.insert(END, "\n\nTotal Walk In's: ")
        txtArea.insert(END, u[0])

    cur.execute("SELECT count(time) FROM TRANSACT where TTYPE='WALK IN' and time='DAY'")
    two = cur.fetchall()
    for p in two:
        txtArea.insert(END, "\nTotal Walk In (DAY) ")
        txtArea.insert(END, p[0])

    cur.execute("SELECT count(time) FROM TRANSACT where TTYPE='WALK IN' and time='NIGHT'")
    two = cur.fetchall()
    for q in two:
        txtArea.insert(END, "\nTotal Walk In (NIGHT) ")
        txtArea.insert(END, q[0])

    #RESERVATION
    txtArea.insert(END,"\n\nRESERVATION")
    cur.execute("SELECT FACILITY, count(FACILITY) FROM TRANSACT  WHERE TTYPE='RESERVATION' GROUP by FACILITY ORDER by count(facility) DESC LIMIT 1")
    data = cur.fetchall()
    for m in data:
        txtArea.insert(END, "\nThe Most Frequently Used Facility is the ")
        txtArea.insert(END, m[0])

    cur.execute("SELECT count(FACILITY) FROM TRANSACT  WHERE TTYPE='RESERVATION' AND FACILITY = ? GROUP by FACILITY ORDER by count(facility) DESC",[m[0]])
    rec = cur.fetchall()
    for n in rec:
        txtArea.insert(END, "\nNumber Of Reservations: ")
        txtArea.insert(END, n[0])

    cur.execute("SELECT FACILITY, count(FACILITY) FROM TRANSACT  WHERE TTYPE='RESERVATION' GROUP by FACILITY ORDER by count(facility) ASC LIMIT 1")
    one = cur.fetchall()
    for o in one:
        txtArea.insert(END, "\nThe Least Used Facility is the ")
        txtArea.insert(END, o[0])

    cur.execute("SELECT count(FACILITY) FROM TRANSACT  WHERE TTYPE='RESERVATION' AND FACILITY = ? GROUP by FACILITY ORDER by count(facility) ASC LIMIT 1",[o[0]])
    rec = cur.fetchall()
    for p in rec:
        txtArea.insert(END, "\nNumber Of Reservations: ")
        txtArea.insert(END, p[0])

    cur.execute("SELECT count(FACILITY) from TRANSACT WHERE TTYPE = 'RESERVATION'")
    fe = cur.fetchall()
    tot = p[0] + n[0]
    for t in fe:
        otherR = t[0] - tot
        txtArea.insert(END, "\nNumber of Reservations in Other Facilities: ")
        txtArea.insert(END, otherR)
        txtArea.insert(END,"\n\nTotal Reservations: ")
        txtArea.insert(END, t[0])

    cur.execute("SELECT count(time) FROM TRANSACT where TTYPE='RESERVATION' and time='DAY'")
    three = cur.fetchall()
    for r in three:
        txtArea.insert(END, "\nTotal Reservations(DAY): ")
        txtArea.insert(END, r[0])

    cur.execute("SELECT count(time) FROM TRANSACT where TTYPE='RESERVATION' and time='NIGHT'")
    four = cur.fetchall()
    for s in four:
        txtArea.insert(END, "\nTotal Reservations(NIGHT): ")
        txtArea.insert(END, s[0])

def gui():
    root = Tk()
    root.geometry("1366x705+-3+7")
    root.minsize(120, 1)
    root.maxsize(1370, 749)
    root.resizable(1, 1)
    root.title("Sports Center")

    txtName = StringVar()
    txtMonth = StringVar()
    txtDay = StringVar()
    txtYear = StringVar()
    txtFacility = StringVar()
    txtType = StringVar()  # WALK IN OR RESERVATION
    txtTime = StringVar()  # NIGHT OR DAY
    txtDuration = StringVar()  # HOURS INT OR "EXCLUSIVE"
    txtPtype = StringVar()
    txtAmount = StringVar()

    # Frame Setup
    ContentFrame = Frame(root)
    ContentFrame.place(relx=0.010, rely=0.014, relheight=0.973, relwidth=0.980)
    ContentFrame.configure(background="#fdb5bf")

    TitleFrame = tk.Frame(ContentFrame)
    TitleFrame.place(relx=0.0, rely=0.0, relheight=0.14, relwidth=1.0)
    TitleFrame.configure(background="#359aff")

    Title = tk.Label(TitleFrame)
    Title.place(relx=0.277, rely=0.208, height=53, width=564)
    Title.configure(font="-family {Stencil} -size 24 -weight bold")
    Title.configure(foreground="#000000")
    Title.configure(background="#359aff")
    Title.configure(text='''SPORTS CENTER''')

    OutFrame = tk.Frame(ContentFrame)
    OutFrame.place(relx=0.0, rely=0.656, relheight=0.343, relwidth=1.0)
    OutFrame.configure(background="#d9d9d9")

    # Label Setup
    lblName = tk.Label(ContentFrame, text='''Name:''', background="#fdb5bf", foreground="#000000",
                       font="-family {Segoe UI} -size 10 -weight bold")
    lblName.place(relx=0.057, rely=0.16, height=34, width=58)

    lblDate = tk.Label(ContentFrame, background="#fdb5bf", text='''Date:''',
                       font="-family {Segoe UI} -size 10 -weight bold")
    lblDate.place(relx=0.055, rely=0.233, height=32, width=58)

    lblFacility = tk.Label(ContentFrame, background="#fdb5bf", text='''Facility:''',
                           font="-family {Segoe UI} -size 10 -weight bold")
    lblFacility.place(relx=0.06, rely=0.335, height=22, width=62)

    lblMonth = tk.Label(ContentFrame, background="#fdb5bf", text='''Month''',
                        font="-family {Segoe UI} -size 9 -slant italic")
    lblMonth.place(relx=0.157, rely=0.292, height=12, width=123)

    lblDay = tk.Label(ContentFrame, background="#fdb5bf", text='''Day''',
                      font="-family {Segoe UI} -size 9 -slant italic")
    lblDay.place(relx=0.269, rely=0.292, height=12, width=55)

    lblYear = tk.Label(ContentFrame, background="#fdb5bf", text='''Year''',
                       font="-family {Segoe UI} -size 9 -slant italic")
    lblYear.place(relx=0.329, rely=0.292, height=12, width=84)

    lblPtype = tk.Label(ContentFrame, background="#fdb5bf", text='''Payment Type:''',
                        font="-family {Segoe UI} -size 10 -weight bold")
    lblPtype.place(relx=0.457, rely=0.335, height=22, width=97)

    lblDuration = tk.Label(ContentFrame, background="#fdb5bf", text='''Duration:''',
                           font="-family {Segoe UI} -size 10 -weight bold")
    lblDuration.place(relx=0.457, rely=0.233, height=22, width=62)

    lblSubDuration = tk.Label(ContentFrame, background="#fdb5bf",
                              text='''Enter the amount of hours or the word "EXCLUSIVE" if the option has a default 8 hours''',
                              font="-family {Segoe UI} -size 9 -slant italic")
    lblSubDuration.place(relx=0.539, rely=0.277, height=21, width=447)

    lblTime = tk.Label(ContentFrame, background="#fdb5bf", font="-family {Segoe UI} -size 10 -weight bold",
                       text='''Time:''')
    lblTime.place(relx=0.457, rely=0.16, height=31, width=41)

    lblAmount = tk.Label(ContentFrame, background="#fdb5bf", font="-family {Segoe UI} -size 10 -weight bold",
                         text='''Amount:''')
    lblAmount.place(relx=0.457, rely=0.408, height=23, width=61)

    lblType = tk.Label(ContentFrame, background="#fdb5bf", font="-family {Segoe UI} -size 10 -weight bold",
                       text='''Transaction Type:''')
    lblType.place(relx=0.06, rely=0.408, height=22, width=118)

    # TextArea Setup
    txtArea = tk.Text(OutFrame, font="-family {Segoe UI} -size 10 -weight bold", selectbackground="#c4c4c4")
    txtArea.insert(END, "When Adding all Parameters are Required")
    txtArea.insert(END,
                   "\nWhen Editing only The Facility, Transaction, Time, Duration, Payment Type and Amount will be Updated.")
    txtArea.insert(END, "\nWhen Deleting Name, Month, Day and Year is Required")
    txtArea.place(relx=0.0, rely=0.043, relheight=0.864, relwidth=0.999)

    # Entry Setup & Combo-box Setup
    txtName = tk.Entry(ContentFrame, background="white", font="-family {Segoe UI} -size 10")
    txtName.place(relx=0.154, rely=0.16, height=30, relwidth=0.243)

    txtMonth = ttk.Combobox(ContentFrame, values=
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
     'December'])
    txtMonth.place(relx=0.157, rely=0.233, relheight=0.045, relwidth=0.107)

    txtDay = tk.Entry(ContentFrame, background="white", font="-family {Segoe UI} -size 10")
    txtDay.place(relx=0.277, rely=0.233, height=30, relwidth=0.04)

    txtYear = tk.Entry(ContentFrame, background="white", font="-family {Segoe UI} -size 10")
    txtYear.place(relx=0.329, rely=0.233, height=30, relwidth=0.063)

    txtFacility = ttk.Combobox(ContentFrame, values=
    ["Soccerfield(w/ 25 lights)", "Soccerfield(w/ 50 lights)", "Soccerfield(w/ 75 lights)",
     "Soccerfield(w/ 100 lights)", "Basketball gym", "Basketball open court", "Table Tennis",
     "Badminton", "Volleyball", "Lawntennis", "Sepak Takraw", "Swimming pool", "Running track(3 1/2 hrs/session)",
     "Boxing ring set(3 1/2 hrs/session)",
     "Billiards(2 boxes equipment)", "Comference rooms(2 boxes equipment, 8 hours use)",
     "Basketball gym covered court(8 hours use)", "Oval, Open courts(8 hours use)", "Swimming Pool(8 hours use)",
     "Lawntennis(8 hours use)", "Badminton(8 hours use/ 3 courts)", "Table tennis(8 hours use/ 4 courts)",
     "Sepak Takraw(8 hours use)"
     ])
    txtFacility.place(relx=0.157, rely=0.321, relheight=0.047, relwidth=0.242)

    txtType = ttk.Combobox(ContentFrame, values=['WALK IN', 'RESERVATION', ])
    txtType.place(relx=0.157, rely=0.408, relheight=0.045, relwidth=0.243)

    txtTime = ttk.Combobox(ContentFrame, values=['DAY', 'NIGHT', ])
    txtTime.place(relx=0.539, rely=0.16, relheight=0.045, relwidth=0.243)

    txtDuration = tk.Entry(ContentFrame, background="white", font="-family {Segoe UI} -size 10")
    txtDuration.place(relx=0.539, rely=0.233, height=30, relwidth=0.243)

    txtPtype = ttk.Combobox(ContentFrame, values=['CASH', 'CREDIT CARD', ])
    txtPtype.place(relx=0.539, rely=0.335, relheight=0.045, relwidth=0.243)

    txtAmount = tk.Entry(ContentFrame, background="white", font="-family {Segoe UI} -size 10")
    txtAmount.place(relx=0.539, rely=0.408, height=30, relwidth=0.243)

    # Button Setup
    buttAdd = tk.Button(ContentFrame, text='''Add''', command=add)
    buttAdd.place(relx=0.21, rely=0.525, height=34, width=97)

    buttEdit = tk.Button(ContentFrame, text='''Edit''', command=update)
    buttEdit.place(relx=0.314, rely=0.525, height=34, width=97)

    buttDel = tk.Button(ContentFrame, text='''Delete''', command=delete)
    buttDel.place(relx=0.524, rely=0.525, height=34, width=97)

    buttAnalysis = tk.Button(ContentFrame, text='''Data Analysis''', command=danalysis)
    buttAnalysis.place(relx=0.629, rely=0.525, height=34, width=97)

    buttView = tk.Button(ContentFrame, text='''View''', command=view)
    buttView.place(relx=0.419, rely=0.525, height=34, width=97)

    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.geometry("1366x705+-3+7")
    root.minsize(120, 1)
    root.maxsize(1370, 749)
    root.resizable(1, 1)
    root.title("Sports Center")

    txtName = StringVar()
    txtMonth = StringVar()
    txtDay = StringVar()
    txtYear = StringVar()
    txtFacility = StringVar()
    txtType = StringVar()  # WALK IN OR RESERVATION
    txtTime = StringVar()  # NIGHT OR DAY
    txtDuration = StringVar()  # HOURS INT OR "EXCLUSIVE"
    txtPtype = StringVar()
    txtAmount = StringVar()

    # Frame Setup
    ContentFrame = Frame(root)
    ContentFrame.place(relx=0.010, rely=0.014, relheight=0.973, relwidth=0.980)
    ContentFrame.configure(background="#fdb5bf")

    TitleFrame = tk.Frame(ContentFrame)
    TitleFrame.place(relx=0.0, rely=0.0, relheight=0.14, relwidth=1.0)
    TitleFrame.configure(background="#359aff")

    Title = tk.Label(TitleFrame)
    Title.place(relx=0.277, rely=0.208, height=53, width=564)
    Title.configure(font="-family {Stencil} -size 24 -weight bold")
    Title.configure(foreground="#000000")
    Title.configure(background="#359aff")
    Title.configure(text='''SPORTS CENTER''')

    OutFrame = tk.Frame(ContentFrame)
    OutFrame.place(relx=0.0, rely=0.656, relheight=0.343, relwidth=1.0)
    OutFrame.configure(background="#d9d9d9")

    # Label Setup
    lblName = tk.Label(ContentFrame, text='''Name:''', background="#fdb5bf", foreground="#000000",
                       font="-family {Segoe UI} -size 10 -weight bold")
    lblName.place(relx=0.057, rely=0.16, height=34, width=58)

    lblDate = tk.Label(ContentFrame, background="#fdb5bf", text='''Date:''',
                       font="-family {Segoe UI} -size 10 -weight bold")
    lblDate.place(relx=0.055, rely=0.233, height=32, width=58)

    lblFacility = tk.Label(ContentFrame, background="#fdb5bf", text='''Facility:''',
                           font="-family {Segoe UI} -size 10 -weight bold")
    lblFacility.place(relx=0.06, rely=0.335, height=22, width=62)

    lblMonth = tk.Label(ContentFrame, background="#fdb5bf", text='''Month''',
                        font="-family {Segoe UI} -size 9 -slant italic")
    lblMonth.place(relx=0.157, rely=0.292, height=12, width=123)

    lblDay = tk.Label(ContentFrame, background="#fdb5bf", text='''Day''',
                      font="-family {Segoe UI} -size 9 -slant italic")
    lblDay.place(relx=0.269, rely=0.292, height=12, width=55)

    lblYear = tk.Label(ContentFrame, background="#fdb5bf", text='''Year''',
                       font="-family {Segoe UI} -size 9 -slant italic")
    lblYear.place(relx=0.329, rely=0.292, height=12, width=84)

    lblPtype = tk.Label(ContentFrame, background="#fdb5bf", text='''Payment Type:''',
                        font="-family {Segoe UI} -size 10 -weight bold")
    lblPtype.place(relx=0.457, rely=0.335, height=22, width=97)

    lblDuration = tk.Label(ContentFrame, background="#fdb5bf", text='''Duration:''',
                           font="-family {Segoe UI} -size 10 -weight bold")
    lblDuration.place(relx=0.457, rely=0.233, height=22, width=62)

    lblSubDuration = tk.Label(ContentFrame, background="#fdb5bf",
                              text='''Enter the amount of hours or the word "EXCLUSIVE" if the option has a default 8 hours''',
                              font="-family {Segoe UI} -size 9 -slant italic")
    lblSubDuration.place(relx=0.539, rely=0.277, height=21, width=447)

    lblTime = tk.Label(ContentFrame, background="#fdb5bf", font="-family {Segoe UI} -size 10 -weight bold",
                       text='''Time:''')
    lblTime.place(relx=0.457, rely=0.16, height=31, width=41)

    lblAmount = tk.Label(ContentFrame, background="#fdb5bf", font="-family {Segoe UI} -size 10 -weight bold",
                         text='''Amount:''')
    lblAmount.place(relx=0.457, rely=0.408, height=23, width=61)

    lblType = tk.Label(ContentFrame, background="#fdb5bf", font="-family {Segoe UI} -size 10 -weight bold",
                       text='''Transaction Type:''')
    lblType.place(relx=0.06, rely=0.408, height=22, width=118)

    # TextArea Setup
    txtArea = tk.Text(OutFrame, font="-family {Segoe UI} -size 10 -weight bold", selectbackground="#c4c4c4")
    txtArea.insert(END, "When Adding all Parameters are Required")
    txtArea.insert(END, "\nWhen Editing only The Facility, Transaction, Time, Duration, Payment Type and Amount will be Updated.")
    txtArea.insert(END, "\nWhen Deleting Name, Month, Day and Year is Required")
    txtArea.place(relx=0.0, rely=0.043, relheight=0.864, relwidth=0.999)

    # Entry Setup & Combo-box Setup
    txtName = tk.Entry(ContentFrame, background="white", font="-family {Segoe UI} -size 10")
    txtName.place(relx=0.154, rely=0.16, height=30, relwidth=0.243)

    txtMonth = ttk.Combobox(ContentFrame, values=
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
     'December'])
    txtMonth.place(relx=0.157, rely=0.233, relheight=0.045, relwidth=0.107)

    txtDay = tk.Entry(ContentFrame, background="white", font="-family {Segoe UI} -size 10")
    txtDay.place(relx=0.277, rely=0.233, height=30, relwidth=0.04)

    txtYear = tk.Entry(ContentFrame, background="white", font="-family {Segoe UI} -size 10")
    txtYear.place(relx=0.329, rely=0.233, height=30, relwidth=0.063)

    txtFacility = ttk.Combobox(ContentFrame, values=
    ["Soccerfield(w/ 25 lights)", "Soccerfield(w/ 50 lights)", "Soccerfield(w/ 75 lights)","Soccerfield(w/ 100 lights)", "Basketball gym", "Basketball open court", "Table Tennis",
    "Badminton", "Volleyball", "Lawntennis", "Sepak Takraw", "Swimming pool", "Running track(3 1/2 hrs/session)", "Boxing ring set(3 1/2 hrs/session)",
     "Billiards(2 boxes equipment)", "Comference rooms(2 boxes equipment, 8 hours use)", "Basketball gym covered court(8 hours use)", "Oval, Open courts(8 hours use)", "Swimming Pool(8 hours use)",
     "Lawntennis(8 hours use)", "Badminton(8 hours use/ 3 courts)", "Table tennis(8 hours use/ 4 courts)", "Sepak Takraw(8 hours use)"
     ])
    txtFacility.place(relx=0.157, rely=0.321, relheight=0.047, relwidth=0.242)

    txtType = ttk.Combobox(ContentFrame, values=['WALK IN', 'RESERVATION', ])
    txtType.place(relx=0.157, rely=0.408, relheight=0.045, relwidth=0.243)

    txtTime = ttk.Combobox(ContentFrame, values=['DAY', 'NIGHT', ])
    txtTime.place(relx=0.539, rely=0.16, relheight=0.045, relwidth=0.243)

    txtDuration = tk.Entry(ContentFrame, background="white", font="-family {Segoe UI} -size 10")
    txtDuration.place(relx=0.539, rely=0.233, height=30, relwidth=0.243)

    txtPtype = ttk.Combobox(ContentFrame, values=['CASH', 'CREDIT CARD', ])
    txtPtype.place(relx=0.539, rely=0.335, relheight=0.045, relwidth=0.243)

    txtAmount = tk.Entry(ContentFrame, background="white", font="-family {Segoe UI} -size 10")
    txtAmount.place(relx=0.539, rely=0.408, height=30, relwidth=0.243)

    # Button Setup
    buttAdd = tk.Button(ContentFrame, text='''Add''', command=add)
    buttAdd.place(relx=0.21, rely=0.525, height=34, width=97)

    buttEdit = tk.Button(ContentFrame, text='''Edit''', command=update)
    buttEdit.place(relx=0.314, rely=0.525, height=34, width=97)

    buttDel = tk.Button(ContentFrame, text='''Delete''', command=delete)
    buttDel.place(relx=0.524, rely=0.525, height=34, width=97)

    buttAnalysis = tk.Button(ContentFrame, text='''Data Analysis''', command=danalysis)
    buttAnalysis.place(relx=0.629, rely=0.525, height=34, width=97)

    buttView = tk.Button(ContentFrame, text='''View''', command=view)
    buttView.place(relx=0.419, rely=0.525, height=34, width=97)

    root.mainloop()