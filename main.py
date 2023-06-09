import tkinter.messagebox
from tkinter.ttk import Entry
from typing import Union

from test import PDF
import psycopg2
import text
import os
# import tkinter as tk
# from tkinter import ttk
#
con = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='AlwaysInShape')
cur = con.cursor()
sentence = "SELECT username FROM PUBLIC.\"Admin\" WHERE username = 'Jose'"
cur.execute(sentence)
reg = cur.fetchall()
#print(reg)


# window = tk.Tk()
# window.geometry("205x80")
# window.title("Home")
# c = (205/2)-35
#
# def clickLogin():
#     window = tk.Tk()
#     window.geometry("205x80")
#     window.title("Home")
#     lab1 = ttk.Label(window, text="Name:").pack()
#
# login = ttk.Button(text="LOGIN", command=clickLogin())
# login.grid(row=0, column=0, sticky=tk.E)
# newUser = ttk.Button(text="NEW USER")
# newUser.grid(row=1, column=0, sticky=tk.E)
# login.place(x=c, y=10)
# newUser.place(x=c, y=40)
#
# window.mainloop()

from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk, Entry

main = Tk()
main.geometry("205x80")
main.title("HOME")
c = (205/2)-35

x = ''

def close():
    main.destroy()
def close2():
    main2.destroy()
def close3():
    main3.destroy()
def close4():
    main4.destroy()
def close5():
    main5.destroy()
def close6():
    main6.destroy()
def close7():
    main7.destroy()
def close8():
    main8.destroy()
def close9():
    main9.destroy()
def close10():
    main10.destroy()
def close11():
    main11.destroy()
def close12():
    main12.destroy()
def close13():
    main13.destroy()
def close14():
    main14.destroy()
def close15():
    main15.destroy()
def close16():
    main16.destroy()
def close17():
    main17.destroy()

def openLogin():
    close()
    #newWindow = Toplevel(main)
    global main2
    main2 = Tk()

    main2.title("LOGIN")

    main2.geometry("200x130")

    Label(main2, text="USERNAME:").pack()
    global entry1
    entry1 = Entry(main2, width=20)
    entry1.pack()
    Label(main2, text="PASSWORD:").pack()
    global entry2
    entry2 = Entry(main2, show='*', width=20)
    entry2.pack()
    Button(main2, text="ENTER", command=clickEnter).pack()
    #Button(main2, text="Return", command=).pack()


def clickEnter():
    entryUser = entry1.get()
    entryPass = entry2.get()
    senUser = "SELECT username FROM PUBLIC.\"Admin\" WHERE username = \'" + entryUser + "'"
    senPass = "SELECT password FROM PUBLIC.\"Admin\" WHERE password = \'" + entryPass + "'"
    cur.execute(senUser)
    r1 = str(cur.fetchall())
    cur.execute(senPass)
    r2 = str(cur.fetchall())

    if entryUser in r1 and entryPass in r2 and entryUser != '' and entryPass != '':
        openMenu()
        close2()
    else:
        tkinter.messagebox.showerror(title=None, message="ERROR INCORRECT USERNAME OR PASSWORD")

def openMenu():
    global main3
    main3 = Tk()
    main3.title("MENU")
    main3.geometry("200x300")

    Button(main3, text="Rooms", command=clickRooms).pack()
    Button(main3, text="Devices", command=clickDevices).pack()
    Button(main3, text="Assigned", command=clickAssigned).pack()
    Button(main3, text="Classes", command=clickClasses).pack()
    Button(main3, text="Impart", command=clickImpart).pack()
    Button(main3, text="Instructors", command=clickInstructors).pack()
    Button(main3, text="Attend", command=clickAttend).pack()
    Button(main3, text="Members", command=clickMembers).pack()
    Button(main3, text="Reservation", command=clickReservation).pack()
    Button(main3, text="Squash Courts", command=clickSquashCourts).pack()
    Button(main3, text='View Reports', command=clickReports).pack()

    try:
        close4()
    except:
        print("")

    try:
        close5()
    except:
        print("")

    try:
        close6()
    except:
        print("")
    try:
        close7()
    except:
        print("")

    try:
        close8()
    except:
        print("")
    try:
        close9()
    except:
        print("")
    try:
        close10()
    except:
        print("")
    try:
        close11()
    except:
        print("")
    try:
        close12()
    except:
        print("")
    try:
        close13()
    except:
        print("")
    try:
        close14()
    except:
        print("")
    try:
        close17()
    except:
        print("")

def clickRooms():
    global main4
    main4 = Tk()
    main4.title("ROOMS")
    main4.geometry("850x300")
    global text1
    text1 = tk.StringVar()
    text1.set("")
    global text2
    text2 = tk.StringVar()
    text2.set("")

    Label(main4, text='SELECT').place(x=5, y=1)
    Button(main4, text='Select All', command=roomSelectAll).place(x=5, y=25)
    Button(main4, text='Select by ID', command=roomSelectID).place(x=5, y=50)
    global roomSelectIdEntry
    roomSelectIdEntry = Entry(main4, width=3)
    roomSelectIdEntry.place(x=85, y=50)
    #Label(main4, textvariable=text1).place(x=5, y=75)
    Button(main4, text='Select by type', command=roomSelectType).place(x=5, y=75)
    global roomSelectTypeEntry
    roomSelectTypeEntry = Entry(main4, width=9)
    roomSelectTypeEntry.place(x=90, y=75)

    Label(main4, text='INSERT').place(x=200, y=1)
    Button(main4, text='Insert new', command=roomInsert).place(x=200, y=25)
    Label(main4, text='ID:').place(x=200, y=50)
    global roomInsertID
    roomInsertID = Entry(main4, width=3)
    roomInsertID.place(x=220, y=50)
    Label(main4, text='Space:').place(x=200, y=75)
    global roomInsertSpace
    roomInsertSpace = Entry(main4, width=8)
    roomInsertSpace.place(x=240, y=75)
    Label(main4, text='Location:').place(x=200, y=100)
    global roomInsertLocation
    roomInsertLocation = Entry(main4, width=25)
    roomInsertLocation.place(x=255, y=100)
    Label(main4, text='Type:').place(x=200, y=125)
    global roomInsertType
    roomInsertType = Entry(main4, width=9)
    roomInsertType.place(x=235, y=125)

    Label(main4, text='UPDATE').place(x=440, y=1)
    Button(main4, text='Update by ID', command=roomUpdateID).place(x=440, y=25)
    Label(main4, text='ID:').place(x=520, y=25)
    global entryUpdateID
    entryUpdateID = Entry(main4, width=3)
    entryUpdateID.place(x=540, y=25)
    Label(main4, text='New ID:').place(x=440, y=50)
    global entryUpdateIDID
    entryUpdateIDID = Entry(main4, width=3)
    entryUpdateIDID.place(x=490, y=50)
    Label(main4, text='New Space:').place(x=440, y=75)
    global entryUpdateIDSpace
    entryUpdateIDSpace = Entry(main4, width=5)
    entryUpdateIDSpace.place(x=510, y=75)
    Label(main4, text='New Location:').place(x=440, y=100)
    global entryUpdateIDLocation
    entryUpdateIDLocation = Entry(main4, width=10)
    entryUpdateIDLocation.place(x=525, y=100)
    Label(main4, text='New type:').place(x=440, y=125)
    global entryUpdateIDType
    entryUpdateIDType = Entry(main4, width=9)
    entryUpdateIDType.place(x=505, y=125)

    Button(main4, text='Update by type', command=roomUpdateType).place(x=440, y=150)
    Label(main4, text='Type:').place(x=530, y=150)
    global entryUpdateType
    entryUpdateType = Entry(main4, width=9)
    entryUpdateType.place(x=565, y=150)
    Label(main4, text='New ID:').place(x=440, y=175)
    global entryUpdateTypeID
    entryUpdateTypeID = Entry(main4, width=3)
    entryUpdateTypeID.place(x=490, y=175)
    Label(main4, text='New Space:').place(x=440, y=200)
    global entryUpdateTypeSpace
    entryUpdateTypeSpace = Entry(main4, width=5)
    entryUpdateTypeSpace.place(x=510, y=200)
    Label(main4, text='New Location:').place(x=440, y=225)
    global entryUpdateTypeLocation
    entryUpdateTypeLocation = Entry(main4, width=10)
    entryUpdateTypeLocation.place(x=525, y=225)
    Label(main4, text='New type:').place(x=440, y=250)
    global entryUpdateTypeType
    entryUpdateTypeType = Entry(main4, width=9)
    entryUpdateTypeType.place(x=505, y=250)

    Label(main4, text='DELETE').place(x=680, y=1)
    Button(main4, text='Delete by ID', command=roomDeleteID).place(x=680, y=25)
    global roomDeleteIdEntry
    roomDeleteIdEntry = Entry(main4, width=3)
    roomDeleteIdEntry.place(x=760, y=25)
    Button(main4, text='Delete by type', command=roomDeleteType).place(x=680, y=50)
    global roomDeleteTypeEntry
    roomDeleteTypeEntry = Entry(main4, width=9)
    roomDeleteTypeEntry.place(x=770, y=50)
    Button(main4, text='Delete All', command=roomDeleteAll).place(x=680, y=75)
    global roomConfirmation
    roomConfirmation = Entry(main4, width=4)
    roomConfirmation.place(x=760, y=75)

    Button(main4, text='RETURN', command=openMenu).place(x=770, y=265)

    close3()

def roomSelectAll():
    sent = 'SELECT * FROM public."Rooms" ORDER BY "roomID" ASC'
    cur.execute(sent)
    res = str(cur.fetchall())
    list = []
    var = ""

    for e in res:
        if e != ")":
            var += e
        else:
            newvar = var.replace('[', '').replace('(', '')
            list.append(newvar)
            var = ""

    string = ''
    for e in list:
        string += (e + "\n")

    tkinter.messagebox.showinfo(message=string)

def roomSelectID():
    getEntry =  roomSelectIdEntry.get()
    sen = "SELECT * FROM Public.\"Rooms\" WHERE \"roomID\" = " + str(getEntry) + ""
    try:
        cur.execute(sen)
        string = str(cur.fetchall())
        newstring = string.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
        text1.set(newstring)
        tkinter.messagebox.showinfo(message=newstring)
    except Exception:
        con.rollback()


def roomSelectType():
    getEntry =  roomSelectTypeEntry.get()
    sen = "SELECT * FROM Public.\"Rooms\" WHERE \"type\" = '" + str(getEntry) + "'"
    try:
        cur.execute(sen)
        string = str(cur.fetchall())
        var = ''
        list = []

        for e in string:
            if e != ")":
                var += e
            else:
                newvar = var.replace('[', '').replace('(', '')
                list.append(newvar)
                var = ""

        newstring = ''
        for e in list:
            newstring += (e + "\n")
        text2.set(newstring)
        tkinter.messagebox.showinfo(message=newstring)
    except Exception:
        con.rollback()


def roomInsert():
    getEntry1 = roomInsertID.get()
    getEntry2 = roomInsertSpace.get()
    getEntry3 = roomInsertLocation.get()
    getEntry4 = roomInsertType.get()
    sen = f"INSERT INTO public.\"Rooms\" (\"roomID\", \"space\", \"location\", \"type\") VALUES ({int(getEntry1)}, {int(getEntry2)}, '{str(getEntry3)}', '{str(getEntry4)}')"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def roomUpdateID():
    getEntry = entryUpdateID.get()
    getEntry1 = entryUpdateIDID.get()
    getEntry2 = entryUpdateIDSpace.get()
    getEntry3 = entryUpdateIDLocation.get()
    getEntry4 = entryUpdateIDType.get()
    sen = f"UPDATE public.\"Rooms\" SET"

    if getEntry1 != "":
        sen += f" \"roomID\" = {str(getEntry1)},"
    if getEntry2 != "":
        sen += f" \"space\" = {str(getEntry2)},"
    if getEntry3 != "":
        sen += f" \"location\" = '{str(getEntry3)}',"
    if getEntry4 != "":
        sen += f" \"type\" = '{str(getEntry4)}',"
    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"roomID\" = {str(getEntry)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def roomUpdateType():
    getEntry = entryUpdateType.get()
    getEntry1 = entryUpdateTypeID.get()
    getEntry2 = entryUpdateTypeSpace.get()
    getEntry3 = entryUpdateTypeLocation.get()
    getEntry4 = entryUpdateTypeType.get()
    sen = f"UPDATE public.\"Rooms\" SET"

    if getEntry1 != "":
        sen += f" \"roomID\" = {str(getEntry1)},"
    if getEntry2 != "":
        sen += f" \"space\" = {str(getEntry2)},"
    if getEntry3 != "":
        sen += f" \"location\" = '{str(getEntry3)}',"
    if getEntry4 != "":
        sen += f" \"type\" = '{str(getEntry4)}',"
    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"type\" = '{str(getEntry)}'"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def roomDeleteID():
    getEntry = roomDeleteIdEntry.get()
    sen = f"DELETE FROM public.\"Rooms\" WHERE \"roomID\" = {str(getEntry)}"
    print(sen)
    try:
        cur.execute(sen)
        string = str(cur.fetchall())
    except Exception:
        con.rollback()

