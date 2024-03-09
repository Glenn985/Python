import tkinter as tk
from tkinter import messagebox
import os

from datetime import datetime, date,timedelta

Parking_list =[]


class billing:
    def __init__(self, vehiclenumber, timeofentry, type_of_Vehicle):
        self.vehiclenumber = vehiclenumber
        self.timeofentry = timeofentry
      
        self.type_of_Vehicle = type_of_Vehicle

class CarParking:
    def __init__(self, num_2W, num_4W, num_Truck, num_PhysicallyDisabled):
        self.num_2W = num_2W
        self.num_4W = num_4W
        self.num_Truck = num_Truck
        self.num_PhysicallyDisabled = num_PhysicallyDisabled

   

    def park_vehicle(self, vehicle_type):
        if vehicle_type == '2W':
            if self.num_2W > 0:
                self.num_2W -= 1
                self.update_remaining()
                return True
            else:
                print("No space available for 2-wheelers.")
                return False
        elif vehicle_type == '4W':
            if self.num_4W > 0:
                self.num_4W -= 1
                self.update_remaining()
                return True
            else:
                print("No space available for 4-wheelers.")
                return False
        elif vehicle_type == 'Truck':
            if self.num_Truck > 0:
                self.num_Truck -= 1
                self.update_remaining()
                return True
            else:
                print("No space available for trucks.")
                return False
        elif vehicle_type == 'PhysicallyDisabled':
            if self.num_PhysicallyDisabled > 0:
                self.num_PhysicallyDisabled -= 1
                self.update_remaining()
                return True
            else:
                print("No space available for physically disabled.")
                return False
        else:
            print("Invalid vehicle type.")
            return False

    def unpark_vehicle(self, vehicle_type):
        if vehicle_type == '2W':
            self.num_2W += 1
            self.update_remaining()
        elif vehicle_type == '4W':
            self.num_4W += 1
            self.update_remaining()
        elif vehicle_type == 'Truck':
            self.num_Truck += 1
            self.update_remaining()
        elif vehicle_type == 'PhysicallyDisabled':
            self.num_PhysicallyDisabled += 1
            self.update_remaining()
        else:
            print("Invalid vehicle type.")

    def update_remaining(self):
        app.update_remaining()

        print("f")

