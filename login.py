from tkinter import *
import os

creds = 'tempfile.temp'

def Signup():
    global pwordE
    global nameE
    global roots
    
    roots = Tk()
    roots.title('signup')
    instruction = Label(roots,text='please enter your credentials\n')
    instruction.grid(row=0,column=0,sticky=E)
    
    nameL =Label(roots,text='New Username: ')
    pwordL = Label(roots,text='New Password: ')
    nameL.grid(row=1,column=0,sticky=W)
    pwordL.grid(row=2,column=0,sticky=W)
    
    nameE=Entry(roots)
    pwordE=Entry(roots,show='*')
    nameE.grid(row=1,column=1)
    pwordE.grid(row=2,column=1)
    signupButton=Button(roots,text='Signup',command=FSSignup)
    signupButton.grid(columnspan=2,sticky=W)
    roots.mainloop()
    
def FSSignup():
    with open(creds,'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()    
    roots.destroy()
    
def Login():
    
    global nameEL
    global pwordEL
    global rootA
    
    rootA =Tk()
    rootA.title('Login')
    
    instruction = Label(rootA,text='Please login: ')
    instruction.grid(row=0,sticky=E)
    
    nameL =Label(rootA,text='Username: ')
    pwordL =Label(rootA,text='Passwrod: ')
    nameL.grid(row=1,column=0,sticky=W)
    pwordL.grid(row=2,column=0,sticky=W)
    
    nameEL=Entry(rootA)
    pwordEL=Entry(rootA,show='*')
    nameEL.grid(row=1,column=1)
    pwordEL.grid(row=2,column=1)
    
    loginB=Button(rootA,text='Login',command=Checklogin)
    loginB.grid(row=3,column=0,sticky=W)

    rmuser=Button(rootA,text='Delete user',fg='red',command=DelUser)
    rmuser.grid(row=3,column=1,sticky=W)

    SignupB=Button(rootA,text='Signup',command=Signup)
    SignupB.grid(row=3,column=2,sticky=W)

    rootA.mainloop()
    
def Checklogin():
    if os.path.isfile(creds):
        with open(creds) as f:
            data =f.readlines()
            uname=data[0].rstrip()
            pword=data[1].rstrip()
            
        if nameEL.get() ==uname and pwordEL.get() ==pword:
            r =Tk()
            r.title(':D')
            r.geometry('150x150')
            textappear=Label(r,text='Logged In')
            textappear.grid(row=0,column=0)
            r.mainloop()
            
        else:
            r =Tk()
            r.title(':D')
            r.geometry('150x150')
            textappear=Label(r,text='Login fail')
            textappear.grid(row=0,column=0)
            r.mainloop()
    else:
        r=Tk()
        r.title('Error')
        r.geometry('150x100')
        textappear=Label(r,text='No Previous User Exists')
        textappear.grid(row=0,column=0)
        r.mainloop()
            
       
def DelUser():
    if os.path.isfile(creds):
        os.remove(creds)
    
Login()