def roomDeleteType():
    getEntry = roomDeleteTypeEntry.get()
    sen = f"DELETE FROM public.\"Rooms\" WHERE \"type\" = '{str(getEntry)}'"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def roomDeleteAll():
    entry = roomConfirmation.get()
    if str(entry) == 'YES' or str(entry) == 'yes':
        sen = "DELETE FROM public.\"Rooms\""
        print(sen)
        try:
            cur.execute(sen)
            con.commit()
        except Exception:
            con.rollback()

##########################
###DEVICES
##########################

def clickDevices():
    global main5
    main5 = Tk()
    main5.title("DEVICES")
    main5.geometry("870x400")

    Label(main5, text='SELECT').place(x=5, y=1)
    Button(main5, text='Select All', command=deviceSelectAll).place(x=5, y=25)
    Button(main5, text='Select by code', command=deviceSelectCode).place(x=5, y=50)
    global deviceSelectCodeEntry
    deviceSelectCodeEntry = Entry(main5, width=3)
    deviceSelectCodeEntry.place(x=95, y=50)
    # Label(main4, textvariable=text1).place(x=5, y=75)
    Button(main5, text='Select by room ID', command=deviceSelectRoomID).place(x=5, y=75)
    global deviceSelectRoomIDEntry
    deviceSelectRoomIDEntry = Entry(main5, width=9)
    deviceSelectRoomIDEntry.place(x=110, y=75)
    Button(main5, text='Select by Description', command=deviceSelectDescription).place(x=5, y=100)
    global deviceSelectDescriptionEntry
    deviceSelectDescriptionEntry = Entry(main5, width=9)
    deviceSelectDescriptionEntry.place(x=130, y=100)


    Label(main5, text='INSERT').place(x=200, y=1)
    Button(main5, text='Insert new', command=deviceInsert).place(x=200, y=25)
    Label(main5, text='Code:').place(x=200, y=50)
    global deviceInsertCode
    deviceInsertCode = Entry(main5, width=3)
    deviceInsertCode.place(x=235, y=50)
    Label(main5, text='Description:').place(x=200, y=75)
    global deviceInsertDescription
    deviceInsertDescription = Entry(main5, width=8)
    deviceInsertDescription.place(x=265, y=75)
    Label(main5, text='Status:').place(x=200, y=100)
    global deviceInsertStatus
    deviceInsertStatus = Entry(main5, width=25)
    deviceInsertStatus.place(x=240, y=100)
    Label(main5, text='Room ID:').place(x=200, y=125)
    global deviceInsertRoomID
    deviceInsertRoomID = Entry(main5, width=9)
    deviceInsertRoomID.place(x=250, y=125)


    Label(main5, text='UPDATE').place(x=440, y=1)
    Button(main5, text='Update by Code', command=deviceUpdateCode).place(x=440, y=25)
    Label(main5, text='Code:').place(x=535, y=25)
    global entryUpdateCode
    entryUpdateCode = Entry(main5, width=3)
    entryUpdateCode.place(x=570, y=25)
    Label(main5, text='New Code:').place(x=440, y=50)
    global entryUpdateCodeCode
    entryUpdateCodeCode = Entry(main5, width=3)
    entryUpdateCodeCode.place(x=505, y=50)
    Label(main5, text='New Description:').place(x=440, y=75)
    global entryUpdateCodeDescription
    entryUpdateCodeDescription = Entry(main5, width=5)
    entryUpdateCodeDescription.place(x=535, y=75)
    Label(main5, text='New status:').place(x=440, y=100)
    global entryUpdateCodeStatus
    entryUpdateCodeStatus = Entry(main5, width=10)
    entryUpdateCodeStatus.place(x=505, y=100)
    Label(main5, text='New Room ID:').place(x=440, y=125)
    global entryUpdateCodeRoomID
    entryUpdateCodeRoomID = Entry(main5, width=9)
    entryUpdateCodeRoomID.place(x=520, y=125)

    Button(main5, text='Update by room ID', command=deviceUpdateRoomID).place(x=440, y=150)
    Label(main5, text='Room ID:').place(x=550, y=150)
    global entryUpdateRoomID
    entryUpdateRoomID = Entry(main5, width=9)
    entryUpdateRoomID.place(x=605, y=150)
    Label(main5, text='New Code:').place(x=440, y=175)
    global entryUpdateRoomIDCode
    entryUpdateRoomIDCode = Entry(main5, width=3)
    entryUpdateRoomIDCode.place(x=505, y=175)
    Label(main5, text='New Description:').place(x=440, y=200)
    global entryUpdateRoomIDDescription
    entryUpdateRoomIDDescription = Entry(main5, width=5)
    entryUpdateRoomIDDescription.place(x=535, y=200)
    Label(main5, text='New Status:').place(x=440, y=225)
    global entryUpdateRoomIDStatus
    entryUpdateRoomIDStatus = Entry(main5, width=10)
    entryUpdateRoomIDStatus.place(x=505, y=225)
    Label(main5, text='New Room ID:').place(x=440, y=250)
    global entryUpdateRoomIDRoomID
    entryUpdateRoomIDRoomID = Entry(main5, width=9)
    entryUpdateRoomIDRoomID.place(x=520, y=250)

    Button(main5, text='Update by Description', command=deviceUpdateDescription).place(x=440, y=275)
    Label(main5, text='Description:').place(x=570, y=275)
    global entryUpdateDescription
    entryUpdateDescription = Entry(main5, width=9)
    entryUpdateDescription.place(x=640, y=275)
    Label(main5, text='New Code:').place(x=440, y=300)
    global entryUpdateDescriptionCode
    entryUpdateRoomDescriptionCode = Entry(main5, width=3)
    entryUpdateRoomDescriptionCode.place(x=505, y=300)
    Label(main5, text='New Description:').place(x=440, y=325)
    global entryUpdateDescriptionDescription
    entryUpdateDescriptionDescription = Entry(main5, width=5)
    entryUpdateDescriptionDescription.place(x=535, y=325)
    Label(main5, text='New Status:').place(x=440, y=350)
    global entryUpdateDescriptionStatus
    entryUpdateDescriptionStatus = Entry(main5, width=10)
    entryUpdateDescriptionStatus.place(x=505, y=350)
    Label(main5, text='New Room ID:').place(x=440, y=375)
    global entryUpdateDescriptionRoomID
    entryUpdateDescriptionRoomID = Entry(main5, width=9)
    entryUpdateDescriptionRoomID.place(x=520, y=375)


    Label(main5, text='DELETE').place(x=680, y=1)
    Button(main5, text='Delete by Code', command=deviceDeleteCode).place(x=680, y=25)
    global deviceDeleteCodeEntry
    deviceDeleteCodeEntry = Entry(main5, width=3)
    deviceDeleteCodeEntry.place(x=770, y=25)
    Button(main5, text='Delete by Room ID', command=deviceDeleteRoomID).place(x=680, y=50)
    global deviceDeleteRoomIDEntry
    deviceDeleteRoomIDEntry = Entry(main5, width=9)
    deviceDeleteRoomIDEntry.place(x=790, y=50)
    Button(main5, text='Delete by Description', command=deviceDeleteDescription).place(x=680, y=75)
    global deviceDeleteDescriptionEntry
    deviceDeleteDescriptionEntry = Entry(main5, width=9)
    deviceDeleteDescriptionEntry.place(x=805, y=75)
    Button(main5, text='Delete All', command=deviceDeleteAll).place(x=680, y=100)
    global deviceConfirmation
    deviceConfirmation = Entry(main5, width=4)
    deviceConfirmation.place(x=760, y=100)

    Button(main5, text='RETURN', command=openMenu).place(x=770, y=365)

    close3()

def deviceSelectAll():
    sent = 'SELECT * FROM public."Devices" ORDER BY "code" ASC'
    cur.execute(sent)
    res = str(cur.fetchall())
    list = []
    var = ""

    for e in res:
        if e != ")":
            var += e
        else:
            newvar = var.replace('[', '').replace('(', '')
            list.append(newvar)
            var = ""

    string = ''
    for e in list:
        string += (e + "\n")

    tkinter.messagebox.showinfo(message=string)

def deviceSelectCode():
    getEntry =  deviceSelectCodeEntry.get()
    sen = "SELECT * FROM Public.\"Devices\" WHERE \"code\" = " + str(getEntry) + ""
    try:
        cur.execute(sen)
        string = str(cur.fetchall())
        newstring = string.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
        tkinter.messagebox.showinfo(message=newstring)
    except Exception:
        con.rollback()

def deviceSelectRoomID():
    getEntry =  deviceSelectRoomIDEntry.get()
    sen = "SELECT * FROM Public.\"Devices\" WHERE \"roomID\" = " + str(getEntry) + ""
    try:
        cur.execute(sen)
        string = str(cur.fetchall())
        newstring = string.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
        tkinter.messagebox.showinfo(message=newstring)
    except Exception:
        con.rollback()

def deviceSelectDescription():
    getEntry =  deviceSelectDescriptionEntry.get()
    sen = "SELECT * FROM Public.\"Devices\" WHERE \"description\" = '" + str(getEntry) + "'"
    try:
        cur.execute(sen)
        string = str(cur.fetchall())
        var = ''
        list = []

        for e in string:
            if e != ")":
                var += e
            else:
                newvar = var.replace('[', '').replace('(', '')
                list.append(newvar)
                var = ""

        newstring = ''
        for e in list:
            newstring += (e + "\n")
        tkinter.messagebox.showinfo(message=newstring)
    except Exception:
        con.rollback()



def deviceInsert():
    getEntry1 = deviceInsertCode.get()
    getEntry2 = deviceInsertDescription.get()
    getEntry3 = deviceInsertStatus.get()
    getEntry4 = deviceInsertRoomID.get()
    sen = f"INSERT INTO public.\"Devices\" (\"code\", \"description\", \"status\", \"roomID\") VALUES ({str(getEntry1)}, '{str(getEntry2)}', '{str(getEntry3)}', {str(getEntry4)})"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def deviceUpdateCode():
    getEntry = entryUpdateCode.get()
    getEntry1 = entryUpdateCodeCode.get()
    getEntry2 = entryUpdateCodeDescription.get()
    getEntry3 = entryUpdateCodeStatus.get()
    getEntry4 = entryUpdateCodeRoomID.get()
    sen = f"UPDATE public.\"Devices\" SET"

    if getEntry1 != "":
        sen += f" \"code\" = {str(getEntry1)},"
    if getEntry2 != "":
        sen += f" \"description\" = '{str(getEntry2)}',"
    if getEntry3 != "":
        sen += f" \"status\" = '{str(getEntry3)}',"
    if getEntry4 != "":
        sen += f" \"roomID\" = {str(getEntry4)},"
    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"code\" = {str(getEntry)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def deviceUpdateRoomID():
    getEntry = entryUpdateRoomID.get()
    getEntry1 = entryUpdateRoomIDCode.get()
    getEntry2 = entryUpdateRoomIDDescription.get()
    getEntry3 = entryUpdateRoomIDStatus.get()
    getEntry4 = entryUpdateRoomIDRoomID.get()
    sen = f"UPDATE public.\"Devices\" SET"

    if getEntry1 != "":
        sen += f" \"code\" = {str(getEntry1)},"
    if getEntry2 != "":
        sen += f" \"description\" = '{str(getEntry2)}',"
    if getEntry3 != "":
        sen += f" \"status\" = '{str(getEntry3)}',"
    if getEntry4 != "":
        sen += f" \"roomID\" = {str(getEntry4)},"
    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"roomID\" = {str(getEntry)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def deviceUpdateDescription():
    getEntry = entryUpdateDescription.get()
    getEntry1 = entryUpdateDescriptionCode.get()
    getEntry2 = entryUpdateDescriptionDescription.get()
    getEntry3 = entryUpdateDescriptionStatus.get()
    getEntry4 = entryUpdateDescriptionRoomID.get()
    sen = f"UPDATE public.\"Devices\" SET"

    if getEntry1 != "":
        sen += f" \"code\" = {str(getEntry1)},"
    if getEntry2 != "":
        sen += f" \"description\" = '{str(getEntry2)}',"
    if getEntry3 != "":
        sen += f" \"status\" = '{str(getEntry3)}',"
    if getEntry4 != "":
        sen += f" \"roomID\" = {str(getEntry4)},"
    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"description\" = '{str(getEntry)}'"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def deviceDeleteCode():
    getEntry = deviceDeleteCodeEntry.get()
    sen = f"DELETE FROM public.\"Devices\" WHERE \"code\" = {str(getEntry)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def deviceDeleteRoomID():
    getEntry = deviceDeleteRoomIDEntry.get()
    sen = f"DELETE FROM public.\"Devices\" WHERE \"roomID\" = {str(getEntry)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def deviceDeleteDescription():
    getEntry = deviceDeleteDescriptionEntry.get()
    sen = f"DELETE FROM public.\"Devices\" WHERE \"status\" = '{str(getEntry)}'"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def deviceDeleteAll():
    entry = deviceConfirmation.get()
    if str(entry) == 'YES' or str(entry) == 'yes':
        sen = "DELETE FROM public.\"Devices\""
        print(sen)
        try:
            cur.execute(sen)
            con.commit()
        except Exception:
            con.rollback()



