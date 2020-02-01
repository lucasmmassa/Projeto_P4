from levels_utils import Levels_Manager
from menu_utils import Menu_Manager
from gameplay_utils import *
from tutorial_utils import *


def new_levels_manager():
    return Levels_Manager()

def new_menu_manager():
    return Menu_Manager()

def new_normal_manager():
    return Normal_Manager()

def new_hard_manager():
    return Hard_Manager()

def new_tutorial_manager():
    return Tutorial_Manager()

def new_examples_manager():
    return Examples_Manager()

manager_list = [new_menu_manager, new_levels_manager, new_normal_manager, new_hard_manager,
                new_tutorial_manager, new_examples_manager]