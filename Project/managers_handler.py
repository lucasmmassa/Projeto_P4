from levels_utils import Levels_Manager
from menu_utils import Menu_Manager


def new_levels_manager():
    return Levels_Manager()

def new_menu_manager():
    return Menu_Manager()

manager_list = [new_menu_manager, new_levels_manager]