'''
simple biodata application
fname - entry 
lname - entry
email - entry
phone - entry
gender - radio 
dob - combobox
height - slider
age - spinbox
hobbies - checkbox
About you - text
button -cancel
button -submit
show dialog after submit with all info entered 
'''
import tkinter as tk
from tkinter import ttk
from calendar import month_name
from datetime import date
from tkinter.messagebox import showinfo

# variables
firstname_label = None
firstname_entry = None
lastname_label = None
lastname_entry = None
email_label = None
email_entry = None
phone_label = None
phone_entry = None
gender_label = None
gender_male_radio = None
gender_female_radio = None
dob_label = None
dob_month_cb = None
dob_day_cb = None
dob_year_cb = None
height_label = None
height_slider = None
age_label = None
age_spinbox = None
hobbies_label = None
about_label = None
about_text = None
submit_btn = None
cancel_btn = None

def generate_label_field(container, text, colno, rowno):
    variable = ttk.Label(container, text=text)
    variable.grid(column=colno, row=rowno, sticky=tk.W, padx=5, pady=5)
    return variable

def generate_entry_field(container, colno, rowno):
    variable = ttk.Entry(container)
    variable.grid(column=colno, row=rowno, sticky=tk.EW, padx=5, pady=5)
    return variable

def generate_radio_field(container, text, value, string_var, colno, rowno):
    variable = ttk.Radiobutton(
        container,
        text=text,
        value=value,
        variable=string_var
    )
    variable.grid(column=colno, row=rowno, sticky=tk.W, padx=5, pady=5)

def generate_combobox_field(container, values, string_var, colno, rowno):
    variable = ttk.Combobox(
        container,
        textvariable=string_var,
        width=5
    )
    variable['values'] = values
    variable['state'] = 'readonly'
    variable.grid(column=colno, row=rowno, padx=(0, 5))
    return variable

def generate_slider_field(container, double_var, from_, to, colno, rowno, command):
    variable = ttk.Scale(
        container,
        from_=from_,
        to=to,
        variable=double_var,
        command=command
    )
    variable.set(from_)
    variable.grid(column=colno, row=rowno, sticky=tk.EW, padx=5, pady=5)
    return variable

def slider_changed(event, label, slider_val, key):
    if key == 'height':
        label['text'] = "Height ({:.2f} ft)".format(slider_val.get())
    else:
        label['text'] = slider_val.get()

def generate_spinbox_field(container, string_var, from_, to, colno, rowno):
    variable = ttk.Spinbox(
        container,
        from_=from_,
        to=to,
        textvariable=string_var
    )
    variable.set(from_)
    variable['state'] = 'readonly'
    variable.grid(column=colno, row=rowno, sticky=tk.EW, padx=5, pady=5)
    return variable

def generate_checkbox_field(container, text, onvalue, offvalue, string_var, command, colno, rowno):
    variable = ttk.Checkbutton(
        container,
        text=text,
        onvalue=onvalue, 
        offvalue=offvalue,
        variable=string_var,
        command=command
    )
    variable.grid(column=colno, row=rowno, sticky=tk.W, padx=5, pady=5)
    return variable

def checkbox_changed():
    pass

def generate_text_field(container, colno, rowno, width=0, rowspan=0):
    variable = tk.Text(
        container,
        height=8,
        width=width
    )
    variable.grid(column=colno, row=rowno, rowspan=rowspan, sticky=tk.EW, padx=5, pady=5)
    return variable

def generate_button(container, text, command, colno, rowno):
    variable = ttk.Button(
        container, 
        text=text, 
        command=command
    )
    variable.grid(column=colno, row=rowno, sticky=tk.E, padx=5, pady=5)
    return variable

def handle_submit():
    biodata = "First Name: " + firstname_entry.get() + "\n"
    biodata += "Last Name: " + lastname_entry.get() + "\n"
    biodata += "Email: " + email_entry.get() + "\n"
    biodata += "Phone: " + phone_entry.get() + "\n"
    biodata += "Gender: " + gender_val.get() + "\n"
    dob_str = ""
    if dob_month_val.get() and dob_day_val.get() and dob_year_val.get():
        dob_str = dob_month_val.get() + " " + dob_day_val.get().zfill(2) + ", " + dob_year_val.get()

    biodata += "Date of Birth: " + dob_str + "\n"
    biodata += "Height: " + str("{:.2f}".format(height_val.get())) + " ft\n"
    biodata += "Age: " + age_val.get() + "\n"
    hobby_list = []
    if hobby_reading_val.get():
        hobby_list.append(hobby_reading_val.get())
    if hobby_travel_val.get():
        hobby_list.append(hobby_travel_val.get())
    if hobby_coding_val.get():
        hobby_list.append(hobby_coding_val.get())
    if hobby_gaming_val.get():
        hobby_list.append(hobby_gaming_val.get())

    biodata += "Hobbies: " + ", ".join(hobby_list) + "\n"
    biodata += "About You: " + about_text.get(1.0, "end-1c") + "\n"
    #print(biodata)
    showinfo(
        title='Your Submission',
        message=biodata
    )

