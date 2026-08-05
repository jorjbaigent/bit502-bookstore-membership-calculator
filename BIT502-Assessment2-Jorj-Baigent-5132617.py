# Jorj Baigent 5132617 BIT502 Assessment 2
#
#

# ------------------------------
# Imports
# ------------------------------

import tkinter
from tkinter import messagebox

# ------------------------------
# Tkinter setup
# ------------------------------

window = tkinter.Tk()
window.title("The Aurora Archive")


# ------------------------------
# Variables
# ------------------------------

# Store text in the variables so we can change it later if we need to

plan_standard = "Standard"
plan_premium = "Premium"
plan_kids = "Kids"

plan_monthly = "Monthly"
plan_annual = "Annual"

optional_1 = "Book Rental"
optional_2 = "Private Area Access"
optional_3 = "Monthly Booklet"
optional_4 = "Online ebook Rental"

options_checked = "" #Stores chosen options for writing into text file
plan_chosen = "" #Stores chosen plan for writing into text file
payment_period = "" #Stores chosen payment period for writing into text file and displaying in the total cost label

#Variables storing prices and discounts in case they need to be changed in the future
standard_price = 10
premium_price = 15
kids_price = 5

book_rental = 5
private_area_access = 15
monthly_booklet = 2
ebook_rental = 5

library_card_disc = 0.10

# Variables that store the results of the elements


membership_plan = tkinter.StringVar(window, plan_standard)      # Selected membership type
payment_plan = tkinter.StringVar(window, plan_monthly)          # Duration of payment
extra1 = tkinter.BooleanVar(window, False)                      # Optional extra 1
extra2 = tkinter.BooleanVar(window, False)                      # Optional extra 2
extra3 = tkinter.BooleanVar(window, False)                      # Optional extra 3
extra4 = tkinter.BooleanVar(window, False)                      # Optional extra 4
has_library_card = tkinter.BooleanVar(window, False)            # Library Card
first_name = tkinter.StringVar()
last_name = tkinter.StringVar()
address = tkinter.StringVar()
mobile = tkinter.StringVar()
library_number = tkinter.StringVar()

file_name = ".\\members_data.txt"  # File to store membership details

#Cost holding variables
#Defining variables to hold costs
membership_cost = 0
optional_extra_cost = 0
discounts = 0
total_cost = 0
approx_weekly_cost = 0
    
monthly_price = 0
library_discount = 0
payment_type_disc = 0
# ------------------------------
# Functions
# ------------------------------

#Clears the form
def resetForm():
    #Clear entry boxes
    first_name.set("")
    last_name.set("")
    address.set("")
    mobile.set("")
    library_number.set("")
    
    #Reset radio buttons
    membership_plan.set(plan_standard)
    payment_plan.set(plan_monthly)
    
    #Untick checkboxes
    extra1.set(False)
    extra2.set(False)
    extra3.set(False)
    extra4.set(False)
    has_library_card.set(False)
    
    #Reset totals
    label_total_cost_base.config(text="--")
    label_total_cost_extras.config(text="--")
    label_total_cost_discount.config(text="--")
    label_total_cost_total.config(text="--")
    label_total_cost_weekly.config(text="--")

