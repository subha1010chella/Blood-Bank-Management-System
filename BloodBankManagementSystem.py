import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import pymysql


root = tk.Tk()
root.title("Hospital Management System")
root.geometry("600x500")

frame1 = tk.Frame(root, width=600, height=500)
frame2 = tk.Frame(root, width=600, height=500)
frame3 = tk.Frame(root, width=600, height=500)
frame4 = tk.Frame(root, width=600, height=500)
frame5 = tk.Frame(root, width=600, height=500)
frame6 = tk.Frame(root, width=600, height=500)
frame7 = tk.Frame(root, width=600, height=500)
frame8 = tk.Frame(root, width=600, height=500)
frame9 = tk.Frame(root, width=600, height=500)
frame10 = tk.Frame(root, width=600, height=500)

un = tk.StringVar()
pw = tk.StringVar()

id_ = tk.StringVar()
name_ = tk.StringVar()
age_ = tk.StringVar()
exp_ = tk.StringVar()
contact_ = tk.StringVar()
deptno_ = tk.StringVar()


pid = tk.StringVar()
pname = tk.StringVar()
pcontact = tk.StringVar()
pdob = tk.StringVar()
pbg = tk.StringVar()
pailment = tk.StringVar()
ptreat = tk.StringVar()
pdeptno = tk.StringVar()
pdid = tk.StringVar()


grp = tk.StringVar()
ava = tk.StringVar()

pid_ = tk.StringVar()
did_ = tk.StringVar()

bg = tk.StringVar()

def user():
    global un,pw
    use = un.get()
    pwe = pw.get()
    if str(use) == 'user' and int(pwe) == 0000:
        frame1.pack_forget()
        frame2.pack()
    elif str(use) == 'admin' and int(pwe) == 3333:
        frame1.pack_forget()
        frame3.pack()

    else:
        messagebox.showinfo("Details", "User Not Found")
#--------------------------------------------------------------------


def exit_():
    root.destroy()


def doc_details():
    frame2.pack_forget()
    frame8.pack()

def pat_details():
    frame2.pack_forget()
    frame7.pack()

def blood_details():
    frame2.pack_forget()
    frame10.pack()

def doc_new():
    frame3.pack_forget()
    frame4.pack()

def blood_new():
    frame3.pack_forget()
    frame6.pack()
    
def pat_new():
    frame3.pack_forget()
    frame5.pack()

#-------------------------------------------------------

def GButton_174_command():
    global id_,name_,age_,exp_,contact_,deptno_
    id_=id_.get()
    name_ = name_.get()
    age_ = age_.get()
    exp_ = exp_.get()
    contact_ = contact_.get()
    deptno_ = deptno_.get() 
    print(id_,name_,age_,exp_,contact_,deptno_)
    if id_ == "" or name_ == "" or age_ == "" or exp_ == "" or contact_ == "" or deptno_ == "":
        messagebox.showinfo("Details", "Please Enter All Details")
    else:
        con=pymysql.connect(host='localhost',user='root',password='ssn1',db='varshini')
        cur=con.cursor()
        if(id_=="" or name_=="" or age_=="" or exp_=="" or contact_=="" or deptno_==""):
            tk.messagebox.showinfo("Error","All fields are required")
        else:
            cur.execute("insert into doctors values({0}, '{1}', '{2}', {3}, {4}, {5})".format(int(id_),name_,contact_,int(age_),int(exp_),int(deptno_)))
            con.commit()
            con.close()
            tk.messagebox.showinfo("Success","Record inserted successfully")

