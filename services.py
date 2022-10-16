import json
import copy
import peristalticController

def take_shot():
    peristalticController.dispense(1.5)

def take_shot_o(ounces: float):
    peristalticController.dispense(ounces)