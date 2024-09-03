import tkinter as tk
from tkinter import messagebox
import os
import re
import matplotlib.pyplot as plt
import cv2
import easyocr
import customtkinter as ctk
from tkinter import ttk 

import socket
from threading import Thread
import time
 
  # Import the other file

from datetime import datetime, date,timedelta
#on opening up fill it correctly ,datetime change the way it looks,correct the button size and central align,encryption
#allow multiple laptops to run the same code using my own database



client = None  # Global client socket

def simple_hash(s):
    return sum(ord(char) for char in s) % 100

def run_client_side(): 
    global client
    server_IP = "localhost"
    server_Port = 9999

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((server_IP, server_Port)) 
        receive_thread = Thread(target=receiving_msg, args=(client,))
        receive_thread.start()

        # Can also start sending thread here if needed
        # send_thread = Thread(target=send_msg, args=(client,))
        # send_thread.start()

    except Exception as e:
        print(f"Failed to connect to the server: {e}")
        exit()

def receiving_msg(connection):
    try:
        while True:  # Keep receiving messages
            msg = connection.recv(1024).decode('utf-8')
            print(f"Server: {msg}") 
            return msg
    except Exception as e:
        print(f"Error receiving message: {e}")

def send_msg(connection, msg_send):
    try:
        connection.send(msg_send.encode('utf-8'))
    except Exception as e:
        print(f"Error sending message: {e}")

# Ensure client is initialized when the app starts
run_client_side()



Parking_list ={}
Plotting = []
input_Numberplate = 0

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

