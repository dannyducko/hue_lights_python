import requests
import secrets
import os
import urllib3
from time import sleep

# Using requests to the Hue throws an error due to SSL validation. This stops that.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

lights_json = {}
current_state = ""
number_input = ""


def get_lights():
    clear()
    global lights_json
    global number_input
    url = f"https://{secrets.ip}/api/{secrets.key}/lights"

    headers = {
        'Content-Type': 'text/plain'
    }

    response = requests.request("GET", url, headers=headers, verify=False)

    lights_json = response.json()


def menu():
    clear()
    get_lights()

    global lights_json
    global number_input

    print("\n**********************************\n Welcome to the Hue Lights "
          "script!\n**********************************\n")

    for light in lights_json:
        print(light + ". " + lights_json[light]["name"])

    print("\n0. Exit\n\n Please type the number of the light you would like to query")

    number_input = input("\n What light do you wish to operate? \n > ")
    # checks to see if the number input by user is valid against the hue json/ dict.
    if number_input in lights_json:
        light_state(number_input)
        light_menu(number_input)
    elif number_input == "0":
        print(" Closing script...")
        sleep(2)
        exit()
    else:
        print(" Please type in a correct number, as referenced above...")
        sleep(3)
        get_lights()


def lights_on_off(light_number):
    global lights_json
    payload = ""
    url = f"https://{secrets.ip}/api/{secrets.key}/lights/{light_number}/state"

    # Looks to see if the light is in the state 'on'. Boolean value.
    light_status = lights_json[light_number]['state']['on']

    # If light_status on == true.
    if light_status:
        payload = "{\"on\":false}"
    else:
        payload = "{\"on\":true}"

    headers = {
        'Content-Type': 'text/plain'
    }

    response = requests.request("PUT", url, headers=headers, data=payload, verify=False)


def light_menu(light_number):
    clear()
    global lights_json
    global current_state
    print(
        f"*****************************\n Light: {lights_json[light_number]['name']}\n Current State: {current_state}\n*****************************\n")
    user_input = input("What would you like to do?\n 1. Toggle the light on or off\n 2. Change the colour of the "
                       "light (red, orange, yellow, green, turquoise, blue, purple, pink)\n\n 0. Back to main menu\n > ")
    if user_input == "1":
        lights_on_off(number_input)
        get_lights()
        light_state(number_input)
        light_menu(number_input)
    elif user_input == "0":
        menu()
    else:
        colour_change(user_input)
        get_lights()
        light_state(number_input)
        light_menu(number_input)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def colour_change(colour):
    global lights_json
    global number_input

    payload = ""

    red = "\t{\"on\":true, \"sat\":230, \"bri\":254,\"hue\":1}"
    orange = "\t{\"on\":true, \"sat\":230, \"bri\":254,\"hue\":5000}"
    yellow = "\t{\"on\":true, \"sat\":240, \"bri\":254,\"hue\":10000}"
    green = "\t{\"on\":true, \"sat\":240, \"bri\":254,\"hue\":20000}"
    turquoise = "\t{\"on\":true, \"sat\":240, \"bri\":254,\"hue\":35000}"
    blue = "\t{\"on\":true, \"sat\":240, \"bri\":254,\"hue\":45000}"
    purple = "\t{\"on\":true, \"sat\":240, \"bri\":254,\"hue\":50000}"
    pink = "\t{\"on\":true, \"sat\":240, \"bri\":254,\"hue\":55000}"

    if colour == "red":
        payload = red
    elif colour == "orange":
        payload = orange
    elif colour == "yellow":
        payload = yellow
    elif colour == "green":
        payload = green
    elif colour == "turquoise":
        payload = turquoise
    elif colour == "blue":
        payload = blue
    elif colour == "purple":
        payload = purple
    elif colour == "pink":
        payload = pink
    else:
        sleep(3)
        print("Colour not found")

    headers = {
        'Content-Type': 'text/plain'
    }
    url = f"https://{secrets.ip}/api/{secrets.key}/lights/{number_input}/state"

    response = requests.request("PUT", url, headers=headers, data=payload, verify=False)


def light_state(light_number):
    global current_state
    light_status = lights_json[light_number]['state']['on']
    if light_status:
        current_state = "On"
    else:
        current_state = "Off"


menu()
