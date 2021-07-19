# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 22:05:47 2021

@author: Rakesh Kumar


Libraries Used:
   # TKinter 
"""

from tkinter import * 

#>>>>>>>>>>>>>For Adding(List Creation)

buffer_list=[]


'''
Add Function

Creating a list of list which can save Link.get() and Topic.get()

Add should contain:
    Link and Topic should refresh
    File Name Gui should hide <Hide function is executed here>
    Last added link and topic name should be shown with a option to delete(optionally): <confirm_Safety function is executed here>
        If pressed another function called Delete should get proceed further

'''

'''
Reference for list creation:  
    
    outside_list=[]
    for i in range(0,5):
        inside_list=[]
        inside_list.append(i)
        inside_list.append(i+1)
        outside_list.append(inside_list)

       #you can access any inside_list from the outside_list and append     
        outside_list[1].append(100)
        print(outside_list)  '''

def add(Linkk,Topicc):
    
    for i in range(0,1):
        temp_list=[]
        temp_list.append(Linkk)
        temp_list.append(Topicc)
        buffer_list.append(temp_list)
    pass



'''
hide

This function is a static function which has a constant duty of hiding the Title GUI if Add is pressed
Can set a flag to enable and disable

'''

def hide():
    pass



'''
confirm_Safety Function

Creation of New GUI which shows previous Title, Topic values with a button named 'delete--->delete()-->is called' 
The values are dynamic and taken from buffer_list accessed via index (may be..!)

'''
def confirm_Safety():
    pass



'''
Delete Function

This function is accompanied with confirm_Safety function . If Delete button is pressed,
Now the corresponding List and Topic is deleted from the buffer list (buy deleting the corresponding index value)
And call the confirm_Safety function with the previous Topic and Link value

'''
def delete():
    pass







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
Reference:
        
    file.write("Your First Name " + firstname_info)
    
    file.write("\n")
    
    file.write("Your Last Name " + lastname_info)
    
    file.write("\n")
    
    file.write("Your Age " + str(age_info))
    
    file.close()
    
    '''
    
''' 
Trials:
<html>
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