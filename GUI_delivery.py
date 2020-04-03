from tkinter import *
import tkinter.messagebox


def save_data():
    try:
        with open('./data/deliveries.txt','a') as f:
            f.write('Depot:\n')
            f.write("%s\n"%location.get())
            f.write('Transfer Service:\n')
            f.write("%s\n"%service.get())
            f.write('Description:\n')
            f.write("%s\n"%description.get())
            f.write('Address:\n')
            f.write("%s\n"%address.get("1.0",END))
            #StringVar object has no attribute 'delete'
            location.set(None)
            service.set(None)
            description.delete(0,END)
            address.delete("1.0",END)
    except Exception as ex:
        tkinter.messagebox.showerror("Error!","Can't write to the file %s"%ex)

def read_locations(file):
    locations = []
    with open(file,'r') as f:
        for line in f:
            locations.append(line.rstrip())
    return locations

app = Tk()
app.title('Head-ex Deliveries')
#don't need to keep track of the labels
Label(app,text = "Depot:").pack()
#model for the radion buttons to share
location = StringVar()
location.set(None)

#but this only work well with small location
# Radiobutton(app,
#             text = "Cambridge, UK", 
#             value = "Cambridge, UK", 
#             variable = location).pack()
# Radiobutton(app,
#             text = "Cambridge, MA", 
#             value = "Cambridge, MA", 
#             variable = location).pack()
# Radiobutton(app,
#             text = "Seattle, WA", 
#             value = "Seattle, WA", 
#             variable = location).pack()
# ["Cambridge, MA","Cambridge, UK","Seattle, MA",
# "New York, NY","Dallas, TX","Boston, MA",
# "Rome, Italy","Male, Maldives","Luxor, Egypt",
# "Rhodes, Greece","Edinburgh, Scotland"]


locations = read_locations('./data/locations.txt')
OptionMenu(app,location,*locations).pack()
# depot = Entry(app)
# depot.pack()
Label(app,text = "Transfer Service").pack()
service = StringVar()
service.set(None)
Radiobutton(app,
            text = "First Class", 
            value = "First Class", 
            variable=service).pack()
Radiobutton(app,
            text = "Next Business Day", 
            value = "Next Business Day",variable=service).pack()

Label(app,text="Description:").pack()
description=Entry(app)
description.pack()

Label(app,text="Address:").pack()
address = Text(app)
address.pack()

Button(app,text="Save",command=save_data).pack()
app.mainloop()

