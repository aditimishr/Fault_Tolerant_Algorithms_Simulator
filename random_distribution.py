from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numbers

import matplotlib
matplotlib.use("TkAgg")

from Graph_Page import Graph_Page
from Graph_plot_variables import Graph_plot_variables
graph_plot_variable=""

def call_validator(textbox_entry, popup, entry):
    answer = messagebox.askokcancel("Warning!", "Enter a valid input for "+entry+" field")
    if answer:
        popup.tkraise()
        textbox_entry.delete(0, END)
    else:
        popup.tkraise()


def clear_all_entry(graph_plot_variable):
    graph_plot_variable.textbox_x.delete(0, END)
    graph_plot_variable.textbox_y.delete(0, END)
    graph_plot_variable.textbox_sensing_radius.delete(0, END)
    graph_plot_variable.deployment_variable.set("Choose deployment Type")


def check_for_float(entry):
    try:
        float(entry)
        return True
    except ValueError:
        return False


def frame_for_random(frame, graph_plot_variable, popup):
    graph_plot_variable.sensor_density = ''
    graph_plot_variable.textbox_number_of_sensors = ''
    graph_plot_variable.value_from_range = ''
    graph_plot_variable.value_to_range = ''
    graph_plot_variable.fault_ratio = ''
    graph_plot_variable.fault_value_from = ''
    graph_plot_variable.fault_value_to = ''
    popup_for_random = tk.Tk()
    frame1 = tk.Frame(popup_for_random, borderwidth=1, padx="12", pady="5")
    frame1.grid(row=1, columnspan=3, sticky="nsew")
    frame2 = tk.Frame(popup_for_random, borderwidth=1, padx="12", pady="5")
    frame2.grid(row=3, columnspan=3, sticky="nsew")
    frame3 = tk.Frame(popup_for_random, borderwidth=1, padx="12", pady="5")
    frame3.grid(row=5, columnspan=3, sticky="nsew")

    def activateCheck_for_checkbox(checkbox_variable, checkbox_name):
        if checkbox_variable == "input_for_faults" and (checkbox_name.state() == ('active', 'focus', 'selected', 'hover') or checkbox_name.state() == ('selected',)):
            graph_plot_variable.total_number_of_faults.config(state=NORMAL)
            checkbox_for_input_for_asymmetric_faults.state(['!disabled', 'alternate'])
            checkbox_for_input_for_symmetric_faults.state(['!disabled', 'alternate'])
            checkbox_for_input_for_benign_faults.state(['!disabled', 'alternate'])
        elif checkbox_variable == "input_for_faults" and (checkbox_name.state() == ('active', 'focus', 'hover') or checkbox_name.state() == ()):
            checkbox_for_input_for_asymmetric_faults.state(['disabled', 'alternate'])
            checkbox_for_input_for_symmetric_faults.state(['disabled', 'alternate'])
            checkbox_for_input_for_benign_faults.state(['disabled', 'alternate'])
            graph_plot_variable.total_number_of_faults.delete(0, END)
            graph_plot_variable.number_of_asymmetric_fault.delete(0, END)
            graph_plot_variable.asymmetric_fault_value_from.delete(0, END)
            graph_plot_variable.asymmetric_fault_value_to.delete(0, END)
            graph_plot_variable.number_of_symmetric_fault.delete(0, END)
            graph_plot_variable.symmetric_fault_value_from.delete(0, END)
            textbox_to_symmetric_fault_value.delete(0, END)
            graph_plot_variable.number_of_benign_fault.delete(0, END)
            graph_plot_variable.benign_fault_value_from.delete(0, END)
            graph_plot_variable.benign_fault_value_to.delete(0, END)
            graph_plot_variable.total_number_of_faults.config(state=DISABLED)
            graph_plot_variable.number_of_asymmetric_fault.config(state=DISABLED)
            graph_plot_variable.asymmetric_fault_value_from.config(state=DISABLED)
            graph_plot_variable.asymmetric_fault_value_to.config(state=DISABLED)
            graph_plot_variable.number_of_symmetric_fault.config(state=DISABLED)
            graph_plot_variable.symmetric_fault_value_from.config(state=DISABLED)
            graph_plot_variable.symmetric_fault_value_to.config(state=DISABLED)
            graph_plot_variable.number_of_benign_fault.config(state=DISABLED)
            graph_plot_variable.benign_fault_value_from.config(state=DISABLED)
            graph_plot_variable.benign_fault_value_to.config(state=DISABLED)
        elif checkbox_variable == "input_for_asymmetric_faults" and (checkbox_name.state() == ('active', 'focus', 'selected', 'hover') or checkbox_name.state() == ('selected',)):
            graph_plot_variable.number_of_asymmetric_fault.config(state=NORMAL)
            graph_plot_variable.asymmetric_fault_value_from.config(state=NORMAL)
            graph_plot_variable.asymmetric_fault_value_to.config(state=NORMAL)
        elif checkbox_variable == "input_for_asymmetric_faults" and (checkbox_name.state() == ('active', 'focus', 'hover') or checkbox_name.state() == ()):
            graph_plot_variable.number_of_asymmetric_fault.delete(0, END)
            graph_plot_variable.asymmetric_fault_value_from.delete(0, END)
            graph_plot_variable.asymmetric_fault_value_to.delete(0, END)
            graph_plot_variable.number_of_asymmetric_fault.config(state=DISABLED)
            graph_plot_variable.asymmetric_fault_value_from.config(state=DISABLED)
            graph_plot_variable.asymmetric_fault_value_to.config(state=DISABLED)
        elif checkbox_variable == "input_for_symmetric_faults" and (checkbox_name.state() == ('active', 'focus', 'selected', 'hover') or checkbox_name.state() == ('selected',)):
            graph_plot_variable.number_of_symmetric_fault.config(state=NORMAL)
            graph_plot_variable.symmetric_fault_value_from.config(state=NORMAL)
            graph_plot_variable.symmetric_fault_value_to.config(state=NORMAL)
        elif checkbox_variable == "input_for_symmetric_faults" and (checkbox_name.state() == ('active', 'focus', 'hover') or checkbox_name.state() == ()):
            graph_plot_variable.number_of_symmetric_fault.delete(0, END)
            graph_plot_variable.symmetric_fault_value_from.delete(0, END)
            graph_plot_variable.symmetric_fault_value_to.delete(0, END)
            graph_plot_variable.number_of_symmetric_fault.config(state=DISABLED)
            graph_plot_variable.symmetric_fault_value_from.config(state=DISABLED)
            graph_plot_variable.symmetric_fault_value_to.config(state=DISABLED)
        elif checkbox_variable == "input_for_benign_faults" and (checkbox_name.state() == ('active', 'focus', 'selected', 'hover')or checkbox_name.state() == ('selected',)):
            graph_plot_variable.number_of_benign_fault.config(state=NORMAL)
            graph_plot_variable.benign_fault_value_from.config(state=NORMAL)
            graph_plot_variable.benign_fault_value_to.config(state=NORMAL)
        elif checkbox_variable == "input_for_benign_faults" and (checkbox_name.state() == ('active', 'focus', 'hover') or checkbox_name.state() == ()):
            graph_plot_variable.number_of_benign_fault.delete(0, END)
            graph_plot_variable.benign_fault_value_from.delete(0, END)
            graph_plot_variable.benign_fault_value_to.delete(0, END)
            graph_plot_variable.number_of_benign_fault.config(state=DISABLED)
            graph_plot_variable.benign_fault_value_from.config(state=DISABLED)
            graph_plot_variable.benign_fault_value_to.config(state=DISABLED)

    if graph_plot_variable.deployment_variable.get() == "Uniform":
        popup_for_random.wm_title("Uniform")
        label_uniform = ttk.Label(popup_for_random, text="Input for Uniform Deployment")
        label_uniform.grid(row=0, columnspan=2, sticky="nsew", padx="5")
        label_number_of_sensors = ttk.Label(frame1, text="Total Number of Sensors : ")
        label_number_of_sensors.grid(row=0, column=0, sticky="nsew", padx="10")
        textbox_number_of_sensors = Entry(frame1)
        textbox_number_of_sensors.grid(row=0, column=1, sticky="nsew", padx="5")
        graph_plot_variable.textbox_number_of_sensors = textbox_number_of_sensors
        graph_plot_variable.sensor_density = ''

        frame_faulty_sensor = tk.Frame(frame3, borderwidth=1)
        frame_faulty_sensor.grid(row=0, columnspan=2, sticky="nsew")
        label_fault_ratio = ttk.Label(frame_faulty_sensor, text="Number of faulty sensors(out of total) :")
        label_fault_ratio.grid(row=0, column=0, sticky="nsew", padx="2")
        textbox_fault = Entry(frame_faulty_sensor)
        textbox_fault.grid(row=0, column=1, sticky="nsew", padx="5")

        frame_input_for_asymmetric_faults = tk.Frame(frame3, borderwidth=1, pady="5")
        frame_input_for_asymmetric_faults.grid(row=1, column=0, sticky="nsew")
        checkbox_for_input_for_asymmetric_faults = ttk.Checkbutton(frame_input_for_asymmetric_faults,
                                                                   text="Asymmetric faults : ", state='disable',
                                                                   command=lambda: activateCheck_for_checkbox(
                                                                       "input_for_asymmetric_faults",
                                                                       checkbox_for_input_for_asymmetric_faults))
        checkbox_for_input_for_asymmetric_faults.grid(row=0, column=0, sticky="nsew")

        asymmetric_textbox_fault = Entry(frame_input_for_asymmetric_faults)
        asymmetric_textbox_fault.grid(row=0, column=1, sticky="nsew", padx="5")

        label_from_asymmetric_fault_value = ttk.Label(frame_input_for_asymmetric_faults, text="From :")
        label_from_asymmetric_fault_value.grid(row=1, column=0, sticky="nsew", padx="10")
        textbox_from_asymmetric_fault_value = Entry(frame_input_for_asymmetric_faults)
        textbox_from_asymmetric_fault_value.grid(row=1, column=1, sticky="nsew", padx="5")

        label_to_asymmetric_fault_value = ttk.Label(frame_input_for_asymmetric_faults, text="To :")
        label_to_asymmetric_fault_value.grid(row=1, column=2, sticky="nsew", padx="10")
        textbox_to_asymmetric_fault_value = Entry(frame_input_for_asymmetric_faults)
        textbox_to_asymmetric_fault_value.grid(row=1, column=3, sticky="nsew", padx="5")

        frame_input_for_symmetric_faults = tk.Frame(frame3, borderwidth=1, pady="5")
        frame_input_for_symmetric_faults.grid(row=2, column=0, sticky="nsew")
        checkbox_for_input_for_symmetric_faults = ttk.Checkbutton(frame_input_for_symmetric_faults,
                                                                  text="Symmetric Faults :", state='disable',
                                                                  command=lambda: activateCheck_for_checkbox(
                                                                      "input_for_symmetric_faults",
                                                                      checkbox_for_input_for_symmetric_faults))
        checkbox_for_input_for_symmetric_faults.grid(row=0, column=0, sticky="nsew")

        symmetric_textbox_fault = Entry(frame_input_for_symmetric_faults)
        symmetric_textbox_fault.grid(row=0, column=1, sticky="nsew", padx="10")

        label_from_symmetric_fault_value = ttk.Label(frame_input_for_symmetric_faults, text="From :")
        label_from_symmetric_fault_value.grid(row=1, column=0, sticky="nsew", padx="10")
        textbox_from_symmetric_fault_value = Entry(frame_input_for_symmetric_faults)
        textbox_from_symmetric_fault_value.grid(row=1, column=1, sticky="nsew", padx="10")

        label_to_symmetric_fault_value = ttk.Label(frame_input_for_symmetric_faults, text="To :")
        label_to_symmetric_fault_value.grid(row=1, column=2, sticky="nsew", padx="10")
        textbox_to_symmetric_fault_value = Entry(frame_input_for_symmetric_faults)
        textbox_to_symmetric_fault_value.grid(row=1, column=3, sticky="nsew", padx="10")

        frame_input_for_benign_faults = tk.Frame(frame3, borderwidth=1, pady="5")
        frame_input_for_benign_faults.grid(row=3, column=0, sticky="nsew")
        checkbox_for_input_for_benign_faults = ttk.Checkbutton(frame_input_for_benign_faults, text="Benign Faults :",
                                                               state='disable',
                                                               command=lambda: activateCheck_for_checkbox(
                                                                   "input_for_benign_faults",
                                                                   checkbox_for_input_for_benign_faults))
        checkbox_for_input_for_benign_faults.grid(row=0, column=0, sticky="nsew")

        benign_textbox_fault = Entry(frame_input_for_benign_faults)
        benign_textbox_fault.grid(row=0, column=1, sticky="nsew", padx="29")

        label_from_benign_fault_value = ttk.Label(frame_input_for_benign_faults, text="From :")
        label_from_benign_fault_value.grid(row=1, column=0, sticky="nsew", padx="10")
        textbox_from_benign_fault_value = Entry(frame_input_for_benign_faults)
        textbox_from_benign_fault_value.grid(row=1, column=1, sticky="nsew", padx="29")

        label_to_benign_fault_value = ttk.Label(frame_input_for_benign_faults, text="To :")
        label_to_benign_fault_value.grid(row=1, column=2, sticky="nsew")
        textbox_to_benign_fault_value = Entry(frame_input_for_benign_faults)
        textbox_to_benign_fault_value.grid(row=1, column=3, sticky="nsew", padx="10")

        textbox_fault.config(state=DISABLED)
        asymmetric_textbox_fault.config(state=DISABLED)
        textbox_from_asymmetric_fault_value.config(state=DISABLED)
        textbox_to_asymmetric_fault_value.config(state=DISABLED)
        symmetric_textbox_fault.config(state=DISABLED)
        textbox_from_symmetric_fault_value.config(state=DISABLED)
        textbox_to_symmetric_fault_value.config(state=DISABLED)
        benign_textbox_fault.config(state=DISABLED)
        textbox_from_benign_fault_value.config(state=DISABLED)
        textbox_to_benign_fault_value.config(state=DISABLED)

    elif graph_plot_variable.deployment_variable.get() == "Poisson":
        popup_for_random.wm_title("Poisson")
        label_poisson = ttk.Label(popup_for_random, text="Input for Poisson Deployment")
        label_poisson.grid(row=0, columnspan=2, sticky="nsew", padx="5")
        label_sensor_density = ttk.Label(frame1, text="Sensor Density : ")
        label_sensor_density.grid(row=0, column=0, sticky="nsew", padx="10")
        textbox_sensor_density = Entry(frame1)
        textbox_sensor_density.grid(row=0, column=1, sticky="nsew",padx="5")
        graph_plot_variable.textbox_number_of_sensors = ''
        graph_plot_variable.sensor_density = textbox_sensor_density

        frame_faulty_sensor = tk.Frame(frame3, borderwidth=1)
        frame_faulty_sensor.grid(row=0, columnspan=2, sticky="nsew")
        label_fault_ratio = ttk.Label(frame_faulty_sensor, text="Ratio of faulty sensors :")
        label_fault_ratio.grid(row=0, column=0, sticky="nsew", padx="2")
        textbox_fault = Entry(frame_faulty_sensor)
        textbox_fault.grid(row=0, column=1, sticky="nsew", padx="5")

        frame_input_for_asymmetric_faults = tk.Frame(frame3, borderwidth=1, pady="5")
        frame_input_for_asymmetric_faults.grid(row=1, column=0, sticky="nsew")
        checkbox_for_input_for_asymmetric_faults = ttk.Checkbutton(frame_input_for_asymmetric_faults,
                                                                   text="Ratio of asymmetric faults : ", state='disable',
                                                                   command=lambda: activateCheck_for_checkbox(
                                                                       "input_for_asymmetric_faults",
                                                                       checkbox_for_input_for_asymmetric_faults))
        checkbox_for_input_for_asymmetric_faults.grid(row=0, column=0, sticky="nsew")

        asymmetric_textbox_fault = Entry(frame_input_for_asymmetric_faults)
        asymmetric_textbox_fault.grid(row=0, column=1, sticky="nsew", padx="5")

        label_from_asymmetric_fault_value = ttk.Label(frame_input_for_asymmetric_faults, text="From :")
        label_from_asymmetric_fault_value.grid(row=1, column=0, sticky="nsew", padx="10")
        textbox_from_asymmetric_fault_value = Entry(frame_input_for_asymmetric_faults)
        textbox_from_asymmetric_fault_value.grid(row=1, column=1, sticky="nsew", padx="5")

        label_to_asymmetric_fault_value = ttk.Label(frame_input_for_asymmetric_faults, text="To :")
        label_to_asymmetric_fault_value.grid(row=1, column=2, sticky="nsew", padx="10")
        textbox_to_asymmetric_fault_value = Entry(frame_input_for_asymmetric_faults)
        textbox_to_asymmetric_fault_value.grid(row=1, column=3, sticky="nsew", padx="5")

        frame_input_for_symmetric_faults = tk.Frame(frame3, borderwidth=1, pady="5")
        frame_input_for_symmetric_faults.grid(row=2, column=0, sticky="nsew")
        checkbox_for_input_for_symmetric_faults = ttk.Checkbutton(frame_input_for_symmetric_faults,
                                                                  text="Ratio of symmetric Faults :", state='disable',
                                                                  command=lambda: activateCheck_for_checkbox(
                                                                      "input_for_symmetric_faults",
                                                                      checkbox_for_input_for_symmetric_faults))
        checkbox_for_input_for_symmetric_faults.grid(row=0, column=0, sticky="nsew")

        symmetric_textbox_fault = Entry(frame_input_for_symmetric_faults)
        symmetric_textbox_fault.grid(row=0, column=1, sticky="nsew", padx="10")

        label_from_symmetric_fault_value = ttk.Label(frame_input_for_symmetric_faults, text="From :")
        label_from_symmetric_fault_value.grid(row=1, column=0, sticky="nsew", padx="10")
        textbox_from_symmetric_fault_value = Entry(frame_input_for_symmetric_faults)
        textbox_from_symmetric_fault_value.grid(row=1, column=1, sticky="nsew", padx="10")

        label_to_symmetric_fault_value = ttk.Label(frame_input_for_symmetric_faults, text="To :")
        label_to_symmetric_fault_value.grid(row=1, column=2, sticky="nsew", padx="10")
        textbox_to_symmetric_fault_value = Entry(frame_input_for_symmetric_faults)
        textbox_to_symmetric_fault_value.grid(row=1, column=3, sticky="nsew", padx="10")

        frame_input_for_benign_faults = tk.Frame(frame3, borderwidth=1, pady="5")
        frame_input_for_benign_faults.grid(row=3, column=0, sticky="nsew")
        checkbox_for_input_for_benign_faults = ttk.Checkbutton(frame_input_for_benign_faults, text="Ratio for benign Faults :",
                                                               state='disable',
                                                               command=lambda: activateCheck_for_checkbox(
                                                                   "input_for_benign_faults",
                                                                   checkbox_for_input_for_benign_faults))
        checkbox_for_input_for_benign_faults.grid(row=0, column=0, sticky="nsew")

        benign_textbox_fault = Entry(frame_input_for_benign_faults)
        benign_textbox_fault.grid(row=0, column=1, sticky="nsew", padx="29")

        label_from_benign_fault_value = ttk.Label(frame_input_for_benign_faults, text="From :")
        label_from_benign_fault_value.grid(row=1, column=0, sticky="nsew", padx="10")
        textbox_from_benign_fault_value = Entry(frame_input_for_benign_faults)
        textbox_from_benign_fault_value.grid(row=1, column=1, sticky="nsew", padx="29")

        label_to_benign_fault_value = ttk.Label(frame_input_for_benign_faults, text="To :")
        label_to_benign_fault_value.grid(row=1, column=2, sticky="nsew")
        textbox_to_benign_fault_value = Entry(frame_input_for_benign_faults)
        textbox_to_benign_fault_value.grid(row=1, column=3, sticky="nsew", padx="10")

    label_range = ttk.Label(popup_for_random, text="Range of Initial Values for non-faulty sensors")
    label_range.grid(row=2, columnspan=2, sticky="nsew", padx="5")
    label_from_range = ttk.Label(frame2, text="From : ")
    label_from_range.grid(row=0, column=0, sticky="nsew", padx="10")
    textbox_from_range = Entry(frame2)
    textbox_from_range.grid(row=0, column=1, sticky="nsew", padx="5")
    label_to_range = ttk.Label(frame2, text="To : ")
    label_to_range.grid(row=0, column=2, sticky="nsew", padx="10")
    textbox_to_range = Entry(frame2)
    textbox_to_range.grid(row=0, column=3, sticky="nsew", padx="5")
    graph_plot_variable.value_from_range = textbox_from_range
    graph_plot_variable.value_to_range = textbox_to_range
    graph_plot_variable.change_value_from_range = textbox_from_range
    graph_plot_variable.change_value_to_range = textbox_to_range
    frame_input_for_faults = tk.Frame(popup_for_random, borderwidth=1, pady="5")
    frame_input_for_faults.grid(row=4, columnspan=2, sticky="nsew")
    checkbox_for_input_for_faults = ttk.Checkbutton(frame_input_for_faults, text="Input for Faults", state='active',
                                            command=lambda : activateCheck_for_checkbox("input_for_faults", checkbox_for_input_for_faults))
    checkbox_for_input_for_faults.grid(row=4, column=0, sticky="nsew")

    textbox_fault.config(state=DISABLED)
    asymmetric_textbox_fault.config(state=DISABLED)
    textbox_from_asymmetric_fault_value.config(state=DISABLED)
    textbox_to_asymmetric_fault_value.config(state=DISABLED)
    symmetric_textbox_fault.config(state=DISABLED)
    textbox_from_symmetric_fault_value.config(state=DISABLED)
    textbox_to_symmetric_fault_value.config(state=DISABLED)
    benign_textbox_fault.config(state=DISABLED)
    textbox_from_benign_fault_value.config(state=DISABLED)
    textbox_to_benign_fault_value.config(state=DISABLED)

    graph_plot_variable.total_number_of_faults = textbox_fault
    graph_plot_variable.number_of_asymmetric_fault = asymmetric_textbox_fault
    graph_plot_variable.asymmetric_fault_value_from = textbox_from_asymmetric_fault_value
    graph_plot_variable.asymmetric_fault_value_to = textbox_to_asymmetric_fault_value
    graph_plot_variable.number_of_symmetric_fault = symmetric_textbox_fault
    graph_plot_variable.symmetric_fault_value_from = textbox_from_symmetric_fault_value
    graph_plot_variable.symmetric_fault_value_to = textbox_to_symmetric_fault_value
    graph_plot_variable.number_of_benign_fault = benign_textbox_fault
    graph_plot_variable.benign_fault_value_from = textbox_from_benign_fault_value
    graph_plot_variable.benign_fault_value_to = textbox_to_benign_fault_value

    # button_ok for another page for showing the graph and results
    button_ok = ttk.Button(popup_for_random, text="Next",
                           command=lambda: graph_for_random(frame, graph_plot_variable, popup_for_random, popup))
    button_ok.grid(row=6, column=0, sticky="nsew")
    button_cancel = ttk.Button(popup_for_random, text="Cancel",
                                           command=lambda: popup_for_random.destroy())
    button_cancel.grid(row=6, column=1, sticky="nsew")
    center(popup_for_random)
    popup_for_random.mainloop()


