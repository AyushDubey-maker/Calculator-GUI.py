from tkinter import *
import math
root=Tk()

root.title('Calculator')

input=Entry(root,width=35,borderwidth=5)

input.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#Function for button input
def button_add(number):
    #input.delete(0,END)
    current=str(input.get())
    input.delete(0,END)
    input.insert(0,current+str(number))

def button_clear():
    input.delete(0,END)

def button_carryaddition():
    first_num=input.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_num)
    input.delete(0,END)

def button_show_result():
    second_number=input.get()
    input.delete(0,END)
    sqaure_root_no= f_num**(1/2)
    if math=='addition':
        input.insert(0,f_num+int(second_number))
    if math=='subtraction':
        input.insert(0,f_num-int(second_number))
    if math=='multiply':
        input.insert(0,f_num*int(second_number))
    if math=='division':
        input.insert(0,f_num/int(second_number))
    if math=='square-root':
        input.insert(0,(sqaure_root_no))
    if math=='square':
        input.insert(0,f_num*f_num)
    
   
def button_do_subtraction():
    first_num=input.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_num)
    input.delete(0,END)

def button_do_multiply():
    first_num=input.get()
    global f_num
    global math
    math="multiply"
    f_num=int(first_num)
    input.delete(0,END)

def button_do_division():
    first_num=input.get()
    global f_num
    global math
    math="division"
    f_num=int(first_num)
    input.delete(0,END) 

def button_do_square_root():
    first_num=input.get()
    global f_num
    global math
    math="square-root"
    f_num=int(first_num)
    input.delete(0,END) 

def button_do_square():
    first_num=input.get()
    global f_num
    global math
    math="square"
    f_num=int(first_num)
    input.delete(0,END) 
#Buttons
button_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_add(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda: button_add(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_add(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_add(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_add(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_add(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_add(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_add(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_add(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda:button_add(0))
button_addition=Button(root,text="+",padx=38,pady=20,command=button_carryaddition)
button_equal=Button(root,text="=",padx=90,pady=20,bg="black",fg="white",command=button_show_result)
button_clear=Button(root,text="Clear",padx=79,pady=20,command=button_clear)

button_minus=Button(root,text="-",padx=40,pady=20,command=button_do_subtraction)
button_multiply=Button(root,text="x",padx=40,pady=20,command=button_do_multiply)
button_divide=Button(root,text="/",padx=41,pady=20,command=button_do_division)

button_square_root=Button(root,text="√",padx=40,pady=20,command=button_do_square_root)
button_square=Button(root,text="sq.",padx=40,pady=20,command=button_do_square)


# Put buttons on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_addition.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_minus.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

button_square_root.grid(row=7,column=0)
button_square.grid(row=7,column=1)

root.mainloop()