#################################################################

#CLASSES

##################################################################

def clickClasses():
    global main6
    main6 = Tk()
    main6.title("CLASSES")
    main6.geometry("870x300")

    Label(main6, text='SELECT').place(x=5, y=1)
    Button(main6, text='Select All', command=classSelectAll).place(x=5, y=25)
    Button(main6, text='Select by Code', command=classSelectCode).place(x=5, y=50)
    global classSelectCodeEntry
    classSelectCodeEntry = Entry(main6, width=3)
    classSelectCodeEntry.place(x=95, y=50)
    # Label(main4, textvariable=text1).place(x=5, y=75)
    Button(main6, text='Select by Description', command=classSelectDescription).place(x=5, y=75)
    global classSelectDescriptionEntry
    classSelectDescriptionEntry= Entry(main6, width=9)
    classSelectDescriptionEntry.place(x=130, y=75)


    Label(main6, text='INSERT').place(x=200, y=1)
    Button(main6, text='Insert new', command=classInsert).place(x=200, y=25)
    Label(main6, text='Code:').place(x=200, y=50)
    global classInsertCode
    classInsertCode = Entry(main6, width=3)
    classInsertCode.place(x=235, y=50)
    Label(main6, text='Description:').place(x=200, y=75)
    global classInsertDescription
    classInsertDescription = Entry(main6, width=8)
    classInsertDescription.place(x=270, y=75)
    Label(main6, text='Date:').place(x=200, y=100)
    global classInsertDate
    classInsertDate = Entry(main6, width=25)
    classInsertDate.place(x=235, y=100)
    Label(main6, text='Time:').place(x=200, y=125)
    global classInsertTime
    classInsertTime = Entry(main6, width=9)
    classInsertTime.place(x=240, y=125)


    Label(main6, text='UPDATE').place(x=440, y=1)
    Button(main6, text='Update by Code', command=classUpdateCode).place(x=440, y=25)
    Label(main6, text='Code:').place(x=535, y=25)
    global entryUpdateClassCode
    entryUpdateClassCode = Entry(main6, width=3)
    entryUpdateClassCode.place(x=570, y=25)
    Label(main6, text='New Code:').place(x=440, y=50)
    global entryUpdateClassCodeCode
    entryUpdateClassCodeCode = Entry(main6, width=3)
    entryUpdateClassCodeCode.place(x=505, y=50)
    Label(main6, text='New Description:').place(x=440, y=75)
    global entryUpdateClassCodeDescription
    entryUpdateClassCodeDescription = Entry(main6, width=5)
    entryUpdateClassCodeDescription.place(x=535, y=75)
    Label(main6, text='New Date:').place(x=440, y=100)
    global entryUpdateCodeDate
    entryUpdateCodeDate = Entry(main6, width=10)
    entryUpdateCodeDate.place(x=500, y=100)
    Label(main6, text='New Time:').place(x=440, y=125)
    global entryUpdateCodeTime
    entryUpdateCodeTime = Entry(main6, width=9)
    entryUpdateCodeTime.place(x=505, y=125)


    Button(main6, text='Update by Description', command=classUpdateDescription).place(x=440, y=150)
    Label(main6, text='Description:').place(x=570, y=150)
    global entryUpdateDescriptionC
    entryUpdateDescriptionC = Entry(main6, width=9)
    entryUpdateDescriptionC.place(x=640, y=150)
    Label(main6, text='New Code:').place(x=440, y=175)
    global entryUpdateDescriptionClassCode
    entryUpdateRoomDescriptionClassCode = Entry(main6, width=3)
    entryUpdateRoomDescriptionClassCode.place(x=505, y=175)
    Label(main6, text='New Description:').place(x=440, y=200)
    global entryUpdateDescriptionCDescription
    entryUpdateDescriptionCDescription = Entry(main6, width=5)
    entryUpdateDescriptionCDescription.place(x=535, y=200)
    Label(main6, text='Date:').place(x=440, y=225)
    global entryUpdateDescriptionDate
    entryUpdateDescriptionDate = Entry(main6, width=10)
    entryUpdateDescriptionDate.place(x=475, y=225)
    Label(main6, text='Time:').place(x=440, y=250)
    global entryUpdateDescriptionTime
    entryUpdateDescriptionTime = Entry(main6, width=9)
    entryUpdateDescriptionTime.place(x=480, y=250)


    Label(main6, text='DELETE').place(x=680, y=1)
    Button(main6, text='Delete by Code', command=classDeleteCode).place(x=680, y=25)
    global classDeleteCodeEntry
    classDeleteCodeEntry = Entry(main6, width=3)
    classDeleteCodeEntry.place(x=770, y=25)
    Button(main6, text='Delete by Description', command=classDeleteDescription).place(x=680, y=50)
    global classDeleteDescriptionEntry
    classDeleteDescriptionEntry = Entry(main6, width=9)
    classDeleteDescriptionEntry.place(x=805, y=50)
    Button(main6, text='Delete All', command=classDeleteAll).place(x=680, y=75)
    global classConfirmation
    classConfirmation = Entry(main6, width=4)
    classConfirmation.place(x=760, y=75)

    Button(main6, text='RETURN', command=openMenu).place(x=770, y=250)

    close3()

def classSelectAll():
    sent = 'SELECT * FROM public."Classes" ORDER BY "classCode" ASC'
    cur.execute(sent)
    res = str(cur.fetchall())
    list = []
    var = ""

    for e in res:
        if e != ")":
            var += e
        else:
            newvar = var.replace('[', '').replace('(', '')
            list.append(newvar)
            var = ""

    string = ''
    for e in list:
        string += (e + "\n")

    tkinter.messagebox.showinfo(message=string)

def classSelectCode():
    getEntry =  classSelectCodeEntry.get()
    sen = "SELECT * FROM Public.\"Classes\" WHERE \"classCode\" = " + str(getEntry) + ""
    try:
        cur.execute(sen)
        string = str(cur.fetchall())
        newstring = string.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
        tkinter.messagebox.showinfo(message=newstring)
    except Exception:
        con.rollback()

def classSelectDescription():
    getEntry =  classSelectDescriptionEntry.get()
    sen = "SELECT * FROM Public.\"Classes\" WHERE \"description\" = '" + str(getEntry) + "'"
    try:
        cur.execute(sen)
        string = str(cur.fetchall())
        var = ''
        list = []

        for e in string:
            if e != ")":
                var += e
            else:
                newvar = var.replace('[', '').replace('(', '')
                list.append(newvar)
                var = ""

        newstring = ''
        for e in list:
            newstring += (e + "\n")
        tkinter.messagebox.showinfo(message=newstring)
    except Exception:
        con.rollback()

def classInsert():
    getEntry1 = classInsertCode.get()
    getEntry2 = classInsertDescription.get()
    getEntry3 = classInsertDate.get()
    getEntry4 = classInsertTime.get()
    sen = f"INSERT INTO public.\"Classes\" (\"classCode\", \"description\", \"date\", \"time\") VALUES ({str(getEntry1)}, '{str(getEntry2)}', '{str(getEntry3)}', '{str(getEntry4)}')"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def classUpdateCode():
    getEntry = entryUpdateClassCode.get()
    getEntry1 = entryUpdateClassCodeCode.get()
    getEntry2 = entryUpdateClassCodeDescription.get()
    getEntry3 = entryUpdateCodeDate.get()
    getEntry4 = entryUpdateCodeTime.get()
    sen = f"UPDATE public.\"Classes\" SET"

    if getEntry1 != "":
        sen += f" \"classCode\" = {str(getEntry1)},"
    if getEntry2 != "":
        sen += f" \"description\" = '{str(getEntry2)}',"
    if getEntry3 != "":
        sen += f" \"date\" = '{str(getEntry3)}',"
    if getEntry4 != "":
        sen += f" \"time\" = {str(getEntry4)},"
    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"classCode\" = {str(getEntry)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def classUpdateDescription():
    getEntry = entryUpdateDescriptionC.get()
    getEntry1 = entryUpdateDescriptionClassCode.get()
    getEntry2 = entryUpdateDescriptionCDescription.get()
    getEntry3 = entryUpdateDescriptionDate.get()
    getEntry4 = entryUpdateDescriptionTime.get()
    sen = f"UPDATE public.\"Devices\" SET"

    if getEntry1 != "":
        sen += f" \"classCode\" = {str(getEntry1)},"
    if getEntry2 != "":
        sen += f" \"description\" = '{str(getEntry2)}',"
    if getEntry3 != "":
        sen += f" \"date\" = '{str(getEntry3)}',"
    if getEntry4 != "":
        sen += f" \"time\" = {str(getEntry4)},"
    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"description\" = '{str(getEntry)}'"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def classDeleteCode():
    getEntry = classDeleteCodeEntry.get()
    sen = f"DELETE FROM public.\"Classes\" WHERE \"classCode\" = {str(getEntry)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def classDeleteDescription():
    getEntry = classDeleteDescriptionEntry.get()
    sen = f"DELETE FROM public.\"Classes\" WHERE \"description\" = '{str(getEntry)}'"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def classDeleteAll():
    entry = classConfirmation.get()
    if str(entry) == 'YES' or str(entry) == 'yes':
        sen = "DELETE FROM public.\"Classes\""
        print(sen)
        try:
            cur.execute(sen)
            con.commit()
        except Exception:
            con.rollback()


#################################################################

#INSTRUCTORS

##################################################################

