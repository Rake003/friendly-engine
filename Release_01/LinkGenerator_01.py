# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 13:04:31 2021

@author: Rakesh Kumar
"""
from tkinter import * 

#>>>>>>>>>>>>Variable Declaration

buffer_list=[]
count=0

'''
Add Function :
    Adds data to the buffer_list.
'''
#>>>>>>>>>>>Function Declaration

def add():
    
    Linkk = Link.get()
    Topicc = Topic.get()
    for i in range(0,1):
        temp_list=[]
        temp_list.append(Linkk)
        temp_list.append(Topicc)
        buffer_list.append(temp_list)
    Clear_text()
    #print(len(buffer_list))
    #print(buffer_list)

'''
Clear_text :
    It is used to refresh or delete the content inside the entry box (Link and Topic) when clear button is pressed.
'''

def Clear_text():
    Link_entry.delete(0,'end')
    Topic_entry.delete(0,'end')



#>>>>>>>>>>>>>>File Handling

def save_info():

    #Link_info = Link.get()
    #Topic_info = Topic.get()
    File_name=File.get()
    #print(Link_info,Topic_info)
    
    file = open(File_name+".html","w") #Creating file with .html
    
    #Writing Html format
    
    file.write("<html>")
    file.write("\n")
    file.write("<body>")
    file.write("\n")
    
    #Accessing file data from buffer
    
    for i in buffer_list:
        (temp_link,temp_topic)=i
        Linkerr=('<a href="{}" target="{}">{}</a><br>'.format(temp_link,temp_topic,temp_topic))
        file.write(Linkerr)
        file.write("\n")
    file.write("\n")
    
    file.write("</body>")
    file.write("\n")
    file.write("</html>")
    file.write("\n")

#>>>>>>>>>>>>>>Tkinter 


app = Tk()

app.geometry("500x500")

app.title("Friendly-Engine")

heading = Label(text="Link Generator",fg="black",bg="lightblue",width="500",height="3",font="10")

heading.pack()

#Link,Topic,File_name Entry Lables and Text Boxes
Link_text = Label(text="Link :")
Topic_text = Label(text="Topic :")
File_text=Label(text="File Name :")


Link_text.place(x=15,y=70)
Topic_text.place(x=15,y=140)
File_text.place(x=15,y=210)


Link = StringVar()
Topic = StringVar()
File=StringVar()


Link_entry = Entry(textvariable=Link,width="30")
Topic_entry = Entry(textvariable=Topic,width="30")
File_entry=Entry(textvariable=File,width="30")


Link_entry.place(x=15,y=100)
Topic_entry.place(x=15,y=180)
File_entry.place(x=15,y=250)

#submit button
submit_button = Button(app,text="Submit Data",command=save_info,width="30",height="2",bg="grey")
submit_button.place(x=15,y=290)

#add Button
add_button=Button(app,text="Add",command=add,width="30",height="2",bg="yellow")
add_button.place(x=250,y=290)

#Clear Button    
Clear_Button=Button(app,text="Clear",command=Clear_text,width="30",height="2",bg="lightgreen")
Clear_Button.place(x=250,y=100)




mainloop()