def calculate():
    global options_checked
    global plan_chosen
    global payment_period
    
    global membership_cost
    global optional_extra_cost
    global discounts
    global total_cost
    global approx_weekly_cost
    global monthly_price
    global library_discount
    global payment_type_disc
    
    optional_extra_cost = 0 #For automatic calculation purposes, optional extra cost is reset to 0 each time the function is called
    
    #Calculate base membership cost
    if(membership_plan.get() == plan_standard):
        membership_cost = standard_price
        plan_chosen = plan_standard
    elif(membership_plan.get() == plan_premium):
        membership_cost = premium_price
        plan_chosen = plan_premium
    elif(membership_plan.get() == plan_kids):
        membership_cost = kids_price
        plan_chosen = plan_kids
    
    #Calculate optional extra cost
    if(extra1.get()):
        optional_extra_cost += book_rental
        options_checked += optional_1 + ", "
    if(extra2.get()):
        optional_extra_cost += private_area_access
        options_checked += optional_2 + ", "
    if(extra3.get()):
        optional_extra_cost += monthly_booklet
        options_checked += optional_3 + ", "
    if(extra4.get()):
        optional_extra_cost += ebook_rental
        options_checked += optional_4
        
    #Calculates full monthly cost
    monthly_price = membership_cost + optional_extra_cost
    
    #Calculate discounts
    if(has_library_card.get()): #Calculates discount for having a library card
        library_discount = monthly_price * library_card_disc
    else:
        library_discount = 0
    
    
    if(payment_plan.get() == plan_annual): #Calculates discount for annual membership
        discounted_cost = membership_cost
        
        if(has_library_card.get()): #Calculates discount for annual membership with library card discount
            discounted_cost -= membership_cost * library_card_disc
        
        payment_type_disc = discounted_cost / 12
    else:
        payment_type_disc = 0
    
    #Calculates total monthly discount
    discounts = library_discount + payment_type_disc
    
    #Calculate total cost due and weekly cost
    if(payment_plan.get() == plan_monthly): #Calculates for monthly plans
        total_cost = monthly_price - discounts
        approx_weekly_cost = total_cost / 4
        payment_period = "monthly"
        
    elif(payment_plan.get() == plan_annual): #Calculates for annual plans
        total_cost = (monthly_price - discounts) * 12
        approx_weekly_cost = total_cost / 52
        payment_period = "yearly"
    
    #Update labels
    label_total_cost_base.config(text=f"${membership_cost:.2f}")
    label_total_cost_extras.config(text=f"${optional_extra_cost:.2f}")
    label_total_cost_discount.config(text=f"${discounts:.2f}")
    label_total_cost_total.config(text=f"${total_cost:.2f} {payment_period}")
    label_total_cost_weekly.config(text=f"${approx_weekly_cost:.2f}")

def submit():
    global options_checked
    
    #Assigning user input to variables for easier handling
    user_first_name = first_name.get()
    user_last_name = last_name.get()
    user_address = address.get()
    user_mobile = mobile.get()
    library_id = library_number.get()
    
    #Error Checking
    
    #Check first name
    if(user_first_name.strip() == ""): #Checks first name isn't empty
        messagebox.showinfo("Error","Please enter your first name")
        return
    
    if any(char.isdigit() for char in user_first_name): #Checks there are no numbers in first name
        messagebox.showinfo("Error", "First name cannot contain numbers")
        return
    
    #Check last name
    if(user_last_name.strip() == ""): #Checks last name isn't empty
        messagebox.showinfo("Error", "Please enter your last name")
        return
    
    if any(char.isdigit() for char in user_last_name): #Checks there are no numbers in last name
        messagebox.showinfo("Error", "Last name cannot contain numbers")
        return
    
    #Check address
    if(user_address.strip() == ""): #Checks address isn't empty
        messagebox.showinfo("Error", "Please enter your address")
        return
    
    #Check mobile number
    if(user_mobile.strip() == ""): #Checks mobile number isn't empty
        messagebox.showinfo("Error", "Please enter your mobile number")
        return
    
    if(not user_mobile.strip().isdigit()): #Checks mobile number only contains numbers
        messagebox.showinfo("Error", "Mobile number must only contain integers")
        return
    
    #Check library card 
    if(has_library_card.get()):
        if(library_id.strip() == ""): #Checks library card ID isn't empty
            messagebox.showinfo("Error", "Please enter your library card ID")
            return
        
        if(not library_id.isdigit()): #Checks library card ID only contains numbers
            messagebox.showinfo("Error", "Library card ID must only contain numbers")
            return
        
        if(len(library_id.strip()) != 5): #Checks library card ID contains 5 digits
            messagebox.showinfo("Error", "Library card ID must contain 5 digits")
            return
    
    #Check library card ID hasn't been entered if checkbox is unchecked
    if(not has_library_card.get() and library_id.strip() != ""):
        messagebox.showinfo("Error", "Please check the Library Card box to apply your discount")
        return
    
    #Write user details onto file
    with open(file_name, "a") as f:
        f.write(f"First Name: {user_first_name}\n")
        f.write(f"Last Name: {user_last_name}\n")
        f.write(f"Address: {user_address}\n")
        f.write(f"Mobile: {user_mobile}\n")
        f.write(f"Membership Type: {plan_chosen}\n")
        f.write(f"Extras: {options_checked}\n")
        f.write(f"Payment Plan: {payment_plan.get()}\n")
        if(has_library_card.get()):
            f.write("Library Card: Yes\n")
            f.write(f"Library Card ID: {library_id}\n")
        elif(not has_library_card.get()):
            f.write("Library Card: No\n")
            f.write("Library Card ID: ---\n")
        f.write(f"Base Membership Cost: ${membership_cost:.2f}\n")
        f.write(f"Extras Cost: ${optional_extra_cost:.2f}\n")
        f.write(f"Total Discounts: ${discounts:.2f}\n")
        f.write(f"Total Cost: ${total_cost:.2f}\n")
        f.write(f"Weekly Cost: ${approx_weekly_cost:.2f}\n")
        f.write(f"Payment Due: ${total_cost:.2f}\n")
        f.write("--------------------------------------------------\n")


    messagebox.showinfo("Success", "Your details have been submitted")
    
    resetForm()



