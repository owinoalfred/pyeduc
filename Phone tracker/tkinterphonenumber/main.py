
from tkinter import *
import phonenumbers 
from phonenumbers import geocoder
from phonenumbers import carrier



root = Tk()
root.title('Geolocater')
root.geometry("800x500")

def change(number):
    number = input("number")
    ch_number = phonenumbers.parse(number, "CH")
    print(geocoder.description_for_number(ch_number,  'en'))
    service_provider = phonenumbers.parse(number, "RO")
    print(carrier.name_for_number(service_provider, "en"))
    my_number.delete(0, END)
    asweroFImportsnve  = f"Name is of the service provider is {ch_number} and the number is {service_provider}."
    return asweroFImportsnve

my_number = Entry(root, font = ('Roboto', 28))
my_number.pack(pady=20)

mybutton = Button(root, text = 'input any number', command=change )
mybutton.pack(pady=20)

mylabel = Label(root , text =' change.asweroFImportsnve' )
mylabel.pack(pady=20)


root.mainloop()