def clickInstructors():
    global main7
    main7 = Tk()
    main7.title("INSTRUCTORS")
    main7.geometry("870x500")

    Label(main7, text='SELECT').place(x=5, y=1)
    Button(main7, text='Select All', command=instructorSelectAll).place(x=5, y=25)
    Button(main7, text='Select by SNO', command=instructorSelectSNO).place(x=5, y=50)
    global instructorSelectSNOEntry
    instructorSelectSNOEntry = Entry(main7, width=3)
    instructorSelectSNOEntry.place(x=95, y=50)
    # Label(main4, textvariable=text1).place(x=5, y=75)
    Button(main7, text='Select by Name', command=instructorSelectName).place(x=5, y=75)
    global instructorSelectNameEntry
    instructorSelectNameEntry = Entry(main7, width=9)
    instructorSelectNameEntry.place(x=105, y=75)
    Button(main7, text='Select by Degree', command=instructorSelectDegree).place(x=5, y=100)
    global instructorSelectDegreeEntry
    instructorSelectDegreeEntry = Entry(main7, width=9)
    instructorSelectDegreeEntry.place(x=110, y=100)


    Label(main7, text='INSERT').place(x=200, y=1)
    Button(main7, text='Insert new', command=instructorInsert).place(x=200, y=25)
    Label(main7, text='SNO:').place(x=200, y=50)
    global instructorInsertSNO
    instructorInsertSNO = Entry(main7, width=3)
    instructorInsertSNO.place(x=235, y=50)
    Label(main7, text='Name:').place(x=200, y=75)
    global instructorInsertName
    instructorInsertName = Entry(main7, width=8)
    instructorInsertName.place(x=245, y=75)
    Label(main7, text='Tel:').place(x=200, y=100)
    global instructorInsertTel
    instructorInsertTel = Entry(main7, width=11)
    instructorInsertTel.place(x=225, y=100)
    Label(main7, text='Degree:').place(x=200, y=125)
    global instructorInsertDegree
    instructorInsertDegree = Entry(main7, width=9)
    instructorInsertDegree.place(x=250, y=125)
    Label(main7, text='Experience:').place(x=200, y=150)
    global instructorInsertExp
    instructorInsertExp = Entry(main7, width=9)
    instructorInsertExp.place(x=265, y=150)


    Label(main7, text='UPDATE').place(x=440, y=1)
    Button(main7, text='Update by SNO', command=instructorUpdateSNO).place(x=440, y=25)
    Label(main7, text='SNO:').place(x=535, y=25)
    global entryUpdateSNO
    entryUpdateSNO = Entry(main7, width=3)
    entryUpdateSNO.place(x=565, y=25)
    Label(main7, text='New SNO:').place(x=440, y=50)
    global entryUpdateSNOSNO
    entryUpdateSNOSNO = Entry(main7, width=3)
    entryUpdateSNOSNO.place(x=505, y=50)
    Label(main7, text='New Name:').place(x=440, y=75)
    global entryUpdateSNOName
    entryUpdateSNOName = Entry(main7, width=5)
    entryUpdateSNOName.place(x=510, y=75)
    Label(main7, text='New Tel:').place(x=440, y=100)
    global entryUpdateSNOTel
    entryUpdateSNOTel = Entry(main7, width=10)
    entryUpdateSNOTel.place(x=495, y=100)
    Label(main7, text='New Degree:').place(x=440, y=125)
    global entryUpdateSNODegree
    entryUpdateSNODegree = Entry(main7, width=9)
    entryUpdateSNODegree.place(x=510, y=125)
    Label(main7, text='New Exp:').place(x=440, y=150)
    global entryUpdateSNOExp
    entryUpdateSNOExp = Entry(main7, width=9)
    entryUpdateSNOExp.place(x=495, y=150)

    Button(main7, text='Update by Name', command=instructorUpdateName).place(x=440, y=175)
    Label(main7, text='Name:').place(x=540, y=175)
    global entryUpdateName
    entryUpdateName = Entry(main7, width=9)
    entryUpdateName.place(x=580, y=175)
    Label(main7, text='New SNO:').place(x=440, y=200)
    global entryUpdateNameSNO
    entryUpdateNameSNO = Entry(main7, width=3)
    entryUpdateNameSNO.place(x=505, y=200)
    Label(main7, text='New Name:').place(x=440, y=225)
    global entryUpdateNameName
    entryUpdateNameName = Entry(main7, width=5)
    entryUpdateNameName.place(x=510, y=225)
    Label(main7, text='New Tel:').place(x=440, y=250)
    global entryUpdateNameTel
    entryUpdateNameTel = Entry(main7, width=10)
    entryUpdateNameTel.place(x=495, y=250)
    Label(main7, text='New Degree:').place(x=440, y=275)
    global entryUpdateNameDegree
    entryUpdateNameDegree = Entry(main7, width=9)
    entryUpdateNameDegree.place(x=510, y=275)
    Label(main7, text='New Exp:').place(x=440, y=300)
    global entryUpdateNameExp
    entryUpdateNameExp = Entry(main7, width=9)
    entryUpdateNameExp.place(x=495, y=300)

    Button(main7, text='Update by Degree', command=instructorUpdateDegree).place(x=440, y=325)
    Label(main7, text='Degree:').place(x=545, y=325)
    global entryUpdateDegree
    entryUpdateDegree = Entry(main7, width=9)
    entryUpdateDegree.place(x=590, y=325)
    Label(main7, text='New SNO:').place(x=440, y=350)
    global entryUpdateDegreeSNO
    entryUpdateDegreeSNO = Entry(main7, width=3)
    entryUpdateDegreeSNO.place(x=505, y=350)
    Label(main7, text='New Name:').place(x=440, y=375)
    global entryUpdateDegreeName
    entryUpdateDegreeName = Entry(main7, width=5)
    entryUpdateDegreeName.place(x=510, y=375)
    Label(main7, text='New Tel:').place(x=440, y=400)
    global entryUpdateDegreeTel
    entryUpdateDegreeTel = Entry(main7, width=10)
    entryUpdateDegreeTel.place(x=495, y=400)
    Label(main7, text='New Degree:').place(x=440, y=425)
    global entryUpdateDegreeDegree
    entryUpdateDegreeDegree = Entry(main7, width=9)
    entryUpdateDegreeDegree.place(x=510, y=425)
    Label(main7, text='New Exp:').place(x=440, y=450)
    global entryUpdateDegreeExp
    entryUpdateDegreeExp = Entry(main7, width=9)
    entryUpdateDegreeExp.place(x=495, y=450)

    Label(main7, text='DELETE').place(x=680, y=1)
    Button(main7, text='Delete by SNO', command=instructorDeleteSNO).place(x=680, y=25)
    global instructorDeleteSNOEntry
    instructorDeleteSNOEntry = Entry(main7, width=3)
    instructorDeleteSNOEntry.place(x=770, y=25)
    Button(main7, text='Delete by Name', command=instructorDeleteName).place(x=680, y=50)
    global instructorDeleteNameEntry
    instructorDeleteNameEntry = Entry(main7, width=9)
    instructorDeleteNameEntry.place(x=780, y=50)
    Button(main7, text='Delete by Degree', command=instructorDeleteDegree).place(x=680, y=75)
    global instructorDeleteDegreeEntry
    instructorDeleteDegreeEntry = Entry(main7, width=9)
    instructorDeleteDegreeEntry.place(x=785, y=75)
    Button(main7, text='Delete All', command=instructorDeleteAll).place(x=680, y=100)
    global instructorConfirmation
    instructorConfirmation = Entry(main7, width=4)
    instructorConfirmation.place(x=760, y=100)

    Button(main7, text='RETURN', command=openMenu).place(x=770, y=470)

    close3()

def instructorSelectAll():
    sent = 'SELECT * FROM public."Instructors" ORDER BY "SNO" ASC'
    cur.execute(sent)
    res = str(cur.fetchall())
    list = []
    var = ""

    for e in res:
        if e != ")":
            var += e
        else:
            newvar = var.replace('[', '').replace('(', '')
            list.append(newvar)
            var = ""

    string = ''
    for e in list:
        string += (e + "\n")

    tkinter.messagebox.showinfo(message=string)

def instructorSelectSNO():
    getEntry =  instructorSelectSNOEntry.get()
    sen = "SELECT * FROM Public.\"Instructors\" WHERE \"SNO\" = " + str(getEntry) + ""
    try:
        cur.execute(sen)
        string = str(cur.fetchall())
        newstring = string.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
        tkinter.messagebox.showinfo(message=newstring)
    except Exception:
        con.rollback()

def instructorSelectName():
    getEntry =  instructorSelectNameEntry.get()
    try:
        sen = "SELECT * FROM Public.\"Instructors\" WHERE \"name\" = '" + str(getEntry) + "'"
        cur.execute(sen)
        string = str(cur.fetchall())
        newstring = string.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
        tkinter.messagebox.showinfo(message=newstring)
    except Exception:
        con.rollback()

def instructorSelectDegree():
    getEntry =  instructorSelectDegreeEntry.get()
    sen = "SELECT * FROM Public.\"Instructors\" WHERE \"degree\" = '" + str(getEntry) + "'"
    try:
        cur.execute(sen)
        string = str(cur.fetchall())
        var = ''
        list = []

        for e in string:
            if e != ")":
                var += e
            else:
                newvar = var.replace('[', '').replace('(', '')
                list.append(newvar)
                var = ""

        newstring = ''
        for e in list:
            newstring += (e + "\n")
        tkinter.messagebox.showinfo(message=newstring)
    except Exception:
        con.rollback()

def instructorInsert():
    getEntry1 = instructorInsertSNO.get()
    getEntry2 = instructorInsertName.get()
    getEntry3 = instructorInsertTel.get()
    getEntry4 = instructorInsertDegree.get()
    getEntry5 = instructorInsertExp.get()
    sen = f"INSERT INTO public.\"Instructors\" (\"SNO\", \"name\", \"tel\", \"degree\", \"experience\") VALUES ({str(getEntry1)}, '{str(getEntry2)}', {str(getEntry3)}, '{str(getEntry4)}', '{str(getEntry5)}')"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def instructorUpdateSNO():
    getEntry = entryUpdateSNO.get()
    getEntry1 = entryUpdateSNOSNO.get()
    getEntry2 = entryUpdateSNOName.get()
    getEntry3 = entryUpdateSNOTel.get()
    getEntry4 = entryUpdateSNODegree.get()
    getEntry5 = entryUpdateSNOExp.get()
    sen = f"UPDATE public.\"Instructors\" SET"

    if getEntry1 != "":
        sen += f" \"SNO\" = {str(getEntry1)},"
    if getEntry2 != "":
        sen += f" \"name\" = '{str(getEntry2)}',"
    if getEntry3 != "":
        sen += f" \"tel\" = {str(getEntry3)},"
    if getEntry4 != "":
        sen += f" \"degree\" = '{str(getEntry4)}',"
    if getEntry5 != "":
        sen += f" \"experience\" = '{str(getEntry5)}',"
    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"SNO\" = {str(getEntry)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def instructorUpdateName():
    getEntry = entryUpdateName.get()
    getEntry1 = entryUpdateNameSNO.get()
    getEntry2 = entryUpdateNameName.get()
    getEntry3 = entryUpdateNameTel.get()
    getEntry4 = entryUpdateNameDegree.get()
    getEntry5 = entryUpdateNameExp.get()
    sen = f"UPDATE public.\"Instructors\" SET"

    if getEntry1 != "":
        sen += f" \"SNO\" = {str(getEntry1)},"
    if getEntry2 != "":
        sen += f" \"name\" = '{str(getEntry2)}',"
    if getEntry3 != "":
        sen += f" \"tel\" = {str(getEntry3)},"
    if getEntry4 != "":
        sen += f" \"degree\" = '{str(getEntry4)}',"
    if getEntry5 != "":
        sen += f" \"experience\" = '{str(getEntry5)}',"
    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"name\" = '{str(getEntry)}'"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def instructorUpdateDegree():
    getEntry = entryUpdateDegree.get()
    getEntry1 = entryUpdateDegreeSNO.get()
    getEntry2 = entryUpdateDegreeName.get()
    getEntry3 = entryUpdateDegreeTel.get()
    getEntry4 = entryUpdateDegreeDegree.get()
    getEntry5 = entryUpdateDegreeExp.get()
    sen = f"UPDATE public.\"Instructors\" SET"

    if getEntry1 != "":
        sen += f" \"SNO\" = {str(getEntry1)},"
    if getEntry2 != "":
        sen += f" \"name\" = '{str(getEntry2)}',"
    if getEntry3 != "":
        sen += f" \"tel\" = {str(getEntry3)},"
    if getEntry4 != "":
        sen += f" \"degree\" = '{str(getEntry4)}',"
    if getEntry5 != "":
        sen += f" \"experience\" = '{str(getEntry5)}',"
    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"degree\" = '{str(getEntry)}'"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def instructorDeleteSNO():
    getEntry = instructorDeleteSNOEntry.get()
    sen = f"DELETE FROM public.\"Instructors\" WHERE \"SNO\" = {str(getEntry)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def instructorDeleteName():
    getEntry = instructorDeleteNameEntry.get()
    sen = f"DELETE FROM public.\"Instructors\" WHERE \"name\" = '{str(getEntry)}'"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def instructorDeleteDegree():
    getEntry = instructorDeleteDegreeEntry.get()
    sen = f"DELETE FROM public.\"Instructors\" WHERE \"degree\" = '{str(getEntry)}'"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def instructorDeleteAll():
    entry = instructorConfirmation.get()
    if str(entry) == 'YES' or str(entry) == 'yes':
        sen = "DELETE FROM public.\"Instructors\""
        print(sen)
        try:
            cur.execute(sen)
            con.commit()
        except Exception:
            con.rollback()

#################################################################

