from tkinter import *
import requests
import json

root = Tk()
root.title("Air Quality")
root.geometry("500x200")


def fetch_data():
    try:
        
        zip_code = int(entry.get())
        
     I
        api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=25&API_KEY=0862CA47-FC72-4A3E-8BFE-DD5B6CD6CCBB")
        api = json.loads(api_request.content)
        
       
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        
        
        if category == "Good":
            weather_color = "Green"
        elif category == "Moderate":
            weather_color = "Yellow"
        else:
            weather_color = "Brown"
        
        display_text = f"City: {city}\nAir Quality Index (AQI): {quality}\nCategory: {category}"
        output_label.config(text=display_text, background=weather_color)
    except Exception as e:
      
        output_label.config(text="Error.....")


entry = Entry(root)
entry.pack()


button = Button(root, text="Fetch Data", command=fetch_data)
button.pack()


output_label = Label(root, text="", font=("Arial", 12))
output_label.pack()

root.mainloop()