def graph_for_random(frame, graph_plot_variable, popup_for_random, popup):

    # navigating to Graph_Page page through frame.show()

    if graph_plot_variable.deployment_variable.get() == "Uniform":
        if not(check_for_float(graph_plot_variable.textbox_number_of_sensors.get())):
            call_validator(graph_plot_variable.textbox_number_of_sensors, popup_for_random, "Number of Sensors")
        elif not(isinstance(int(graph_plot_variable.textbox_number_of_sensors.get()), numbers.Real)):
            call_validator(graph_plot_variable.textbox_number_of_sensors, popup_for_random, "Number of Sensors")
        elif not(check_for_float(graph_plot_variable.value_from_range.get())):
            call_validator(graph_plot_variable.value_from_range, popup_for_random, "Range of values")
        elif not(isinstance(float(graph_plot_variable.value_from_range.get()), numbers.Real)):
            call_validator(graph_plot_variable.value_from_range, popup_for_random, "Range of values")
        elif not (check_for_float(graph_plot_variable.value_to_range.get())):
            call_validator(graph_plot_variable.value_to_range, popup_for_random, "Range of values")
        elif not (isinstance(float(graph_plot_variable.value_to_range.get()), numbers.Real)):
            call_validator(graph_plot_variable.value_to_range, popup_for_random, "Range of values")
        elif graph_plot_variable.total_number_of_faults.get()!= '':
            asymmetric = 0
            symmetric = 0
            benign = 0
            if graph_plot_variable.number_of_asymmetric_fault.get() != '':
                asymmetric = int(graph_plot_variable.number_of_asymmetric_fault.get())
            if graph_plot_variable.number_of_symmetric_fault.get() != '':
                symmetric = int(graph_plot_variable.number_of_symmetric_fault.get())
            if graph_plot_variable.number_of_benign_fault.get() != '':
                benign = int(graph_plot_variable.number_of_benign_fault.get())

            if asymmetric + symmetric + benign != int(graph_plot_variable.total_number_of_faults.get()):
                answer = messagebox.askokcancel("Warning!",
                                                "The sum of three types of the fault must be equal to the total number of faulty sensors")
                popup_for_random.tkraise()
            else:
                frame.show(graph_plot_variable)
                popup_for_random.destroy()
                popup.destroy()
                frame.tkraise()
        else:
            frame.show(graph_plot_variable)
            popup_for_random.destroy()
            popup.destroy()
            frame.tkraise()

    elif graph_plot_variable.deployment_variable.get() == "Poisson":
        if not(check_for_float(graph_plot_variable.sensor_density.get())):
            call_validator(graph_plot_variable.sensor_density, popup_for_random, "Sensor Density")
        elif not(isinstance(float(graph_plot_variable.sensor_density.get()), numbers.Real)):
            call_validator(graph_plot_variable.sensor_density, popup_for_random, "Sensor Density")
        elif not(check_for_float(graph_plot_variable.value_from_range.get())):
            call_validator(graph_plot_variable.value_from_range, popup_for_random, "Range of values")
        elif not(isinstance(float(graph_plot_variable.value_from_range.get()), numbers.Real)):
            call_validator(graph_plot_variable.value_from_range, popup_for_random, "Range of values")
        elif not (check_for_float(graph_plot_variable.value_to_range.get())):
            call_validator(graph_plot_variable.value_to_range, popup_for_random, "Range of values")
        elif not (isinstance(float(graph_plot_variable.value_to_range.get()), numbers.Real)):
            call_validator(graph_plot_variable.value_to_range, popup_for_random, "Range of values")
        elif graph_plot_variable.total_number_of_faults.get() != '':
            asymmetric = 0
            symmetric = 0
            benign = 0
            if graph_plot_variable.number_of_asymmetric_fault.get() != '':
                asymmetric = int(graph_plot_variable.number_of_asymmetric_fault.get())
            if graph_plot_variable.number_of_symmetric_fault.get() != '':
                symmetric = int(graph_plot_variable.number_of_symmetric_fault.get())
            if graph_plot_variable.number_of_benign_fault.get() != '':
                benign = int(graph_plot_variable.number_of_benign_fault.get())

            if asymmetric + symmetric + benign != int(100):
                answer = messagebox.askokcancel("Warning!",
                                                "The sum of ratios of all the three faults must be equal to the total ratio")
                popup_for_random.tkraise()
            else:
                frame.show(graph_plot_variable)
                popup_for_random.destroy()
                popup.destroy()
                frame.tkraise()
        else:
            frame.show(graph_plot_variable)
            popup_for_random.destroy()
            popup.destroy()
            frame.tkraise()


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    # win.deiconify()