#MEMBERS

##################################################################

def clickMembers():
    global main8
    main8 = Tk()
    main8.title("MEMBERS")
    main8.geometry("870x390")

    Label(main8, text='SELECT').place(x=5, y=1)
    Button(main8, text='Select All', command=memberSelectAll).place(x=5, y=25)
    Button(main8, text='Select by MembNum', command=memberSelectMembNum).place(x=5, y=50)
    global memberSelectMembNumEntry
    memberSelectMembNumEntry = Entry(main8, width=3)
    memberSelectMembNumEntry.place(x=135, y=50)
    # Label(main4, textvariable=text1).place(x=5, y=75)
    Button(main8, text='Select by Name', command=memberSelectName).place(x=5, y=75)
    global memberSelectNameEntry
    memberSelectNameEntry = Entry(main8, width=9)
    memberSelectNameEntry.place(x=100, y=75)

    Label(main8, text='INSERT').place(x=200, y=1)
    Button(main8, text='Insert new', command=memberInsert).place(x=200, y=25)
    Label(main8, text='MembNum:').place(x=200, y=50)
    global memberInsertMembNum
    memberInsertMembNum = Entry(main8, width=3)
    memberInsertMembNum.place(x=270, y=50)
    Label(main8, text='Name:').place(x=200, y=75)
    global memberInsertName
    memberInsertName = Entry(main8, width=8)
    memberInsertName.place(x=240, y=75)
    Label(main8, text='Bank Dets:').place(x=200, y=100)
    global memberInsertBankDets
    memberInsertBankDets = Entry(main8, width=11)
    memberInsertBankDets.place(x=260, y=100)
    Label(main8, text='Address:').place(x=200, y=125)
    global memberInsertAddress
    memberInsertAddress = Entry(main8, width=9)
    memberInsertAddress.place(x=250, y=125)
    Label(main8, text='Tel:').place(x=200, y=150)
    global memberInsertTel
    memberInsertTel = Entry(main8, width=9)
    memberInsertTel.place(x=225, y=150)
    Label(main8, text='Proffesion:').place(x=200, y=175)
    global memberInsertProffesion
    memberInsertProffesion = Entry(main8, width=9)
    memberInsertProffesion.place(x=265, y=175)

    Label(main8, text='UPDATE').place(x=440, y=1)
    Button(main8, text='Update by MembNum', command=memberUpdateMembNum).place(x=440, y=25)
    Label(main8, text='MembNum:').place(x=570, y=25)
    global entryUpdateMembNum
    entryUpdateMembNum = Entry(main8, width=3)
    entryUpdateMembNum.place(x=640, y=25)
    Label(main8, text='New MembNum:').place(x=440, y=50)
    global entryUpdateMembNumMembNum
    entryUpdateMembNumMembNum = Entry(main8, width=3)
    entryUpdateMembNumMembNum.place(x=535, y=50)
    Label(main8, text='New Name:').place(x=440, y=75)
    global entryUpdateMembNumName
    entryUpdateMembNumName = Entry(main8, width=5)
    entryUpdateMembNumName.place(x=510, y=75)
    Label(main8, text='New Bank Dets:').place(x=440, y=100)
    global entryUpdateMembNumBankDets
    entryUpdateMembNumBankDets = Entry(main8, width=10)
    entryUpdateMembNumBankDets.place(x=530, y=100)
    Label(main8, text='New Address:').place(x=440, y=125)
    global entryUpdateMembNumAddress
    entryUpdateMembNumAddress = Entry(main8, width=9)
    entryUpdateMembNumAddress.place(x=520, y=125)
    Label(main8, text='New Tel:').place(x=440, y=150)
    global entryUpdateMembNumTel
    entryUpdateMembNumTel = Entry(main8, width=9)
    entryUpdateMembNumTel.place(x=490, y=150)
    Label(main8, text='New Proffesion:').place(x=440, y=175)
    global entryUpdateMembNumProffesion
    entryUpdateMembNumProffesion = Entry(main8, width=9)
    entryUpdateMembNumProffesion.place(x=530, y=175)

    Button(main8, text='Update by Name', command=memberUpdateName).place(x=440, y=200)
    Label(main8, text='Name:').place(x=540, y=200)
    global entryUpdateNameM
    entryUpdateNameM = Entry(main8, width=9)
    entryUpdateNameM.place(x=580, y=200)
    Label(main8, text='New MembNum:').place(x=440, y=225)
    global entryUpdateNameMembNum
    entryUpdateNameMembNum = Entry(main8, width=3)
    entryUpdateNameMembNum.place(x=535, y=225)
    Label(main8, text='New Name:').place(x=440, y=250)
    global entryUpdateNameNameM
    entryUpdateNameNameM = Entry(main8, width=5)
    entryUpdateNameNameM.place(x=510, y=250)
    Label(main8, text='New Bank Dets:').place(x=440, y=275)
    global entryUpdateNameBankDets
    entryUpdateNameBankDets = Entry(main8, width=10)
    entryUpdateNameBankDets.place(x=530, y=275)
    Label(main8, text='New Address:').place(x=440, y=300)
    global entryUpdateNameAddress
    entryUpdateNameAddress = Entry(main8, width=9)
    entryUpdateNameAddress.place(x=520, y=300)
    Label(main8, text='New Tel:').place(x=440, y=325)
    global entryUpdateNameTel
    entryUpdateNameTel = Entry(main8, width=9)
    entryUpdateNameTel.place(x=490, y=325)
    Label(main8, text='New Proffesion:').place(x=440, y=350)
    global entryUpdateNameProffesion
    entryUpdateNameProffesion = Entry(main8, width=9)
    entryUpdateNameProffesion.place(x=530, y=350)


    Label(main8, text='DELETE').place(x=680, y=1)
    Button(main8, text='Delete by MembNum', command=memberDeleteMembNum).place(x=680, y=25)
    global memberDeleteMembNumEntry
    memberDeleteMembNumEntry = Entry(main8, width=3)
    memberDeleteMembNumEntry.place(x=810, y=25)
    Button(main8, text='Delete by Name', command=memberDeleteName).place(x=680, y=50)
    global memberDeleteNameEntry
    memberDeleteNameEntry = Entry(main8, width=9)
    memberDeleteNameEntry.place(x=780, y=50)
    Button(main8, text='Delete All', command=memberDeleteAll).place(x=680, y=75)
    global memberConfirmation
    memberConfirmation = Entry(main8, width=4)
    memberConfirmation.place(x=760, y=75)

    Button(main8, text='RETURN', command=openMenu).place(x=770, y=320)

    close3()



def memberSelectAll():
    sent = 'SELECT * FROM public."Members" ORDER BY "membNum" ASC'
    cur.execute(sent)
    res = str(cur.fetchall())
    list = []
    var = ""

    for e in res:
        if e != ")":
            var += e
        else:
            newvar = var.replace('[', '').replace('(', '')
            list.append(newvar)
            var = ""

    string = ''
    for e in list:
        string += (e + "\n")

    tkinter.messagebox.showinfo(message=string)

def memberSelectMembNum():
    getEntry =  memberSelectMembNumEntry.get()
    sen = "SELECT * FROM Public.\"Members\" WHERE \"membNum\" = " + str(getEntry) + ""
    try:
        cur.execute(sen)
        string = str(cur.fetchall())
        newstring = string.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
        tkinter.messagebox.showinfo(message=newstring)
    except Exception:
        con.rollback()

def memberSelectName():
    getEntry =  memberSelectNameEntry.get()
    sen = "SELECT * FROM Public.\"Members\" WHERE \"name\" = '" + str(getEntry) + "'"
    try:
        cur.execute(sen)
        string = str(cur.fetchall())
        newstring = string.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
        tkinter.messagebox.showinfo(message=newstring)
    except Exception:
        con.rollback()

def memberInsert():
    getEntry1 = memberInsertMembNum.get()
    getEntry2 = memberInsertName.get()
    getEntry3 = memberInsertBankDets.get()
    getEntry4 = memberInsertAddress.get()
    getEntry5 = memberInsertTel.get()
    getEntry6 = memberInsertProffesion.get()
    sen = f"INSERT INTO public.\"Members\" (\"membNum\", \"name\", \"bankDets\", \"address\", \"tel\", \"proffesion\") VALUES ({str(getEntry1)}, '{str(getEntry2)}', {str(getEntry3)}, '{str(getEntry4)}', {str(getEntry5)}, '{str(getEntry6)}')"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def memberUpdateMembNum():
    getEntry = entryUpdateMembNum.get()
    getEntry1 = entryUpdateMembNumMembNum.get()
    getEntry2 = entryUpdateMembNumName.get()
    getEntry3 = entryUpdateMembNumBankDets.get()
    getEntry4 = entryUpdateMembNumAddress.get()
    getEntry5 = entryUpdateMembNumTel.get()
    getEntry6 = entryUpdateMembNumProffesion.get()
    sen = f"UPDATE public.\"Members\" SET"

    if getEntry1 != "":
        sen += f" \"membNum\" = {str(getEntry1)},"
    if getEntry2 != "":
        sen += f" \"name\" = '{str(getEntry2)}',"
    if getEntry3 != "":
        sen += f" \"bankDets\" = '{str(getEntry3)}',"
    if getEntry4 != "":
        sen += f" \"address\" = '{str(getEntry4)}',"
    if getEntry5 != "":
        sen += f" \"tel\" = {str(getEntry5)},"
    if getEntry6 != "":
        sen += f" \"proffesion\" = '{str(getEntry6)}',"
    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"membNum\" = {str(getEntry)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()


def memberUpdateName():
    getEntry = entryUpdateNameM.get()
    getEntry1 = entryUpdateNameMembNum.get()
    getEntry2 = entryUpdateNameNameM.get()
    getEntry3 = entryUpdateNameBankDets.get()
    getEntry4 = entryUpdateNameAddress.get()
    getEntry5 = entryUpdateNameTel.get()
    getEntry6 = entryUpdateNameProffesion.get()
    sen = f"UPDATE public.\"Members\" SET"

    if getEntry1 != "":
        sen += f" \"membNum\" = {str(getEntry1)},"
    if getEntry2 != "":
        sen += f" \"name\" = '{str(getEntry2)}',"
    if getEntry3 != "":
        sen += f" \"bankDets\" = '{str(getEntry3)}',"
    if getEntry4 != "":
        sen += f" \"address\" = '{str(getEntry4)}',"
    if getEntry5 != "":
        sen += f" \"tel\" = {str(getEntry5)},"
    if getEntry6 != "":
        sen += f" \"proffesion\" = '{str(getEntry6)}',"
    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"name\" = '{str(getEntry)}'"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def memberDeleteMembNum():
    getEntry = memberDeleteMembNumEntry.get()
    sen = f"DELETE FROM public.\"Members\" WHERE \"membNum\" = {str(getEntry)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def memberDeleteName():
    getEntry = memberDeleteNameEntry.get()
    sen = f"DELETE FROM public.\"Members\" WHERE \"name\" = '{str(getEntry)}'"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def memberDeleteAll():
    entry = memberConfirmation.get()
    if str(entry) == 'YES' or str(entry) == 'yes':
        sen = "DELETE FROM public.\"Members\""
        print(sen)
        try:
            cur.execute(sen)
            con.commit()
        except Exception:
            con.rollback()



######################################################
#SQUASHCOURTS
#####################################################

