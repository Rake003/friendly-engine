# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 22:05:47 2021

@author: Rakesh Kumar


Libraries Used:
   # TKinter 
"""

from tkinter import * 



#>>>>>>>>>>>>>>File Handling

def save_info():
    
    Link_info = Link.get()
    Topic_info = Topic.get()
    File_name=File.get()
    Linker=('<a href="{}" target="{}">{}<br></a>'.format(Link_info,Topic_info,Topic_info))
    
    
    print(Link_info,Topic_info)
    
    file = open(File_name+".html","w")
    file.write("<html>")
    file.write("<body>")
    file.write(Linker)
    
    file.write("</body>")
    file.write("</html>")
    '''
    file.write("Your First Name " + firstname_info)
    
    file.write("\n")
    
    file.write("Your Last Name " + lastname_info)
    
    file.write("\n")
    
    file.write("Your Age " + str(age_info))
    
    file.close()
    
    '''
    
'''    <html>
<body>

<a href="https://www.youtube.com/watch?v=XAwZwj5H9RE" target="_blank">Youtube<br></a>
</body>
</html>  '''



#>>>>>>>>>>>>>Tkinter 

app = Tk()

app.geometry("500x500")

app.title("Friendly-Engine")

heading = Label(text="Link Generator",fg="black",bg="lightblue",width="500",height="3",font="10")

heading.pack()

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

button = Button(app,text="Submit Data",command=save_info,width="30",height="2",bg="grey")

button.place(x=15,y=290)


mainloop()