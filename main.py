from tkinter import *
from manage_widgets import show_entries, show_entry_labels, show_create_btn
from manage_btn_actions import main_read_btn_clicked


main_window = Tk()
main_window.title("Address Book App")
main_window.geometry("+100+100")

# creating table in db
# create_db_table()


def main_create_btn_clicked():
    root = Toplevel(main_window)
    root.title("Create Record")
    root.geometry("+350+100")
    root.attributes('-topmost',True)

    show_entry_labels(root)
    show_entries(root)
    show_create_btn(root)


def show_main_read_btn(window):
    read_btn = Button(
        window,
        text="See All Records",
        padx=10,
        pady=5,
        command=main_read_btn_clicked,
        bg="#a55aad",
        fg="white"
    )
    read_btn.grid(
        row=1,
        column=0,
        padx=10,
        pady=10,
        ipadx=38  # scale the button in x axis
    )



def show_main_create_btn(window):
    read_btn = Button(
        window,
        text="Create New Record",
        padx=10,
        pady=5,
        command=main_create_btn_clicked,
        bg="#449147",
        fg="white"
    )
    read_btn.grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
        ipadx=25  # scale the button in x axis
    )


show_main_create_btn(main_window)
show_main_read_btn(main_window)




main_window.mainloop()