def clickSquashCourts():
    global main9
    main9 = Tk()
    main9.title("SQUASHCOURTS")
    main9.geometry("870x250")

    Label(main9, text='SELECT').place(x=5, y=1)
    Button(main9, text='Select All', command=squashSelectAll).place(x=5, y=25)
    Button(main9, text='Select by courtNum', command=squashSelectCourtNum).place(x=5, y=50)
    global squashSelectCourtNumEntry
    squashSelectCourtNumEntry = Entry(main9, width=3)
    squashSelectCourtNumEntry.place(x=125, y=50)
    Button(main9, text='Select by Location', command=squashSelectLocation).place(x=5, y=75)
    global squashSelectLocationEntry
    squashSelectLocationEntry = Entry(main9, width=9)
    squashSelectLocationEntry.place(x=115, y=75)

    Label(main9, text='INSERT').place(x=200, y=1)
    Button(main9, text='Insert new', command=squashInsert).place(x=200, y=25)
    Label(main9, text='CourtNum:').place(x=200, y=50)
    global squashInsertCourtNum
    squashInsertCourtNum = Entry(main9, width=3)
    squashInsertCourtNum.place(x=270, y=50)
    Label(main9, text='Location:').place(x=200, y=75)
    global squashInsertLocation
    squashInsertLocation = Entry(main9, width=8)
    squashInsertLocation.place(x=255, y=75)
    Label(main9, text='Condition:').place(x=200, y=100)
    global squashInsertCondition
    squashInsertCondition = Entry(main9, width=11)
    squashInsertCondition.place(x=260, y=100)


    Label(main9, text='UPDATE').place(x=440, y=1)
    Button(main9, text='Update by CourtNum', command=squashUpdateMembNum).place(x=440, y=25)
    Label(main9, text='CourtNum:').place(x=565, y=25)
    global entryUpdateCourtNum
    entryUpdateCourtNum = Entry(main9, width=3)
    entryUpdateCourtNum.place(x=630, y=25)
    Label(main9, text='New CourtNum:').place(x=440, y=50)
    global entryUpdateCourtNumCourtNum
    entryUpdateCourtNumCourtNum = Entry(main9, width=3)
    entryUpdateCourtNumCourtNum.place(x=535, y=50)
    Label(main9, text='New Location:').place(x=440, y=75)
    global entryUpdateCourtNumLocation
    entryUpdateCourtNumLocation = Entry(main9, width=5)
    entryUpdateCourtNumLocation.place(x=520, y=75)
    Label(main9, text='New Condition:').place(x=440, y=100)
    global entryUpdateCourtNumCondition
    entryUpdateCourtNumCondition = Entry(main9, width=10)
    entryUpdateCourtNumCondition.place(x=530, y=100)

    Button(main9, text='Update by Location', command=squashUpdateLocation).place(x=440, y=125)
    Label(main9, text='Location:').place(x=555, y=125)
    global entryUpdateLocation
    entryUpdateLocation = Entry(main9, width=9)
    entryUpdateLocation.place(x=610, y=125)
    Label(main9, text='New CourtNum:').place(x=440, y=150)
    global entryUpdateLocationCourtNum
    entryUpdateLocationCourtNum = Entry(main9, width=3)
    entryUpdateLocationCourtNum.place(x=535, y=150)
    Label(main9, text='New Location:').place(x=440, y=175)
    global entryUpdateLocationLocation
    entryUpdateLocationLocation = Entry(main9, width=5)
    entryUpdateLocationLocation.place(x=520, y=175)
    Label(main9, text='New Condition:').place(x=440, y=200)
    global entryUpdateLocationCondition
    entryUpdateLocationCondition = Entry(main9, width=10)
    entryUpdateLocationCondition.place(x=530, y=200)


    Label(main9, text='DELETE').place(x=680, y=1)
    Button(main9, text='Delete by CourtNum', command=squashDeleteCourtNum).place(x=680, y=25)
    global squashDeleteCourtNumEntry
    squashDeleteCourtNumEntry = Entry(main9, width=3)
    squashDeleteCourtNumEntry.place(x=805, y=25)
    Button(main9, text='Delete by Location', command=squashDeleteLocation).place(x=680, y=50)
    global squashDeleteLocationEntry
    squashDeleteLocationEntry = Entry(main9, width=9)
    squashDeleteLocationEntry.place(x=790, y=50)
    Button(main9, text='Delete All', command=squashDeleteAll).place(x=680, y=75)
    global squashConfirmation
    squashConfirmation = Entry(main9, width=4)
    squashConfirmation.place(x=760, y=75)

    Button(main9, text='RETURN', command=openMenu).place(x=770, y=220)

    close3()


def squashSelectAll():
    sent = 'SELECT * FROM public."SquashCourts" ORDER BY "courtNum" ASC'
    cur.execute(sent)
    res = str(cur.fetchall())
    list = []
    var = ""

    for e in res:
        if e != ")":
            var += e
        else:
            newvar = var.replace('[', '').replace('(', '')
            list.append(newvar)
            var = ""

    string = ''
    for e in list:
        string += (e + "\n")

    tkinter.messagebox.showinfo(message=string)

def squashSelectCourtNum():
    getEntry =  squashSelectCourtNumEntry.get()
    sen = "SELECT * FROM Public.\"SquashCourts\" WHERE \"courtNum\" = " + str(getEntry) + ""
    try:
        cur.execute(sen)
        string = str(cur.fetchall())
        newstring = string.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
        tkinter.messagebox.showinfo(message=newstring)
    except Exception:
        con.rollback()

def squashSelectLocation():
    getEntry = squashSelectLocationEntry.get()
    sent = f"SELECT * FROM Public.\"SquashCourts\" WHERE \"location\" = '{getEntry}'"
    try:
        cur.execute(sent)
        res = str(cur.fetchall())
    except Exception:
        con.rollback()

    list = []
    var = ""

    for e in res:
        if e != ")":
            var += e
        else:
            newvar = var.replace('[', '').replace('(', '')
            list.append(newvar)
            var = ""

    string = ''
    for e in list:
        string += (e + "\n")

    tkinter.messagebox.showinfo(message=string)

def squashInsert():
    getEntry1 = squashInsertCourtNum.get()
    getEntry2 = squashInsertLocation.get()
    getEntry3 = squashInsertCondition.get()

    sen = f"INSERT INTO public.\"SquashCourts\" (\"courtNum\", \"location\", \"condition\") VALUES ({str(getEntry1)}, '{str(getEntry2)}', '{str(getEntry3)}')"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def squashUpdateMembNum():
    getEntry = entryUpdateCourtNum.get()
    getEntry1 = entryUpdateCourtNumCourtNum.get()
    getEntry2 = entryUpdateCourtNumLocation.get()
    getEntry3 = entryUpdateCourtNumCondition.get()
    sen = f"UPDATE public.\"SquashCourts\" SET"

    if getEntry1 != "":
        sen += f" \"courtNum\" = {str(getEntry1)},"
    if getEntry2 != "":
        sen += f" \"location\" = '{str(getEntry2)}',"
    if getEntry3 != "":
        sen += f" \"condition\" = '{str(getEntry3)}',"

    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"courtNum\" = {str(getEntry)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def squashUpdateLocation():
    getEntry = entryUpdateLocation.get()
    getEntry1 = entryUpdateLocationCourtNum.get()
    getEntry2 = entryUpdateLocationLocation.get()
    getEntry3 = entryUpdateLocationCondition.get()
    sen = f"UPDATE public.\"SquashCourts\" SET"

    if getEntry1 != "":
        sen += f" \"courtNum\" = {str(getEntry1)},"
    if getEntry2 != "":
        sen += f" \"location\" = '{str(getEntry2)}',"
    if getEntry3 != "":
        sen += f" \"condition\" = '{str(getEntry3)}',"

    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"location\" = '{str(getEntry)}'"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def squashDeleteCourtNum():
    getEntry = squashDeleteCourtNumEntry.get()
    sen = f"DELETE FROM public.\"SquashCourts\" WHERE \"courtNum\" = {str(getEntry)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def squashDeleteLocation():
    getEntry = squashDeleteLocationEntry.get()
    sen = f"DELETE FROM public.\"SquashCourts\" WHERE \"location\" = '{str(getEntry)}'"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def squashDeleteAll():
    entry = squashConfirmation.get()
    if str(entry) == 'YES' or str(entry) == 'yes':
        sen = "DELETE FROM public.\"SquashCourts\""
        print(sen)
        try:
            cur.execute(sen)
            con.commit()
        except Exception:
            con.rollback()





#########################################################
#ASSIGNED
##########################################################

def clickAssigned():
    global main10
    main10 = Tk()
    main10.title("ASSIGNED")
    main10.geometry("500x180")

    Label(main10, text='SELECT').place(x=5, y=1)
    Button(main10, text='Select All', command=assignedSelectAll).place(x=5, y=25)

    Label(main10, text='INSERT').place(x=100, y=1)
    Button(main10, text='Insert new', command=assignedInsert).place(x=100, y=25)
    Label(main10, text='Room ID:').place(x=100, y=50)
    global assignedInsertRoomID
    assignedInsertRoomID = Entry(main10, width=3)
    assignedInsertRoomID.place(x=155, y=50)
    Label(main10, text='Class Code:').place(x=100, y=75)
    global assignedInsertClassCode
    assignedInsertClassCode = Entry(main10, width=3)
    assignedInsertClassCode.place(x=165, y=75)


    Label(main10, text='UPDATE').place(x=250, y=1)
    Button(main10, text='Update', command=assignedUpdate).place(x=250, y=25)
    Label(main10, text='Room ID:').place(x=250, y=50)
    global entryUpdateRoomIDA
    entryUpdateRoomIDA = Entry(main10, width=3)
    entryUpdateRoomIDA.place(x=305, y=50)
    Label(main10, text='Class Code:').place(x=250, y=75)
    global entryUpdateClassCodeA
    entryUpdateClassCodeA = Entry(main10, width=3)
    entryUpdateClassCodeA.place(x=315 , y=75)
    Label(main10, text='New Room ID:').place(x=250, y=100)
    global entryUpdateNewRoomIDA
    entryUpdateNewRoomIDA = Entry(main10, width=3)
    entryUpdateNewRoomIDA.place(x=330, y= 100)
    Label(main10, text='New Class Code:').place(x=250, y=125)
    global entryUpdateNewClassCodeA
    entryUpdateNewClassCodeA = Entry(main10, width=3)
    entryUpdateNewClassCodeA.place(x=345, y=125)


    Label(main10, text='DELETE').place(x=380, y=1)
    Button(main10, text='Delete', command=assignedDelete).place(x=380, y=25)
    Label(main10, text='Room ID:').place(x=380, y=50)
    global assignedDeleteRoomIDEntry
    assignedDeleteRoomIDEntry = Entry(main10, width=3)
    assignedDeleteRoomIDEntry.place(x=440, y=50)
    Label(main10, text='Class Code:').place(x=380, y=75)
    global assignedDeleteClassCodeEntry
    assignedDeleteClassCodeEntry = Entry(main10, width=3)
    assignedDeleteClassCodeEntry.place(x=445, y=75)


    Button(main10, text='RETURN', command=openMenu).place(x=400, y=150)

    close3()

def assignedSelectAll():
    sent = f"SELECT \"Assigned\".\"roomID\", \"Assigned\".\"classCode\", \"Classes\".\"description\" FROM Public.\"Assigned\" INNER JOIN Public.\"Classes\" ON \"Classes\".\"classCode\" = \"Assigned\".\"classCode\";"
    cur.execute(sent)
    res = str(cur.fetchall())
    list = []
    var = ""

    for e in res:
        if e != ")":
            var += e
        else:
            newvar = var.replace('[', '').replace('(', '')
            list.append(newvar)
            var = ""

    string = ''
    for e in list:
        string += (e + "\n")

    tkinter.messagebox.showinfo(message=string)

def assignedInsert():
    getEntry1 = assignedInsertRoomID.get()
    getEntry2 = assignedInsertClassCode.get()

    sen = f"INSERT INTO public.\"Assigned\" (\"roomID\", \"classCode\") VALUES ({str(getEntry1)}, {str(getEntry2)})"
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def assignedUpdate():
    getEntry1 = entryUpdateRoomIDA.get()
    getEntry2 = entryUpdateClassCodeA.get()
    getEntry3 = entryUpdateNewRoomIDA.get()
    getEntry4 = entryUpdateNewClassCodeA.get()

    sen = f"UPDATE public.\"Assigned\" SET"

    if getEntry3 != "":
        sen += f" \"roomID\" = {str(getEntry3)},"
    if getEntry4 != "":
        sen += f" \"classCode\" = {str(getEntry4)},"

    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"roomID\" = {str(getEntry1)} AND \"classCode\" = {str(getEntry2)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def assignedDelete():
    getEntry1 = assignedDeleteRoomIDEntry.get()
    getEntry2 = assignedDeleteClassCodeEntry.get()

    sen = f"DELETE FROM public.\"Assigned\" WHERE \"roomID\" = {str(getEntry1)} AND \"classCode\" = {str(getEntry2)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()





#######################################################################################################

#IMPART

#######################################################################################################

