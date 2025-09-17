import tkinter as tk
import json
import pandas as pd
import os
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import requests
from io import BytesIO
from PIL import Image,ImageTk
              #nested dict
Hmarks=[]
Hname=[]
Hsubjects=[]
subject={}
studentlite={}
name=""
semester=""
counter=0
recordss={}
class App:
    def __init__(self):
        try:                        #for refresh window coz add new class or edit class
            if self.window is not None:     #old version has slow startups and flick if back button is press because __init__ is called and rebuild, put if inside try can avoid declaration of window error at back
                try:                        #for try if first line error second line does not execute, but now works because windowinput must open from windowview
                    self.windowView.destroy()
                    self.windowInput.destroy()
                except:
                    pass
                self.student={}
                self.stclass=[]
                os.makedirs("assets",exist_ok=True)    #make folder if exist just pass, use makedirs not mkdir(need to use if os path exists to check manually)
                self.filenameclass="classes.json"
                self.localpath1=os.path.join("assets",self.filenameclass)
                if os.path.exists(self.localpath1):
                    with open(self.localpath1,'r') as f:
                        self.stclass=json.load(f)
                
        except:
            self.student={}
            self.stclass=[]
            os.makedirs("assets",exist_ok=True)    #make folder if exist just pass, use makedirs not mkdir(need to use if os path exists to check manually)
            self.filenameclass="classes.json"
            self.localpath1=os.path.join("assets",self.filenameclass)
            if os.path.exists(self.localpath1):
                with open(self.localpath1,'r') as f:
                    self.stclass=json.load(f)
            self.window=tk.Tk()
            self.screen_w = self.window.winfo_screenwidth()      #get screensize, cross platform gui
            self.screen_h = self.window.winfo_screenheight()
            self.window.geometry(f"700x800+{int(self.screen_w/2)-350}+{int(self.screen_h/2)-440}")
            self.window.title("Student grade manager")
            self.window.configure(background="#ffffff")
            canvas = tk.Canvas(self.window,width=700,height=800,highlightthickness=0,bg="#ffffff")
            # canvas.place(x=0,y=0)
            canvas.grid(row=0, column=0)
            url3="https://ik.imagekit.io/meis8v81a/_Pngtree_fresh%20green%20dot%20style%20flower_4480919.png?updatedAt=1757668521988"        #theme
            # responsemain2=requests.get(url3)              #every time startup need to redownload cause slow startups, change to download at first time user then use local files afterwards
            # img_datamain2= responsemain2.content
            # imgmain2 = Image.open(BytesIO(img_datamain2))
            localpath=self.download(url3,"theme")
            imgmain2=Image.open(localpath)
            imgmain2 = imgmain2.resize((805,920),Image.Resampling.LANCZOS)
            self.textphotomain2=ImageTk.PhotoImage(imgmain2)
            # textphotomain2=tk.Label(self.window,image=self.textphotomain2,background="#ffffff")
            # textphotomain2.place(x=0,y=0)
            canvas.create_image(353,396,image=self.textphotomain2,anchor="center")
            url2="https://ik.imagekit.io/meis8v81a/vecteezy_hand-drawn-rectangle-frame-decoration-element-with-flowers_22186063.png?updatedAt=1757654754838"        #title frame
            # responsemain1=requests.get(url2)
            # img_datamain1= responsemain1.content
            # imgmain1 = Image.open(BytesIO(img_datamain1))
            localpath=self.download(url2,"titleframe")
            imgmain1=Image.open(localpath)
            imgmain1 = imgmain1.resize((670,195),Image.Resampling.LANCZOS)
            self.textphotomain1=ImageTk.PhotoImage(imgmain1)
            # textphotomain1=tk.Label(self.window,image=self.textphotomain1,background="#ffffff")
            # textphotomain1.place(x=10,y=50)
            canvas.create_image(22,50,image=self.textphotomain1,anchor="nw")
            url="https://ik.imagekit.io/meis8v81a/generated_text%20(4).png?updatedAt=1757651849972"         #guidance
            # response=requests.get(url)
            # img_data= response.content
            # img = Image.open(BytesIO(img_data))
            localpath=self.download(url,"guidance")
            img=Image.open(localpath)
            img = img.resize((400,40),Image.Resampling.LANCZOS)
            self.textphoto=ImageTk.PhotoImage(img)
            textphoto=tk.Label(self.window,image=self.textphoto,background="#ffffff")
            textphoto.place(x=105,y=300)
            url1="https://ik.imagekit.io/meis8v81a/generated_text%20(5).png?updatedAt=1757653533445"        #title
            # responsemain=requests.get(url1)
            # img_datamain= responsemain.content
            # imgmain = Image.open(BytesIO(img_datamain))
            localpath=self.download(url1,"title")
            imgmain=Image.open(localpath)
            imgmain = imgmain.resize((604,34),Image.Resampling.LANCZOS)
            self.textphotomain=ImageTk.PhotoImage(imgmain)
            # textphotomain=tk.Label(self.window,image=self.textphotomain,background="#ffffff")
            # textphotomain.place(x=50,y=150)
            canvas.create_image(55,130,image=self.textphotomain,anchor="nw")
            # label=tk.Label(self.window,text="Student Grade Manager", font=("Comic Sans Ms",50))
            # label.place(x=120,y=120)
            url4="https://ik.imagekit.io/meis8v81a/vecteezy_yellow-banner-button_36444073.png?updatedAt=1757670905548"        #button
            # responsebutton2=requests.get(url4)
            # img_databutton2= responsebutton2.content
            # imgmainbutton2 = Image.open(BytesIO(img_databutton2))
            localpath=self.download(url4,"button")
            imgmainbutton2=Image.open(localpath)
            imgmainbutton2 = imgmainbutton2.resize((210,60),Image.Resampling.LANCZOS)
            self.textphotobutton2=ImageTk.PhotoImage(imgmainbutton2)
            button=tk.Button(self.window,text="Add Class",activebackground="white",activeforeground="white",fg="#800020",bg="white",command=self.addclass,
                            font=("Courier New",18,"bold"),image=self.textphotobutton2,compound="center",borderwidth=0,highlightbackground="white")
            button.place(x=105,y=610)
            button2=tk.Button(self.window,text="Rename Class",activebackground="white",activeforeground="white",fg="#800020",bg="white",command=self.rename,
                            font=("Courier New",18,"bold"),image=self.textphotobutton2,compound="center",borderwidth=0,highlightbackground="white")
            button2.place(x=380,y=610)
            self.listboxclass= tk.Listbox(self.window,width=23,height=6, font=("Bookman Old Style",25),justify="center")
            self.listboxclass.place(x=105,y=340)
            self.scrollbarclass=tk.Scrollbar(self.window,orient="vertical",command=self.listboxclass.yview)
            self.scrollbarclass.place(x=569,y=340,width=20,height=255)
            self.listboxclass.config(yscrollcommand=self.scrollbarclass.set)
            if len(self.stclass)==0:
                self.stclass=["Class 1","Class 2","Class 3"]
            for x in self.stclass:
                self.listboxclass.insert("end",x)
            self.listboxclass.bind("<Double-Button-1>",self.view)     #double click to call function
            url5="https://ik.imagekit.io/meis8v81a/vecteezy_rejected-cross-mark-icon-in-flat-style_22062815.png?updatedAt=1757772634617"        #button
            # responsebutton2=requests.get(url4)
            # img_databutton2= responsebutton2.content
            # imgmainbutton2 = Image.open(BytesIO(img_databutton2))
            localpath=self.download(url5,"remove")
            imgmainbuttonremove=Image.open(localpath)
            imgmainbuttonremove= imgmainbuttonremove.resize((25,25),Image.Resampling.LANCZOS)
            self.textphotobuttonremove=ImageTk.PhotoImage(imgmainbuttonremove)
            self.buttonrem=tk.Button(self.window,bg="white",command=self.removeclass,
                                image=self.textphotobuttonremove,borderwidth=0,highlightbackground="white")
            self.listboxclass.bind("<<ListboxSelect>>",self.removebutton)   #use listboxselect not button 1 because button1 need to build selection and() at first click, next click only write index and consider as one button left click
    def removeclass(self):
        response=messagebox.askyesno("Info","Delete class?")
        if response:
            path=os.path.join("assets",self.listboxclass.get(self.listboxclass.curselection()[0])+".json")
            try:
                if os.path.exists(path):
                    os.remove(path)                                         #delete student file of that class
            except:
                pass
            x=int(self.listboxclass.curselection()[0])
            self.stclass.pop(x)                                             #delete class in class list
            self.listboxclass.delete(self.listboxclass.curselection()[0])   #delete listbox, this need to put at las because other line above still use it as index else it will out of range error
            self.databaseclass()        #save

    def removebutton(self,event=None):
        if self.listboxclass.curselection()!=():    
            self.buttonrem.place(x=600,y=350+42*int(self.listboxclass.curselection()[0]))    #405,440
        else:
            self.buttonrem.place_forget()
    def download(self,url,localfilename):
        os.makedirs("assets",exist_ok=True)    #make folder if exist just pass, use makedirs not mkdir(need to use if os path exists to check manually)
        localpath=os.path.join("assets",localfilename)
        if not os.path.exists(localpath):
            r=requests.get(url)
            with open(localpath,"wb") as f:
                f.write(r.content)
        else:
            pass
        return localpath
    def addclass(self):
        self.windowaddclass=tk.Toplevel(self.window)
        self.windowaddclass.geometry("500x300+1000+100")
        self.labelclass=tk.Label(self.windowaddclass,text="Class Name:", font=("Comic Sans Ms",30,"bold"), fg="darkblue")
        self.labelclass.place(x=20,y=30)
        self.entryclass=tk.Entry(self.windowaddclass,width=19,font=("Courier New",30))
        self.entryclass.place(x=20,y=100)
        buttonclass=tk.Button(self.windowaddclass,text="Save",activebackground="black",activeforeground="white",fg="green",bg="lightgrey",command=self.addclassreal,
                        height=2,width=10,font=("Courier New",20,"bold"))
        buttonclass.place(x=170,y=180)
    def rename(self,event=None):     #must put event although not use 
        if self.listboxclass.curselection()!=():        #data is in tuple so if empty it will be () but not "()"
            self.rename=self.listboxclass.curselection()[0]     #index of selection
            self.oldclassname=self.listboxclass.get(self.rename)+".json"    #get old name to search its existing json
            print(self.oldclassname)
            self.newclassname=simpledialog.askstring("Rename","Enter new name:")   #like messagebox but got input, entry lite version
            if self.newclassname not in self.stclass:                       #prevent user rename to same name
                if self.newclassname:
                    self.listboxclass.delete(self.rename)                   #replace name in listbox
                    self.stclass[self.rename]=self.newclassname             #edit real data in list classes but not yet chg existing file name 
                    self.listboxclass.insert(self.rename,self.newclassname)
                    self.databaseclass()     #call func to save, for current flow if user __init__ then rename, student data is empty coz __init__ refresh data and data restore at view but now rename will save to database without restore from view func,so need to separate store class and student data
                    self.oldclasspath=os.path.join("assets",self.oldclassname)
                    self.newclasspath=os.path.join("assets",self.newclassname+".json")
                    if os.path.exists(self.oldclasspath):
                        os.rename(self.oldclasspath,self.newclasspath)   #chg existing file name
                        print("rename success")
                        print(self.newclasspath)
                    else:
                        pass
            else:
                messagebox.showinfo("Info","Class name repeated")
        else:
            messagebox.showinfo("Info","Please select class first")
            return
        
    def addclassreal(self):
        self.stclass.append(self.entryclass.get())
        self.listboxclass.insert("end",self.entryclass.get())
        self.databaseclass()
        self.__init__()
    def addinput(self):
        try:
            self.windowView.destroy()
        except:
            pass
        self.windowInput=tk.Toplevel(self.window,bg="#f0f0f0")
        self.windowInput.title("Student grade manager")
        self.windowInput.geometry(f"700x800+{int(self.screen_w/2)-350}+{int(self.screen_h/2)-440}")
        self.label=tk.Label(self.windowInput,text="Student Name:", font=("Comic Sans Ms",22,"bold"), fg="blue",bg="#f0f0f0")
        self.label.place(x=50,y=110)
        self.entryname=tk.Entry(self.windowInput,width=35,font=("Times New Roman",19))
        self.entryname.place(x=50,y=160)
        self.label2=tk.Label(self.windowInput,text="Student info", font=("Segoe Script",40),background="#f0f0f0")
        self.label2.place(x=190,y=20)
        self.entrysub=tk.Entry(self.windowInput,width=30,font=("Times New Roman",19))
        self.entrysub.place(x=50,y=250)
        self.label3=tk.Label(self.windowInput,text="Subject:", font=("Comic Sans Ms",22,"bold"), fg="blue",background="#f0f0f0")
        self.label3.place(x=50,y=200)
        self.entrymark=tk.Entry(self.windowInput,width=30,font=("Times New Roman",19))
        self.entrymark.place(x=50,y=340)
        self.label4=tk.Label(self.windowInput,text="Marks:", font=("Comic Sans Ms",22,"bold"), fg="blue",background="#f0f0f0")
        self.label4.place(x=50,y=290)
        self.label5=tk.Label(self.windowInput,text="Current grades:", font=("Comic Sans Ms",22,"bold"), fg="orange",background="#f0f0f0")
        self.label5.place(x=50,y=460)
        self.textsem=tk.Text(self.windowInput,wrap="word", font=("Times New Roman",19))
        self.textsem.place(x=500,y=250,width=120,height=32)
        self.textsem.insert("end","Sem 1")              #help user input default
        print(self.textsem.get("1.0",tk.END).strip())
        self.listbox= tk.Listbox(self.windowInput,width=52,height=6, font=("Times New Roman",17))       #declare listbox
        self.listbox.place(x=50,y=510)
        self.scrollbar=tk.Scrollbar(self.windowInput,orient="horizontal",command=self.listbox.xview)
        self.scrollbar.place(x=50,y=675,width=578,height=20)
        self.listbox.config(xscrollcommand=self.scrollbar.set)
        url5="https://ik.imagekit.io/meis8v81a/vecteezy_neumorphic-rectangle-button_11888173.png?updatedAt=1757670905798"        #button
        # responsebutton2=requests.get(url4)
        # img_databutton2= responsebutton2.content
        # imgmainbutton2 = Image.open(BytesIO(img_databutton2))
        localpath=self.download(url5,"button2")
        imgmainbutton3=Image.open(localpath)
        imgmainbutton3 = imgmainbutton3.resize((280,87),Image.Resampling.LANCZOS)
        self.textphotobutton3=ImageTk.PhotoImage(imgmainbutton3)
        self.button3=tk.Button(self.windowInput,text="Add",activebackground="#f0f0f0",activeforeground="gold",fg="#313131",bg="#f0f0f0",command=self.addinputreal,
                    image=self.textphotobutton3,compound="center",borderwidth=0,highlightbackground="#f0f0f0",font=("Courier New",18,"bold"))
        self.button3.place(x=360,y=375)
        self.button6=tk.Button(self.windowInput,text="View data",activebackground="#f0f0f0",activeforeground="gold",fg="#505050",bg="#f0f0f0",command=self.view,
                    image=self.textphotobutton3,compound="center",borderwidth=0,highlightbackground="#f0f0f0",font=("Courier New",18,"bold"))
        self.button6.place(x=50,y=375)
        backbutton2=tk.Button(self.windowInput,image=self.photo,
                               command=self.__init__,
                               borderwidth=0,background="#f0f0f0",highlightbackground="#f0f0f0")
        backbutton2.place(x=30,y=700)
    def addinputreal(self):
        global name,counter,subject,semester,studentlite     #self.textsem.get("1.0",tk.END).strip() is get data from tk.text ,need to specify index and strip()to remove \n of data
        if self.entryname.get()=="" or self.entrysub.get()=="" or self.entrymark.get()=="" or self.textsem.get("1.0",tk.END).strip()=="":     #if user input blank things
            messagebox.showinfo("Info","Insufficient input")
        else:    
            if name != self.entryname.get() or semester!=self.textsem.get("1.0",tk.END).strip():    #name or semester input is diff
                self.listbox.delete(0,"end")
                
                try:    #if new file without any data it will have keyerror
                    if self.entryname.get() in self.student[self.textsem.get("1.0",tk.END).strip()]:    #name input is exist in specific semester that already exist (old name old sem)
                        subject=self.student[self.textsem.get("1.0",tk.END).strip()][self.entryname.get()]      #obtain subject with name, sem
                        studentlite=self.student[self.textsem.get("1.0",tk.END).strip()]    #need to inherit old sem data
                        print("1")
                        if self.entrysub.get() in subject:      #name exist, subject exist and chg mark
                            counter=0
                            for x in subject:       #counter for index of existing subject
                                if x!=self.entrysub.get():
                                    counter+=1
                                else:
                                    break
                        else:
                            counter=len(subject)
                    elif self.textsem.get("1.0",tk.END).strip() not in self.student:    #new name new sem       #for old file that does not raise error to use
                        subject={}
                        studentlite={}
                        counter=0
                        print("newstudent")
                    elif self.textsem.get("1.0",tk.END).strip() in self.student:   #new name old sem
                        subject={}
                        counter=0
                        studentlite=self.student[self.textsem.get("1.0",tk.END).strip()]    #need to inherit old sem data
                        print("newstudent")
                    else:   #old name new sem
                        subject={}
                        counter=0
                        print("newsem")
                except:     #for new file that raise error
                    if self.textsem.get("1.0",tk.END).strip() not in self.student:    #new name new sem
                        subject={}
                        studentlite={}
                        counter=0
                        print("newstudent")
                    
            elif self.entrysub.get() in subject:        #name remain but subject same in old record(not listbox) just chg marks
                counter=0
                for x in subject:
                    if x!=self.entrysub.get():
                        counter+=1
                    else:
                        break 
            name=self.entryname.get()
            subjects=self.entrysub.get()
            mark=self.entrymark.get()
            subject[subjects]=mark    #this is {subject:marks}
            semester=self.textsem.get("1.0",tk.END).strip()
            studentlite[name]=subject.copy()   #this is {student name:{sub:marks}}
            self.student[semester]=studentlite.copy()
            print(studentlite)
            self.item=list(subject.items())     #dict cannot access with INDEX
            if subjects in subject:     #if existing duplicate subject in listbox, delete it
                try:
                    lists=self.listbox.get(0,"end")
                    print(lists)
                    ind=[x for x,y in enumerate(lists) if subjects in y]       #list comprehension-for loop in single line, enumerate is giving index numbers to list, if keyword in list
                    self.listbox.delete(ind)
                except:
                    pass
            if subject:
                print(self.item[counter])
                print(self.textsem.get("1.0",tk.END).strip())
                print(self.student[semester])
                self.listbox.delete(0,3)    #not using .delete(0) .delete(1) .delete(2) because delete first line then existing second line become first line so .delete(1) fail
                self.listbox.insert("end",self.item[counter])
                self.listbox.insert("0","--------Changes added--------")
                self.listbox.insert("0",self.item)
                self.listbox.insert("0",self.entryname.get())
                self.listbox.insert("0",self.textsem.get("1.0",tk.END).strip())
                self.entrysub.delete(0,"end")
                self.entrymark.delete(0,"end")
                counter+=1
            self.databasestudent()

    def databasestudent(self):
        try:
            with open(self.localpath2,"w") as f:
                json.dump(self.student,f,indent=4)
        except:
            pass
    def databaseclass(self):
        try:
            with open(self.localpath1,"w") as f:
                json.dump(self.stclass,f,indent=4)
        except:
            pass
    def view(self,event=None):
        url="https://ik.imagekit.io/meis8v81a/1410611-200.png?updatedAt=1757601021751"
        # response=requests.get(url)
        # img_data= response.content
        # img = Image.open(BytesIO(img_data))
        localpath=self.download(url,"backbutton")
        img=Image.open(localpath)
        img = img.resize((100,100),Image.Resampling.LANCZOS)
        self.photo=ImageTk.PhotoImage(img)
        try:
            self.windowInput.destroy()
        except:
            pass
        try:
            self.classnameindex=self.listboxclass.curselection()
        except:
            pass
        if self.classnameindex:     #after select class, index is obtained, now start to read file or create new student file if none
            self.classname=self.listboxclass.get(self.classnameindex)
            self.filename=f"{self.classname}.json"
            self.localpath2=os.path.join("assets",self.filename)
            if os.path.exists(self.localpath2):
                with open(self.localpath2,"r") as f:
                    self.student=json.load(f)
        style=ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading",font=("Georgia",15,"bold"),foreground="grey",
                        relief="sunken")
        style.configure("Treeview",font=("Century Gothic",15),
                        foreground="darkblue",
                        background="lightblue",
                        rowheight=30,
                        fieldbackground="white",
                        relief="raised"
                        )
        
        columns=["Semester"]+["Name"]+["subject"]+["marks"]              #let treeview split column
        self.windowView=tk.Toplevel(self.window,bg="white")
        self.windowView.geometry(f"700x800+{int(self.screen_w/2)-350}+{int(self.screen_h/2)-440}")
        url6="https://ik.imagekit.io/meis8v81a/vecteezy_a-green-empty-button_54655112.png?updatedAt=1757759366415"        #button
        # responsebutton2=requests.get(url4)
        # img_databutton2= responsebutton2.content
        # imgmainbutton2 = Image.open(BytesIO(img_databutton2))
        localpath=self.download(url6,"button3")
        imgmainbutton4=Image.open(localpath)
        imgmainbutton4 = imgmainbutton4.resize((173,225),Image.Resampling.LANCZOS)
        self.textphotobutton4=ImageTk.PhotoImage(imgmainbutton4)
        self.button4=tk.Button(self.windowView,text="Remove row",activebackground="white",  #make button delete row but just delete treeview only not real data
                               activeforeground="white",fg="#001F3F",bg="white",
                               command=self.deletesel,
                               image=self.textphotobutton4,compound="center",borderwidth=0,highlightbackground="#ffffff",font=("Courier New",15,"bold"))
        imgmainbutton5 = imgmainbutton4.resize((285,225),Image.Resampling.LANCZOS)
        self.textphotobutton5=ImageTk.PhotoImage(imgmainbutton5)
        self.button5=tk.Button(self.windowView,text="Add/Edit Student Info",activebackground="white",  #make button edit or add student
                               activeforeground="white",fg="#001F3F",bg="white",
                               command=self.addinput,
                               image=self.textphotobutton5,compound="center",borderwidth=0,highlightbackground="#ffffff",font=("Courier New",15,"bold"))
        self.button7=tk.Button(self.windowView,text="Analyse info",activebackground="white",  #make button analyse data
                               activeforeground="black",fg="#660000",bg="lightgreen",borderwidth=0,highlightbackground="white",
                               command=self.analyse,
                               height=2,width=13,font=("Courier New",15,"bold"))
        backbutton=tk.Button(self.windowView,image=self.photo,
                               command=self.__init__,
                               borderwidth=0,background="white",highlightbackground="white")
        backbutton.place(x=30,y=675)
        url8="https://ik.imagekit.io/meis8v81a/vecteezy_microsoft-excel-mobile-apps-logo_17396806.png?updatedAt=1757930788963"        #button
        # responsebutton2=requests.get(url4)
        # img_databutton2= responsebutton2.content
        # imgmainbutton2 = Image.open(BytesIO(img_databutton2))
        localpath=self.download(url8,"button8")
        imgmainbutton8=Image.open(localpath)
        imgmainbutton8 = imgmainbutton8.resize((54,54),Image.Resampling.LANCZOS)
        self.excel=ImageTk.PhotoImage(imgmainbutton8)
        excelbutton=tk.Button(self.windowView,image=self.excel,text="Export to Excel",activebackground="light grey",
                               activeforeground="white",fg="#660000",
                               command=self.convexcel,
                               borderwidth=0,bg="lightgreen",highlightbackground="white",compound="left",font=("Courier New",17,"bold"))
        self.button4.place(x=147,y=575)
        self.button5.place(x=350,y=575)
        self.button7.place(x=155,y=720)
        excelbutton.place(x=360,y=720)
        self.tree=ttk.Treeview(self.windowView,columns=columns,show="headings")     #table like structure for viewing
        self.tree.place(x=0,y=0,width=700,height=650)     
        self.tree.tag_configure("oddperson",background="lightblue")
        self.tree.tag_configure("evenperson",background="lightgreen")   
        self.tree.heading(columns[0],text="Semester")     #setting first column
        self.tree.heading(columns[1],text="Name")     #setting first column
        self.tree.heading(columns[2],text="Subject")     
        self.tree.heading(columns[3],text="Marks")   
        self.tree.column(columns[0],width=170)     #center align the numbers
        self.tree.column(columns[1],width=170)     #center align the numbers
        self.tree.column(columns[2],width=170)     #center align the numbers  
        self.tree.column(columns[3],anchor="center",width=170)     #center align the numbers
        self.scrollbarview=tk.Scrollbar(self.windowView,orient="vertical",command=self.tree.yview)
        self.scrollbarview.place(x=680,y=0,width=20,height=649)
        self.tree.config(yscrollcommand=self.scrollbarview.set)
        self.sub=[]
        c=1     #change colour per person
        self.sortedstudentcomplete={}
        for a,b in self.student.items():
            self.sortedstudent={}       #sort subject each person so subject in table is in order, put here to refresh dict data and assignment,else data will be repeating
            for x,y in b.items():    #sort subject each person so subject in table is in order
                self.sortedsubject=dict(sorted(y.items()))
                self.sortedstudent[x]=self.sortedsubject
                self.sortedstudentcomplete[a]=self.sortedstudent
        for a,b in self.sortedstudentcomplete.items():
            e=""
            for x,y in b.items():
                d=""
                c+=1
                for z,n in y.items():   
                    if c%2!=0:      #change colour per person
                        if d!=x:                            #make repeated name appear only once
                            if e!=a:
                                self.tree.insert("","end",values=(a,x,z,n),tags="oddperson")
                                e=a
                            else:
                                self.tree.insert("","end",values=("",x,z,n),tags="oddperson")
                            d=x
                        else:
                            if e!=a:
                                self.tree.insert("","end",values=(a,"",z,n),tags="oddperson")
                                e=a
                            else:
                                self.tree.insert("","end",values=("","",z,n),tags="oddperson")
                    else:
                        if d!=x:                            #make repeated name appear only once
                            if e!=a:
                                self.tree.insert("","end",values=(a,x,z,n),tags="evenperson")
                                e=a
                            else:
                                self.tree.insert("","end",values=("",x,z,n),tags="evenperson")
                            d=x
                        else:
                            if e!=a:
                                self.tree.insert("","end",values=(a,"",z,n),tags="evenperson")
                                e=a
                            else:
                                self.tree.insert("","end",values=("","",z,n),tags="evenperson")
    def convexcel(self):
        with pd.ExcelWriter("grades.xlsx") as writer:
            for x,y in self.student.items():
                df=pd.DataFrame(y).T
                df.to_excel(writer,sheet_name=x)
    def deletesel(self):        #select row delete in treeview and data in dict
        select=self.tree.selection()
        if len(select)==1:      #only select one, multiple i dunno yet
            for x in select:
                data=self.tree.item(x)      #all info about that row but we dont use it
                data1=self.tree.item(x,"values")    #only value
                selectprev=int(x[1:],16)    #because semester,name only appear at first row of each student so we cant delete real data without semester,name
                selectprevb=str(x[0])       
                print(data)
                print(f"Deleted {data1}")
                print(x)
                if data1[0]=="":                #if selected row does not have semester
                    data1b=data1[2]             #variable to inherit selected row subject
                    z=0
                    data1a=""
                    if data1[1]!="" and z==0:       #if selected have name without looking upwards
                            data1a=data1[1]
                            z=1
                    while data1[0]=="":         #so we search semester,name from above row and keep looping until first row of each subject
                        selectprev-=1
                        selectprevc=selectprevb+f"{selectprev:03X}"     #selection give 4 digit prefix with number 16bit so need to split and combine
                        for x in (selectprevc,):
                            print((selectprevc,))
                            data1=self.tree.item(x,"values")
                            print(data1[0])
                            print(data1b)
                        if data1[1]!="" and z==0:       #while looping upwards if found first name then lock it
                            data1a=data1[1]
                            print(data1[1])
                            z=1
                    del self.student[data1[0]][data1a][data1b]  #data1[0] is semester,data1a is name,data1b is subject
                else:
                    del self.student[data1[0]][data1[1]][data1[2]]
                self.tree.delete(x)
            self.databasestudent()
            self.windowView.destroy()   #important so old window can destroy
            self.view()     #refresh window so name will reappear at top of each student to prevent first row selected and name does not reappear
        else:
            messagebox.showinfo("Info","Please select one row")
        
    def analyse(self):
        try:
            self.windowAnalyse.destroy()
        except:
            pass
        self.windowAnalyse=tk.Toplevel(self.window,bg="blue")
        self.windowAnalyse.geometry("600x500+1100+100")
        self.textAnalyse=tk.Text(self.windowAnalyse,wrap="word", font=("Times New Roman",20), fg="black",background="lightgreen")
        self.textAnalyse.place(x=0,y=0,width=600,height=500)
        self.scrollbartext=tk.Scrollbar(self.windowAnalyse,orient="vertical",command=self.textAnalyse.yview)
        self.scrollbartext.place(x=580,y=0,width=20,height=500)
        self.textAnalyse.config(yscrollcommand=self.scrollbartext.set)
        self.textAnalyse.insert("end","Analyse Report")
        for a,b in self.student.items():
            for x,y in b.items():         #x y is keys,value 
                mark=-1
                lmark=100
                for z,n in y.items():           #z n is keys,value
                    if int(n)>int(mark):
                        subjects=z
                        mark=n
                    if int(n)<int(lmark):
                        lsubjects=z
                        lmark=n
                name=x
                print(f"\nHighest marks for {name} is {mark} in {subjects}\n")     #only can put here coz marks will be refresh by next student unless new dict for max marks
                self.textAnalyse.insert("end","\n"+f"Highest marks for {name} is {mark} in {subjects} at {a}")
                self.textAnalyse.insert("end","\n"+f"Lowest marks for {name} is {lmark} in {lsubjects} at {a}")
        for a,b in self.student.items():
            for x,y in b.items():
                for z,n in y.items():
                    recordss.setdefault(z,{})[x]=n
        print(recordss)
        print("\n")
        self.textAnalyse.insert("end","\n")
        for x,y in recordss.items():         #x y is keys,value
            marksss=-1
            lmarksss=100
            names="" 
            lnames=""
            for z,n in y.items():           #z n is keys,value
                if int(n)>int(marksss):
                    names=z
                    marksss=n
                if int(n)<int(lmarksss):
                    lnames=z
                    lmarksss=n
            print(f"Highest marks for {x} is {marksss} by {names}")
            self.textAnalyse.insert("end","\n"+f"Highest marks for {x} is {marksss} by {names} at {a}")
            self.textAnalyse.insert("end","\n"+f"Lowest marks for {x} is {lmarksss} by {lnames} at {a}")
        self.textAnalyse.config(state="disabled")