class ParkingApp(tk.Tk):
    def __init__(self):
        super().__init__() 

        self.label = tk.Label(self, text="Parking Management System", font=('Arial', 14))
        self.label.grid(row=0, column=0, columnspan=2, pady=5)

        self.label_remaining = tk.Label(self, text="")
        self.label_remaining.grid(row=1, column=0, columnspan=2, pady=5)

        # Entry widgets
        self.Entrypayment = tk.Entry(self, width=50)
        self.Entrypayment.grid(row=2, column=0, columnspan=2, pady=5)
        self.Entrypayment.insert(0, "Vehicle payment:")

        self.EntryNumber = tk.Entry(self, width=50)
        self.EntryNumber.grid(row=3, column=0, columnspan=2, pady=5)
        self.EntryNumber.insert(0, "Vehicle Number:")

        self.EntryUnpark = tk.Entry(self, width=50)
        self.EntryUnpark.grid(row=4, column=0, columnspan=2, pady=5)
        self.EntryUnpark.insert(0, "Unpark Vehicle Number:")

        # Buttons
        self.button_park_2W = tk.Button(self, text="Park 2-Wheeler", command=lambda: self.park_vehicle('2W'))
        self.button_park_2W.grid(row=5, column=0, padx=5, pady=5)

        self.button_unpark_2W = tk.Button(self, text="Unpark 2-Wheeler", command=lambda: self.unpark_vehicle('2W'))
        self.button_unpark_2W.grid(row=5, column=1, padx=5, pady=5)

        self.button_park_4W = tk.Button(self, text="Park 4-Wheeler", command=lambda: self.park_vehicle('4W'))
        self.button_park_4W.grid(row=6, column=0, padx=5, pady=5)

        self.button_unpark_4W = tk.Button(self, text="Unpark 4-Wheeler", command=lambda: self.unpark_vehicle('4W'))
        self.button_unpark_4W.grid(row=6, column=1, padx=5, pady=5)
        
        self.button_park_Truck = tk.Button(self, text="Park Truck", command=lambda: self.park_vehicle('Truck'))
        self.button_park_Truck.grid(row=7, column=0, padx=5, pady=5)

        self.button_unpark_Truck = tk.Button(self, text="Unpark Truck", command=lambda: self.unpark_vehicle('Truck'))
        self.button_unpark_Truck.grid(row=7, column=1, padx=5, pady=5)

        self.button_park_PD = tk.Button(self, text="Park Physically Disabled", command=lambda: self.park_vehicle('PhysicallyDisabled'))
        self.button_park_PD.grid(row=8, column=0, padx=5, pady=5)

        self.button_unpark_PD = tk.Button(self, text="Unpark Physically Disabled", command=lambda: self.unpark_vehicle('PhysicallyDisabled'))
        self.button_unpark_PD.grid(row=8, column=1, padx=5, pady=5)

        self.button_exit = tk.Button(self, text="Exit", command=self.destroy)
        self.button_exit.grid(row=9, column=0, columnspan=2, pady=5)

        self.parking_lot = CarParking(num_2W=10, num_4W=20, num_Truck=5, num_PhysicallyDisabled=2)
 
     
    
        
    def update_remaining(self):
        remaining_text = f"Remaining Spaces: 2W: {self.parking_lot.num_2W}, 4W: {self.parking_lot.num_4W}, Truck: {self.parking_lot.num_Truck}, Physically Disabled: {self.parking_lot.num_PhysicallyDisabled}"
        self.label_remaining.config(text=remaining_text)

    def park_vehicle(self, vehicle_type):
        if self.parking_lot.park_vehicle(vehicle_type):
            print(f"{vehicle_type} parked successfully!")
            entered_value = self.EntryNumber.get().split(":")[1].strip()
            payment_mode = self.Entrypayment.get().split(":")[1].strip()
            current_datetime = datetime.now()
        
            Parking_list.append(billing(entered_value,current_datetime, vehicle_type))
            response =  messagebox.showinfo("information","parked")
            Label(self,text=response).pack()
         
            
        else:
            print(f"Unable to park {vehicle_type}.")
            

    def unpark_vehicle(self, vehicle_type):
        self.parking_lot.unpark_vehicle(vehicle_type)
        print(f"{vehicle_type} unparked successfully!")
        payment_mode = self.Entrypayment.get().split(":")[1].strip()
        
        
        



        found = False
        Unpark_number = self.EntryUnpark.get().split(":")[1].strip()

        for bill in Parking_list:
          if Unpark_number == bill.vehiclenumber:
           unpark_datetime = datetime.now()
           Time_parked = (unpark_datetime - bill.timeofentry).total_seconds() / 3600
           file_path = "C:\\Users\\glenn\\OneDrive\\Desktop\\python\\File-forcarpark.txt"
           with open(file_path,'a') as file:
           

        # Calculate the bill based on the type of vehicle
            if bill.type_of_Vehicle == "Truck":
             bill_amount = Time_parked * 50
            elif bill.type_of_Vehicle == "2W":
             bill_amount = Time_parked * 10
            elif bill.type_of_Vehicle == "4W":
             bill_amount = Time_parked * 25
            elif bill.type_of_Vehicle == "PhysicallyDisabled":
              bill_amount = Time_parked * 5

        # Show the bill as a message info
            response = messagebox.showinfo("Bill", f"Your bill amount is: {bill_amount} {payment_mode}")
            content = f"Bill amount: {bill_amount}, Unpark datetime: {unpark_datetime}, Payment mode: {payment_mode}\n"
            file.write(content)

           
          found = True
          break

        if found:
         print("Yes")
        else:
         print("No")





       





if __name__ == "__main__":
    app = ParkingApp()
    app.mainloop()



#create a 2d  list for adding vehicle number and entry time of all parked vehicles and remove them from list when unpark button is pressed
#when unpark button pressed take current time subtract from the starting time to calculate the charges
