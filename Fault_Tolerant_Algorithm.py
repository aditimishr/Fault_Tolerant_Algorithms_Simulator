import tkinter as tk
from Calculate_link_density import Calculate_link_density
sensors = []
graph_plots = ""
sensor_copy = []
graph_plots_copy = []
convergence_rate = []

class Fault_Tolerant_Algorithm:
    def __init__(self, sensors_from_graph_page, graph_plot_from_graph_page, sensor_copy1, graph_plot_copy1):
        global sensors
        global graph_plots
        global sensor_copy
        global graph_plots_copy
        sensors = sensors_from_graph_page
        graph_plots = graph_plot_from_graph_page
        sensor_copy = sensor_copy1
        graph_plots_copy = graph_plot_copy1

    def voting_function(self, sensors, graph_plots):

        # apply midpoint voting function and get the value
        for sens in range(len(sensors)):
            tau = 0  # tau is equal to number of malicious faults
            a = 0  # a is asymmetric faults
            s = 0  # s is symmetric faults
            b = 0  # b is benign faults

            # find the reduced multiset - removing the tau largest and tau smallest values from multiset
            trace_position = []   # this list will trace the positions of benign fault connected to the sensor
            reduced_multiset = []
            submultiset = []
            if sensors[sens].neighbor > 0:  # apply algorithm only when sensor has neighbors
                for value in range(len(sensors[sens].multiset)):
                    # first calculate the number of faulty neighbors
                    if sensors[sens].neighbors_type_of_fault[value] == "a":
                        a += 1
                    elif sensors[sens].neighbors_type_of_fault[value] == "s":
                        s += 1
                    elif sensors[sens].neighbors_type_of_fault[value] == "b":   # trace the position of benign faults
                        b += 1
                        trace_position.append(value)

                # check for the fault-tolerance condition whether there are enough number of nodes
                if int(len(sensors[sens].multiset) - 1) < int(3 * a + 2 * s + b + 1):  # -1 because multiset includes its own value also
                    graph_plots.no_of_times_fault_tolerant_condition_fails += 1

                # Now remove the benign faults corresponding to the position
                for value_place in reversed(trace_position):
                    if sensors[sens].neighbors_id[value_place] != sensors[sens].value:
                        sensors[sens].neighbors_id.remove(sensors[sens].neighbors_id[value_place])
                        sensors[sens].multiset.remove(sensors[sens].multiset[value_place])
                        sensors[sens].neighbors_faulty.remove(sensors[sens].neighbors_faulty[value_place])
                        sensors[sens].neighbors_type_of_fault.remove(sensors[sens].neighbors_type_of_fault[value_place])

                sensors[sens].multiset.sort()
                tau = a + s

                reduced_multiset = sensors[sens].multiset

                # forming a reduced multiset
                for value_in_multiset in range(tau):
                    if len(reduced_multiset) > 2:
                        reduced_multiset.remove(reduced_multiset[len(reduced_multiset) - 1])
                        reduced_multiset.remove(reduced_multiset[0])

                # after masking the faults, form sub-multiset according to the algorithms

                if len(reduced_multiset) > 1:
                    sensors[sens].previous_value = sensors[sens].value
                    if graph_plots.type_of_voting_algorithm.get() == "Fault-Tolerant Midpoint":
                        submultiset.append(reduced_multiset[0])
                        submultiset.append(reduced_multiset[len(reduced_multiset) - 1])
                    elif graph_plots.type_of_voting_algorithm.get() == "Fault-Tolerant Mean":
                        submultiset = reduced_multiset

                    # now take average of the elements in the submultiset

                    value = 0
                    for i in submultiset:
                        value = value + i

                    sensors[sens].value = value / len(reduced_multiset)

                elif len(reduced_multiset) == 1:
                    sensors[sens].previous_value = sensors[sens].value
                    sensors[sens].value = (reduced_multiset[0])
                else:
                    sensors[sens].previous_value = sensors[sens].value

            else:
                sensors[sens].previous_value = sensors[sens].value


    def check_for_agreement(self, sensors, graph_plots):
        global convergence_rate
        increase_link_density = 0
        graph_plots.round_of_voting += 1
        convergent_round = 0

        for sens1 in range(len(sensors)):
            if graph_plots.round_of_voting == 1:
                sensors[sens1].previous_value = 0

        calculate_link_density = Calculate_link_density(sensors, graph_plots)
        calculate_link_density.link_density()
        self.voting_function(sensors, graph_plots)

        # if round convergent then check for agreement reached or
        # not else check if the value diameter is equal to the previous value diameter

        all_correct_values = []
        for sens1 in range(len(sensors)):
            if not sensors[sens1].is_faulty:
                all_correct_values.append(sensors[sens1].value)
        if len(all_correct_values) > 0:
            all_correct_values.sort()
            value_diameter = all_correct_values[len(all_correct_values) - 1] - all_correct_values[0]

        # check for agreement first
        if value_diameter < 1:
            convergent_round = 0
        # check for convergent round
        else:
            if round(float(value_diameter), 2) < round(float(graph_plots.value_diameter), 2):
                convergent_round += 1
            # check if all correct values are equal to their previous values
            elif round(float(value_diameter), 2) >= round(float(graph_plots.value_diameter), 2):
                convergent_round -= 1
                for sens1 in range(len(sensors)):
                    if not sensors[sens1].is_faulty:
                        sensor_value = float(sensors[sens1].value)
                        sensor_previous_value = float(sensors[sens1].previous_value)
                        if round(sensor_value, 2) != round(sensor_previous_value, 2):
                            increase_link_density += 1

        # calculate the convergence rate c
        c = value_diameter/graph_plots.value_diameter
        graph_plots.change_value_from_range = all_correct_values[0]
        graph_plots.change_value_to_range = all_correct_values[len(all_correct_values) - 1]
        graph_plots.value_diameter = value_diameter

        # check for agreement condition
        if convergent_round == 0:
            convergence_rate.append(c)
            val = 0
            for i in convergence_rate:
                val = val + i
            graph_plots.convergence_rate = val / len(convergence_rate)
            graph_plots.agreement_reached = "Yes"
        elif convergent_round >= 1:
            convergence_rate.append(c)
            self.check_for_agreement(sensors, graph_plots)
        elif convergent_round < 0:
            # if values of all sensors are same as their previous value, then no agreement reached
            if increase_link_density > 0:
                self.check_for_agreement(sensors, graph_plots)
            else:
                graph_plots.agreement_reached = "No"

    def put_result(self_coming, r):
        global graph_plots
        global graph_plots_copy
        global sensors
        global sensor_copy
        global convergence_rate
        not_same = 0
        convergence_rate = []
        graph_plots.no_of_times_fault_tolerant_condition_fails = 0

        # check whether there is any change in the field
        # (this will be the case when we want to compare the results after inserting, deleting or moving the sensors)
        if len(sensors) != len(sensor_copy):
            not_same += 1
        else:
            for values in sensors:
                for values_copy in sensor_copy:
                    if values.id == values_copy.id:
                        if values.value != values_copy.value or values.x_coordinate != values_copy.x_coordinate or values.y_coordinate != values_copy.y_coordinate or values.sensor_radius != values_copy.sensor_radius:
                            not_same += 1

        if not_same == 0:
            self_coming.check_for_agreement(sensors, graph_plots)
        elif not_same > 0:
            for values in sensors:
                values.value = values.initial_value

            self_coming.check_for_agreement(sensors, graph_plots)
            self = graph_plots.adding_self
            label_result = tk.Label(self, text="Result 2")
            label_result.config(font=("Ariel", 16))
            label_result.grid(row=0, column=27, sticky="nsew")
            frame_for_info_two = tk.Frame(self, borderwidth=2, relief="solid")
            frame_for_info_two.grid(row=1, rowspan=7, column=27, sticky="nsew")