# ------------------------------
# Widget definitions
# ------------------------------
# The widget definitions are found in this section, no positioning has been done here, just declaration


#### Labels ####

label_first_name = tkinter.Label(window, text = "First Name:")
label_last_name = tkinter.Label(window, text = "Last Name:")
label_address = tkinter.Label(window, text = "Address:")
label_mobile = tkinter.Label(window, text = "Mobile:")

label_membership_type = tkinter.Label(window, text = "Membership Plan:")
label_membership_payment_plan = tkinter.Label(window, text = "Payment Plan:")
label_library_card = tkinter.Label(window, text = "Library Card:")
label_library_number = tkinter.Label(window, text = "Card Number:")

label_optional_extras = tkinter.Label(window, text = "Optional Extras:")

label_total_header = tkinter.Label(window, text = "Totals")
label_total_base = tkinter.Label(window, text = "Membership Cost:")
label_total_extras = tkinter.Label(window, text = "Extra Charges:")
label_total_weekly = tkinter.Label(window, text = "Weekly Cost:")
label_total_discount = tkinter.Label(window, text = "Total Discount:")
label_total_final = tkinter.Label(window, text = "Total Cost:")


label_total_cost_base = tkinter.Label(window, text = "--")
label_total_cost_extras = tkinter.Label(window, text = "--")
label_total_cost_weekly = tkinter.Label(window, text = "--")
label_total_cost_discount = tkinter.Label(window, text = "--")
label_total_cost_total = tkinter.Label(window, text = "--")


#### Entry text boxes ####

entry_first_name = tkinter.Entry(window, textvariable=first_name)
entry_last_name = tkinter.Entry(window, textvariable=last_name)
entry_address = tkinter.Entry(window, textvariable=address)
entry_mobile = tkinter.Entry(window, textvariable=mobile)

entry_library_number = tkinter.Entry(window, textvariable=library_number)

#### Radio buttons ####

radio_membership_1 = tkinter.Radiobutton(window, text = plan_standard, variable = membership_plan, value = plan_standard, command=calculate)
radio_membership_2 = tkinter.Radiobutton(window, text = plan_premium, variable = membership_plan, value = plan_premium, command=calculate)
radio_membership_3 = tkinter.Radiobutton(window, text = plan_kids, variable = membership_plan, value = plan_kids, command=calculate)

radio_payment_plan_1 = tkinter.Radiobutton(window, text = plan_monthly, variable = payment_plan, value = plan_monthly, command=calculate)
radio_payment_plan_2 = tkinter.Radiobutton(window, text = plan_annual, variable = payment_plan, value = plan_annual, command=calculate)