def clickImpart():
    global main11
    main11 = Tk()
    main11.title("IMPART")
    main11.geometry("500x180")

    Label(main11, text='SELECT').place(x=5, y=1)
    Button(main11, text='Select All', command=impartSelectAll).place(x=5, y=25)

    Label(main11, text='INSERT').place(x=100, y=1)
    main11 = main11
    Button(main11, text='Insert new', command=impartInsert).place(x=100, y=25)
    Label(main11, text='Class Code:').place(x=100, y=50)
    global impartInsertClassCode
    impartInsertClassCode = Entry(main11, width=3)
    impartInsertClassCode.place(x=165, y=50)
    Label(main11, text='SNO:').place(x=100, y=75)
    global impartInsertSNO
    impartInsertSNO = Entry(main11, width=3)
    impartInsertSNO.place(x=130, y=75)


    Label(main11, text='UPDATE').place(x=250, y=1)
    Button(main11, text='Update', command=impartUpdate).place(x=250, y=25)
    Label(main11, text='Class Code:').place(x=250, y=50)
    global entryUpdateClassCodeI
    entryUpdateClassCodeI = Entry(main11, width=3)
    entryUpdateClassCodeI.place(x=315, y=50)
    Label(main11, text='SNO:').place(x=250, y=75)
    global entryUpdateSNOI
    entryUpdateSNOI = Entry(main11, width=3)
    entryUpdateSNOI.place(x=280 , y=75)
    Label(main11, text='New Class Code:').place(x=250, y=100)
    global entryUpdateNewClassCodeI
    entryUpdateNewClassCodeI = Entry(main11, width=3)
    entryUpdateNewClassCodeI.place(x=345, y= 100)
    Label(main11, text='New SNO:').place(x=250, y=125)
    global entryUpdateNewSNOI
    entryUpdateNewSNOI = Entry(main11, width=3)
    entryUpdateNewSNOI.place(x=310, y=125)


    Label(main11, text='DELETE').place(x=380, y=1)
    Button(main11, text='Delete', command=impartDelete).place(x=380, y=25)
    Label(main11, text='Class Code:').place(x=380, y=50)
    global impartDeleteClassCodeEntry
    impartDeleteClassCodeEntry = Entry(main11, width=3)
    impartDeleteClassCodeEntry.place(x=445, y=50)
    Label(main11, text='SNO:').place(x=380, y=75)
    global impartDeleteSNOEntry
    impartDeleteSNOEntry = Entry(main11, width=3)
    impartDeleteSNOEntry.place(x=415, y=75)


    Button(main11, text='RETURN', command=openMenu).place(x=400, y=150)

    close3()


def impartSelectAll():
    sent = f'''SELECT \"Impart\".\"classCode\", \"Classes\".\"description\", \"Impart\".\"instructorSNO\", \"Instructors\".\"name\" 
        FROM Public.\"Impart\"    
        INNER JOIN Public.\"Classes\"
        ON \"Classes\".\"classCode\" = \"Impart\".\"classCode\"
        INNER JOIN Public.\"Instructors\"
        ON \"Instructors\".\"SNO\" = \"Impart\".\"instructorSNO\"'''
    cur.execute(sent)
    res = str(cur.fetchall())
    list = []
    var = ""

    for e in res:
        if e != ")":
            var += e
        else:
            newvar = var.replace('[', '').replace('(', '')
            list.append(newvar)
            var = ""

    string = ''
    for e in list:
        string += (e + "\n")

    tkinter.messagebox.showinfo(message=string)

def impartInsert():
    getEntry1 = impartInsertClassCode.get()
    getEntry2 = impartInsertSNO.get()

    sen = f"INSERT INTO public.\"Impart\" (\"classCode\", \"instructorSNO\") VALUES ({str(getEntry1)}, {str(getEntry2)})"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def impartUpdate():
    getEntry1 = entryUpdateClassCodeI.get()
    getEntry2 = entryUpdateSNOI.get()
    getEntry3 = entryUpdateNewClassCodeI.get()
    getEntry4 = entryUpdateNewSNOI.get()

    sen = f"UPDATE public.\"Impart\" SET"

    if getEntry3 != "":
        sen += f" \"classCode\" = {str(getEntry3)},"
    if getEntry4 != "":
        sen += f" \"instructorSNO\" = {str(getEntry4)},"

    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"classCode\" = {str(getEntry1)} AND \"instructorSNO\" = {str(getEntry2)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

def impartDelete():
    getEntry1 = impartDeleteClassCodeEntry.get()
    getEntry2 = impartDeleteSNOEntry.get()

    sen = f"DELETE FROM public.\"Impart\" WHERE \"classCode\" = {str(getEntry1)} AND \"instructorSNO\" = {str(getEntry2)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()





#########################################################################################################################

#ATTEND

#########################################################################################################################


def clickAttend():
    global main12
    main12 = Tk()
    main12.title("ATTEND")
    main12.geometry("500x180")

    Label(main12, text='SELECT').place(x=5, y=1)
    Button(main12, text='Select All', command=attendSelectAll).place(x=5, y=25)

    Label(main12, text='INSERT').place(x=100, y=1)
    main12 = main12
    Button(main12, text='Insert new', command=attendInsert).place(x=100, y=25)
    Label(main12, text='Class Code:').place(x=100, y=50)
    global attendInsertClassCode
    attendInsertClassCode = Entry(main12, width=3)
    attendInsertClassCode.place(x=165, y=50)
    Label(main12, text='Memb Num:').place(x=100, y=75)
    global attendInsertMembNum
    attendInsertMembNum = Entry(main12, width=3)
    attendInsertMembNum.place(x=175, y=75)


    Label(main12, text='UPDATE').place(x=250, y=1)
    Button(main12, text='Update', command=attendUpdate).place(x=250, y=25)
    Label(main12, text='Class Code:').place(x=250, y=50)
    global entryUpdateClassCodeAt
    entryUpdateClassCodeAt = Entry(main12, width=3)
    entryUpdateClassCodeAt.place(x=315, y=50)
    Label(main12, text='Memb Num:').place(x=250, y=75)
    global entryUpdateMembNumAt
    entryUpdateMembNumAt = Entry(main12, width=3)
    entryUpdateMembNumAt.place(x=325 , y=75)
    Label(main12, text='New Class Code:').place(x=250, y=100)
    global entryUpdateNewClassCodeAt
    entryUpdateNewClassCodeAt = Entry(main12, width=3)
    entryUpdateNewClassCodeAt.place(x=345, y= 100)
    Label(main12, text='New Memb Num:').place(x=250, y=125)
    global entryUpdateNewMembNumAt
    entryUpdateNewMembNumAt = Entry(main12, width=3)
    entryUpdateNewMembNumAt.place(x=350, y=125)


    Label(main12, text='DELETE').place(x=380, y=1)
    Button(main12, text='Delete', command=attendDelete).place(x=380, y=25)
    Label(main12, text='Class Code:').place(x=380, y=50)
    global attendDeleteClassCodeEntry
    attendDeleteClassCodeEntry = Entry(main12, width=3)
    attendDeleteClassCodeEntry.place(x=445, y=50)
    Label(main12, text='Memb Num:').place(x=380, y=75)
    global attendDeleteMembNumEntry
    attendDeleteMembNumEntry = Entry(main12, width=3)
    attendDeleteMembNumEntry.place(x=455, y=75)


    Button(main12, text='RETURN', command=openMenu).place(x=400, y=150)

    close3()


def attendSelectAll():
    sent = f'''
            SELECT \"Attend\".\"classCode\", \"Classes\"."description\", \"Attend\".\"membNum\", \"Members\".\"name\" 
            FROM Public.\"Attend\"    
            INNER JOIN Public.\"Classes\"
            ON \"Classes\".\"classCode\" = \"Attend\".\"classCode\"
            INNER JOIN Public.\"Members\"
            ON \"Members\".\"membNum\" = \"Attend\".\"membNum\"
            '''
    cur.execute(sent)
    res = str(cur.fetchall())
    list = []
    var = ""

    for e in res:
        if e != ")":
            var += e
        else:
            newvar = var.replace('[', '').replace('(', '')
            list.append(newvar)
            var = ""

    string = ''
    for e in list:
        string += (e + "\n")

    tkinter.messagebox.showinfo(message=string)


def attendInsert():
    getEntry1 = attendInsertClassCode.get()
    getEntry2 = attendInsertMembNum.get()

    sen = f"INSERT INTO public.\"Attend\" (\"classCode\", \"membNum\") VALUES ({str(getEntry1)}, {str(getEntry2)})"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()


def attendUpdate():
    getEntry1 = entryUpdateClassCodeAt.get()
    getEntry2 = entryUpdateMembNumAt.get()
    getEntry3 = entryUpdateNewClassCodeAt.get()
    getEntry4 = entryUpdateNewMembNumAt.get()

    sen = f"UPDATE public.\"Attend\" SET"

    if getEntry3 != "":
        sen += f" \"classCode\" = {str(getEntry3)},"
    if getEntry4 != "":
        sen += f" \"membNum\" = {str(getEntry4)},"

    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"classCode\" = {str(getEntry1)} AND \"membNum\" = {str(getEntry2)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()


def attendDelete():
    getEntry1 = attendDeleteClassCodeEntry.get()
    getEntry2 = attendDeleteMembNumEntry.get()

    sen = f"DELETE FROM public.\"Attend\" WHERE \"classCode\" = {str(getEntry1)} AND \"membNum\" = {str(getEntry2)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()





########################################################################################################################

#RESERVATION

########################################################################################################################


def clickReservation():
    global main13
    main13 = Tk()
    main13.title("RESERVATION")
    main13.geometry("500x220")

    Label(main13, text='SELECT').place(x=5, y=1)
    Button(main13, text='Select All', command=reservationSelectAll).place(x=5, y=25)

    Label(main13, text='INSERT').place(x=100, y=1)
    main13 = main13
    Button(main13, text='Insert new', command=reservationInsert).place(x=100, y=25)
    Label(main13, text='Memb Num:').place(x=100, y=50)
    global reservationInsertMembNum
    reservationInsertMembNum = Entry(main13, width=3)
    reservationInsertMembNum.place(x=175, y=50)
    Label(main13, text='Court Num:').place(x=100, y=75)
    global reservationInsertCourtNum
    reservationInsertCourtNum = Entry(main13, width=3)
    reservationInsertCourtNum.place(x=170, y=75)
    Label(main13, text='Date:').place(x=100, y=100)
    global reservationInsertDate
    reservationInsertDate = Entry(main13, width=5)
    reservationInsertDate.place(x=135, y=100)
    Label(main13, text='Time:').place(x=100, y=125)
    global reservationInsertTime
    reservationInsertTime = Entry(main13, width=5)
    reservationInsertTime.place(x=135, y=125)


    Label(main13, text='UPDATE').place(x=250, y=1)
    Button(main13, text='Update', command=reservationUpdate).place(x=250, y=25)
    Label(main13, text='Memb Num:').place(x=250, y=50)
    global entryUpdateMembNumR
    entryUpdateMembNumR = Entry(main13, width=3)
    entryUpdateMembNumR.place(x=325, y=50)
    Label(main13, text='Court Num:').place(x=250, y=75)
    global entryUpdateCourtNumR
    entryUpdateCourtNumR = Entry(main13, width=3)
    entryUpdateCourtNumR.place(x=320, y=75)
    Label(main13, text='New Memb Num:').place(x=250, y=100)
    global entryUpdateNewMembNumR
    entryUpdateNewMembNumR = Entry(main13, width=3)
    entryUpdateNewMembNumR.place(x=350, y= 100)
    Label(main13, text='New Court Num:').place(x=250, y=125)
    global entryUpdateNewCourtNumR
    entryUpdateNewCourtNumR = Entry(main13, width=3)
    entryUpdateNewCourtNumR.place(x=345, y=125)
    Label(main13, text='New Date:').place(x=250, y=150)
    global entryUpdateNewDateR
    entryUpdateNewDateR = Entry(main13, width=3)
    entryUpdateNewDateR.place(x=310, y=150)
    Label(main13, text='New Time:').place(x=250, y=175)
    global entryUpdateNewTimeR
    entryUpdateNewTimeR = Entry(main13, width=3)
    entryUpdateNewTimeR.place(x=310, y=175)


    Label(main13, text='DELETE').place(x=380, y=1)
    Button(main13, text='Delete', command=reservationDelete).place(x=380, y=25)
    Label(main13, text='Memb Num:').place(x=380, y=50)
    global reservationDeleteMembNumEntry
    reservationDeleteMembNumEntry = Entry(main13, width=3)
    reservationDeleteMembNumEntry.place(x=455, y=50)
    Label(main13, text='Court Num:').place(x=380, y=75)
    global reservationDeleteCourtNumEntry
    reservationDeleteCourtNumEntry = Entry(main13, width=3)
    reservationDeleteCourtNumEntry.place(x=450, y=75)


    Button(main13, text='RETURN', command=openMenu).place(x=400, y=185)

    close3()



