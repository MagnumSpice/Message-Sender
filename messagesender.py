import smtplib
from tkinter import *

bg = '#30ACB2'
fg = '#003E71'

sender = 'Enter Email'
password = 'Enter password'

def send_mail(receiver,message):
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(sender,password)
    s.sendmail(sender,receiver,message)
    s.quit()
root = Tk()
root.title = 'Message Sender'
root.geometry('600x300')
root.configure(bg=bg)


Label(root,text="Email Sender",font=('Times New Roman',30),fg=fg,bg=bg).place(x=190,y=10)
Label(root,text="Send to:",font=('Times New Roman',20),fg=fg,bg=bg).place(x=0,y=70)
Label(root,text="Message:",font=('Times New Roman',18),fg=fg,bg=bg).place(x=0,y=110)

rec_name = Entry(root,font=("",17),width = 30)
rec_name.place(x=120,y=70)
msg = Text(root,height = 5, width = 30,font =("",17))
msg.place(x=120,y=110)
Button(root,text=" SEND ",font =("Times New Roman",10),fg=fg,command=lambda : 
    send_mail(rec_name.get(),msg.get("1.0",END))).place(x=280,y=265
    )
root.mainloop()