class ParkingApp(ctk.CTk):
    def __init__(self):
        super().__init__()



        

        self.frame = tk.Frame(self)
        self.frame.grid(row=1, column=2, rowspan=20, padx=10, pady=10, sticky='nsew')

        self.table = ttk.Treeview(self.frame, columns=('first', 'second', 'third', 'fourth', 'fifth'), show='headings')
        self.table.heading('first', text='Vehicle Number')
        self.table.heading('second', text='Time of Entry')
        self.table.heading('third', text='Time of Exit')
        self.table.heading('fourth', text='Fees Paid')
        self.table.heading('fifth', text='Additional Info')

        self.table.column('first', width=150)
        self.table.column('second', width=150)
        self.table.column('third', width=150)
        self.table.column('fourth', width=100)
        self.table.column('fifth', width=200)

        self.table.pack(expand=True, fill='both')
        
        options = ["Report", "today", "last 3 days"]

        # Create a CTkComboBox
        self.selected_option = tk.StringVar(self)
        self.selected_option.set("Report")  # Default value

        self.option_menu = ctk.CTkComboBox(self, values=options,command=self.get_reports)
        self.option_menu.grid(row=0, column=2)

        # Button to generate the report based on selected option
        

 
        



        self.selected_option = ctk.StringVar(self)
        self.selected_option.set("today")  # Default value for testing
        self.selected_option.trace("w", self.get_reports)



        self.label = ctk.CTkLabel(self, text="Parking Management System", font=('Arial', 14))
        self.label.grid(row=0, column=0, columnspan=2, pady=5)

        self.label_remaining = ctk.CTkLabel(self, text="")
        self.label_remaining.grid(row=14, column=0, columnspan=2, pady=5)

        # Entry widgets
        self.Entrypayment = ctk.CTkEntry(self, width=500)
        self.Entrypayment.grid(row=1, column=0)
        self.Entrypayment.insert(0, "Vehicle payment:")

        self.EntryNumber = ctk.CTkEntry(self, width=500)
        self.EntryNumber.grid(row=2, column=0, columnspan=1, pady=0)
        self.EntryNumber.insert(0, "Vehicle Number:")
        

         

        # Buttons
        self.button_park_2W = ctk.CTkButton(self, height=30,width=250, text="Park 2-Wheeler", command=lambda: self.park_vehicle('2W'))
        self.button_park_2W.grid(row=4, column=0,pady=2)

        self.button_unpark_2W = ctk.CTkButton(self,height=30,width=250, text="Unpark 2-Wheeler",fg_color="red", command=lambda: self.unpark_vehicle('2W'))
        self.button_unpark_2W.grid(row=5, column=0,pady=2)

        self.button_park_4W = ctk.CTkButton(self,height=30,width=250,text="Park 4-Wheeler", command=lambda: self.park_vehicle('4W'))
        self.button_park_4W.grid(row=6, column=0,pady=2)

        self.button_unpark_4W = ctk.CTkButton(self,height=30,width=250, text="Unpark 4-Wheeler",fg_color="red", command=lambda: self.unpark_vehicle('4W'))
        self.button_unpark_4W.grid(row=7, column=0,pady=2)
        
        self.button_park_Truck = ctk.CTkButton(self,height=30,width=250, text="Park Truck", command=lambda: self.park_vehicle('Truck'))
        self.button_park_Truck.grid(row=8, column=0,pady=2)

        self.button_unpark_Truck = ctk.CTkButton(self,height=30,width=250, text="Unpark Truck",fg_color="red", command=lambda: self.unpark_vehicle('Truck'))
        self.button_unpark_Truck.grid(row=9, column=0,pady=2)

        self.button_park_PD = ctk.CTkButton(self,height=30,width=250, text="Park Physically Disabled", command=lambda: self.park_vehicle('PhysicallyDisabled'))
        self.button_park_PD.grid(row=10, column=0,pady=2)

        self.button_unpark_PD = ctk.CTkButton(self,height=30,width=250,fg_color="red", text="Unpark Physically Disabled", command=lambda: self.unpark_vehicle('PhysicallyDisabled'))
        self.button_unpark_PD.grid(row=11, column=0,padx=0,pady=2)

        self.update_table = ctk.CTkButton(self,height=30,width=250, text="Update the table", command=self.update_table)
        self.update_table.grid(row=13, column=0,padx=0,pady=2)

        #lambda needed when arugements are there in the function

        self.button_exit = ctk.CTkButton(self,height=30,width=250, text="Exit", command=self.get_reports)
        self.button_exit.grid(row=12, column=0,padx=10,pady=2)
        
        
        self.parking_lot = CarParking(num_2W=10, num_4W=20, num_Truck=5, num_PhysicallyDisabled=2)
        
           
        for row in self.table.get_children():
          self.table.delete(row)

          
  
        file_path = "File-forcarpark.txt"
        with open(file_path,'r') as file:
         for line in file:

          split_string = line.strip().split(" ")
          unpark_entry = split_string[0]
          bill_entry = split_string[1]
          time_entry2 = split_string[2].split(".")
          time_exit2 = split_string[3].split(".")

          self.table.insert('', 'end', values=(unpark_entry,time_entry2,time_exit2,bill_entry))
        file.close()

        
    
    def update_table(self):

        
        for row in self.table.get_children():
          self.table.delete(row)

          
  
        file_path = "File-forcarpark.txt"
        with open(file_path,'r') as file:
         for line in file:

          split_string = line.strip().split(" ")
          unpark_entry = split_string[0]
          bill_entry = split_string[1]
          date_entry = split_string[2]
          time_entry2 = split_string[3]

          self.table.insert('', 'end', values=(unpark_entry,time_entry2,date_entry,bill_entry))
        file.close()  
        
     
        
    def update_remaining(self):
        remaining_text = f"Remaining Spaces: 2W: {self.parking_lot.num_2W}, 4W: {self.parking_lot.num_4W}, Truck: {self.parking_lot.num_Truck}, Physically Disabled: {self.parking_lot.num_PhysicallyDisabled}"
        self.label_remaining.configure(text=remaining_text)

    def park_vehicle(self, vehicle_type):
        if self.parking_lot.park_vehicle(vehicle_type):
            print(f"{vehicle_type} parked successfully!")
            
            if  self.EntryNumber.get().split(":")[1].strip()== "":
             entered_value = self.get_licenseplate()
            else:
                entered_value= self.EntryNumber.get().split(":")[1].strip()

            payment_mode = self.Entrypayment.get().split(":")[1].strip()
            current_datetime = datetime.now()
            licenseplatehash = simple_hash(entered_value) 
            print(licenseplatehash)
            Parking_list[licenseplatehash] = billing(entered_value, current_datetime, vehicle_type) 
            print(Parking_list[licenseplatehash].vehiclenumber)
            response =  messagebox.showinfo("information",Parking_list[licenseplatehash].vehiclenumber)
            Label(self,text=response).pack()
         
            
        else:
            print(f"Unable to park {vehicle_type}.")
            

    def unpark_vehicle(self, vehicle_type): 
        global client
        self.parking_lot.unpark_vehicle(vehicle_type)
        print(f"{vehicle_type} unparked successfully!")
        payment_mode = self.Entrypayment.get().split(":")[1].strip()  
        Unpark_number = self.EntryNumber.get().split(":")[1].strip()
        if Unpark_number =="":
           Unpark_number = self.get_licenseplate()
        hash_of_unpark= (simple_hash(Unpark_number))

        
        #for bill in Parking_list:
          #if Unpark_number == bill.vehiclenumber:
        if   Parking_list[hash_of_unpark].vehiclenumber == Unpark_number:
            unpark_datetime = datetime.now()
            Time_parked = (unpark_datetime - Parking_list[simple_hash(Unpark_number)].timeofentry).total_seconds() / 3600
            file_path = "File-forcarpark.txt"
            with open(file_path,'a') as file:
             send_msg(client,"Update_File")


           

        # Calculate the bill based on the type of vehicle
            if Parking_list[hash_of_unpark].type_of_Vehicle == "Truck":
             bill_amount = Time_parked * 50
            elif Parking_list[hash_of_unpark].type_of_Vehicle == "2W":
             bill_amount = Time_parked * 10
            elif Parking_list[hash_of_unpark].type_of_Vehicle == "4W":
             bill_amount = Time_parked * 25
            elif Parking_list[hash_of_unpark].type_of_Vehicle == "PhysicallyDisabled":
              bill_amount = Time_parked * 5

        # Show the bill as a message info
            response = messagebox.showinfo("Bill", f"Your bill amount is: {bill_amount} {payment_mode}")
            
            content = Unpark_number + " " + str(bill_amount) + " " + str(unpark_datetime) + " " + str(payment_mode) + "\n"
            
            time_entry = Parking_list[hash_of_unpark].timeofentry
            print(Parking_list[hash_of_unpark])
            print(bill_amount)
            self.table.insert('', 'end', values=(Unpark_number,time_entry,unpark_datetime,bill_amount,payment_mode))
            
           
            
 

            send_msg(client,content)
              

           
           

        

     


        
    def get_reports(self):
         selected_option = self.selected_option.get()
         
         file_path = 'File-forcarpark.txt'
         
         with open(file_path, 'r') as file:
          print("Selected option:", selected_option)
       
          if selected_option == "today":
            date_Now = datetime.now()

            current_date = datetime.today()
            formatted_date = current_date.strftime("%Y-%m-%d")  # Match the date format in your file

            Plotting = []  # Initialize list to store hours

            for line in file:
              split_string = line.strip().split(" ")

              date_entry = split_string[2]
              time_entry2 = split_string[3]

              if date_entry == formatted_date:
                hour_entry = time_entry2.split(":")[0]  # Extract hour from time_entry2
                Plotting.append(hour_entry)  # Store extracted hour in the list

            if Plotting:  # Ensure the list is not empty before plotting
              hours = list(set(Plotting))  # Unique hours
              counts = [Plotting.count(hour) for hour in hours]  # Count occurrences of each hour
                
              print("Hours:", hours)
              print("Counts:", counts)

              plt.bar(hours, counts)  
              plt.xlabel('Hour')
              plt.ylabel('Frequency')
              plt.title('Number of Cars Parked by Hour')
              plt.show()
            else:
             print("No data for the current date.")


    
    def get_licenseplate(self):

      if self.EntryNumber.get().split(":")[1].strip() == "":
       cap = cv2.VideoCapture(0)

       reader = easyocr.Reader(['en'])

       while True:
    # Capture frame-by-frame
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     
        edged = cv2.Canny(gray,30,200)

        contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10] #all edges circle or square anything etc

    # Find the contour representing the license plate either a rectangle or square
        license_plate_contour = None
        for contour in contours:
           approx = cv2.approxPolyDP(contour, 10, True)
           if len(approx) == 4:
              license_plate_contour = approx
              break

    # Extract the license plate region
        if license_plate_contour is not None:
          x, y, w, h = cv2.boundingRect(license_plate_contour)
          cropped_image = frame[y:y+h, x:x+w]

#Extracting the Region of Interest (ROI):

# cropped_image = frame[y:y+h, x:x+w] uses the coordinates and dimensions from the bounding box to extract the region of interest (ROI) from the original frame.
 # frame[y:y+h, x:x+w]: This slices the original frame to get the sub-image containing only the license plate.
 # y:y+h: Selects all rows from y to y + h.
 # x:x+w: Selects all columns from x to x + w.
 # The resulting cropped_image is a smaller image that contains only the license plate, which can then be processed further.



        # Convert cropped image to grayscale
          cropped_image_gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

        # Perform OCR on the cropped image
          result = reader.readtext(cropped_image_gray)

        # Process the OCR result
          for detection in result:
            text = detection[1]
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            pattern = r'^[A-Za-z]{3} \d{4}[A-Za-z]$'
            if re.match(pattern,text):
             print(text)
             input_Numberplate = text
             return text
             
              
    # Display the frame with detected text
        cv2.imshow('License Plate Detection', frame)
         

    # Check for key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
         break
        

# Releaf       se the camera and close all OpenCV windows
       cap.release()
       cv2.destroyAllWindows()


                       


      






















   
       





if __name__ == "__main__":
    app = ParkingApp()
    app.mainloop()