def reservationSelectAll():
    sent = f'''
            SELECT "Reservation"."membNum", "Members"."name", "Reservation"."courtNum", "SquashCourts"."location", "Reservation"."date", "Reservation"."time"  
            FROM Public."Reservation"    
            INNER JOIN Public."Members"
            ON "Members"."membNum" = "Reservation"."membNum"
            INNER JOIN Public."SquashCourts"
            ON "SquashCourts"."courtNum" = "Reservation"."courtNum"
            '''
    cur.execute(sent)
    res = str(cur.fetchall())
    list = []
    var = ""

    for e in res:
        if e != ")":
            var += e
        else:
            newvar = var.replace('[', '').replace('(', '')
            list.append(newvar)
            var = ""

    string = ''
    for e in list:
        string += (e + "\n")

    tkinter.messagebox.showinfo(message=string)


def reservationInsert():
    getEntry1 = reservationInsertMembNum.get()
    getEntry2 = reservationInsertCourtNum.get()
    getEntry3 = reservationInsertDate.get()
    getEntry4 = reservationInsertTime.get()

    sen = f"INSERT INTO public.\"Reservation\" (\"membNum\", \"courtNum\", \"date\", \"time\") VALUES ({str(getEntry1)}, {str(getEntry2)}, '{str(getEntry3)}', '{str(getEntry4)}')"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()


def reservationUpdate():
    getEntry1 = entryUpdateMembNumR.get()
    getEntry2 = entryUpdateCourtNumR.get()
    getEntry3 = entryUpdateNewMembNumR.get()
    getEntry4 = entryUpdateNewCourtNumR.get()
    getEntry5 = entryUpdateNewDateR.get()
    getEntry6 = entryUpdateNewTimeR.get()

    sen = f"UPDATE public.\"Reservation\" SET"

    if getEntry3 != "":
        sen += f" \"membNum\" = {str(getEntry3)},"
    if getEntry4 != "":
        sen += f" \"courtNum\" = {str(getEntry4)},"
    if getEntry5 != "":
        sen += f" \"date\" = '{str(getEntry5)}',"
    if getEntry6 != "":
        sen += f" \"time\" = '{str(getEntry6)}',"

    sen = sen.rstrip(sen[-1])
    sen += f" WHERE \"membNum\" = {str(getEntry1)} AND \"courtNum\" = {str(getEntry2)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()


def reservationDelete():
    getEntry1 = reservationDeleteMembNumEntry.get()
    getEntry2 = reservationDeleteCourtNumEntry.get()

    sen = f"DELETE FROM public.\"Reservation\" WHERE \"membNum\" = {str(getEntry1)} AND \"courtNum\" = {str(getEntry2)}"
    print(sen)
    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()


def clickReports():
    global main14
    main14 = Tk()
    main14.title("REPORTS")
    main14.geometry("250x160")

    Button(main14, text="List of Classes by Instructor", command=clickClassesByInstructor).pack()
    Button(main14, text="List of Members by Class", command=clickMembersByClass).pack()
    Button(main14, text="List of Members by Instructor", command=clickMembersByInstructor).pack()
    Button(main14, text="List of All the Equipment", command=clickAllEquipment).pack()
    Button(main14, text="List of Equipement by Room", command=clickEquipmentByRoom).pack()
    global entryRoomIDReports
    entryRoomIDReports = Entry(main14, width=3)
    entryRoomIDReports.place(x=210, y=102)

    Button(main14, text='RETURN', command=openMenu).pack()

    close3()


def clickClassesByInstructor():
    name = 'ListOfClassesByInstructor'
    path = 'listOfClassesByInstructor.pdf'
    sen = f'''
            SELECT \"Impart\".\"classCode\", \"Classes\".\"description\", \"Impart\".\"instructorSNO\", \"Instructors\".\"name\"
            FROM Public.\"Impart\"
            INNER JOIN Public.\"Classes\"
            ON \"Classes\".\"classCode\" = \"Impart\".\"classCode\"
            INNER JOIN Public.\"Instructors\"
            ON \"Instructors\".\"SNO\" = \"Impart\".\"instructorSNO\"
            '''

    text.createText(sen, name, "CLASS CODE, DESCRIPTION, SNO, NAME")

    pdf = PDF()
    pdf.add_page()
    pdf.texts(name)
    pdf.titles('List of Classes by Instructor from ALWAYS IN SHAPE')
    pdf.set_author('ALWAYS IN SHAPE')
    pdf.output(path)

    os.system(path)


def clickMembersByClass():
    name = 'ListOfMembersByClass'
    path = 'listOfMembersByClass.pdf'
    sen = f'''
            SELECT \"Attend\".\"classCode\", \"Classes\"."description\", \"Attend\".\"membNum\", \"Members\".\"name\", \"Classes\".\"date\", \"Classes\".\"time\"  
            FROM Public.\"Attend\"    
            INNER JOIN Public.\"Classes\"
            ON \"Classes\".\"classCode\" = \"Attend\".\"classCode\"
            INNER JOIN Public.\"Members\"
            ON \"Members\".\"membNum\" = \"Attend\".\"membNum\"
            '''

    text.createText(sen, name, "CLASS CODE, DESCRIPTION, MEMBER NUM, NAME, DATE, TIME")

    pdf = PDF()
    pdf.add_page()
    pdf.titles('List of Members By Class from ALWAYS IN SHAPE')
    pdf.texts(name)
    pdf.set_author('ALWAYS IN SHAPE')
    pdf.output(path)

    os.system(path)


def clickMembersByInstructor():
    name = 'ListOfMembersByInstructor'
    path = 'listOfMembersByInstructor.pdf'
    sen = f'''
            SELECT "Attend"."classCode", "Classes"."description", "Attend"."membNum", "Members"."name", "Impart"."instructorSNO", "Instructors"."name"  
            FROM Public."Attend"    
            INNER JOIN Public."Classes"
            ON "Classes"."classCode" = "Attend"."classCode"
            INNER JOIN Public."Members"
            ON "Members"."membNum" = "Attend"."membNum"
            INNER JOIN Public."Impart"
            ON "Impart"."classCode" = "Classes"."classCode"
            INNER JOIN Public."Instructors"
            ON "Instructors"."SNO" = "Impart"."instructorSNO"
            '''

    text.createText(sen, name, "CLASS CODE, DESCRIPTION, MEMBER NUM, NAME, INSTRUCTOR SNO, NAME")

    pdf = PDF()
    pdf.add_page()
    pdf.titles('List of Members by Instructor from ALWAYS IN SHAPE')
    pdf.texts(name)
    pdf.set_author('ALWAYS IN SHAPE')
    pdf.output(path)

    os.system(path)


def clickAllEquipment():
    name = 'ListOfAllEquipment'
    path = 'ListOfAllEquipment.pdf'
    sen = f'''
            SELECT * FROM Public."Devices"
            '''

    text.createText(sen, name, "Device Code, Description, Status, Room ID")

    pdf = PDF()
    pdf.add_page()
    pdf.titles('List of All Equipment from ALWAYS IN SHAPE')
    pdf.texts(name)
    pdf.set_author('ALWAYS IN SHAPE')
    pdf.output(path)

    os.system(path)


def clickEquipmentByRoom():
    getEntry = entryRoomIDReports.get()

    name = 'ListOfEquipmentByRoom' + str(getEntry)
    path = 'ListOfAllEquipment' + str(getEntry) + '.pdf'
    sen = f'''
            SELECT "Rooms"."roomID", "Rooms"."type", "Rooms"."location", "Devices"."code", "Devices"."description", "Devices"."status"
            FROM Public."Devices"
            INNER JOIN Public."Rooms"
            ON "Rooms"."roomID" = "Devices"."roomID"
            WHERE "Rooms"."roomID" = {getEntry}
            '''

    text.createText(sen, name, "Room ID, Room Type, Room Location, Device Code, Device Description, Device Status")

    pdf = PDF()
    pdf.add_page()
    pdf.titles('List of Equipment in Room ' + str(getEntry) +  ' from ALWAYS IN SHAPE')
    pdf.texts(name)
    pdf.set_author('ALWAYS IN SHAPE')
    pdf.output(path)

    os.system(path)



def clickNewUser():

    tkinter.messagebox.showinfo(message='IN ORDER TO ADD A NEW USER AN ALREADY IN SYSTEM USER HAS TO LOGIN')

    global main15
    main15 = Tk()

    main15.title("NEW USER")

    main15.geometry("200x130")

    Label(main15, text="USERNAME:").pack()
    global entry3
    entry3 = Entry(main15, width=20)
    entry3.pack()
    Label(main15, text="PASSWORD:").pack()
    global entry4
    entry4 = Entry(main15, show='*', width=20)
    entry4.pack()
    Button(main15, text="ENTER", command=clickEnter2).pack()
    # Button(main2, text="Return", command=).pack()
    close()

def clickEnter2():
    entryUser = entry3.get()
    entryPass = entry4.get()
    senUser = f"SELECT username FROM PUBLIC.\"Admin\" WHERE username = '{str(entryUser)}'"
    senPass = f"SELECT password FROM PUBLIC.\"Admin\" WHERE password = \'" + str(entryPass) + "'"
    cur.execute(senUser)
    r1 = str(cur.fetchall())
    cur.execute(senPass)
    r2 = str(cur.fetchall())

    if entryUser in r1 and entryPass in r2 and entryUser != "" and entryPass != "":
        openLogin2()
        close15()
    else:
        tkinter.messagebox.showerror(title=None, message="ERROR INCORRECT USERNAME OR PASSWORD")



def openLogin2():
    global main16
    main16 = Tk()

    main16.title("NEW USER")

    main16.geometry("200x130")

    Label(main16, text="NEW USERNAME:").pack()
    global entry5
    entry5 = Entry(main16, width=20)
    entry5.pack()
    Label(main16, text="NEW PASSWORD:").pack()
    global entry6
    entry6 = Entry(main16, show='*', width=20)
    entry6.pack()
    Button(main16, text="ENTER", command=clickEnter3).pack()


def clickEnter3():
    getEntry1 = entry5.get()
    getEntry2 = entry6.get()

    s = 'SELECT "Admin"."ID" FROM Public."Admin"'
    cur.execute(s)
    l = cur.fetchall()
    c = 0

    for e in l:
        c += 1

    id = c + 1

    sen = f"INSERT INTO Public.\"Admin\" (\"ID\", \"username\", \"password\") VALUES ({id}, '{getEntry1}', {getEntry2})"

    try:
        cur.execute(sen)
        con.commit()
    except Exception:
        con.rollback()

    if getEntry1 != "" and getEntry2 != "":
        openLogin3()
    else:
        tkinter.messagebox.showerror(title=None, message="ERROR INCORRECT USERNAME OR PASSWORD")



def openLogin3():
    global main17
    main17 = Tk()

    main17.title("LOGIN")

    main17.geometry("200x130")

    Label(main17, text="USERNAME:").pack()
    global entry7
    entry7 = Entry(main17, width=20)
    entry7.pack()
    Label(main17, text="PASSWORD:").pack()
    global entry8
    entry8 = Entry(main17, show='*', width=20)
    entry8.pack()
    Button(main17, text="ENTER", command=clickEnter4).pack()


def clickEnter4():
    entryUser = entry7.get()
    entryPass = entry8.get()
    senUser = f"SELECT username FROM PUBLIC.\"Admin\" WHERE username = '{str(entryUser)}'"
    senPass = f"SELECT password FROM PUBLIC.\"Admin\" WHERE password = \'" + str(entryPass) + "'"
    cur.execute(senUser)
    r1 = str(cur.fetchall())
    cur.execute(senPass)
    r2 = str(cur.fetchall())

    if entryUser in r1 and entryPass in r2 and entryUser != "" and entryPass != "":
        openMenu()
        close16()
    else:
        tkinter.messagebox.showerror(title=None, message="ERROR INCORRECT USERNAME OR PASSWORD")



login = Button(main, text="LOGIN", command=openLogin)
newUser = Button(main, text="NEW USER", command=clickNewUser)
login.place(x=c, y=10)
newUser.place(x=c, y=40)

mainloop()
con.commit()
cur.close()
con.close()
