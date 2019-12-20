#!/bin/env python
# -*- coding: UTF-8 -*-
#
# Hobin Liang 08/20/2019
#

import os, sys, Tkinter
from Tkinter import *
import tkFileDialog, tkMessageBox
reload(sys)
sys.setdefaultencoding('utf-8')

app = Tkinter.Tk()
src_path = StringVar()
dst_path = StringVar()
exclude_files = StringVar()
exclude_files.set("Temp;")
widget_console = Text(app)
widget_show_text = StringVar()

# test - default
# src_path.set("D:/source/client/best2/trunk/20190701_best2_client")
# dst_path.set("D:/source/client/cbev3")

def askdirectory_src():
    dirname = tkFileDialog.askdirectory()
    src_path.set(dirname)
    return dirname

def askdirectory_dst():
    dirname = tkFileDialog.askdirectory()
    dst_path.set(dirname)
    return dirname

def set_widget_console_text(text):
    widget_console.config(state = NORMAL)
    widget_console.delete(1.0, 'end')
    widget_console.insert('insert', text)
    widget_console.see('end')
    widget_console.config(state = DISABLED)

def do_mklink():
    exclude = {}
    src = src_path.get().encode('utf-8')
    dst = dst_path.get().encode('utf-8')
    for file in exclude_files.get().split(";"):
        file = file.strip()
        if len(file) > 0:
            exclude[file] = True
    if len(src) == 0:
        tkMessageBox.showerror("ERROR", "Please select the Source Folder.")
        return False
    if not os.path.isdir(src):
        tkMessageBox.showerror("ERROR", "Source Folder not exists: " + src)
        return False
    if len(dst) == 0:
        tkMessageBox.showerror("ERROR", "Please select the New Folder.")
        return False
    if not os.path.isdir(dst):
        tkMessageBox.showerror("ERROR", "New Folder not exists: " + dst)
        return False
    if src == dst:
        tkMessageBox.showerror("ERROR", "They are the same folder: " + src)
        return False

    log_temp = ''
    for file in os.listdir(src):
        src_full = src + "/" + file
        dst_full = dst + "/" + file
        log_file = file.decode('gb2312').encode('utf-8')
        if exclude.has_key(file):
            print("Exclude file: " + file)
            log_temp = log_temp + "Exclude file: " + log_file + "\n"
        elif os.path.exists(dst_full):
            print("File exists: " + file)
            log_temp = log_temp + "File exists: " + log_file + "\n"
        else:
            opt = os.path.isdir(src_full) and " /j" or ""
            cmd = "mklink" + opt + " \"" + dst_full + "\" \"" + src_full + "\""
            print(cmd)
            res = os.system(cmd)
            log_temp = log_temp + "Make link: " + log_file + " ... " + (0 == res and 'OK' or 'failed') + "\n"
    log_temp = log_temp + '\nLinking completed.\n' + "Source Folder: " + src + "\nNew Folder: " + dst
    set_widget_console_text(log_temp)
    tkMessageBox.showinfo("MAKE LINK SUCCESS", "Source Folder: " + src + "\nNew Folder: " + dst)
    return True

# title
app.title("FOLDER LINKING")

# source project
Label(app, text = 'Source Folder:').grid(row = 0, column = 0, sticky = E, padx = 5, pady = 5)
Entry(app, textvariable = src_path, width = 50).grid(row = 0, column = 1, padx = 0, pady = 5)
Button(app, text= ' SELECT ', command = askdirectory_src).grid(row = 0, column = 2, padx = 5, pady = 5)

# new project
Label(app, text = 'New Folder:').grid(row = 1, column = 0, sticky = E, padx = 5, pady = 5)
Entry(app, textvariable = dst_path, width = 50).grid(row = 1, column = 1, padx = 0, pady = 5)
Button(app, text= ' SELECT ', command = askdirectory_dst).grid(row = 1, column = 2, padx = 5, pady = 5)

# exclude
Label(app, text = 'Exclude Files:').grid(row = 2, column = 0, sticky = E, padx = 5, pady = 5)
Entry(app, textvariable = exclude_files, width = 50).grid(row = 2, column = 1, padx = 0, pady = 5)

# copy button
Button(app, text=' MAKE LINK ', command = do_mklink).grid(row = 3, column = 0, columnspan = 3, padx = 0, pady = 10)

# console
widget_console.config(width = 73, height = 15, fg = "#00FF00", bg = "#000000", state = DISABLED)

# show console
widget_show_text.set('SHOW CONSOLE')
widget_console_visible = False
def do_show_console(event):
    global widget_console_visible
    if widget_console_visible:
        widget_show_text.set('SHOW CONSOLE')
        widget_console.grid_forget()
    else:
        widget_show_text.set('HIDE CONSOLE')
        widget_console.grid(row = 5, column = 0, sticky = W, columnspan = 3, padx = 5, pady = 5)
    widget_console_visible = not widget_console_visible
widget_show = Label(app, textvariable = widget_show_text)
widget_show.grid(row = 4, column = 0, sticky = W, columnspan = 3, padx = 5, pady = 0)
widget_show.bind('<Button-1>', do_show_console)

app.mainloop()