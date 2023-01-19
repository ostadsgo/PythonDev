# Build calculator application with pysimplegui
from tkinter import Button
import PySimpleGUI as sg

sg.theme("DarkAmber")  # Add a touch of color
# All the stuff inside your window.

equal_pressd = False


def clear_all(event):
    window["inputbox"].update(value="")


def clear_one(event):
    input_value = window["inputbox"].get()
    window["inputbox"].update(value=input_value[:-1])


def on_number(event):
    global equal_pressd

    if equal_pressd:
        clear_all(event)
        equal_pressd = False

    calcbox = window["inputbox"]
    old_val = calcbox.get()
    calcbox.update(value=old_val + event)


def on_operator(event):
    global equal_pressd
    if window["inputbox"].get() == "":
        return
    equal_pressd = False
    calcbox = window["inputbox"]
    old_val = calcbox.get()
    calcbox.update(value=old_val + event)


def on_equal(event):
    global equal_pressd
    equal_pressd = True
    calcbox = window["inputbox"]
    equation = calcbox.get()
    try:
        calcbox.update(value=eval(equation))
    except ZeroDivisionError:
        calcbox.update(value="Zero Divison Error")
    except Exception as e:
        calcbox.update(value=e)


b = {"size": (7, 2), "button_color": ("black", "#F8F8F8")}
# bt = {"size": (7, 2), "button_color": ("black", "#F1EABC")}
layout = [
    [sg.InputText(key="inputbox", size=(30, 1), font=("Roboto", 14))],
    [sg.Button(item, **b) for item in ["C", "CC", "%", "/"]],
    [sg.Button(item, **b) for item in ["9", "8", "7", "*"]],
    [sg.Button(item, **b) for item in ["6", "5", "4", "-"]],
    [sg.Button(item, **b) for item in ["3", "2", "1", "+"]],
    [
        [sg.Button(item, **b) for item in ["0", "."]]
        + [sg.Button("=", size=(20, 2), bind_return_key=True)]
    ],
]

# Create the Window
window = sg.Window("PySimpleGUI Calculator", layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event in [str(i) for i in range(10)]:
        on_number(event)
    if event in ["+", "-", "*", "/", "%", "."]:
        on_operator(event)
    if event == "=":
        on_equal(event)
    if event == "CC":
        clear_all(event)
    if event == "C":
        clear_one(event)
window.close()
