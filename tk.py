import tkinter
from tkinter import messagebox
# Create a  window first 

window=tkinter.Tk()

# We use geometry to fix the size of winow 
window.geometry('600x600')
window.title('DON BOSCO SCHOOL')
label=tkinter.Label(window,text='This is my first tkinter window').pack()

#command is used to do the working in the backend
#for this we have to create a function for it's working first 

def myFunction():
     msg=messagebox.askquestion('Close Application','Are you sure you want to close the Application', icon='warning')
     print(msg)


# now if we want to close the window then we have to use Destory method 
     
     if msg=='yes':
       msg=window.destroy()
     else:
         msg=messagebox.showinfo('Return','You will now return to the application screen')

 # Now we can use Button , Button is already declared in Tkinter 
button=tkinter.Button(window,text=' Close the application', command=myFunction).pack()# Here we can use bg ( background) and fg(foreground)
#Always use the mainloop in the end of the program
window.mainloop()