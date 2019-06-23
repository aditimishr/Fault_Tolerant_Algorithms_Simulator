import math
sensors_for_link_density = []
graph_plots_for_link_density = ""
multiset = []


class Calculate_link_density:
    def __init__(self, sensors, graph_plot):
        global sensors_for_link_density
        global graph_plots_for_link_density
        sensors_for_link_density = sensors
        graph_plots_for_link_density = graph_plot

    def link_density(self):

        # check how many sensors lie within the range of a outer_sensor
        for outer_sensor in range(len(sensors_for_link_density)):
            sensors_for_link_density[outer_sensor].neighbor = 0
            neighbors_id = [] # including itself

            # multiset is the data structure used for storing values of neighbors of every node
            # multiset is equal to V which is different for every node
            multiset = []
            neighbors_faulty = []
            type_of_fault = []

            neighbors_id.append(sensors_for_link_density[outer_sensor].id)
            # sensor sends value to itself also
            multiset.append(sensors_for_link_density[outer_sensor].value)

            # neighbors_faulty stores the corresponding data for
            # whether the neighbor node is faulty or not including itself
            neighbors_faulty.append(sensors_for_link_density[outer_sensor].is_faulty)

            if sensors_for_link_density[outer_sensor].is_faulty:
                type_of_fault.append(sensors_for_link_density[outer_sensor].type_of_fault)
            else:
                type_of_fault.append("")

            for inner_sensor in range(len(sensors_for_link_density)):

                # calculate Euclidean distance
                distance = math.sqrt(math.pow(sensors_for_link_density[outer_sensor].x_coordinate - sensors_for_link_density[inner_sensor].x_coordinate, 2) + math.pow(sensors_for_link_density[outer_sensor].y_coordinate - sensors_for_link_density[inner_sensor].y_coordinate, 2))

                # check if the distance is less than the sensor radius of outer sensor and id is not same
                if distance <= float(sensors_for_link_density[outer_sensor].sensor_radius) and sensors_for_link_density[outer_sensor].id!=sensors_for_link_density[inner_sensor].id:
                    sensors_for_link_density[outer_sensor].neighbor += 1
                    neighbors_id.append(sensors_for_link_density[inner_sensor].id)
                    multiset.append(sensors_for_link_density[inner_sensor].value)
                    neighbors_faulty.append(sensors_for_link_density[inner_sensor].is_faulty)
                    if sensors_for_link_density[inner_sensor].is_faulty:
                        type_of_fault.append(sensors_for_link_density[inner_sensor].type_of_fault)
                    else:
                        type_of_fault.append("")

            # neighbor_id for storing the id of the neighbors
            sensors_for_link_density[outer_sensor].neighbors_id = neighbors_id
            sensors_for_link_density[outer_sensor].multiset = multiset
            sensors_for_link_density[outer_sensor].neighbors_faulty = neighbors_faulty
            sensors_for_link_density[outer_sensor].neighbors_type_of_fault = type_of_fault


