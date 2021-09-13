import pandas as pd
from tkinter import *
from tkinter import messagebox
from manage_database import create_new_record, read_all_records, delete_record, reset_table_index, update_record
from utils import clear_all_entries, clear_all_widgets


def create_btn_clicked(root, first_name, last_name, street, city, state, zipcode):
    create_new_record(
        first_name=first_name.get(),
        last_name=last_name.get(),
        street=street.get(),
        city=city.get(),
        state=state.get(),
        zipcode=zipcode.get()
    )

    record_created_label = Label(
        root,
        text=f"Record Created For : {first_name.get()} {last_name.get()}",
        padx=10,
        pady=10
    )
    record_created_label.grid(
        row=7,
        column=0,
        columnspan=2,
        padx=(20, 10),
        pady=10,
        ipadx=30
    )

    clear_all_entries(first_name, last_name, street, city, state, zipcode)


def save_edits(frame, oid_num, edit_entry_list):
    dict_to_insert = dict(
            oid_num=oid_num,
            first_name=edit_entry_list[0].get(),
            last_name=edit_entry_list[1].get(),
            street=edit_entry_list[2].get(),
            city=edit_entry_list[3].get(),
            state=edit_entry_list[4].get(),
            zipcode=edit_entry_list[5].get()
        )
    
    update_record(dict_to_insert)

    clear_all_widgets(frame)
    record_list = read_all_records()
    read_records_in_new_window(frame, record_list)


def cancel_edits(frame):
    clear_all_widgets(frame)
    record_list = read_all_records()
    read_records_in_new_window(frame, record_list)


def edit_btn_clicked(frame, i, j,oid_num):
    edit_entry_list = []
    for widget in frame.winfo_children():
        wid_row = widget.grid_info()["row"]
        wid_col = widget.grid_info()["column"]
        if wid_row == i:
            # print(widget.winfo_class())
            if isinstance(widget, Label):
                if wid_col != 0:
                    # print(True)
                    edit_entry = Entry(
                        frame,
                        width=10
                    )
                    edit_entry.delete(0, "end")
                    edit_entry.insert(0, widget["text"])
                    # widget.destroy()
                    edit_entry.grid(
                        row=wid_row,
                        column=wid_col,
                        sticky="nsew"
                    )
                    edit_entry_list.append(edit_entry)
                    if wid_col == 1:
                        edit_entry.focus_set()
            
            elif isinstance(widget, Button):
                if wid_col == j:
                    save_btn = Button(
                        frame,
                        text="Save",
                        fg="white",
                        bg="#449147",
                        padx=10,
                        pady=10,
                        command=lambda: save_edits(frame, oid_num, edit_entry_list)
                    )
                    save_btn.grid(
                        row=wid_row,
                        column=wid_col,
                        sticky="nsew",
                        padx=(10, 0),
                    )
                elif wid_col == j + 1:
                    cancel_btn = Button(
                        frame,
                        text="Cancel",
                        fg="white",
                        bg="#a8472f",
                        padx=10,
                        pady=10,
                        command=lambda: cancel_edits(frame)
                    )
                    cancel_btn.grid(
                        row=wid_row,
                        column=wid_col,
                        sticky="nsew"
                    )


def delete_btn_clicked(frame, oid_num):
    response = messagebox.askyesno(
        "Delete Record",
        "Are You Sure, You Want to Delete This Record."
    )

    if response == 1:

        delete_record(oid_num)
        clear_all_widgets(frame) # destroying all widgets from the top window
        try:
            reset_table_index()
        finally:
            record_list = read_all_records()
            read_records_in_new_window(frame, record_list) # redrawing all widgets from the top window



def show_edit_btn(frame, i, j, oid_num):
    edit_btn = Button(
                frame,
                text="Edit",
                padx=10,
                pady=10,
                bg="#4d6fab",
                fg="white",
                command=lambda: edit_btn_clicked(frame, i, j, oid_num)
            )
    edit_btn.grid(
        row=i,
        column=j,
        padx=(10, 0),
        # columnspan=1,
        sticky="nsew"
    )


def show_delete_btn(frame, i, j, oid_num):
    delete_btn = Button(
        frame,
        text="Delete",
        padx=10,
        pady=10,
        bg="#bd4470",
        fg="white",
        command=lambda: delete_btn_clicked(frame, oid_num)
    )
    delete_btn.grid(
        row=i,
        column=j+1,
        # padx=(10, 0),
        # columnspan=1,
        sticky="nsew"
    )


def read_records_in_new_window(frame, record_list):
    
    headers = ("Id" ,"First Name", "Last Name", "Street", "City", "State", "Zip Code")
    record_list.insert(0, headers)
    
    i = 0
    for record in record_list:
        j = 0
        for item in record:
            if item == "":
                item = " "
            lbl = Label(
                frame,
                text=item,
                padx=10,
                pady=10,
                # border="",
                borderwidth=1,
                relief=RIDGE
            )
            lbl.grid(
                row=i,
                column=j,
                # columnspan=1,
                sticky="nsew"
            )
            
            j += 1
        
        if i != 0:
            oid_num = record[0]
            show_edit_btn(frame, i, j, oid_num)
            show_delete_btn(frame, i, j, oid_num)
        
        i += 1


def main_read_btn_clicked():
    record_list = read_all_records()

    top = Toplevel()
    top.title("See Records")
    top.geometry("+700+100")
    top.attributes('-topmost',True)

    frame = Frame(
        top,
        padx=10,
        pady=10
    )
    frame.grid(
        row=0,
        column=0,
    )

    read_records_in_new_window(frame, record_list)

    

















# def some_random():
#     # todo: add a vertical and horizontal scroll bar in text widget and solve size problem of text widget.
#     # todo: make a custom fuction for showing data and placing delete and edit button at the end of each row.

#     df = pd.DataFrame(record_list, columns=["Id" ,"First Name", "Last Name", "Street", "City", "State", "Zip Code"])
#     df.set_index("Id", inplace=True)
#     str_df = df.to_markdown(tablefmt="pretty")  # 'tablefmt' is kwarg for "tabulate" package which pandas uses in background.

#     str_df_text_wid = Text(
#         root,
#         # width=100,
#         # height=100,
#         padx=10,
#         pady=10,
#     )
#     str_df_text_wid.insert("end", str_df)
#     str_df_text_wid.grid(
#         row=7,
#         column=0,
#         columnspan=2,
#         padx=10,
#         pady=10,
#     )

#     # vertical_scrollbar = Scrollbar(
#     #     str_df_text_wid,
#     #     orient="vertical"
#     # )
#     # vertical_scrollbar.grid(
#     #     row=7,
#     #     column=1,
#     # )

#     # vertical_scrollbar.config(command=str_df_text_wid.yview)
#     # str_df_text_wid.config(yscrollcommand=vertical_scrollbar.set)

