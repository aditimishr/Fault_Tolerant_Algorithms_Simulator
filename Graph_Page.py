from tkinter import *
import tkinter as tk
from tkinter import ttk
import numbers
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from Graph_plot_variables import Graph_plot_variables
import numpy as np
from tkinter import messagebox

from Sensors import Sensors
from Fault_Tolerant_Algorithm import Fault_Tolerant_Algorithm
import random
import math
from matplotlib import gridspec
from Link_density_ratios import Link_density_ratios
from Link_densities_for_one_round import Link_densities_for_one_round

Insert_button_clicked = "No"
Delete_button_clicked = "No"
graph_plots = ""
sensors = []
paths = []
centreCircle = []
deleting_sensor = ""
check_for_sensing_radius = 0
check_for_is_faulty = 0
popup_for_insert = ""
inserting_sensor = ""
apply_algorithm = 0

# copy is used to differentiate between the sensors before adding, deleting or moving the sensors and after that.

sensor_copy = []
graph_plot_copy = []


def call_function(self_coming, sensor, graph_plots, frame_for_info):
    def on_configure(event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        canvas.configure(scrollregion=canvas.bbox('all'))

    frame_input_parameters = tk.Frame(frame_for_info, borderwidth=1, padx="30", pady="15")
    frame_input_parameters.grid(row=0, sticky="nsew")
    label = ttk.Label(frame_input_parameters, text="                      Input Parameters", anchor="center")
    label.grid(row=0, column=0, sticky="nsew")
    label.config(font=("Ariel", 12))

    frame_inputs = tk.Frame(frame_for_info, borderwidth=1, padx="12")
    frame_inputs.grid(row=2, sticky="nsew")
    label_size_of_field = ttk.Label(frame_inputs, text="Field size : ")
    label_size_of_field.grid(row=0, column=0, sticky="nsew")
    label_size_of_field.config(font=("Ariel", 8))

    label_size_of_field_user = ttk.Label(frame_inputs, text=graph_plots.textbox_x + " X " + graph_plots.textbox_y)
    label_size_of_field_user.grid(row=0, column=1, sticky="nsew")
    label_size_of_field_user.config(font=("Ariel", 8))

    label_radius_sensor = ttk.Label(frame_inputs, text="Sensor radius : ")
    label_radius_sensor.grid(row=1, column=0, sticky="nsew")
    label_radius_sensor.config(font=("Ariel", 8))

    label_radius_sensor_user = ttk.Label(frame_inputs, text=graph_plots.textbox_sensing_radius)
    label_radius_sensor_user.grid(row=1, column=1, sticky="nsew")
    label_radius_sensor_user.config(font=("Ariel", 8))

    label_deployment_type = ttk.Label(frame_inputs, text="Deployment Type : ")
    label_deployment_type.grid(row=2, column=0, sticky="nsew")
    label_deployment_type.config(font=("Ariel", 8))

    label_deployment_type_user = ttk.Label(frame_inputs, text=graph_plots.deployment_variable.get())
    label_deployment_type_user.grid(row=2, column=1, sticky="nsew")
    label_deployment_type_user.config(font=("Ariel", 8))

    label_number_of_sensors = ttk.Label(frame_inputs, text="Total number of Sensors : ")
    label_number_of_sensors.grid(row=3, column=0, sticky="nsew")
    label_number_of_sensors.config(font=("Ariel", 8))

    label_number_of_sensors_user = ttk.Label(frame_inputs, text=len(sensor))
    label_number_of_sensors_user.grid(row=3, column=1, sticky="nsew")
    label_number_of_sensors_user.config(font=("Ariel", 8))

    number_of_faults = 0
    for i in range(len(sensor)):
        if sensor[i].is_faulty:
            number_of_faults += 1

    number_of_correct_nodes = len(sensor) - number_of_faults
    label_number_of_correct_sensors = ttk.Label(frame_inputs, text="Number of correct sensors : ")
    label_number_of_correct_sensors.grid(row=4, column=0, sticky="nsew")
    label_number_of_correct_sensors.config(font=("Ariel", 8))

    label_number_of_correct_sensors_user = ttk.Label(frame_inputs, text=int(number_of_correct_nodes))
    label_number_of_correct_sensors_user.grid(row=4, column=1, sticky="nsew")
    label_number_of_correct_sensors_user.config(font=("Ariel", 8))

    label_range_of_correct_values = ttk.Label(frame_inputs, text="Range of initial correct values : ")
    label_range_of_correct_values.grid(row=5, column=0, sticky="nsew")
    label_range_of_correct_values.config(font=("Ariel", 8))

    label_range_of_correct_values_user = ttk.Label(frame_inputs, text=str(int(graph_plots.value_from_range))+" to "+str(int(graph_plots.value_to_range)))
    label_range_of_correct_values_user.grid(row=5, column=1, sticky="nsew")
    label_range_of_correct_values_user.config(font=("Ariel", 8))

    label_number_of_faulty_sensors = ttk.Label(frame_inputs, text="Number of faulty sensors : ")
    label_number_of_faulty_sensors.grid(row=6, column=0, sticky="nsew")
    label_number_of_faulty_sensors.config(font=("Ariel", 8))

    label_number_of_faulty_sensors_user = ttk.Label(frame_inputs, text=int(number_of_faults))
    label_number_of_faulty_sensors_user.grid(row=6, column=1, sticky="nsew")
    label_number_of_faulty_sensors_user.config(font=("Ariel", 8))

    if graph_plots.number_of_asymmetric_fault != '':
        label_number_of_faulty_sensors = ttk.Label(frame_inputs, text="Asymmetric Faults : ")
        label_number_of_faulty_sensors.grid(row=7, column=0, sticky="nsew")
        label_number_of_faulty_sensors.config(font=("Ariel", 8))

        label_number_of_faulty_sensors_user = ttk.Label(frame_inputs, text=int(graph_plots.number_of_asymmetric_fault))
        label_number_of_faulty_sensors_user.grid(row=7, column=1, sticky="nsew")
        label_number_of_faulty_sensors_user.config(font=("Ariel", 8))

        label_number_of_faulty_sensors = ttk.Label(frame_inputs, text="Range of values for Asymmetric Faults : ")
        label_number_of_faulty_sensors.grid(row=8, column=0, sticky="nsew")
        label_number_of_faulty_sensors.config(font=("Ariel", 8))

        label_number_of_faulty_sensors_user = ttk.Label(frame_inputs, text=str(int(graph_plots.asymmetric_fault_value_from))+" to "+str(int(graph_plots.asymmetric_fault_value_to)))
        label_number_of_faulty_sensors_user.grid(row=8, column=1, sticky="nsew")
        label_number_of_faulty_sensors_user.config(font=("Ariel", 8))

    if graph_plots.number_of_symmetric_fault !='':
        label_number_of_faulty_sensors = ttk.Label(frame_inputs, text="Symmetric Faults : ")
        label_number_of_faulty_sensors.grid(row=9, column=0, sticky="nsew")
        label_number_of_faulty_sensors.config(font=("Ariel", 8))

        label_number_of_faulty_sensors_user = ttk.Label(frame_inputs, text=int(graph_plots.number_of_symmetric_fault))
        label_number_of_faulty_sensors_user.grid(row=9, column=1, sticky="nsew")
        label_number_of_faulty_sensors_user.config(font=("Ariel", 8))

        label_number_of_faulty_sensors = ttk.Label(frame_inputs, text="Range of values for Symmetric Faults : ")
        label_number_of_faulty_sensors.grid(row=10, column=0, sticky="nsew")
        label_number_of_faulty_sensors.config(font=("Ariel", 8))

        label_number_of_faulty_sensors_user = ttk.Label(frame_inputs, text=str(
            int(graph_plots.symmetric_fault_value_from)) + " to " + str(int(graph_plots.symmetric_fault_value_to)))
        label_number_of_faulty_sensors_user.grid(row=10, column=1, sticky="nsew")
        label_number_of_faulty_sensors_user.config(font=("Ariel", 8))

    if graph_plots.number_of_benign_fault != '':
        label_number_of_faulty_sensors = ttk.Label(frame_inputs, text="Benign Faults : ")
        label_number_of_faulty_sensors.grid(row=11, column=0, sticky="nsew")
        label_number_of_faulty_sensors.config(font=("Ariel", 8))

        label_number_of_faulty_sensors_user = ttk.Label(frame_inputs, text=int(graph_plots.number_of_benign_fault))
        label_number_of_faulty_sensors_user.grid(row=11, column=1, sticky="nsew")
        label_number_of_faulty_sensors_user.config(font=("Ariel", 8))

        label_number_of_faulty_sensors = ttk.Label(frame_inputs, text="Range of values for Benign Faults : ")
        label_number_of_faulty_sensors.grid(row=12, column=0, sticky="nsew")
        label_number_of_faulty_sensors.config(font=("Ariel", 8))

        label_number_of_faulty_sensors_user = ttk.Label(frame_inputs, text=str(
            int(graph_plots.benign_fault_value_from)) + " to " + str(int(graph_plots.benign_fault_value_to)))
        label_number_of_faulty_sensors_user.grid(row=12, column=1, sticky="nsew")
        label_number_of_faulty_sensors_user.config(font=("Ariel", 8))

    if graph_plots.deployment_variable.get() == "Poisson":
        label_range_of_faulty_values = ttk.Label(frame_inputs, text="Sensor Density : ")
        label_range_of_faulty_values.grid(row=8, column=0, sticky="nsew")
        label_range_of_faulty_values.config(font=("Ariel", 10))

        label_range_of_faulty_values_user = ttk.Label(frame_inputs, text=graph_plots.sensor_density)
        label_range_of_faulty_values_user.grid(row=8, column=1, sticky="nsew")
        label_range_of_faulty_values_user.config(font=("Ariel", 10))

    sep = ttk.Separator(frame_for_info, orient=tk.HORIZONTAL)
    sep.grid(row=3, sticky="nsew")
    frame_output_parameters = tk.Frame(frame_for_info, borderwidth=1, padx="30", pady="15")
    frame_output_parameters.grid(row=4, sticky="nsew")
    label_output = ttk.Label(frame_output_parameters, text="                       Output", anchor="center")
    label_output.grid(row=0, column=0, sticky="nsew")
    label_output.config(font=("Ariel", 12))

    frame_outputs = tk.Frame(frame_for_info, borderwidth=1, padx="12")
    frame_outputs.grid(row=5, sticky="nsew")

    label_type_of_algorithm = ttk.Label(frame_outputs, text="Type of Algorithm : ")
    label_type_of_algorithm.grid(row=0, column=0, sticky="nsew")
    label_type_of_algorithm.config(font=("Ariel", 10))

    label_type_of_algorithm_user = ttk.Label(frame_outputs, text=graph_plots.type_of_voting_algorithm.get())
    label_type_of_algorithm_user.grid(row=0, column=1, sticky="nsew")
    label_type_of_algorithm_user.config(font=("Ariel", 10))

    label_agreement = ttk.Label(frame_outputs, text="Agreement Reached : ")
    label_agreement.grid(row=1, column=0, sticky="nsew")
    label_agreement.config(font=("Ariel", 10))

    label_agreement_result = ttk.Label(frame_outputs, text=graph_plots.agreement_reached)
    label_agreement_result.grid(row=1, column=1, sticky="nsew")
    label_agreement_result.config(font=("Ariel", 10))

    label_agreement = ttk.Label(frame_outputs, text="Range of final correct values : ")
    label_agreement.grid(row=2, column=0, sticky="nsew")
    label_agreement.config(font=("Ariel", 10))

    label_agreement_result = ttk.Label(frame_outputs,
                                       text=str(round(graph_plots.change_value_from_range, 2)) + " to " + str(
                                           round(graph_plots.change_value_to_range, 2)))
    label_agreement_result.grid(row=2, column=1, sticky="nsew")
    label_agreement_result.config(font=("Ariel", 10))

    if graph_plots.agreement_reached == "Yes":
        label_agreement_rounds = ttk.Label(frame_outputs, text="Number of rounds : ")
        label_agreement_rounds.grid(row=3, column=0, sticky="nsew")
        label_agreement_rounds.config(font=("Ariel", 10))

        label_agreement_rounds_result = ttk.Label(frame_outputs, text=graph_plots.round_of_voting)
        label_agreement_rounds_result.grid(row=3, column=1, sticky="nsew")
        label_agreement_rounds_result.config(font=("Ariel", 10))

    sep = ttk.Separator(frame_for_info, orient=tk.HORIZONTAL)
    sep.grid(row=6, sticky="nsew")

    frame_sensors = tk.Frame(frame_for_info, borderwidth=1, padx="30", pady="15")
    frame_sensors.grid(row=7, sticky="nsew")
    label = ttk.Label(frame_sensors, text="                         Value of Sensors", anchor="center")
    label.grid(row=0, column=0, sticky="nsew")
    label.config(font=("Ariel", 12))

    label = ttk.Label(frame_sensors, text="Coordinates", anchor="center")
    label.grid(row=1, column=0, sticky="nsew")
    label.config(font=("Ariel", 10))

    label = ttk.Label(frame_sensors, text="Value", anchor="center")
    label.grid(row=1, column=1, sticky="nsew")
    label.config(font=("Ariel", 10))

    label = ttk.Label(frame_sensors, text="          Is faulty", anchor="center")
    label.grid(row=1, column=2, sticky="nsew")
    label.config(font=("Ariel", 10))

    frame_value_sensors = tk.Frame(frame_for_info, borderwidth=1, padx="12")
    frame_value_sensors.grid(row=8, column=0, sticky="nsew")

    canvas = tk.Canvas(frame_value_sensors)
    canvas.pack(side=tk.LEFT)

    scrollbar = tk.Scrollbar(frame_value_sensors, command=canvas.yview)
    scrollbar.pack(side=tk.LEFT, fill='y')

    canvas.configure(yscrollcommand=scrollbar.set)

    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.bind('<Configure>', on_configure)

    # --- put frame in canvas ---

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    # --- add widgets in frame ---

    for i in range(len(sensor)):
        l1 = tk.Label(frame, text="Sensor " + str(sensor[i].id) + " :              (" + str(
            round(sensor[i].x_coordinate, 2)) + ", " + str(
            round(sensor[i].y_coordinate, 2)) + ")")
        # "+str(round(i.value,2))+"                 "+str(i.is_faulty))
        l1.grid(row=i, column=0, sticky="nsew")
        l2 = tk.Label(frame, text="                        " + str(round(sensor[i].value, 2)))
        l2.grid(row=i, column=1, sticky="nsew")
        l3 = tk.Label(frame, text="                " + str(sensor[i].is_faulty))
        l3.grid(row=i, column=2, sticky="nsew")

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


def check_for_float(entry):
    try:
        float(entry)
        return True
    except ValueError:
        return False


def on_click(event):
    # called when user clicks on the field
    global Insert_button_clicked
    global Delete_button_clicked
    global sensors
    global paths
    global centreCircle
    global deleting_sensor
    global graph_plots
    global popup_for_insert
    global apply_algorithm
    global sensor_copy
    global graph_plot_copy
    if event.inaxes is not None:
        print(event.xdata, event.ydata)
        x = event.xdata
        y = event.ydata
        if int(graph_plots.textbox_sensing_radius) > 1:
            x1 = round(x - 1, 1)
            x2 = round(x + 1, 1)
            y1 = round(y - 1, 1)
            y2 = round(y + 1, 1)
        else:
            x1 = round(x - 0.1, 2)
            x2 = round(x + 0.1, 2)
            y1 = round(y - 0.1, 2)
            y2 = round(y + 0.1, 2)

        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0
        if x2 > float(graph_plots.textbox_x):
            x2 = float(graph_plots.textbox_x)
        if y2 > float(graph_plots.textbox_y):
            y2 = float(graph_plots.textbox_y)

        id = -1
        if int(graph_plots.textbox_sensing_radius) > 1:
            for sens in range(len(sensors)):
                for x_coordinate in np.arange(x1, x2, 0.1):
                    for_x = round(x_coordinate, 1)
                    for y_coordinate in np.arange(y1, y2, 0.1):
                        for_y = round(y_coordinate, 1)
                        if (round(sensors[sens].x_coordinate, 1) == for_x and round(sensors[sens].y_coordinate, 1) == for_y):
                            id = sensors[sens].id
                            break
        else:
            for sens in range(len(sensors)):
                for x_coordinate in np.arange(x1, x2, 0.01):
                    for_x = round(x_coordinate, 2)
                    for y_coordinate in np.arange(y1, y2, 0.01):
                        for_y = round(y_coordinate, 2)
                        if (round(sensors[sens].x_coordinate, 2) == for_x and round(sensors[sens].y_coordinate, 2) == for_y):
                            id = sensors[sens].id
                            break

        graph_plots.round_of_voting = 0
        graph_plots.change_value_from_range = graph_plots.value_from_range
        graph_plots.change_value_to_range = graph_plots.value_to_range
        graph_plots.value_diameter = graph_plots.value_diameter = float(graph_plots.change_value_to_range) - float(graph_plots.change_value_from_range)
        if Insert_button_clicked == "Yes":
            Insert_button_clicked = "No"
            insert_sensor(x, y, "")
            apply_algorithm = 1
            if popup_for_insert != "":
                popup_for_insert.destroy()
        elif Insert_button_clicked == "move":
            Insert_button_clicked = "No"
            if deleting_sensor.id!=-1:
                delete_sensor(deleting_sensor.id)
            insert_sensor(x, y, deleting_sensor)
            deleting_sensor = ""
            apply_algorithm = 1
        elif Delete_button_clicked == "Yes":
            Delete_button_clicked = "No"
            delete_sensor(id)
            apply_algorithm = 1
        else:
            if int(graph_plots.textbox_sensing_radius) > 1:
                for sens in range(len(sensors)):
                    for x_coordinate in np.arange(x1, x2, 0.1):
                        for_x = round(x_coordinate, 1)
                        for y_coordinate in np.arange(y1, y2, 0.1):
                            for_y = round(y_coordinate, 1)
                            if (round(sensors[sens].x_coordinate, 1) == for_x and round(sensors[sens].y_coordinate,
                                                                                        1) == for_y):
                                answer = messagebox.askokcancel("Warning!",
                                                                "Click inside the field to place this sensor")
                                if answer:
                                    deleting_sensor = sensors[sens]
                                    Insert_button_clicked = "move"
                                break
            else:
                for sens in range(len(sensors)):
                    for x_coordinate in np.arange(x1, x2, 0.01):
                        for_x = round(x_coordinate, 2)
                        for y_coordinate in np.arange(y1, y2, 0.01):
                            for_y = round(y_coordinate, 2)
                            if (round(sensors[sens].x_coordinate, 2) == for_x and round(sensors[sens].y_coordinate,
                                                                                        2) == for_y):
                                answer = messagebox.askokcancel("Warning!",
                                                                "Click inside the field to place this sensor")
                                if answer:
                                    deleting_sensor = sensors[sens]
                                    Insert_button_clicked = "move"
                                break

    else:
        print('Clicked ouside axes bounds but inside plot window')

    # when any sensor is inserted or deleted or moved from the fiels
    if apply_algorithm == 1:
        apply_algorithm = 0
        fault = Fault_Tolerant_Algorithm(sensors, graph_plots, sensor_copy, graph_plot_copy)
        fault.put_result()
        print(graph_plots.round_of_voting)


def insert_sensor(x, y, deleting_node):

    # this method is called after clicking on the field to change the parameters of sensors and graph_plots
    global graph_plots
    global sensors
    global inserting_sensor
    global check_for_sensing_radius
    global check_for_is_faulty
    sensing_radius = ""
    graph_plots.number_of_sensor_for_both = graph_plots.number_of_sensor_for_both + 1
    if deleting_node!="":
        selecting_id = deleting_node.id
        neighbors = deleting_node.neighbor
        neighbors_id = deleting_node.neighbors_id
        multiset = deleting_node.multiset
        value = deleting_node.value
        is_faulty = deleting_node.is_faulty
        sensing_radius = deleting_node.sensor_radius
        if is_faulty!="" and is_faulty==False:
            color = "red"
        else:
            color = "blue"
    else:
        selecting_id = graph_plots.number_of_sensor_for_both-1
        neighbors = ""
        neighbors_id = ""
        multiset = ""
        if check_for_is_faulty == 1:
            is_faulty = True
            color = "blue"
            value = np.random.uniform(float(graph_plots.fault_value_from), float(graph_plots.fault_value_to))
        else:
            value = np.random.uniform(float(graph_plots.value_from_range), float(graph_plots.value_to_range))
            if float(value) < float(graph_plots.change_value_from_range) or float(value) > float(graph_plots.change_value_to_range):
                is_faulty = True
                color = "blue"
            else:
                is_faulty = False
                color = "red"
        if check_for_sensing_radius == 1:
            if inserting_sensor.sensor_radius != "":
                sensing_radius = inserting_sensor.sensor_radius
        else:
            sensing_radius = graph_plots.textbox_sensing_radius

    sensors.append(Sensors(selecting_id, x, y, sensing_radius, neighbors, neighbors_id, value, "", multiset, is_faulty, value))
    graph_plots.paths.append(graph_plots.subplot.scatter(x, y))
    centreCircle.append(plt.Circle((x, y), float(sensing_radius), color=color, alpha=0.2))
    graph_plots.subplot.add_artist(centreCircle[graph_plots.number_of_sensor_for_both - 1])
    graph_plots.canvas.draw()


def delete_sensor(id):
    global graph_plots
    global sensors
    for i in range(len(sensors)):
        if sensors[i].id == id:
            sensors.remove(sensors[i])
            graph_plots.paths[i].remove()
            graph_plots.paths.remove(paths[i])
            centreCircle[i].remove()
            centreCircle.remove(centreCircle[i])
            break
    graph_plots.number_of_sensor_for_both = graph_plots.number_of_sensor_for_both - 1
    graph_plots.canvas.draw()
    graph_plots.canvas.mpl_connect('button_press_event', on_click)


def poisson(lambda_number,area):
    L = math.exp(-(lambda_number*area))
    p = 1.0
    k = 0

    while(p>L):
        k = k+1
        p = p * random.uniform(0, 1)

    return k-1


def click_delete_sensors():
    answer = messagebox.askokcancel("Warning!", "Select a Sensor to delete")
    if answer:
        global Delete_button_clicked
        Delete_button_clicked = "Yes"


def input_for_insert_sensor():

    # UI for inserting a sensor
        global check_for_sensing_radius
        global check_for_is_faulty
        global popup_for_insert
        global inserting_sensor
        global graph_plots
        check_for_sensing_radius = 0
        check_for_is_faulty = 0
        popup_for_insert = ""
        inserting_sensor.sensor_radius = ''
        popup = tk.Tk()
        label_input_for_sensor = ttk.Label(popup, text="Input for Sensor")
        label_input_for_sensor.grid(row=0, column=0, sticky="nsew", padx="5")
        popup.wm_title("Insert Sensor")
        frame = tk.Frame(popup, borderwidth=1, padx="12", pady="15")
        frame.grid(row=2, columnspan=4, sticky="nsew")

        label_input_for_sensor = ttk.Label(frame, text="Sensor radius : ")
        label_input_for_sensor.grid(row=0, column=0, sticky="nsew", padx="5")
        textbox_change_sensor_radius = Entry(frame)
        textbox_change_sensor_radius.grid(row=0, column=1, sticky="nsew")

        label_input = ttk.Label(popup, text="Fault Range")
        label_input.grid(row=4, column=0, sticky="nsew", padx="5")

        frame1 = tk.Frame(popup, borderwidth=1, padx="12", pady="5")
        frame1.grid(row=5, columnspan=4, sticky="nsew")
        label_input_from = ttk.Label(frame1, text="From : ")
        label_input_from.grid(row=0, column=0, sticky="nsew", padx="5")
        textbox_from = Entry(frame1)
        textbox_from.grid(row=0, column=1, sticky="nsew")
        label_input_to = ttk.Label(frame1, text="To : ")
        label_input_to.grid(row=0, column=2, sticky="nsew", padx="5")
        textbox_to = Entry(frame1)
        textbox_to.grid(row=0, column=3, sticky="nsew")

        def activateCheck_for_checkbox1():
            global check_for_sensing_radius
            if check_for_sensing_radius == 0:
                textbox_change_sensor_radius.config(state=NORMAL)
                check_for_sensing_radius = 1
            else:
                check_for_sensing_radius = 0
                textbox_change_sensor_radius.config(state=DISABLED)

        def activateCheck_for_checkbox2():
            global check_for_is_faulty
            if check_for_is_faulty == 0:
                textbox_from.config(state=NORMAL)
                textbox_to.config(state=NORMAL)
                check_for_is_faulty = 1
            else:
                check_for_is_faulty = 0
                textbox_from.config(state=DISABLED)
                textbox_to.config(state=DISABLED)

        var1 = IntVar()
        frame_for_checkbox1 = tk.Frame(popup, borderwidth=1, padx="12", pady="5")
        frame_for_checkbox1.grid(row=1, columnspan=4, sticky="nsew")
        Checkbutton(frame_for_checkbox1, text='Change sensor radius', var=var1,
                    command=lambda :activateCheck_for_checkbox1()).grid(row=0, column=0, sticky="nsew")

        var2 = IntVar()
        frame_for_checkbox2 = tk.Frame(popup, borderwidth=1, padx="12", pady="5")
        frame_for_checkbox2.grid(row=3, columnspan=4, sticky="nsew")
        Checkbutton(frame_for_checkbox2, text='Is Faulty', var=var2,
                    command=lambda: activateCheck_for_checkbox2()).grid(row=0, column=0, sticky="nsew")

        textbox_change_sensor_radius.config(state=DISABLED)
        textbox_from.config(state=DISABLED)
        textbox_to.config(state=DISABLED)

        Button(popup, text='Insert', command=lambda: click_insert_sensor(popup, textbox_change_sensor_radius, textbox_from, textbox_to)).grid(
            column=0, row=6, sticky="nsew")
        center(popup)


def click_insert_sensor(popup, textbox_change_sensor_radius, textbox_from, textbox_to):
    # check for all the validation while inserting any node
    global check_for_sensing_radius
    global check_for_is_faulty
    global Insert_button_clicked
    global popup_for_insert
    global inserting_sensor
    global graph_plots
    popup_for_insert = popup

    # check if checkbox is checked but no entry in their respective textbox
    if check_for_sensing_radius == 1 and check_for_is_faulty == 1:
        if check_for_float(textbox_change_sensor_radius.get()) and check_for_float(textbox_from.get()) and check_for_float(textbox_to.get()) and isinstance(float(textbox_change_sensor_radius.get()), numbers.Real) and isinstance(float(textbox_from.get()), numbers.Real) and isinstance(float(textbox_to.get()), numbers.Real):
            answer = messagebox.askokcancel("Warning!", "Click inside the field to insert Sensor")
            if answer:
                inserting_sensor.sensor_radius = textbox_change_sensor_radius.get()
                graph_plots.fault_value_from = textbox_from.get()
                graph_plots.fault_value_to = textbox_to.get()
                Insert_button_clicked = "Yes"
                # print(Insert_button_clicked)
        elif not(check_for_float(textbox_change_sensor_radius.get())) and not(isinstance(float(textbox_change_sensor_radius.get()), numbers.Real)):
            answer = messagebox.askokcancel("Warning!", "Enter a valid sensor radius value or uncheck the 'Change sensor radius' checkbox")
            popup.tkraise()
        else:
            answer = messagebox.askokcancel("Warning!",
                                                        "Enter a valid fault range or uncheck the 'Is Faulty' checkbox")
            popup.tkraise()

    elif check_for_sensing_radius == 1 and check_for_is_faulty == 0:
        if check_for_float(textbox_change_sensor_radius.get()) and isinstance(float(textbox_change_sensor_radius.get()), numbers.Real):
            answer = messagebox.askokcancel("Warning!", "Click inside the field to insert Sensor")
            if answer:
                inserting_sensor.sensor_radius = textbox_change_sensor_radius.get()
                Insert_button_clicked = "Yes"
                # print(Insert_button_clicked)
        else:
            answer = messagebox.askokcancel("Warning!", "Enter a valid sensor radius value or uncheck the 'Change sensor radius' checkbox")
            popup.tkraise()
    elif check_for_sensor_radius == 0 and check_for_is_faulty == 1:
        if check_for_float(textbox_from.get()) and isinstance(float(textbox_from.get()), numbers.Real) and check_for_float(textbox_to.get()) and isinstance(float(textbox_to.get()), numbers.Real):
            answer = messagebox.askokcancel("Warning!", "Click inside the field to insert Sensor")
            if answer:
                graph_plots.fault_value_from = textbox_from.get()
                graph_plots.fault_value_to = textbox_to.get()
                Insert_button_clicked = "Yes"
                # print(Insert_button_clicked)
        else:
            answer = messagebox.askokcancel("Warning!", "Enter a valid fault range or uncheck the 'Is Faulty' checkbox")
            popup.tkraise()
    else:

        # this window popups when everything is fine
        answer = messagebox.askokcancel("Warning!", "Click inside the field to insert Sensor")
        if answer:
            Insert_button_clicked = "Yes"
            # print(Insert_button_clicked)



class Graph_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

    def show(self, graph_plot_variable):
        global sensors
        global paths
        global centreCircle
        global graph_plots
        global check_for_sensor_radius
        global Insert_button_clicked
        global Delete_button_clicked
        global deleting_sensor
        global inserting_sensor
        global sensor_copy
        global graph_plot_copy
        average_number_of_rounds = []
        link_densities_ratio = []
        avg_convergence_rate = []
        label = tk.Label(self, text="Field")
        label.config(font=("Ariel", 16))
        label.grid(row = 0, columnspan = 25, sticky="nsew")
        label_result = tk.Label(self, text="Result 1")
        label_result.config(font=("Ariel", 16))
        label_result.grid(row=0, column=26, sticky="nsew")
        f = plt.Figure(figsize=(7, 7))
        gs = gridspec.GridSpec(1, 1)
        a = f.add_subplot(gs[:, :], aspect='equal')
        a.set_xlim([0, float(graph_plot_variable.textbox_x.get())])
        a.set_ylim([0, float(graph_plot_variable.textbox_y.get())])

        sensor_density = ""

        area = float(graph_plot_variable.textbox_x.get()) * float(graph_plot_variable.textbox_y.get())
        if not (graph_plot_variable.textbox_number_of_sensors == ''):
            number_of_sensors = int(graph_plot_variable.textbox_number_of_sensors.get())

        if graph_plot_variable.deployment_variable.get() == "Poisson":
            sensor_density = graph_plot_variable.sensor_density.get()
            number_of_sensors = poisson(float(graph_plot_variable.sensor_density.get()), area)
            if graph_plot_variable.total_number_of_faults.get() != '':
                number_of_faulty_sensors = (int(number_of_sensors) * float(graph_plot_variable.total_number_of_faults.get())) / 100
                graph_plot_variable.total_number_of_faults = math.ceil(number_of_faulty_sensors)
                left = graph_plot_variable.total_number_of_faults
                if graph_plot_variable.number_of_asymmetric_fault.get() != '':
                    asymmetric_faults = (graph_plot_variable.total_number_of_faults * int(
                        graph_plot_variable.number_of_asymmetric_fault.get())) / 100
                    graph_plot_variable.number_of_asymmetric_fault = math.ceil(asymmetric_faults)
                    left = left - graph_plot_variable.number_of_asymmetric_fault
                else:
                    graph_plot_variable.number_of_asymmetric_fault = ''
                if left > 0:
                    if graph_plot_variable.number_of_symmetric_fault.get() != '':
                        symmetric_faults = (number_of_faulty_sensors * int(
                            graph_plot_variable.number_of_symmetric_fault.get())) / 100
                        graph_plot_variable.number_of_symmetric_fault = int(symmetric_faults)
                    else:
                        graph_plot_variable.number_of_symmetric_fault = ''
                else:
                    graph_plot_variable.number_of_symmetric_fault = ''
                if left > 0:
                    if graph_plot_variable.number_of_benign_fault.get() != '':
                        benign_faults = (number_of_faulty_sensors * int(
                            graph_plot_variable.number_of_benign_fault.get())) / 100
                        graph_plot_variable.number_of_benign_fault = int(benign_faults)
                    else:
                        graph_plot_variable.number_of_benign_fault = ''
                else:
                    graph_plot_variable.number_of_benign_fault = ''
            else:
                graph_plot_variable.total_number_of_faults = ''

        else:
            # this is done to maintain the consistency between Entry widget and string entry
            graph_plot_variable.total_number_of_faults = graph_plot_variable.total_number_of_faults.get()
            graph_plot_variable.number_of_asymmetric_fault = graph_plot_variable.number_of_asymmetric_fault.get()
            graph_plot_variable.number_of_symmetric_fault = graph_plot_variable.number_of_symmetric_fault.get()
            graph_plot_variable.number_of_benign_fault = graph_plot_variable.number_of_benign_fault.get()

        # number of sensors for uniform or poisson
        graph_plot_variable.number_of_sensor_for_both = number_of_sensors

        for r in range(int(graph_plot_variable.textbox_simulation_run.get())):
            a.clear()
            check_for_sensor_radius = 0
            Insert_button_clicked = "No"
            Delete_button_clicked = "No"
            graph_plots = ""
            sensors = []
            paths = []
            centreCircle = []
            sensor_copy = []
            graph_plot_copy = []
            deleting_sensor = -1
            inserting_sensor = Sensors("", "", "", "", "", "", "", "", "", "", "", "", "", "",)

            # calculating random positions of the sensors
            x = np.random.uniform(0, float(graph_plot_variable.textbox_x.get()), number_of_sensors)
            y = np.random.uniform(0, float(graph_plot_variable.textbox_y.get()), number_of_sensors)

            if graph_plot_variable.total_number_of_faults != '':
                correct_sensors = number_of_sensors - int(graph_plot_variable.total_number_of_faults)
            else:
                correct_sensors = number_of_sensors
            manage_id = 0

            # placing sensors on the field with random values

            # for correct sensors
            for i in range(correct_sensors):
                value_of_sensor = np.random.uniform(float(graph_plot_variable.value_from_range.get()),
                                                    float(graph_plot_variable.value_to_range.get()))
                sensors.append(
                    Sensors(manage_id, x[manage_id], y[manage_id], graph_plot_variable.textbox_sensing_radius.get(), 0,
                            "",
                            value_of_sensor, "", "", False, value_of_sensor, "", "", ""))
                sensor_copy.append(
                    Sensors(manage_id, x[manage_id], y[manage_id], graph_plot_variable.textbox_sensing_radius.get(), 0,
                            "",
                            value_of_sensor, "", "", False, value_of_sensor, "", "", ""))
                paths.append(a.scatter(x[manage_id], y[manage_id]))
                centreCircle.append(
                    plt.Circle((x[manage_id], y[manage_id]), float(graph_plot_variable.textbox_sensing_radius.get()),
                               color="red", alpha=0.2))
                manage_id += 1

            # for asymmetric faults
            if graph_plot_variable.number_of_asymmetric_fault != '':
                for asym_fault in range(int(graph_plot_variable.number_of_asymmetric_fault)):
                    value_of_sensor = np.random.uniform(float(graph_plot_variable.asymmetric_fault_value_from.get()),
                                                        float(graph_plot_variable.asymmetric_fault_value_to.get()))
                    sensors.append(
                        Sensors(manage_id, x[manage_id], y[manage_id], graph_plot_variable.textbox_sensing_radius.get(),
                                0, "",
                                value_of_sensor, "", "", True, value_of_sensor, "", "a", ""))
                    sensor_copy.append(
                        Sensors(manage_id, x[manage_id], y[manage_id], graph_plot_variable.textbox_sensing_radius.get(),
                                0, "",
                                value_of_sensor, "", "", True, value_of_sensor, "", "a", ""))
                    paths.append(a.scatter(x[manage_id], y[manage_id]))
                    centreCircle.append(
                        plt.Circle((x[manage_id], y[manage_id]),
                                   float(graph_plot_variable.textbox_sensing_radius.get()),
                                   color="blue",
                                   alpha=0.2))
                    manage_id += 1

            # for symmetric faults
            if graph_plot_variable.number_of_symmetric_fault != '':
                for sym_fault in range(int(graph_plot_variable.number_of_symmetric_fault)):
                    value_of_sensor = np.random.uniform(float(graph_plot_variable.symmetric_fault_value_from.get()),
                                                        float(graph_plot_variable.symmetric_fault_value_to.get()))
                    sensors.append(
                        Sensors(manage_id, x[manage_id], y[manage_id], graph_plot_variable.textbox_sensing_radius.get(),
                                0, "",
                                value_of_sensor, "", "", True, value_of_sensor, "", "s", ""))
                    sensor_copy.append(
                        Sensors(manage_id, x[manage_id], y[manage_id], graph_plot_variable.textbox_sensing_radius.get(),
                                0, "",
                                value_of_sensor, "", "", True, value_of_sensor, "", "s", ""))
                    paths.append(a.scatter(x[manage_id], y[manage_id]))
                    centreCircle.append(
                        plt.Circle((x[manage_id], y[manage_id]),
                                   float(graph_plot_variable.textbox_sensing_radius.get()),
                                   color="blue",
                                   alpha=0.2))
                    manage_id += 1

            # for benign faults
            if graph_plot_variable.number_of_benign_fault != '':
                for sym_fault in range(int(graph_plot_variable.number_of_benign_fault)):
                    value_of_sensor = np.random.uniform(float(graph_plot_variable.benign_fault_value_from.get()),
                                                        float(graph_plot_variable.benign_fault_value_to.get()))
                    sensors.append(
                        Sensors(manage_id, x[manage_id], y[manage_id], graph_plot_variable.textbox_sensing_radius.get(),
                                0, "",
                                value_of_sensor, "", "", True, value_of_sensor, "", "b", ""))
                    sensor_copy.append(
                        Sensors(manage_id, x[manage_id], y[manage_id], graph_plot_variable.textbox_sensing_radius.get(),
                                0, "",
                                value_of_sensor, "", "", True, value_of_sensor, "", "b", ""))
                    paths.append(a.scatter(x[manage_id], y[manage_id]))
                    centreCircle.append(
                        plt.Circle((x[manage_id], y[manage_id]),
                                   float(graph_plot_variable.textbox_sensing_radius.get()),
                                   color="blue",
                                   alpha=0.2))
                    manage_id += 1
            # initializing graph_plots and graph_plot_copy and using it all around the application
            graph_plots = Graph_plot_variables(graph_plot_variable.textbox_x.get(), graph_plot_variable.textbox_y.get(),
                                               graph_plot_variable.textbox_sensing_radius.get(), graph_plot_variable.textbox_simulation_run.get(), "",
                                               graph_plot_variable.deployment_variable, sensor_density, a, "", f,
                                               graph_plot_variable.number_of_sensor_for_both, self, paths,
                                               graph_plot_variable.value_from_range.get(),
                                               graph_plot_variable.value_to_range.get(),
                                               graph_plot_variable.change_value_from_range.get(),
                                               graph_plot_variable.change_value_to_range.get(),
                                               graph_plot_variable.total_number_of_faults,
                                               graph_plot_variable.round_of_voting,
                                               graph_plot_variable.agreement_reached,
                                               graph_plot_variable.type_of_voting_algorithm, "", "",
                                               graph_plot_variable.number_of_asymmetric_fault,
                                               graph_plot_variable.asymmetric_fault_value_from.get(),
                                               graph_plot_variable.asymmetric_fault_value_to.get(),
                                               graph_plot_variable.number_of_symmetric_fault,
                                               graph_plot_variable.symmetric_fault_value_from.get(),
                                               graph_plot_variable.symmetric_fault_value_to.get(),
                                               graph_plot_variable.number_of_benign_fault,
                                               graph_plot_variable.benign_fault_value_from.get(),
                                               graph_plot_variable.benign_fault_value_to.get(), "")
            graph_plot_copy = Graph_plot_variables(graph_plot_variable.textbox_x.get(),
                                                   graph_plot_variable.textbox_y.get(),
                                                   graph_plot_variable.textbox_sensing_radius.get(), graph_plot_variable.textbox_simulation_run.get(), "",
                                                   graph_plot_variable.deployment_variable, sensor_density, a, "",
                                                   f,
                                                   graph_plot_variable.number_of_sensor_for_both, self, paths,
                                                   graph_plot_variable.value_from_range.get(),
                                                   graph_plot_variable.value_to_range.get(),
                                                   graph_plot_variable.change_value_from_range.get(),
                                                   graph_plot_variable.change_value_to_range.get(),
                                                   graph_plot_variable.total_number_of_faults,
                                                   graph_plot_variable.round_of_voting,
                                                   graph_plot_variable.agreement_reached,
                                                   graph_plot_variable.type_of_voting_algorithm, "", "",
                                                   graph_plot_variable.number_of_asymmetric_fault,
                                                   graph_plot_variable.asymmetric_fault_value_from.get(),
                                                   graph_plot_variable.asymmetric_fault_value_to.get(),
                                                   graph_plot_variable.number_of_symmetric_fault,
                                                   graph_plot_variable.symmetric_fault_value_from.get(),
                                                   graph_plot_variable.symmetric_fault_value_to.get(),
                                                   graph_plot_variable.number_of_benign_fault,
                                                   graph_plot_variable.benign_fault_value_from.get(),
                                                   graph_plot_variable.benign_fault_value_to.get(), "")

            graph_plots.round_of_voting = 0
            graph_plot_copy.round_of_voting = 0
            graph_plots.no_of_times_fault_tolerant_condition_fails = 0
            graph_plots.change_value_from_range = graph_plots.value_from_range
            graph_plots.change_value_to_range = graph_plots.value_to_range
            graph_plot_copy.change_value_from_range = graph_plots.value_from_range
            graph_plot_copy.change_value_to_range = graph_plots.value_to_range
            graph_plots.value_diameter = float(graph_plots.change_value_to_range) - float(
                graph_plots.change_value_from_range)
            graph_plot_copy.value_diameter = float(graph_plots.change_value_to_range) - float(
                graph_plots.change_value_from_range)
            fault = Fault_Tolerant_Algorithm(sensors, graph_plots, sensor_copy, graph_plot_copy)
            fault.put_result(r)

            link_density = []
            for i in sensors:
                link_density.append(i.neighbor)
            link_density.sort()
            max_link_density = link_density[len(link_density) - 1]

            # calculate number of rounds and convergence rate only when agreement is reached
            if graph_plots.agreement_reached == "Yes":
                average_number_of_rounds.append(graph_plots.round_of_voting)
                avg_convergence_rate.append(graph_plots.convergence_rate)

            # calculating the ratios of link densities
            list_for_one_round = []
            for j in range(0, max_link_density + 1):
                list_for_one_round.append(
                    Link_densities_for_one_round(j, link_density.count(j),
                                                 (link_density.count(j) / len(sensors)) * 100))
            link_densities_ratio.append(
                Link_density_ratios(r, list_for_one_round, graph_plots.agreement_reached, graph_plots.convergence_rate,
                                    graph_plots.no_of_times_fault_tolerant_condition_fails, graph_plots.round_of_voting))

        for i in range(len(centreCircle)):
            a.add_artist(centreCircle[i])

        # showing Graph page
        a.set_title("Sensors", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, rowspan=4, columnspan=25, sticky="nsew")

        # toolbar below the field frame
        toolbarFrame = Frame(self)
        toolbarFrame.grid(row=5, columnspan=17, sticky="nsew")
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
        toolbar.update()

        canvas.mpl_connect('button_press_event', on_click)

        graph_plot_variable.subplot = a
        graph_plot_variable.canvas = canvas
        graph_plot_variable.figure = f
        graph_plot_variable.paths = paths
        button_insert_node = tk.Button(self, text="Insert", command=lambda: input_for_insert_sensor())
        button_insert_node.grid(row=5, column=23, sticky="nsew")
        button_delete_node = tk.Button(self, text="Delete", command=lambda: click_delete_sensors())
        button_delete_node.grid(row=5, column=24, sticky="nsew")


        val = 0
        for i in average_number_of_rounds:
            val = val + i

        val1 = 0
        for i in avg_convergence_rate:
            val1 = val1 + i

        print("Average convergence rate:")
        if val1 != 0:
            print(round((val1/len(avg_convergence_rate)), 4))
        print("Average round of convergence:")

        # the following code is done because python round function does not give the accurate result

        if val != 0:
            round_of = round(val/len(average_number_of_rounds), 0)
            if int(round_of) - int(val/len(average_number_of_rounds)) >= 0.5:
                print(math.ceil(val/len(average_number_of_rounds)))
            else:
                print(round_of)

        # print all the link density ratios
        count_agreement = 0
        for k in link_densities_ratio:

            # print(k.ratio_list_of_round, k.agreement_reached)
            if k.agreement_reached == "Yes":
                count_agreement += 1
                print("Agreement reached for ", k.number_of_round, "simulation")
                print("Number of rounds to reach agreement for this simulation : ", k.round_of_voting)
                print("Convergence rate for this simulation : ", k.convergence_rate)
                print("Number of times the fault tolerant condition fails")
                print(graph_plots.no_of_times_fault_tolerant_condition_fails)  # number of times fault tolerant condition fails
                print("Now print link density ratio for a round")
                for j in k.ratio_list_of_round:
                    print(j.link_density, j.link_density_count, j.ratio)
            else:
                print("No agreement reached for ", k.number_of_round, "simulation")
                print(k.convergence_rate)
                print("Now print link density ratio for a round - no agreement")
                for j in k.ratio_list_of_round:
                    print(j.link_density, j.link_density_count, j.ratio)

        print("Number of times agreement is reached : ", count_agreement)

        frame_for_info = tk.Frame(self, borderwidth=2, relief="solid")
        frame_for_info.grid(row=1, rowspan=7, column=26, sticky="nsew")
        call_function(self, sensors, graph_plots, frame_for_info)
