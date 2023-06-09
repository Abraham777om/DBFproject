import psycopg2
from fpdf import FPDF
# import tkinter as tk
# from tkinter import ttk
#


def createText(sen, name, elements):
    con = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='AlwaysInShape')
    cur = con.cursor()
    c = 0

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

    for e in list:
        print(e[1:])

    list2 = []
    for e in list:
        if c == 0:
            e = " " + e
            list2.append(e)
            c += 1
        if c > 0:
            e = (e[1:])
            list2.append(e)

    try:
        file = open(name, 'w', encoding='utf-8')
        file.write(elements +  "\n")
        file.write(" \n")
        for e in list2:
            file.write(e + "\n")
    except Exception as e:
        print(e)
    finally:
        file.close()



    con.commit()
    cur.close()
    con.close()