class Network_Simulator_Main_Page(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Simulator")

        # main frame of the application

        container = tk.Frame(self)
        container.grid(row = 0,column=0, sticky = "nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # menu bar of the application
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command= lambda : self.entry_for_deployment_type(container))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu = filemenu)

        tk.Tk.config(self, menu=menubar)

    def show_frame(self, cont, graph_plot_variable, popup):
        frame = self.frames[cont]

        # check all the validations

        if not(check_for_float(graph_plot_variable.textbox_x.get())):
            call_validator(graph_plot_variable.textbox_x, popup, "x")
        elif not(check_for_float(graph_plot_variable.textbox_y.get())):
            call_validator(graph_plot_variable.textbox_y, popup, "y")
        elif not(check_for_float(graph_plot_variable.textbox_sensing_radius.get())):
            call_validator(graph_plot_variable.textbox_sensing_radius, popup, "sensing radius")
        elif not(isinstance(float(graph_plot_variable.textbox_x.get()), numbers.Real)):
            call_validator(graph_plot_variable.textbox_x, popup, "x")
        elif not(isinstance(float(graph_plot_variable.textbox_y.get()), numbers.Real)):
            call_validator(graph_plot_variable.textbox_y, popup, "y")
        elif not(isinstance(float(graph_plot_variable.textbox_sensing_radius.get()), numbers.Real)):
            call_validator(graph_plot_variable.textbox_sensing_radius, popup, "sensing radius")
        elif graph_plot_variable.deployment_variable.get() == "Choose deployment type":
            answer = messagebox.askokcancel("Warning!", "Choose a deployment type")
            popup.tkraise()
        elif graph_plot_variable.type_of_voting_algorithm.get() == "Choose algorithm type":
            answer = messagebox.askokcancel("Warning!", "Choose algorithm type")
            popup.tkraise()
        else:

            # another popup for random deployment entries
            frame_for_random(frame, graph_plot_variable,popup)


    def entry_for_deployment_type(self, container):
        global graph_plot_variable

        OPTIONS = [
            "Choose deployment type",
            "Uniform",
            "Poisson"
        ]

        VOTING_ALGORITHM = [
            "Choose algorithm type",
            "Fault-Tolerant Mean",
            "Fault-Tolerant Midpoint"
        ]
        # first popup window

        self.popup = tk.Tk()
        label_main = ttk.Label(self.popup, text="Input for Sensors")
        label_main.grid(row=0, column=0, sticky="nsew", padx="5")

        frame = tk.Frame(self.popup, borderwidth=1, padx="12", pady="15")
        frame.grid(row=1, columnspan=4, sticky="nsew")
        self.popup.wm_title("Entry for Deployment Type")
        label_field_size = ttk.Label(frame, text="Field Size:                            X : ")
        label_field_y = ttk.Label(frame, text="  Y : ")

        label_field_size.grid(row=0, column=1, sticky="nsew")
        label_field_y.grid(row=0, column=3, sticky="nsew")

        label_sensor_radius = ttk.Label(frame, text="Sensor Radius  :  ")
        label_sensor_radius.grid(row=1, column=1, sticky="nsew")

        textbox_x = Entry(frame)
        textbox_x.grid(row=0, column=2, sticky="nsew")
        textbox_x.focus()
        textbox_y = Entry(frame)
        textbox_y.grid(row=0, column=4, sticky="nsew")

        textbox_sensing_radius = Entry(frame)
        textbox_sensing_radius.grid(row=1, column=2, sticky="nsew")

        label_simulation_run = ttk.Label(frame, text="Number of simulation run  :  ")
        label_simulation_run.grid(row=2, column=1, sticky="nsew")
        textbox_simulation_run = Entry(frame)
        textbox_simulation_run.grid(row=2, column=2, sticky="nsew")

        # can add more frames or pages
        self.frames = {}
        frame_for_pages = Graph_Page(container, self)
        self.frames[Graph_Page] = frame_for_pages
        frame_for_pages.grid(row=0, column=0, sticky="nsew")

        variable = StringVar(self.popup)
        variable.set(OPTIONS[0])

        voting_algorithm = StringVar(self.popup)
        voting_algorithm.set(VOTING_ALGORITHM[0])

        label_deployment_type = ttk.Label(self.popup, text="Deployment Type : ")
        label_deployment_type.grid(row=3, column=0, columnspan=2, sticky="nsew", padx="5")

        deployment_type = OptionMenu(self.popup, variable, *OPTIONS)
        deployment_type.grid(row=3, column=1, columnspan=2, sticky="nsew")

        label_algorithm_type = ttk.Label(self.popup, text="Voting Algorithm Type : ")
        label_algorithm_type.grid(row=4, column=0, columnspan=2, sticky="nsew", padx="5")

        algorithm_type = OptionMenu(self.popup, voting_algorithm, *VOTING_ALGORITHM)
        algorithm_type.grid(row=4, column=1, columnspan=2, sticky="nsew")

        # an object of Graph_plot_variable
        graph_plot_variable = Graph_plot_variables(textbox_x, textbox_y, textbox_sensing_radius, textbox_simulation_run,"", variable, "", "", "", "", "", "", "", "", "", "", "", "", "", "", voting_algorithm, "", "", "", "", "", "", "", "", "", "", "", "")
        button_next = ttk.Button(self.popup, text="Next", command=lambda: self.show_frame(Graph_Page, graph_plot_variable,  self.popup))
        button_next.grid(row=5, column=0, sticky="nsew")
        button_clear = ttk.Button(self.popup, text="Clear", command=lambda: clear_all_entry(graph_plot_variable))
        button_clear.grid(row=5, column=1, sticky="nsew")
        button_cancel = ttk.Button(self.popup, text="Cancel", command=lambda: self.popup.destroy())
        button_cancel.grid(row=5, column=2, sticky="nsew")

        center(self.popup)
        self.popup.mainloop()


# application start

print("Hello")
simulator = Network_Simulator_Main_Page()
simulator.geometry("580x580")
simulator.mainloop()