#-------------------------------------------------------
def GButton_999_command():
    global pid,pname,pcontact,pdob,pbg,pailment,ptreat,pdeptno,pdid
    pid = pid.get()
    pname = pname.get()
    pcontact = pcontact.get()
    pdob = pdob.get()
    pbg = pbg.get()
    pailment = pailment.get()
    ptreat = ptreat.get()
    pdeptno = pdeptno.get()
    pdid = pdid.get()
    if pid == "" or pname == "" or pcontact == "" or pdob == "" or pbg == "" or pailment == "" or ptreat == "" or pdeptno == "" or pdid=="":
        messagebox.showinfo("Details", "Please Enter All Details")
    else:
        con=pymysql.connect(host='localhost',user='root',password='ssn1',db='varshini')
        cur=con.cursor()
        if(pid=="" or pname=="" or pcontact=="" or pdob=="" or pbg=="" or pailment=="" or ptreat=="" or pdeptno==""):
            tk.messagebox.showinfo("Error","All fields are required")
        else:
            cur.execute("insert into patients values({0}, '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', {7}, {8} )".format(int(pid),pname,pcontact,pdob,pbg,pailment,ptreat,int(pdeptno),int(pdid)))
            con.commit()
            con.close()
            tk.messagebox.showinfo("Success","Record inserted successfully")

#-------------------------------------------------------
def enter():
    global grp,ava
    con=pymysql.connect(host='localhost',user='root',password='ssn1',db='varshini')
    cur=con.cursor()
    ava=ava.get()
    grp = grp.get()
    if grp == "" or ava=="":
        messagebox.showinfo("Details", "Please Enter All Details")
    else:
        cur.execute("update blood set availability = {0} where bgroup = '{1}'".format(int(ava),grp.capitalize()))
        con.commit()
        con.close()
        tk.messagebox.showinfo("Success","Availability updated successfully")

#----------------------------------------------------------

def GButton_432_command():
    global pid_
    con = pymysql.connect(host='localhost', user='root', password='ssn1', db='varshini')
    cur = con.cursor()
    
    cur.execute("SELECT * FROM patients WHERE patientid = {0}".format(int(pid_.get())))

    result = cur.fetchall()

    if len(result) == 0:
        messagebox.showinfo("Error", "Patient ID not found")
    else:
        messagebox.showinfo('Found', 'Name: {0}\nContact: {1}\nDOB: {2}\nBlood group: {3}\nAilment: {4}\nTreatment id: {5}\nDoctor id: {6}'.format(result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6], result[0][8]))

    con.close() 

#-------------------------------------------------------------------
def GButton_433_command():
    global did_

    con = pymysql.connect(host='localhost', user='root', password='ssn1', db='varshini')
    cur = con.cursor()

    if did_.get() == "":
        messagebox.showinfo("Details", "Please Enter All Details")
    else:
        cur.execute("SELECT name, contactno, exper, deptno FROM doctors WHERE doctorid = {0}".format(int(did_.get())))

        result = cur.fetchall()

        if len(result) == 0:
            tk.messagebox.showinfo("Error", "Doctor ID not found")
        else:
            tk.messagebox.showinfo('Found', 'Name: {0}\nContact: {1}\nExperience: {2}\nDepartment no: {3}'.format(result[0][0], result[0][1], result[0][2], result[0][3]))

    con.close()

#----------------------------------------
def GButton_530_command():
    global bg
    con = pymysql.connect(host='localhost', user='root', password='ssn1', db='varshini')
    cur = con.cursor()

    if bg.get() == "":
        messagebox.showinfo("Details", "Please Enter All Details")
    else:
        cur.execute("select availability from blood where bgroup='{0}'".format(bg.get().capitalize()))
        data=cur.fetchall()
        avail=data[0][0]
        if avail > 0:

            messagebox.showinfo("Blood availablity", "Blood you need is Available!")
        else:
            messagebox.showinfo("Blood availablity", "Sorry, Blood you need is Not Available!")
 

