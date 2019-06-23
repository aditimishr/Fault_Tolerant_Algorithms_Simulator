
class Sensors:

    def __init__(self, id, x_coordinate, y_coordinate, sensor_radius, neighbor, neighbors_id, value, previous_value, multiset, is_faulty, initial_value, neighbors_faulty, type_of_fault, neighbors_type_of_fault):
        self.id = id
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.sensor_radius = sensor_radius
        self.neighbor = neighbor
        self.neighbors_id = neighbors_id
        self.value = value
        self.previous_value = previous_value
        self.multiset = multiset
        self.is_faulty = is_faulty
        self.initial_value = initial_value
        self.neighbors_faulty = neighbors_faulty
        self.type_of_fault = type_of_fault
        self.neighbors_type_of_fault = neighbors_type_of_fault