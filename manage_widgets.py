from tkinter import *
from manage_btn_actions import create_btn_clicked


def show_create_btn(root):
    global first_name, last_name, street, city, state, zipcode

    create_btn = Button(
        root,
        text="Create Record",
        padx=10,
        pady=5,
        command=lambda: create_btn_clicked(root, first_name, last_name, street, city, state, zipcode),
        bg="#449147",
        fg="white"
    )
    create_btn.grid(
        row=6,
        column=0,
        columnspan=2,
        padx=(20, 10),
        pady=10,
        ipadx=30  # scale the button in x axis
    )


def show_entry_labels(root):
    # create entry label
    first_name_label = Label(
        root,
        text="First Name",
    )
    first_name_label.grid(
        row=0,
        column=0,
        pady=10,
        padx=10
    )

    last_name_label = Label(
        root,
        text="Last Name"
    )
    last_name_label.grid(
        row=1,
        column=0,
        pady=10,
        padx=10
    )

    street_label = Label(
        root,
        text="Street",
    )
    street_label.grid(
        row=2,
        column=0,
        pady=10,
        padx=10
    )

    city_label = Label(
        root,
        text="City"
    )
    city_label.grid(
        row=3,
        column=0,
        pady=10,
        padx=10
    )

    state_label = Label(
        root,
        text="State"
    )
    state_label.grid(
        row=4,
        column=0,
        pady=10,
        padx=10
    )

    zipcode_label = Label(
        root,
        text="Zip Code"
    )
    zipcode_label.grid(
        row=5,
        column=0,
        pady=10,
        padx=10
    )


def show_entries(root):
    global first_name, last_name, street, city, state, zipcode

    # create entry
    first_name = Entry(
        root,
        width=30
    )
    first_name.focus_set()
    first_name.grid(
        row=0,
        column=1,
        padx=20,
        pady=10
    )

    last_name = Entry(
        root,
        width=30
    )
    last_name.grid(
        row=1,
        column=1,
        padx=20,
        pady=10
    )
    
    street = Entry(
        root,
        width=30
    )
    street.grid(
        row=2,
        column=1,
        padx=20,
        pady=10
    )

    city = Entry(
        root,
        width=30
    )
    city.grid(
        row=3,
        column=1,
        padx=20,
        pady=10
    )

    state = Entry(
        root,
        width=30
    )
    state.grid(
        row=4,
        column=1,
        padx=20,
        pady=10
    )

    zipcode = Entry(
        root,
        width=30
    )
    zipcode.grid(
        row=5,
        column=1,
        padx=20,
        pady=10
    )




