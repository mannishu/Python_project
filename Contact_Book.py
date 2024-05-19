#import library
from tkinter import *
from tkinter import messagebox


#Initialize window
root = Tk()
root.geometry('700x450')
root.config(bg = '#6E6E6E')
root.title('Contact Book')
root.resizable(0,0)
contactlist = [
    ['Vikash','8005478263'],
    ['Mukesh', '7854962358'],
    ['Diwakar', '7458759685'],
    ['Durgesh', '78548585'],
    ['Amit', '8585747496'],
    ]

Name = StringVar()
Number = StringVar()


#Create frame
frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set,font=('Times new roman',16),bg="#f0fffc",width=15,height=20,borderwidth=3,relief="groove")
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)


#function to get select value

def Selected():
	print("hello",len(select.curselection()))
	if len(select.curselection())==0:
		messagebox.showerror("Error", "Please Select the Name")
	else:
		return int(select.curselection()[0])
    
#function to add new contact
def AddContact():
    if Name.get()!="" and Number.get()!="":
        contactlist.append([Name.get() ,Number.get()])
        print(contactlist)
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")

    else:
        messagebox.showerror("Error","Please fill the information")


# fun to edit existing contact

def UpdateDetail():
	if Name.get() and Number.get():
		contactlist[Selected()] = [Name.get(), Number.get()]
    

		messagebox.showinfo("Confirmation", "Successfully Update Contact")
		EntryReset()
		Select_set()

	elif not(Name.get()) and not(Number.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Please fill the information")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Please Select the Name and \n press Load button")
		else:
			message1 = """To Load the all information of \n 
						  selected row press Load button\n.
						  """   
			messagebox.showerror("Error", message1)

def EntryReset():
	Name.set('')
	Number.set('')

#function to delete selected contact
def Delete_Entry():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
        if result==True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')

   
# func to view contact
def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
        


def EXIT():
    root.destroy()


def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)
Select_set()


#define buttons labels and entry widget 
Label(root, text = 'Name', font=("Times new roman",20,"bold"), bg = 'SlateGray3').place(x= 30, y=20)
Entry(root, textvariable = Name, width=30).place(x= 200, y=30)
Label(root, text = 'Contact No.', font=("Times new roman",18,"bold"),bg = 'SlateGray3').place(x= 30, y=70)
Entry(root, textvariable = Number, width=30).place(x= 200, y=80)

Button(root,text=" ADD", font='Century',bg='#e8c1c7', command = AddContact, padx=20). place(x= 20, y=120)
Button(root,text="EDIT", font='Century',bg='#e8c1c7',command = UpdateDetail, padx=20).place(x= 20, y=160)
Button(root,text="DELETE", font='Century',bg='#e8c1c7',command = Delete_Entry, padx=20).place(x= 20, y=200)
Button(root,text="VIEW", font='Century',bg='#e8c1c7', command = VIEW).place(x= 20, y=240)
Button(root,text="RESET", font='Century',bg='#e8c1c7', command = EntryReset).place(x= 20, y=280)
Button(root,text="EXIT", font='Century',bg='#BCFD4C', command = EXIT).place(x= 250, y=320)

root.mainloop()
  