root = tk.Tk()
root.title("Biodata")
root.geometry("450x500")
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

dob_frame = ttk.Frame(root)
dob_frame.columnconfigure(0, weight=1)
dob_frame.columnconfigure(1, weight=1)
dob_frame.columnconfigure(2, weight=1)
dob_frame.grid(column=1, row=5, columnspan=3, sticky=tk.W, padx=5, pady=5)

btns_frame = ttk.Frame(root)
btns_frame.columnconfigure(0, weight=1)
btns_frame.columnconfigure(1, weight=1)
btns_frame.grid(column=1, row=14, columnspan=2, sticky=tk.E, padx=5, pady=5)

# selected values
gender_val = tk.StringVar()
dob_month_val = tk.StringVar()
dob_day_val = tk.StringVar()
dob_year_val = tk.StringVar()
height_val = tk.DoubleVar()
age_val = tk.StringVar()
hobby_reading_val = tk.StringVar()
hobby_travel_val = tk.StringVar()
hobby_coding_val = tk.StringVar()
hobby_gaming_val = tk.StringVar()

hobbies = [
    ("Reading", hobby_reading_val), 
    ("Travel", hobby_travel_val), 
    ("Coding", hobby_coding_val), 
    ("Gaming", hobby_gaming_val)
]

dob_months = [month_name[m][0:3] for m in range(1, 13)]
dob_days = list(range(1, 32))
dob_years = list(range(1950, date.today().year + 1))

firstname_label = generate_label_field(root, "First Name", 0, 0)
firstname_entry = generate_entry_field(root, 0, 1)

lastname_label = generate_label_field(root, "Last Name", 1, 0)
lastname_entry = generate_entry_field(root, 1, 1)

email_label = generate_label_field(root, "Email", 0, 2)
email_entry = generate_entry_field(root, 0, 3)

phone_label = generate_label_field(root, "Phone", 1, 2)
phone_entry = generate_entry_field(root, 1, 3)

gender_label = generate_label_field(root, "Gender", 0, 4)
gender_male_radio = generate_radio_field(root, "Male", "male", gender_val, 0, 5)
gender_female_radio = generate_radio_field(root, "Female", "female", gender_val, 0, 6)

dob_label = generate_label_field(root, "Date of Birth", 1, 4)
dob_month_cb = generate_combobox_field(dob_frame, dob_months, dob_month_val, 0, 0)
dob_day_cb = generate_combobox_field(dob_frame, dob_days, dob_day_val, 1, 0)
dob_year_cb = generate_combobox_field(dob_frame, dob_years, dob_year_val, 2, 0)

height_label = generate_label_field(root, "Height (5 ft)", 0, 7)
height_slider = generate_slider_field(
    container=root, 
    double_var=height_val, 
    from_=5, 
    to=8, 
    colno=0, 
    rowno=8,
    command=lambda event: slider_changed(event, height_label, height_val, 'height')
)

age_label = generate_label_field(root, "Age", 1, 7)
age_spinbox = generate_spinbox_field(
    container=root, 
    string_var=age_val, 
    from_=18, 
    to=80, 
    colno=1, 
    rowno=8
)

hobbies_label = generate_label_field(root, "Hobbies", 0, 9)
for index, hobby in enumerate(hobbies):
    generate_checkbox_field(
        container=root, 
        text=hobby[0], 
        onvalue=hobby[0],
        offvalue="",
        string_var=hobby[1], 
        command=checkbox_changed, 
        colno=0, 
        rowno=10 + index
    )

about_label = generate_label_field(root, "About You", 1, 9)
about_text = generate_text_field(
    container=root, 
    colno=1, 
    rowno=10, 
    width=20,
    rowspan=4
)

submit_btn = generate_button(btns_frame, "Submit", handle_submit, 1, 0)
cancel_btn = generate_button(btns_frame, "Cancel", lambda: root.quit(), 0, 0)

root.mainloop()