#### Checkbuttons ####

checkbutton_has_library_card = tkinter.Checkbutton(window, text = "", variable = has_library_card, onvalue = True, offvalue = False, command=calculate)

checkbutton_extra1 = tkinter.Checkbutton(window, text = optional_1, variable = extra1, onvalue = True, offvalue = False, command=calculate)
checkbutton_extra2 = tkinter.Checkbutton(window, text = optional_2, variable = extra2, onvalue = True, offvalue = False, command=calculate)
checkbutton_extra3 = tkinter.Checkbutton(window, text = optional_3, variable = extra3, onvalue = True, offvalue = False, command=calculate)
checkbutton_extra4 = tkinter.Checkbutton(window, text = optional_4, variable = extra4, onvalue = True, offvalue = False, command=calculate)


#### Buttons ####

button_reset = tkinter.Button(window, text = "Reset", command = resetForm)
button_submit = tkinter.Button(window, text = "Submit", command = submit)


# ------------------------------
# Widget positioning
# ------------------------------
# All of the widget positioning is found here
# Another method of positioning widgets can be used if you comment this code out and use your own design

label_first_name.grid(row = 0, column = 0, sticky = "w")
label_last_name.grid(row = 1, column = 0, sticky = "w")
label_address.grid(row = 2, column = 0, sticky = "w")
label_mobile.grid(row = 3, column = 0, sticky = "w")

label_membership_type.grid(row = 4, column = 0, sticky = "w")
label_membership_payment_plan.grid(row = 7, column = 0, sticky = "w")
label_library_card.grid(row = 14, column = 0, sticky = "w")

entry_first_name.grid(row = 0, column = 1, sticky = "w")
entry_last_name.grid(row = 1, column = 1, sticky = "w")
entry_address.grid(row = 2, column = 1, sticky = "w")
entry_mobile.grid(row = 3, column = 1, sticky = "w")

radio_membership_1.grid(row = 4, column = 1, sticky = "w")
radio_membership_2.grid(row = 5, column = 1, sticky = "w")
radio_membership_3.grid(row = 6, column = 1, sticky = "w")

radio_payment_plan_1.grid(row = 7, column = 1, sticky = "w")
radio_payment_plan_2.grid(row = 8, column = 1, sticky = "w")

label_optional_extras.grid(row = 10, column = 0, sticky = "w")
checkbutton_extra1.grid(row = 10, column = 1, sticky = "w")
checkbutton_extra2.grid(row = 11, column = 1, sticky = "w")
checkbutton_extra3.grid(row = 12, column = 1, sticky = "w")
checkbutton_extra4.grid(row = 13, column = 1, sticky = "w")

label_library_number.grid(row = 15, column = 0, sticky = "w")
checkbutton_has_library_card.grid(row = 14, column = 1, sticky = "w")
entry_library_number.grid(row = 15, column = 1, sticky = "w")

label_total_header.grid(row = 19, column = 0, sticky = "w")
label_total_base.grid(row = 20, column = 0, sticky = "w")
label_total_extras.grid(row = 21, column = 0, sticky = "w")
label_total_weekly.grid(row = 22, column = 0, sticky = "w")
label_total_discount.grid(row = 23, column = 0, sticky = "w")
label_total_final.grid(row = 24, column = 0, sticky = "w")

label_total_cost_base.grid(row = 20, column = 1, sticky = "w")
label_total_cost_extras.grid(row = 21, column = 1, sticky = "w")
label_total_cost_weekly.grid(row = 22, column = 1, sticky = "w")
label_total_cost_discount.grid(row = 23, column = 1, sticky = "w")
label_total_cost_total.grid(row = 24, column = 1, sticky = "w")

button_reset.grid(row = 25, column = 0)
button_submit.grid(row = 25, column = 1)

# ----------------------------------
# Tkinter mainloop
window.mainloop()