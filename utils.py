def clear_all_entries(first_name, last_name, street, city, state, zipcode):
    first_name.delete(0, "end")
    last_name.delete(0, "end")
    street.delete(0, "end")
    city.delete(0, "end")
    state.delete(0, "end")
    zipcode.delete(0, "end")

    first_name.focus_set()


def clear_all_widgets(window):
    for widget in window.winfo_children():
        widget.destroy()