
#Website Blocker using tkinter

from tkinter import *
import time
from datetime import datetime as dt
from tkinter import messagebox
from tkinter import Tk, Canvas, Frame, BOTH

#initialize window
window=Tk()
#to prevent change in size
window.resizable(0,0)
window.title("Website Blocker")
window.geometry("570x345")

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

window.configure(bg=_from_rgb((255, 236, 212)))
Label(window, text = 'Website Blocker',bg=_from_rgb((255, 236, 212)),fg='black', font = 'arial 30').pack()


#temporary host
host_temp = "/private/etc/hosts"
#Path to the host file
hosts_path = "/private/etc/hosts"
# localhost IP- ip at which file redirected to nothing
redirect = "127.0.0.1"


Label(window,bg=_from_rgb((255, 236, 212)),fg='black', text= 'Enter Website :', font = 'arial 13 ').place(x=100,y=80)
Websites = Text(window,bg='white',fg='black', font = 'arial 13',height ='1', width = '30', wrap = WORD)
Websites.place(x = 230, y =80)
temp = Websites

Label(window,bg=_from_rgb((255, 236, 212)),fg='black', text= 'Start Time of Work (24H) :', font = 'arial 13 ').place(x=37,y=140)
Websites = Text(window,bg='white',fg='black', font = 'arial 13', height ='1', width = '15', wrap = WORD)
Websites.place(x = 230, y =140)
temp1 = Websites

Label(window,bg=_from_rgb((255, 236, 212)),fg='black', text= 'End Time of Work (24H) :', font = 'arial 13 ').place(x=42,y=200)
Websites = Text(window,bg='white',fg='black', font = 'arial 13', height ='1', width = '15', wrap = WORD)
Websites.place(x = 230, y =200)
temp2 = Websites


#for vertical line
canvas=Canvas(window,bg='black',width=1,height=150,bd=0,highlightthickness=0)
canvas.place(x=210,y=80)


l=list()
l1=list()

#Button Functions
def Blocker():
    website_list = temp.get(1.0,'end-1c')
    website_list = list(website_list.split(","))
    if len(website_list[0]) != 0:
        for i in website_list:
            l.append('www.'+str(i))
        l.extend(website_list)
        n=temp1.get(1.0,'end-1c')
        m=temp2.get(1.0,'end-1c')

        if n=='':n=0
        else: n=int(n)
        if m=='':n=0
        else: m=int(m)
        print(n,m)
        # print(website_list)
        count=0

        if dt(dt.now().year, dt.now().month, dt.now().day,n)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,m):
            print("Work hour")
            with open(host_temp, 'r+') as file:
                content = file.read()
                print(website_list)
                for website in l:
                    if website in content:
                        # Label(window, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=400)
                        count=1
                        # messagebox.showinfo("showinfo", "Already Blocked")
                        print(content)
                        pass
                    else:
                        # mapping hostnames to your localhost IP address
                        # Label(window, text = "Blocked", font = 'arial 12 bold').place(x=200,y =500)
                        count=2
                        # messagebox.showwarning("showwarning", "Blocked")
                        file.write(redirect + " " + website + "\n")

            if count==1:
                messagebox.showinfo("showinfo", "Already Blocked")
            elif count==2:
                messagebox.showinfo("showinfo", "Blocked")


        else:
            messagebox.showerror("showerror", "Incorrect Values Entered")
    else:
        messagebox.showerror("showerror", "No Website Entered")


def unBlocker():
    website_list = temp.get(1.0,'end-1c')
    website_list = list(website_list.split(","))
    if len(website_list[0]) != 0:
        for i in website_list:
            l1.append('www.'+str(i))
        l1.extend(website_list)
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in l1):
                    file.write(line)
            file.truncate()
            # Label(window, text = 'Free time' , font = 'arial 12 bold').place(x=200,y=600)
            messagebox.showerror("showerror", "Un-Blocked")
        print("Un-Blocked")
    else:
        messagebox.showerror("showerror", "No Website Entered")

def unBlockerAll():
    with open(hosts_path, 'r+') as file:
        content=file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in l):
                file.write(line)
        file.truncate()
        # Label(window, text = 'Free time' , font = 'arial 12 bold').place(x=200,y=600)
        messagebox.showerror("showerror", "Un-Blocked All")
    print("Un-Blocked all")



#f55d5d
block_btn = Button(window, text = 'Block' , font = 'arial 15', command = Blocker, height=2, width=10, activeforeground='#f55d5d')
block_btn.place(x = 70, y =260)
unblock_btn = Button(window, text = 'Un-Block' , font = 'arial 15', command = unBlocker, height=2, width=10, activeforeground='#aaffaa')
unblock_btn.place(x = 240, y =260)
unblockall_btn = Button(window, text = 'Un-Block All' , font = 'arial 15', command = unBlockerAll, height=2, width=10, activeforeground='#aaffaa')
unblockall_btn.place(x = 400, y =260)

window.mainloop()
