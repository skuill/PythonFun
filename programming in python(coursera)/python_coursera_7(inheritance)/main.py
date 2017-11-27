class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        
    def get_photo_file_ext(self):
        filename, file_extension = os.path.splitext(self.photo_file_name)
        return file_extension
    
    def __str__(self):
        return 'car_type {}, brand {}, photo_file_name {}, extension {}, carrying {}'.format(self.car_type,
        self.brand,
        self.photo_file_name,
        self.get_photo_file_ext(),
        self.carrying)

class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        CarBase.__init__(self, car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
    def __str__(self):
        return '{}, passenger_seats_count {}'.format(CarBase.__str__(self), self.passenger_seats_count)


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        CarBase.__init__(self, car_type, brand, photo_file_name, carrying)
        if not body_whl:
            self.body_width = 0
            self.body_height = 0
            self.body_length = 0
        else:            
            self.body_length, self.body_width, self.body_height = tuple(map(float,body_whl.split('x')))
            
    def get_body_volume(self):
        return self.body_length*self.body_width*self.body_height
    def __str__(self):
        return '{}, get_body_volume {}'.format(CarBase.__str__(self), self.get_body_volume())

class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        CarBase.__init__(self, car_type, brand, photo_file_name, carrying)
        self.extra = extra
    def __str__(self):
        return '{}, extra {}'.format(CarBase.__str__(self), self.extra)


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if row:
                print (row)
                if (len(row) < 7):
                    print ('Недостаточно данных', row)
                if (row[0] == 'car'):
                    car_list.append(Car(row[0], row[1], row[3], row[5], row[2]))
                    continue
                if (row[0] == 'truck'):
                    car_list.append(Truck(row[0], row[1], row[3], row[5], row[4]))
                    continue
                if (row[0] == 'spec_machine'):
                    car_list.append(SpecMachine(row[0], row[1], row[3], row[5], row[6]))
                    continue
    return car_list

import os
import csv

cars = get_car_list('coursera_week3_cars.csv')
print("\n".join(str(car) for car in cars))