GLineEdit_970=tk.Entry(frame1)
GLineEdit_970["bg"] = "#dfd3c3"
GLineEdit_970["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_970["font"] = ft
GLineEdit_970["fg"] = "#333333"
GLineEdit_970["justify"] = "center"
GLineEdit_970["text"] = "Username"
GLineEdit_970["textvariable"] = un
GLineEdit_970.place(x=310,y=80,width=180,height=60)

GLineEdit_221=tk.Entry(frame1,show="*")
GLineEdit_221["bg"] = "#dfd3c3"
GLineEdit_221["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_221["font"] = ft
GLineEdit_221["fg"] = "#333333"
GLineEdit_221["justify"] = "center"
GLineEdit_221["text"] = "Password"
GLineEdit_221["textvariable"] = pw
GLineEdit_221.place(x=310,y=240,width=180,height=60)

GButton_530=tk.Button(frame1)
GButton_530["bg"] = "#f9e0be"
ft = tkFont.Font(family='Times',size=18)
GButton_530["font"] = ft
GButton_530["fg"] = "#000000"
GButton_530["justify"] = "center"
GButton_530["text"] = "Login"
GButton_530.place(x=220,y=350,width=130,height=60)
GButton_530["command"] = user

GLabel_353=tk.Label(frame1)
GLabel_353["bg"] = "#c7b198"
ft = tkFont.Font(family='Times',size=18)
GLabel_353["font"] = ft
GLabel_353["fg"] = "#393d49"
GLabel_353["justify"] = "center"
GLabel_353["text"] = "Username"
GLabel_353.place(x=70,y=80,width=180,height=60)

GLabel_187=tk.Label(frame1)
GLabel_187["bg"] = "#c7b198"
ft = tkFont.Font(family='Times',size=18)
GLabel_187["font"] = ft
GLabel_187["fg"] = "#333333"
GLabel_187["justify"] = "center"
GLabel_187["text"] = "Password"
GLabel_187.place(x=70,y=240,width=180,height=60)

#--------------------------------------------------------

GButton_432=tk.Button(frame2)
GButton_432["bg"] = "#3e8e7e"
ft = tkFont.Font(family='Times',size=18)
GButton_432["font"] = ft
GButton_432["fg"] = "#000000"
GButton_432["justify"] = "center"
GButton_432["text"] = "Patient details"
GButton_432.place(x=190,y=30,width=210,height=70)
GButton_432["command"] = pat_details

GButton_234=tk.Button(frame2)
GButton_234["bg"] = "#7cd1b8"
ft = tkFont.Font(family='Times',size=18)
GButton_234["font"] = ft
GButton_234["fg"] = "#000000"
GButton_234["justify"] = "center"
GButton_234["text"] = "Doctor details"
GButton_234.place(x=190,y=140,width=210,height=70)
GButton_234["command"] = doc_details

GButton_175=tk.Button(frame2)
GButton_175["bg"] = "#fabb51"
ft = tkFont.Font(family='Times',size=18)
GButton_175["font"] = ft
GButton_175["fg"] = "#000000"
GButton_175["justify"] = "center"
GButton_175["text"] = "Blood Availability"
GButton_175.place(x=190,y=260,width=210,height=70)
GButton_175["command"] = blood_details

GButton_336=tk.Button(frame2)
GButton_336["bg"] = "#faedc6"
ft = tkFont.Font(family='Times',size=18)
GButton_336["font"] = ft
GButton_336["fg"] = "#000000"
GButton_336["justify"] = "center"
GButton_336["text"] = "Exit"
GButton_336.place(x=190,y=370,width=210,height=70)
GButton_336["command"] = exit_

#--------------------------------------------------

GButton_561=tk.Button(frame3)
GButton_561["bg"] = "#feece9"
ft = tkFont.Font(family='Times',size=18)
GButton_561["font"] = ft
GButton_561["fg"] = "#393d49"
GButton_561["justify"] = "center"
GButton_561["text"] = "New Patient"
GButton_561.place(x=190,y=80,width=210,height=70)
GButton_561["command"] = pat_new

GButton_541=tk.Button(frame3)
GButton_541["bg"] = "#ccd1e4"
ft = tkFont.Font(family='Times',size=18)
GButton_541["font"] = ft
GButton_541["fg"] = "#393d49"
GButton_541["justify"] = "center"
GButton_541["text"] = "New Doctor"
GButton_541.place(x=190,y=220,width=210,height=70)
GButton_541["command"] = doc_new

GButton_669=tk.Button(frame3)
GButton_669["bg"] = "#fe7e6d"
ft = tkFont.Font(family='Times',size=18)
GButton_669["font"] = ft
GButton_669["fg"] = "#393d49"
GButton_669["justify"] = "center"
GButton_669["text"] = "Blood Level Update"
GButton_669.place(x=190,y=360,width=210,height=70)
GButton_669["command"] = blood_new

#----------------------


GLabel_788=tk.Label(frame4)
GLabel_788["bg"] = "#676FA3"
ft = tkFont.Font(family='Times',size=18)
GLabel_788["font"] = ft
GLabel_788["fg"] = "#333333"
GLabel_788["justify"] = "center"
GLabel_788["text"] = "Doctor Id"
GLabel_788.place(x=70,y=40,width=180,height=40)

GLabel_881=tk.Label(frame4)
GLabel_881["bg"] = "#676FA3"
ft = tkFont.Font(family='Times',size=18)
GLabel_881["font"] = ft
GLabel_881["fg"] = "#333333"
GLabel_881["justify"] = "center"
GLabel_881["text"] = "Name"
GLabel_881.place(x=70,y=100,width=180,height=40)

GLineEdit_356=tk.Entry(frame4)
GLineEdit_356["bg"] = "#CDDEFF"
GLineEdit_356["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_356["font"] = ft
GLineEdit_356["fg"] = "#333333"
GLineEdit_356["justify"] = "center"
GLineEdit_356["text"] = "id"
GLineEdit_356["textvariable"] = id_
GLineEdit_356.place(x=310,y=40,width=180,height=40)

GLineEdit_536=tk.Entry(frame4)
GLineEdit_536["bg"] = "#CDDEFF"
GLineEdit_536["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_536["font"] = ft
GLineEdit_536["fg"] = "#333333"
GLineEdit_536["justify"] = "center"
GLineEdit_536["text"] = "name"
GLineEdit_536["textvariable"] = name_
GLineEdit_536.place(x=310,y=100,width=180,height=40)

GButton_174=tk.Button(frame4)
GButton_174["bg"] = "#548CFF"
ft = tkFont.Font(family='Times',size=18)
GButton_174["font"] = ft
GButton_174["fg"] = "#393d49"
GButton_174["justify"] = "center"
GButton_174["text"] = "Enter"
GButton_174.place(x=210,y=410,width=130,height=40)
GButton_174["command"] = GButton_174_command

GLabel_899=tk.Label(frame4)
GLabel_899["bg"] = "#676FA3"
ft = tkFont.Font(family='Times',size=18)
GLabel_899["font"] = ft
GLabel_899["fg"] = "#333333"
GLabel_899["justify"] = "center"
GLabel_899["text"] = "Age"
GLabel_899.place(x=70,y=160,width=180,height=40)

GLineEdit_322=tk.Entry(frame4)
GLineEdit_322["bg"] = "#CDDEFF"
GLineEdit_322["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_322["font"] = ft
GLineEdit_322["fg"] = "#333333"
GLineEdit_322["justify"] = "center"
GLineEdit_322["text"] = "age"
GLineEdit_322["textvariable"] = age_
GLineEdit_322.place(x=310,y=160,width=180,height=40)

GLabel_461=tk.Label(frame4)
GLabel_461["bg"] = "#676FA3"
ft = tkFont.Font(family='Times',size=18)
GLabel_461["font"] = ft
GLabel_461["fg"] = "#333333"
GLabel_461["justify"] = "center"
GLabel_461["text"] = "Experience"
GLabel_461.place(x=70,y=220,width=180,height=40)

GLineEdit_852=tk.Entry(frame4)
GLineEdit_852["bg"] = "#CDDEFF"
GLineEdit_852["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_852["font"] = ft
GLineEdit_852["fg"] = "#333333"
GLineEdit_852["justify"] = "center"
GLineEdit_852["text"] = "exp"
GLineEdit_852["textvariable"] = exp_
GLineEdit_852.place(x=310,y=220,width=180,height=40)

GLabel_972=tk.Label(frame4)
GLabel_972["bg"] = "#676FA3"
ft = tkFont.Font(family='Times',size=18)
GLabel_972["font"] = ft
GLabel_972["fg"] = "#333333"
GLabel_972["justify"] = "center"
GLabel_972["text"] = "Contact"
GLabel_972.place(x=70,y=280,width=180,height=40)

GLineEdit_929=tk.Entry(frame4)
GLineEdit_929["bg"] = "#CDDEFF"
GLineEdit_929["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_929["font"] = ft
GLineEdit_929["fg"] = "#333333"
GLineEdit_929["justify"] = "center"
GLineEdit_929["text"] = "contact"
GLineEdit_929["textvariable"] = contact_
GLineEdit_929.place(x=310,y=280,width=180,height=40)

GLabel_84=tk.Label(frame4)
GLabel_84["bg"] = "#676FA3"
ft = tkFont.Font(family='Times',size=18)
GLabel_84["font"] = ft
GLabel_84["fg"] = "#333333"
GLabel_84["justify"] = "center"
GLabel_84["text"] = "Department No."
GLabel_84.place(x=70,y=340,width=180,height=40)

GLineEdit_544=tk.Entry(frame4)
GLineEdit_544["bg"] = "#CDDEFF"
GLineEdit_544["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_544["font"] = ft
GLineEdit_544["fg"] = "#333333"
GLineEdit_544["justify"] = "center"
GLineEdit_544["text"] = "deptno"
GLineEdit_544["textvariable"] = deptno_
GLineEdit_544.place(x=310,y=340,width=180,height=40)

#------------------------------------------------------
GLabel_788=tk.Label(frame5)
GLabel_788["bg"] = "#f999b7"
ft = tkFont.Font(family='Times',size=18)
GLabel_788["font"] = ft
GLabel_788["fg"] = "#333333"
GLabel_788["justify"] = "center"
GLabel_788["text"] = "Patient Id"
GLabel_788.place(x=70,y=10,width=180,height=40)

GLabel_881=tk.Label(frame5)
GLabel_881["bg"] = "#f999b7"
ft = tkFont.Font(family='Times',size=18)
GLabel_881["font"] = ft
GLabel_881["fg"] = "#333333"
GLabel_881["justify"] = "center"
GLabel_881["text"] = "Name"
GLabel_881.place(x=70,y=60,width=180,height=40)

GLineEdit_356=tk.Entry(frame5)
GLineEdit_356["bg"] = "#f9c5d5"
GLineEdit_356["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_356["font"] = ft
GLineEdit_356["fg"] = "#333333"
GLineEdit_356["justify"] = "center"
GLineEdit_356["text"] = "id"
GLineEdit_356["textvariable"]=pid
GLineEdit_356.place(x=310,y=10,width=180,height=40)

GLineEdit_536=tk.Entry(frame5)
GLineEdit_536["bg"] = "#f9c5d5"
GLineEdit_536["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_536["font"] = ft
GLineEdit_536["fg"] = "#333333"
GLineEdit_536["justify"] = "center"
GLineEdit_536["text"] = "name"
GLineEdit_536["textvariable"]=pname
GLineEdit_536.place(x=310,y=60,width=180,height=40)

GButton_999=tk.Button(frame5)
GButton_999["bg"] = "#f2789f"
ft = tkFont.Font(family='Times',size=18)
GButton_999["font"] = ft
GButton_999["fg"] = "#393d49"
GButton_999["justify"] = "center"
GButton_999["text"] = "Enter"
GButton_999.place(x=210,y=455,width=130,height=35)
GButton_999["command"] = GButton_999_command

GLabel_899=tk.Label(frame5)
GLabel_899["bg"] = "#f999b7"
ft = tkFont.Font(family='Times',size=18)
GLabel_899["font"] = ft
GLabel_899["fg"] = "#333333"
GLabel_899["justify"] = "center"
GLabel_899["text"] = "Contact No."
GLabel_899.place(x=70,y=110,width=180,height=40)

GLineEdit_322=tk.Entry(frame5)
GLineEdit_322["bg"] = "#f9c5d5"
GLineEdit_322["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_322["font"] = ft
GLineEdit_322["fg"] = "#333333"
GLineEdit_322["justify"] = "center"
GLineEdit_322["text"] = "contact"
GLineEdit_322["textvariable"]=pcontact
GLineEdit_322.place(x=310,y=110,width=180,height=40)

GLineEdit_852=tk.Entry(frame5)
GLineEdit_852["bg"] = "#f9c5d5"
GLineEdit_852["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_852["font"] = ft
GLineEdit_852["fg"] = "#333333"
GLineEdit_852["justify"] = "center"
GLineEdit_852["text"] = "dob"
GLineEdit_852["textvariable"]=pdob
GLineEdit_852.place(x=310,y=160,width=180,height=40)

GLabel_972=tk.Label(frame5)
GLabel_972["bg"] = "#f999b7"
ft = tkFont.Font(family='Times',size=18)
GLabel_972["font"] = ft
GLabel_972["fg"] = "#333333"
GLabel_972["justify"] = "center"
GLabel_972["text"] = "Blood Group"
GLabel_972.place(x=70,y=210,width=180,height=40)

GLineEdit_929=tk.Entry(frame5)
GLineEdit_929["bg"] = "#f9c5d5"
GLineEdit_929["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_929["font"] = ft
GLineEdit_929["fg"] = "#333333"
GLineEdit_929["justify"] = "center"
GLineEdit_929["text"] = "bg"
GLineEdit_929["textvariable"]=pbg
GLineEdit_929.place(x=310,y=210,width=180,height=40)

GLabel_84=tk.Label(frame5)
GLabel_84["bg"] = "#f999b7"
ft = tkFont.Font(family='Times',size=18)
GLabel_84["font"] = ft
GLabel_84["fg"] = "#333333"
GLabel_84["justify"] = "center"
GLabel_84["text"] = "Ailment"
GLabel_84.place(x=70,y=260,width=180,height=40)

GLineEdit_544=tk.Entry(frame5)
GLineEdit_544["bg"] = "#f9c5d5"
GLineEdit_544["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_544["font"] = ft
GLineEdit_544["fg"] = "#333333"
GLineEdit_544["justify"] = "center"
GLineEdit_544["text"] = "ailment"
GLineEdit_544["textvariable"]=pailment
GLineEdit_544.place(x=310,y=260,width=180,height=40)

GLabel_245=tk.Label(frame5)
GLabel_245["bg"] = "#f999b7"
ft = tkFont.Font(family='Times',size=18)
GLabel_245["font"] = ft
GLabel_245["fg"] = "#333333"
GLabel_245["justify"] = "center"
GLabel_245["text"] = "Treatment Id"
GLabel_245.place(x=70,y=310,width=180,height=40)

GLabel_296=tk.Label(frame5)
GLabel_296["bg"] = "#f999b7"
ft = tkFont.Font(family='Times',size=18)
GLabel_296["font"] = ft
GLabel_296["fg"] = "#333333"
GLabel_296["justify"] = "center"
GLabel_296["text"] = "Dept. No."
GLabel_296.place(x=70,y=360,width=180,height=40)

GLabel_647=tk.Label(frame5)
GLabel_647["bg"] = "#f999b7"
ft = tkFont.Font(family='Times',size=18)
GLabel_647["font"] = ft
GLabel_647["fg"] = "#333333"
GLabel_647["justify"] = "center"
GLabel_647["text"] = "Doctor Id"
GLabel_647.place(x=70,y=410,width=180,height=40)

GLineEdit_812=tk.Entry(frame5)
GLineEdit_812["bg"] = "#f9c5d5"
GLineEdit_812["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_812["font"] = ft
GLineEdit_812["fg"] = "#333333"
GLineEdit_812["justify"] = "center"
GLineEdit_812["text"] = "treat"
GLineEdit_812["textvariable"]=ptreat
GLineEdit_812.place(x=310,y=310,width=180,height=40)

GLineEdit_954=tk.Entry(frame5)
GLineEdit_954["bg"] = "#f9c5d5"
GLineEdit_954["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_954["font"] = ft
GLineEdit_954["fg"] = "#333333"
GLineEdit_954["justify"] = "center"
GLineEdit_954["text"] = "deptno"
GLineEdit_954["textvariable"]=pdeptno
GLineEdit_954.place(x=310,y=360,width=180,height=40)

GLineEdit_14=tk.Entry(frame5)
GLineEdit_14["bg"] = "#f9c5d5"
GLineEdit_14["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_14["font"] = ft
GLineEdit_14["fg"] = "#333333"
GLineEdit_14["justify"] = "center"
GLineEdit_14["text"] = "did"
GLineEdit_14["textvariable"]=pdid
GLineEdit_14.place(x=310,y=410,width=180,height=40)

GLabel_601=tk.Label(frame5)
GLabel_601["bg"] = "#f999b7"
ft = tkFont.Font(family='Times',size=18)
GLabel_601["font"] = ft
GLabel_601["fg"] = "#393d49"
GLabel_601["justify"] = "center"
GLabel_601["text"] = "DOB"
GLabel_601.place(x=70,y=160,width=180,height=40)


#---------------------------

GLineEdit_970=tk.Entry(frame6)
GLineEdit_970["bg"] = "#FF7272"
GLineEdit_970["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_970["font"] = ft
GLineEdit_970["fg"] = "#333333"
GLineEdit_970["justify"] = "center"
GLineEdit_970["text"] = "bg"
GLineEdit_970["textvariable"] = grp  
GLineEdit_970.place(x=310,y=80,width=180,height=60)

GLineEdit_221=tk.Entry(frame6)
GLineEdit_221["bg"] = "#FF7272"
GLineEdit_221["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_221["font"] = ft
GLineEdit_221["fg"] = "#333333"
GLineEdit_221["justify"] = "center"
GLineEdit_221["text"] = "av"
GLineEdit_221["textvariable"] = ava
GLineEdit_221.place(x=310,y=240,width=180,height=60)

GButton_530=tk.Button(frame6)
GButton_530["bg"] = "#FF5959"
ft = tkFont.Font(family='Times',size=18)
GButton_530["font"] = ft
GButton_530["fg"] = "#393d49"
GButton_530["justify"] = "center"
GButton_530["text"] = "enter"
GButton_530.place(x=220,y=350,width=130,height=60)
GButton_530["command"] = enter

GLabel_353=tk.Label(frame6)
GLabel_353["bg"] = "#FF7272"
ft = tkFont.Font(family='Times',size=18)
GLabel_353["font"] = ft
GLabel_353["fg"] = "#393d49"
GLabel_353["justify"] = "center"
GLabel_353["text"] = "Blood Group"
GLabel_353.place(x=70,y=80,width=180,height=60)

GLabel_187=tk.Label(frame6)
GLabel_187["bg"] = "#FF7272"
ft = tkFont.Font(family='Times',size=18)
GLabel_187["font"] = ft
GLabel_187["fg"] = "#333333"
GLabel_187["justify"] = "center"
GLabel_187["text"] = "Availability"
GLabel_187.place(x=70,y=240,width=180,height=60)

#-----------------------------------------------------------

GLabel_594=tk.Label(frame7)
GLabel_594["bg"] = "#93ffd8"
GLabel_594["disabledforeground"] = "#672c2c"
ft = tkFont.Font(family='Times',size=18)
GLabel_594["font"] = ft
GLabel_594["fg"] = "#393d49"
GLabel_594["justify"] = "center"
GLabel_594["text"] = "Patient Id"
GLabel_594.place(x=60,y=70,width=180,height=75)

GLineEdit_965=tk.Entry(frame7)
GLineEdit_965["bg"] = "#cfffdc"
GLineEdit_965["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_965["font"] = ft
GLineEdit_965["fg"] = "#333333"
GLineEdit_965["justify"] = "center"
GLineEdit_965["text"] = "pid"
GLineEdit_965["textvariable"] = pid_
GLineEdit_965.place(x=320,y=70,width=180,height=75)

GButton_432=tk.Button(frame7)
GButton_432["bg"] = "#3fa796"
ft = tkFont.Font(family='Times',size=18)
GButton_432["font"] = ft
GButton_432["fg"] = "#393d49"
GButton_432["justify"] = "center"
GButton_432["text"] = "Search"
GButton_432.place(x=190,y=180,width=180,height=75)
GButton_432["command"] = GButton_432_command


#-------------------------------------------------------------


GLabel_595=tk.Label(frame8)
GLabel_595["bg"] = "#93ffd8"
GLabel_595["disabledforeground"] = "#672c2c"
ft = tkFont.Font(family='Times',size=18)
GLabel_595["font"] = ft
GLabel_595["fg"] = "#393d49"
GLabel_595["justify"] = "center"
GLabel_595["text"] = "Doctor Id"
GLabel_595.place(x=60,y=70,width=180,height=75)

GLineEdit_966=tk.Entry(frame8)
GLineEdit_966["bg"] = "#cfffdc"
GLineEdit_966["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_966["font"] = ft
GLineEdit_966["fg"] = "#333333"
GLineEdit_966["justify"] = "center"
GLineEdit_966["text"] = "Entry"
GLineEdit_966["textvariable"] = did_
GLineEdit_966.place(x=320,y=70,width=180,height=75)

GButton_433=tk.Button(frame8)
GButton_433["bg"] = "#3fa796"
ft = tkFont.Font(family='Times',size=18)
GButton_433["font"] = ft
GButton_433["fg"] = "#393d49"
GButton_433["justify"] = "center"
GButton_433["text"] = "Search"
GButton_433.place(x=190,y=180,width=180,height=75)
GButton_433["command"] = GButton_433_command



GLineEdit_970=tk.Entry(frame10)
GLineEdit_970["bg"] = "#baabda"
GLineEdit_970["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
GLineEdit_970["font"] = ft
GLineEdit_970["fg"] = "#333333"
GLineEdit_970["justify"] = "center"
GLineEdit_970["text"] = "bg"
GLineEdit_970["textvariable"] = bg
GLineEdit_970.place(x=310,y=140,width=180,height=60)

GButton_530=tk.Button(frame10)
GButton_530["bg"] = "#9145b6"
ft = tkFont.Font(family='Times',size=18)
GButton_530["font"] = ft
GButton_530["fg"] = "#393d49"
GButton_530["justify"] = "center"
GButton_530["text"] = "check"
GButton_530.place(x=220,y=250,width=130,height=60)
GButton_530["command"] = GButton_530_command

GLabel_353=tk.Label(frame10)
GLabel_353["bg"] = "#8267be"
ft = tkFont.Font(family='Times',size=18)
GLabel_353["font"] = ft
GLabel_353["fg"] = "#393d49"
GLabel_353["justify"] = "center"
GLabel_353["text"] = "Blood Group"
GLabel_353.place(x=70,y=140,width=180,height=60)







frame1.pack()

root.mainloop()












# #random
