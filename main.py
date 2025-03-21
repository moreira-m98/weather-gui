from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import requests
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv

# Dicionário de traduções básicas #
traducao_clima = {
    "clear sky": "céu limpo",
    "few clouds": "poucas nuvens",
    "scattered clouds": "nuvens dispersas",
    "broken clouds": "nuvens quebradas",
    "shower rain": "chuva passageira",
    "rain": "chuva",
    "thunderstorm": "tempestade",
    "snow": "neve",
    "mist": "névoa",
    "light rain": "chuva leve"
}

#################cores ###############
co0 = "#444466"  # Preto
co1 = "#feffff"  # Branco
co2 = "#6f9fbd"  # Azul

back_day="#6cc4cc"
back_night="#484f60"
back_afternoon = "#bfb86d"

back = back_day

window = Tk()
window.title("")
window.geometry("320x350")
window.configure(bg=back)
ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)


# creating frames
frame_top = Frame(window, width=320, height=50, bg=co1, pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_body = Frame(window, width=320, height=300, bg=back, pady=12, padx=0)
frame_body.grid(row=2, column=0, sticky=NW)

style = ttk.Style(window)
style.theme_use("clam")

load_dotenv()

global l_img # global variable to store image

# function to get the weather information
def info():
    API_KEY = os.getenv("API_KEY")
    city = e_local.get()
    api_link = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}'.format(city, API_KEY)

    # get the data from the api
    response = requests.get(api_link)
    # convert the data to json
    data = response.json()


    # obtaining city, country and timezone
    country_code = data['city']['country']

    # time zone
    time_zone = pytz.country_timezones[country_code]

    # country
    country = pytz.country_names[country_code]

    # date and time
    zone = pytz.timezone(time_zone[0])
    zone_hours = datetime.now(zone)
    zone_hours = zone_hours.strftime('%d/%m/%Y | %H:%M:%S')

    # obtaining the temperature
    temp = data['list'][0]['main']['temp']
    temp = round(temp - 273.15, 2)
    temp = round(temp)
    pressure = data['list'][0]['main']['pressure']
    humidity = data['list'][0]['main']['humidity']
    description = data['list'][0]['weather'][0]['description']
    # Traduz, se houver no dicionário; senão, mantém original
    translated_description = traducao_clima.get(description, description)
    translated_description = translated_description.capitalize()

    #giving info to labels

    l_city['text'] = city.capitalize() + " - " + country.capitalize()
    l_date['text'] = zone_hours
    l_humidity['text'] = 'Umidade: ' + str(humidity) + '%'
    l_temp['text'] = str(temp)  + ' \u00B0C'
    # l_temp_symbol['text'] = '°'
    # l_temp_name['text'] = 'C'
    l_pressure['text'] = "Pressão: " + str(pressure) + ' hPa'
    l_description['text'] = translated_description

    #changing image and background

    zone_time = datetime.now(zone)
    zone_time = zone_time.strftime('%H')

    global l_img

    zone_time = int(zone_time)
    if zone_time <= 5:
        # image
        l_img = Image.open("img/moon-and-stars-100.png")
        backg = back_night
    elif zone_time <= 12:
        # image
        l_img = Image.open("img/sun-100.png")
        backg = back_day
    elif zone_time <= 18:
        # image
        l_img = Image.open("img/sun-afternoon-100.png")
        backg = back_afternoon
    elif zone_time <= 24:
        # image
        l_img = Image.open("img/moon-and-stars-100.png")
        backg = back_night
    else:
        pass

    # giving info to labels
    window.config(bg=backg)
    frame_top.config(bg=backg)
    frame_body.config(bg=backg)


    l_city['bg'] = backg
    l_date['bg'] = backg
    l_humidity['bg'] = backg
    l_temp['bg'] = backg
    l_temp_symbol['bg'] = backg
    l_temp_name['bg'] = backg
    l_pressure['bg'] = backg
    l_description['bg'] = backg


    l_img = l_img.resize((130, 130))
    l_img = ImageTk.PhotoImage(l_img)

    l_img_label = Label(frame_body, image=l_img, bg=backg)
    l_img_label.place(x=160, y=50)


##configing top frame##


#entry text
e_local = Entry(frame_top, width=20, justify=LEFT, font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)

#button to see the weather
b_see = Button(frame_top, command=info, text='Ver Clima', bg=co1, fg=co2, font=("Ivy 9 bold"), relief=RAISED, overrelief=RIDGE)
b_see.place(x=250, y=10)

#configing body frame
l_city = Label(frame_body, text='', anchor='center', bg=back, fg=co1, font=("Arial 14"))
l_city.place(x=10, y=4)

#date
l_date = Label(frame_body, text='', anchor='center', bg=back, fg=co1, font=("Arial 10"))
l_date.place(x=10, y=54)


#temperature
l_temp = Label(frame_body, text='', anchor='center', bg=back, fg=co1, font=("Arial 45"))
l_temp.place(x=10, y=100)


#temperature symbol
l_temp_symbol = Label(frame_body, text='', anchor='center', bg=back, fg=co1, font=("Arial 12"))
l_temp_symbol.place(x=90, y=110)


#temperature name
l_temp_name = Label(frame_body, text='', anchor='center', bg=back, fg=co1, font=("Arial 25"))
l_temp_name.place(x=85, y=120)


#humidity
l_humidity = Label(frame_body, text='', anchor='center', bg=back, fg=co1, font=("Arial 10"))
l_humidity.place(x=11.5, y=184)


#pressure
l_pressure = Label(frame_body, text='', anchor='center', bg=back, fg=co1, font=("Arial 10"))
l_pressure.place(x=11.5, y=212)

#description
l_description = Label(frame_body, text='', anchor='center', bg=back, fg=co1, font=("Arial 10"))
l_description.place(x=180, y=180)


window.mainloop()