if __name__=="__main__":
    app=App()
    app.window.mainloop()


# while True:
#     name=""
#     name=input("Enter student name (if no enter 'done'): ")
#     if name=='done':
#         break
#     else:
#         subject={}          #put here to refresh each students for for same course because dict cannot have duplicates so mark will be latest person if put at back
#         while True:
#             a=""
#             a=input(f"Any subjects for {name}(if no enter 'done')? ")
#             if a=='done':
#                 break
#             else:
#                 mark=float(input(f"Enter marks for {a}:"))
#                 subject[a]=mark    
#                 student[name]=subject

#                 markss=list(subject.values())       #to record highest marks
#                 for x,y in student.items():         #x y is keys,value 
#                     for z,n in y.items():           #z n is keys,value
#                         if n==max(markss):
#                             subjects=z
#         # print(f"\nHighest marks for {name} is {max(markss)} in {subjects}\n")     #only can put here coz marks will be refresh by next student unless new dict for max marks
#         Hmarks.append(max(markss))
#         Hname.append(name)
#         Hsubjects.append(subjects)
        
        

# print(f"\n{student}")

# records={}
# recordss={}
# for x, y in student.items():
#     for sub,value in y.items():
#         # if sub not in recordss:           #for loop long version algorithm
#         #     recordss[sub]={}              #need to declare a inner loop first
#         # recordss[sub][x]=value
#         recordss.setdefault(sub,{})[x]=value
# print(recordss)

# print("\n")
# i=0
# while i<len(Hmarks):
#     print(f'Highest marks for {Hname[i]} is {Hmarks[i]} in {Hsubjects[i]}')
#     i+=1

# print("\n")
# # for x,y in recordss.items():         #x y is keys,value       same function as below but diff style
# #     marksss=[] 
# #     for z,n in y.items():           #z n is keys,value
# #         marksss.append(n)
# #         for z,n in y.items():
# #             if n==max(marksss):
# #                 names=z
# #     print(f"Highest marks for {x} is {max(marksss)} by {names}")


# for x,y in recordss.items():         #x y is keys,value
#     marksss=-1
#     names="" 
#     for z,n in y.items():           #z n is keys,value
#         if n>marksss:
#             names=z
#             marksss=n
#     print(f"Highest marks for {x} is {marksss} by {names}")
